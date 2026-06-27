"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: PRT
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE
from ..datatypes.EI import EI
from ..datatypes.PL import PL
from ..datatypes.XAD import XAD
from ..datatypes.XCN import XCN
from ..datatypes.XON import XON
from ..datatypes.XTN import XTN


class PRT(HL7Model):
    """HL7 v2 PRT segment.

    Attributes
    ----------
    prt_1 : EI | None
        PRT.1 (opt) - Participation Instance ID (EI)

    prt_2 : str
        PRT.2 (req) - Action Code (ID)

    prt_3 : CWE | None
        PRT.3 (opt) - Action Reason (CWE)

    prt_4 : CWE
        PRT.4 (req) - Participation (CWE)

    prt_5 : list[XCN] | None
        PRT.5 (opt, rep) - Participation Person (XCN)

    prt_6 : CWE | None
        PRT.6 (opt) - Participation Person Provider Type (CWE)

    prt_7 : CWE | None
        PRT.7 (opt) - Participant Organization Unit Type (CWE)

    prt_8 : list[XON] | None
        PRT.8 (opt, rep) - Participation Organization (XON)

    prt_9 : list[PL] | None
        PRT.9 (opt, rep) - Participant Location (PL)

    prt_10 : list[EI] | None
        PRT.10 (opt, rep) - Participation Device (EI)

    prt_11 : str | None
        PRT.11 (opt) - Participation Begin Date/Time (arrival time) (DTM)

    prt_12 : str | None
        PRT.12 (opt) - Participation End Date/Time (departure time) (DTM)

    prt_13 : CWE | None
        PRT.13 (opt) - Participation Qualitative Duration (CWE)

    prt_14 : list[XAD] | None
        PRT.14 (opt, rep) - Participation Address (XAD)

    prt_15 : list[XTN] | None
        PRT.15 (opt, rep) - Participant Telecommunication Address (XTN)
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
        description="Item #2379",
    )

    prt_2: str = Field(
        validation_alias=AliasChoices(
            "prt_2",
            "action_code",
            "PRT.2",
        ),
        serialization_alias="PRT.2",
        title="Action Code",
        description="Item #816 | Table HL70206",
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
        description="Item #2380",
    )

    prt_4: CWE = Field(
        validation_alias=AliasChoices(
            "prt_4",
            "participation",
            "PRT.4",
        ),
        serialization_alias="PRT.4",
        title="Participation",
        description="Item #2381 | Table HL70912",
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
        description="Item #2382",
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
        description="Item #2383",
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
        description="Item #2384 | Table HL70406",
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
        description="Item #2385",
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
        description="Item #2386",
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
        description="Item #2348",
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
        description="Item #2387",
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
        description="Item #2388",
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
        description="Item #2389",
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
        description="Item #2390",
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
        description="Item #2391",
    )

    @field_validator("prt_11", "prt_12", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        import re
        if re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = {"populate_by_name": True}
