"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: PRT
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, ValidationInfo, field_validator
from hl7types.hl7 import HL7Model
from hl7types.hl7._validators import _apply_dt_fallback

from ..datatypes.CWE import CWE
from ..datatypes.EI import EI
from ..datatypes.PL import PL
from ..datatypes.XAD import XAD
from ..datatypes.XCN import XCN
from ..datatypes.XON import XON
from ..datatypes.XTN import XTN

_RE_DTM = re.compile(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?')


class PRT(HL7Model):
    """Participation Information (S7.4.4).

    Attributes
    ----------
    prt_1 : EI | None
        PRT.1 - Participation Instance ID (EI) C S7.4.4.1

    prt_2 : str
        PRT.2 - Action Code (ID) R S4.A.9.2 | 0206 - Segment Action Code

    prt_3 : CWE | None
        PRT.3 - Action Reason (CWE) O S7.4.4.3

    prt_4 : CWE
        PRT.4 - Participation (CWE) R S7.4.4.4 | 0912 - Participation

    prt_5 : list[XCN] | None
        PRT.5 - Participation Person (XCN) C rep S7.4.4.5

    prt_6 : CWE | None
        PRT.6 - Participation Person Provider Type (CWE) C S7.4.4.6

    prt_7 : CWE | None
        PRT.7 - Participant Organization Unit Type (CWE) C S7.4.4.7 | 0406 - Organization Unit Type

    prt_8 : list[XON] | None
        PRT.8 - Participation Organization (XON) C rep S7.4.4.8

    prt_9 : list[PL] | None
        PRT.9 - Participant Location (PL) C rep S7.4.4.9

    prt_10 : list[EI] | None
        PRT.10 - Participation Device (EI) C rep S7.4.4.10

    prt_11 : str | None
        PRT.11 - Participation Begin Date/Time (arrival time) (DTM) O S7.4.4.11

    prt_12 : str | None
        PRT.12 - Participation End Date/Time (departure time) (DTM) O S7.4.4.12

    prt_13 : CWE | None
        PRT.13 - Participation Qualitative Duration (CWE) O S7.4.4.13

    prt_14 : list[XAD] | None
        PRT.14 - Participation Address (XAD) C rep S7.4.4.14

    prt_15 : list[XTN] | None
        PRT.15 - Participant Telecommunication Address (XTN) O rep S7.4.4.15
    """

    prt_1: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prt_1",
            "participation_instance_id",
            "PRT.1",
        ),
        serialization_alias="PRT.1",
        title="Participation Instance ID",
        description="C | Item #02379",
    )

    prt_2: str = Field(
        validation_alias=AliasChoices(
            "prt_2",
            "action_code",
            "PRT.2",
        ),
        serialization_alias="PRT.2",
        title="Action Code",
        description="R | Item #00816 | Table 0206 - Segment Action Code",
    )

    prt_3: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prt_3",
            "action_reason",
            "PRT.3",
        ),
        serialization_alias="PRT.3",
        title="Action Reason",
        description="O | Item #02380",
    )

    prt_4: CWE = Field(
        validation_alias=AliasChoices(
            "prt_4",
            "participation",
            "PRT.4",
        ),
        serialization_alias="PRT.4",
        title="Participation",
        description="R | Item #02381 | Table 0912 - Participation",
    )

    prt_5: Optional[List[XCN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prt_5",
            "participation_person",
            "PRT.5",
        ),
        serialization_alias="PRT.5",
        title="Participation Person",
        description="C | Item #02382",
    )

    prt_6: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prt_6",
            "participation_person_provider_type",
            "PRT.6",
        ),
        serialization_alias="PRT.6",
        title="Participation Person Provider Type",
        description="C | Item #02383",
    )

    prt_7: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prt_7",
            "participant_organization_unit_type",
            "PRT.7",
        ),
        serialization_alias="PRT.7",
        title="Participant Organization Unit Type",
        description="C | Item #02384 | Table 0406 - Organization Unit Type",
    )

    prt_8: Optional[List[XON]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prt_8",
            "participation_organization",
            "PRT.8",
        ),
        serialization_alias="PRT.8",
        title="Participation Organization",
        description="C | Item #02385",
    )

    prt_9: Optional[List[PL]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prt_9",
            "participant_location",
            "PRT.9",
        ),
        serialization_alias="PRT.9",
        title="Participant Location",
        description="C | Item #02386",
    )

    prt_10: Optional[List[EI]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prt_10",
            "participation_device",
            "PRT.10",
        ),
        serialization_alias="PRT.10",
        title="Participation Device",
        description="C | Item #02348",
    )

    prt_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prt_11",
            "participation_begin_date_time_arrival_time",
            "PRT.11",
        ),
        serialization_alias="PRT.11",
        title="Participation Begin Date/Time (arrival time)",
        description="O | Item #02387",
    )

    prt_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prt_12",
            "participation_end_date_time_departure_time",
            "PRT.12",
        ),
        serialization_alias="PRT.12",
        title="Participation End Date/Time (departure time)",
        description="O | Item #02388",
    )

    prt_13: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prt_13",
            "participation_qualitative_duration",
            "PRT.13",
        ),
        serialization_alias="PRT.13",
        title="Participation Qualitative Duration",
        description="O | Item #02389",
    )

    prt_14: Optional[List[XAD]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prt_14",
            "participation_address",
            "PRT.14",
        ),
        serialization_alias="PRT.14",
        title="Participation Address",
        description="C | Item #02390",
    )

    prt_15: Optional[List[XTN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prt_15",
            "participant_telecommunication_address",
            "PRT.15",
        ),
        serialization_alias="PRT.15",
        title="Participant Telecommunication Address",
        description="O | Item #02391",
    )

    @field_validator("prt_11", "prt_12", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        if _RE_DTM.fullmatch(v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = ConfigDict(populate_by_name=True)
