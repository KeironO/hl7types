from __future__ import annotations

import warnings
import pytest

from pydantic import ValidationError

from hl7types import NonStandardDateWarning, decode_er7
from hl7types.codecs.er7.decoder import decode_er7_segment
from hl7types.codecs.xml.decoder import decode_xml, decode_xml_segment
from hl7types.hl7._validators import _apply_dt_fallback
from hl7types.hl7.v2_4.datatypes import TS as TS_v24
from hl7types.hl7.v2_5_1.segments import MSA, MSH, PID


def _isodate_to_hl7(v: str) -> str:
    from datetime import datetime
    return datetime.strptime(v, "%Y-%m-%d").strftime("%Y%m%d")


def _isodt_to_hl7(v: str) -> str:
    from datetime import datetime
    for fmt in ("%Y-%m-%dT%H:%M:%S", "%Y-%m-%d"):
        try:
            return datetime.strptime(v, fmt).strftime(
                "%Y%m%d%H%M%S" if "T" in v else "%Y%m%d"
            )
        except ValueError:
            continue
    raise ValueError(f"Cannot parse {v!r} as ISO date/datetime")


def _always_fails(v: str) -> str:
    raise ValueError(f"cannot parse {v!r}")


_ACK_ISO_DATE = (
    "MSH|^~\\&|SEND||RECV||2026-01-01||ACK|001|P|2.5.1\r"
    "MSA|AA|001"
)
_ACK_GOOD_DATE = (
    "MSH|^~\\&|SEND||RECV||20260101||ACK|001|P|2.5.1\r"
    "MSA|AA|001"
)
_PID_ISO_DOB = "PID|1||MRN001||DOE^JOHN||2026-11-01"

_ACK_XML_ISO = (
    '<?xml version="1.0" encoding="UTF-8"?>'
    '<ACK xmlns="urn:hl7-org:v2xml">'
    "<MSH><MSH.1>|</MSH.1><MSH.2>^~\\&amp;</MSH.2>"
    "<MSH.7><TS.1>2026-01-01</TS.1></MSH.7>"
    "<MSH.9><MSG.1>ACK</MSG.1></MSH.9>"
    "<MSH.10>001</MSH.10>"
    "<MSH.11><PT.1>P</PT.1></MSH.11>"
    "<MSH.12><VID.1>2.5.1</VID.1></MSH.12>"
    "</MSH>"
    "<MSA><MSA.1>AA</MSA.1><MSA.2>001</MSA.2></MSA>"
    "</ACK>"
)
_ACK_XML_GOOD = (
    '<?xml version="1.0" encoding="UTF-8"?>'
    '<ACK xmlns="urn:hl7-org:v2xml">'
    "<MSH><MSH.1>|</MSH.1><MSH.2>^~\\&amp;</MSH.2>"
    "<MSH.7><TS.1>20260101</TS.1></MSH.7>"
    "<MSH.9><MSG.1>ACK</MSG.1></MSH.9>"
    "<MSH.10>001</MSH.10>"
    "<MSH.11><PT.1>P</PT.1></MSH.11>"
    "<MSH.12><VID.1>2.5.1</VID.1></MSH.12>"
    "</MSH>"
    "<MSA><MSA.1>AA</MSA.1><MSA.2>001</MSA.2></MSA>"
    "</ACK>"
)


def test_fallback_returns_normalised_value() -> None:
    with pytest.warns(NonStandardDateWarning):
        result = _apply_dt_fallback("2026-11-01", parser=_isodate_to_hl7, datatype="DTM", field_path="TS.1")
    assert result == "20261101"


def test_fallback_warning_content() -> None:
    with pytest.warns(NonStandardDateWarning, match=r"2026-11-01.*TS\.1.*20261101"):
        _apply_dt_fallback("2026-11-01", parser=_isodate_to_hl7, datatype="DTM", field_path="TS.1")


def test_fallback_warning_contains_field_path() -> None:
    with pytest.warns(NonStandardDateWarning, match=r"PID\.7"):
        _apply_dt_fallback("2026-11-01", parser=_isodate_to_hl7, datatype="DTM", field_path="PID.7")


def test_fallback_warning_contains_datatype() -> None:
    with pytest.warns(NonStandardDateWarning, match="DTM"):
        _apply_dt_fallback("2026-11-01", parser=_isodate_to_hl7, datatype="DTM", field_path="TS.1")


def test_fallback_no_parser_raises() -> None:
    with pytest.raises(ValueError, match="not empty or a valid HL7 DTM"):
        _apply_dt_fallback("2026-11-01", parser=None, datatype="DTM", field_path="TS.1")


def test_fallback_failing_parser_raises_descriptive_error() -> None:
    with pytest.raises(ValueError, match=r"Fallback DTM parser failed.*2026-bad.*TS\.1"):
        _apply_dt_fallback("2026-bad", parser=_always_fails, datatype="DTM", field_path="TS.1")


def test_fallback_failing_parser_chains_original_exception() -> None:
    with pytest.raises(ValueError) as exc_info:
        _apply_dt_fallback("2026-bad", parser=_always_fails, datatype="DTM", field_path="TS.1")
    assert exc_info.value.__cause__ is not None


def test_fallback_dt_datatype_label() -> None:
    with pytest.warns(NonStandardDateWarning, match="DT"):
        _apply_dt_fallback("2026-11-01", parser=_isodate_to_hl7, datatype="DT", field_path="TS.1")


def test_nonstandarddatewarning_is_user_warning() -> None:
    assert issubclass(NonStandardDateWarning, UserWarning)


def test_nonstandarddatewarning_importable_from_hl7types() -> None:
    from hl7types import NonStandardDateWarning as W  # noqa: F401
    assert issubclass(W, UserWarning)


def test_dateparser_importable_from_hl7types() -> None:
    from hl7types import DateParser  # noqa: F401


def test_decode_er7_segment_accepts_dtm_parser_kwarg() -> None:
    seg = decode_er7_segment("MSA|AA|MSG001", MSA, dtm_parser=_isodate_to_hl7)
    assert seg.msa_1 == "AA"


def test_decode_er7_accepts_dtm_parser_kwarg() -> None:
    msg = decode_er7(_ACK_GOOD_DATE, dtm_parser=_isodate_to_hl7)
    assert msg.MSA.msa_1 == "AA"


def test_model_validate_er7_accepts_dtm_parser_kwarg() -> None:
    seg = MSA.model_validate_er7("MSA|AA|MSG001", dtm_parser=_isodate_to_hl7)
    assert seg.msa_1 == "AA"


def test_decode_xml_accepts_dtm_parser_kwarg() -> None:
    msg = decode_xml(_ACK_XML_GOOD, dtm_parser=_isodate_to_hl7)
    assert msg.MSA.msa_1 == "AA"


def test_decode_xml_segment_accepts_dtm_parser_kwarg() -> None:
    from xml.etree.ElementTree import fromstring
    elem = fromstring("<MSA><MSA.1>AA</MSA.1><MSA.2>001</MSA.2></MSA>")
    seg = decode_xml_segment(elem, MSA, dtm_parser=_isodate_to_hl7)
    assert seg.msa_1 == "AA"


def test_no_parser_leaves_valid_values_unchanged() -> None:
    seg = decode_er7_segment("MSA|AA|MSG001", MSA)
    assert seg.msa_1 == "AA"


def test_er7_nonstandard_date_accepted_with_dtm_parser() -> None:
    with pytest.warns(NonStandardDateWarning, match="2026-01-01"):
        msg = decode_er7(_ACK_ISO_DATE, dtm_parser=_isodt_to_hl7)
    assert msg.MSH.msh_7.ts_1 == "20260101"


def test_er7_nonstandard_date_rejected_without_parser() -> None:
    with pytest.raises(ValidationError):
        decode_er7(_ACK_ISO_DATE)


def test_er7_segment_nonstandard_date_accepted() -> None:
    with pytest.warns(NonStandardDateWarning, match="2026-11-01"):
        seg = decode_er7_segment(_PID_ISO_DOB, PID, dtm_parser=_isodt_to_hl7)
    assert seg.pid_7.ts_1 == "20261101"


def test_er7_model_validate_er7_nonstandard_date_accepted() -> None:
    with pytest.warns(NonStandardDateWarning):
        seg = PID.model_validate_er7(_PID_ISO_DOB, dtm_parser=_isodt_to_hl7)
    assert seg.pid_7.ts_1 == "20261101"


def test_er7_failing_parser_produces_validation_error() -> None:
    with pytest.raises(ValidationError, match="Fallback DTM parser failed"):
        decode_er7(_ACK_ISO_DATE, dtm_parser=_always_fails)


def test_er7_valid_hl7_date_does_not_warn() -> None:
    with warnings.catch_warnings(record=True) as rec:
        warnings.simplefilter("always")
        decode_er7(_ACK_GOOD_DATE, dtm_parser=_isodt_to_hl7)
    assert not any(issubclass(w.category, NonStandardDateWarning) for w in rec)


def test_xml_nonstandard_date_accepted_with_dtm_parser() -> None:
    with pytest.warns(NonStandardDateWarning, match="2026-01-01"):
        msg = decode_xml(_ACK_XML_ISO, dtm_parser=_isodt_to_hl7)
    assert msg.MSH.msh_7.ts_1 == "20260101"


def test_xml_nonstandard_date_rejected_without_parser() -> None:
    with pytest.raises(ValidationError):
        decode_xml(_ACK_XML_ISO)


def test_xml_segment_nonstandard_date_accepted() -> None:
    from xml.etree.ElementTree import fromstring
    elem = fromstring(
        "<MSH>"
        "<MSH.1>|</MSH.1>"
        "<MSH.2>^~\\&amp;</MSH.2>"
        "<MSH.7><TS.1>2026-01-01</TS.1></MSH.7>"
        "</MSH>"
    )
    with pytest.warns(NonStandardDateWarning):
        seg = decode_xml_segment(elem, MSH, dtm_parser=_isodt_to_hl7)
    assert seg.msh_7.ts_1 == "20260101"


def test_pre25_nonstandard_date_accepted_with_dt_parser() -> None:
    with pytest.warns(NonStandardDateWarning, match="DT"):
        ts = TS_v24.model_validate({"TS.1": "2026-11-01"}, context={"dt_parser": _isodate_to_hl7})
    assert ts.ts_1 == "20261101"


def test_pre25_dtm_parser_not_used_for_dt_field() -> None:
    with pytest.raises(ValidationError):
        TS_v24.model_validate({"TS.1": "2026-11-01"}, context={"dtm_parser": _isodate_to_hl7})
