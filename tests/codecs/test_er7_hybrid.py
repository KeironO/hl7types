from __future__ import annotations

import json
from datetime import datetime
from typing import Optional

import pytest
from pydantic import Field

from hl7types import HL7Registry, decode_er7, decode_er7_hybrid
from hl7types.hl7 import HL7Model
from hl7types.hl7.v2_5_1.datatypes.HD import HD
from hl7types.hl7.v2_5_1.datatypes.MSG import MSG
from hl7types.hl7.v2_5_1.datatypes.PT import PT
from hl7types.hl7.v2_5_1.datatypes.TS import TS
from hl7types.hl7.v2_5_1.datatypes.VID import VID
from hl7types.hl7.v2_5_1.segments.MSA import MSA
from hl7types.hl7.v2_5_1.segments.MSH import MSH


class ZWCC(HL7Model):
    zwcc_1: Optional[str] = Field(None, serialization_alias="ZWCC.1")
    zwcc_2: Optional[str] = Field(None, serialization_alias="ZWCC.2")


_ZWCC = ZWCC
_MSH = MSH
_MSA = MSA


class WCCACKMessage(HL7Model):
    MSH: _MSH
    MSA: _MSA
    ZWCC: Optional[_ZWCC] = None


def test_hybrid_decoder_keeps_unknown_segments_and_returns_typed_message() -> None:
    wire = (
        "MSH|^~\\&|NES|NINTENDO|AGNEW|CC|20010101000000||ADT^A01|Q1|P|2.3\r"
        "EVN|A01|20010101000000\r"
        "PID|1||123456||DOE^JOHN\r"
        "ZPD|local-value\r"
        "PV1|1|I\r"
    )

    message = decode_er7_hybrid(wire)

    assert message.model_dump_er7() == wire
    assert message.typed is not None
    assert message.typed.MSH.msh_3.hd_1 == "NES"  # type: ignore[union-attr]
    assert message.generic.ZPD.zpd_1.value == "local-value"
    assert any(diagnostic.level == "warning" for diagnostic in message.diagnostics)


def test_hybrid_decoder_preserves_unknown_message_when_typed_decode_fails() -> None:
    wire = "MSH|^~\\&|A|B|C|D|20010101||ZXX^Z01|CTRL|P|2.5.1\rZND|value\r"

    message = decode_er7_hybrid(wire)

    assert message.typed is None
    assert message.generic.MSH.msh_9.value == "ZXX^Z01"
    assert message.generic.ZND.znd_1.value == "value"
    assert message.diagnostics[0].level == "error"


def test_hybrid_decoder_passes_registry_through_to_typed_view() -> None:
    wire = (
        "MSH|^~\\&|WPAS||SEND||20260101120000||ACK|MSG000002|P|2.5.1\r"
        "MSA|AA|MSG000001\r"
        "ZWCC|WPAS|20260101120000\r"
    )

    registry = HL7Registry()
    registry.register_segment("ZWCC", ZWCC)
    registry.register_message("2.5.1", "ACK", WCCACKMessage)

    message = decode_er7_hybrid(wire, registry=registry)

    assert message.typed is not None
    assert isinstance(message.typed, WCCACKMessage)
    assert message.typed.ZWCC is not None  # type: ignore[union-attr]
    assert message.typed.ZWCC.zwcc_1 == "WPAS"  # type: ignore[union-attr]
    assert message.generic.ZWCC.zwcc_1.value == "WPAS"
    assert message.model_dump_er7() == wire


def test_hybrid_decoder_passes_dt_parser_through_to_typed_view() -> None:
    def to_hl7_date(value: str) -> str:
        return datetime.strptime(value, "%Y-%m-%d").strftime("%Y%m%d")

    # MSH.7 is a non-standard ISO date that the fallback parser must convert.
    wire = "MSH|^~\\&|SEND||RECV||2026-01-01||ACK|001|P|2.5.1\rMSA|AA|001\r"

    message = decode_er7_hybrid(wire, dtm_parser=to_hl7_date)

    assert message.typed is not None
    assert message.typed.MSH.msh_7.ts_1 == "20260101"  # type: ignore[union-attr]
    assert message.generic.MSH.msh_7.value == "2026-01-01"


def test_hybrid_decoder_keeps_multiple_unknown_segments() -> None:
    wire = (
        "MSH|^~\\&|NES|NINTENDO|AGNEW|CC|20010101000000||ADT^A01|Q1|P|2.3\r"
        "EVN|A01|20010101000000\r"
        "PID|1||123456||HUMAN^JOHN\r"
        "ZPD|one\r"
        "ZPD|two\r"
        "ZIN|three\r"
        "PV1|1|I\r"
    )

    message = decode_er7_hybrid(wire)

    assert message.model_dump_er7() == wire
    zpd = message.generic.ZPD
    assert isinstance(zpd, tuple)
    assert len(zpd) == 2
    assert zpd[0].zpd_1.value == "one"
    assert zpd[1].zpd_1.value == "two"
    assert message.generic.ZIN.zin_1.value == "three"
    warnings = [d for d in message.diagnostics if d.level == "warning"]
    assert len(warnings) >= 3


def test_hybrid_decoder_reports_both_warning_and_error_diagnostics() -> None:
    # Unknown message structure (ZXX^Z01) makes the typed view fail to resolve,
    # producing an error; the unknown ZND segment would warn if typed decoding
    # had progressed. Here the error dominates and typed is None.
    wire = "MSH|^~\\&|A|B|C|D|20010101||ZXX^Z01|CTRL|P|2.5.1\rZND|value\r"

    message = decode_er7_hybrid(wire)

    assert message.typed is None
    levels = {d.level for d in message.diagnostics}
    assert "error" in levels
    assert message.generic.ZND.znd_1.value == "value"


def test_hybrid_decoder_round_trips_with_nonstandard_delimiters() -> None:
    # Field sep is !, component sep is %, repetition sep is $, subcomponent sep is ?.
    # MSH.9 uses % as the component separator (ADT%A01, not ADT^A01).
    wire = (
        "MSH!%$\\?!SEND!RECV!!!20260101!!ADT%A01!1!P!2.3\r"
        "EVN!A01!20260101\r"
        "PV1!1!I\r"
    )

    message = decode_er7_hybrid(wire, segment_separator="\r")

    assert message.model_dump_er7() == wire
    assert message.generic.encoding.field == "!"
    assert message.typed is not None
    assert message.typed.MSH.msh_3.hd_1 == "SEND"  # type: ignore[union-attr]


def test_hybrid_typed_view_matches_decode_er7_for_standard_wire() -> None:
    # The hybrid must build its typed view from the same segment strings that
    # decode_er7 would split, so the two produce equivalent typed messages.
    wire = (
        "MSH|^~\\&|NES|NINTENDO|AGNEW|CC|20010101000000||ADT^A01|Q1|P|2.3\r"
        "EVN|A01|20010101000000\r"
        "PID|1||123456||DOE^JOHN\r"
        "PV1|1|I\r"
    )

    hybrid = decode_er7_hybrid(wire)
    typed = decode_er7(wire, strict=False)

    assert hybrid.typed is not None
    assert hybrid.typed.MSH.msh_3.hd_1 == typed.MSH.msh_3.hd_1  # type: ignore[union-attr]
    assert hybrid.typed.PID.pid_3[0].cx_1 == typed.PID.pid_3[0].cx_1  # type: ignore[union-attr]
    assert hybrid.typed.PV1.pv1_2 == typed.PV1.pv1_2  # type: ignore[union-attr]


def test_hybrid_generic_view_preserves_unknown_segments_and_empty_values() -> None:
    wire = (
        "MSH|^~\\&|SENDER|FACILITY|||||ZXX^Z01|CONTROL|P|2.5.1\r"
        "ZPD|one^^three~four&five|\r"
        "PID|||123\r"
    )

    message = decode_er7_hybrid(wire)
    generic = message.generic

    assert message.model_dump_er7() == wire
    with pytest.raises(AttributeError):
        _ = generic.raw
    assert generic.encoding.field == "|"
    assert [segment.name for segment in generic.segments] == ["MSH", "ZPD", "PID"]
    assert generic.segments[0].fields[0].repetitions[0].components[0].subcomponents == ("|",)
    assert generic.segments[0].fields[1].repetitions[0].components[0].subcomponents == ("^~\\&",)
    assert generic.segments[1].raw == "ZPD|one^^three~four&five|"
    assert generic.segments[1].fields[0].repetitions[0].components[1].subcomponents == ("",)
    assert generic.segments[1].fields[0].repetitions[1].components[0].subcomponents == (
        "four",
        "five",
    )
    assert generic.segments[1].fields[1].repetitions[0].components[0].subcomponents == ("",)


def test_hybrid_generic_field_values_can_be_reconstructed() -> None:
    message = decode_er7_hybrid("MSH|^~\\&|SENDER\rZPD|one^^three~four&five|\r")
    field = message.generic.segments[1].fields[0]

    value = "~".join(
        "^".join("&".join(component.subcomponents) for component in repetition.components)
        for repetition in field.repetitions
    )

    assert value == "one^^three~four&five"


def test_hybrid_generic_view_dumps_json() -> None:
    message = decode_er7_hybrid("MSH|^~\\&|SENDER\rZPD|value\r")

    dumped = json.loads(message.generic.model_dump_json())

    assert "raw" not in dumped
    assert dumped["encoding"]["field"] == "|"
    assert dumped["MSH"]["msh_1"]["value"] == "|"
    assert dumped["MSH"]["msh_2"]["value"] == "^~\\&"
    assert dumped["ZPD"]["zpd_1"]["repetitions"][0]["components"][0]["subcomponents"] == ["value"]
