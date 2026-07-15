"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: AIL
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CNE import CNE
from ..datatypes.CWE import CWE
from ..datatypes.PL import PL


class AIL(HL7Model):
    """Appointment Information - Location Resource (S10.6.6).

    Attributes
    ----------
    ail_1 : str
        AIL.1 - Set ID - AIL (SI) R S10.6.6.1

    ail_2 : str | None
        AIL.2 - Segment Action Code (ID) C S10.6.3.2 | 0206 - Segment action code

    ail_3 : list[PL] | None
        AIL.3 - Location Resource ID (PL) C rep S10.6.6.3

    ail_4 : CWE | None
        AIL.4 - Location Type - AIL (CWE) C S10.6.6.4 | 0305 - Person location type

    ail_5 : CWE | None
        AIL.5 - Location Group (CWE) O S10.6.6.5

    ail_6 : str | None
        AIL.6 - Start Date/Time (DTM) C S10.6.4.4

    ail_7 : str | None
        AIL.7 - Start Date/Time Offset (NM) C S10.6.4.5

    ail_8 : CNE | None
        AIL.8 - Start Date/Time Offset Units (CNE) C S10.6.4.6

    ail_9 : str | None
        AIL.9 - Duration (NM) O S10.6.4.7

    ail_10 : CNE | None
        AIL.10 - Duration Units (CNE) O S10.6.4.8

    ail_11 : str | None
        AIL.11 - Allow Substitution Code (IS) C S10.6.4.9 | 0279 - Allow Substitution Codes

    ail_12 : CWE | None
        AIL.12 - Filler Status Code (CWE) C S10.6.2.25 | 0278 - Filler status codes
    """

    ail_1: str = Field(
        validation_alias=AliasChoices(
            "ail_1",
            "set_id_ail",
            "AIL.1",
        ),
        serialization_alias="AIL.1",
        title="Set ID - AIL",
        description="R | Item #00902 | LEN:4",
    )

    ail_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ail_2",
            "segment_action_code",
            "AIL.2",
        ),
        serialization_alias="AIL.2",
        title="Segment Action Code",
        description=(
            "C | Item #00763 | Table 0206 - Segment action code | LEN:3"
        ),
    )

    ail_3: Optional[List[PL]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ail_3",
            "location_resource_id",
            "AIL.3",
        ),
        serialization_alias="AIL.3",
        title="Location Resource ID",
        description="C | Item #00903",
    )

    ail_4: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ail_4",
            "location_type_ail",
            "AIL.4",
        ),
        serialization_alias="AIL.4",
        title="Location Type - AIL",
        description="C | Item #00904 | Table 0305 - Person location type",
    )

    ail_5: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ail_5",
            "location_group",
            "AIL.5",
        ),
        serialization_alias="AIL.5",
        title="Location Group",
        description="O | Item #00905",
    )

    ail_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ail_6",
            "start_date_time",
            "AIL.6",
        ),
        serialization_alias="AIL.6",
        title="Start Date/Time",
        description="C | Item #01202 | LEN:24",
    )

    ail_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ail_7",
            "start_date_time_offset",
            "AIL.7",
        ),
        serialization_alias="AIL.7",
        title="Start Date/Time Offset",
        description="C | Item #00891 | LEN:20",
    )

    ail_8: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ail_8",
            "start_date_time_offset_units",
            "AIL.8",
        ),
        serialization_alias="AIL.8",
        title="Start Date/Time Offset Units",
        description="C | Item #00892",
    )

    ail_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ail_9",
            "duration",
            "AIL.9",
        ),
        serialization_alias="AIL.9",
        title="Duration",
        description="O | Item #00893 | LEN:20",
    )

    ail_10: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ail_10",
            "duration_units",
            "AIL.10",
        ),
        serialization_alias="AIL.10",
        title="Duration Units",
        description="O | Item #00894",
    )

    ail_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ail_11",
            "allow_substitution_code",
            "AIL.11",
        ),
        serialization_alias="AIL.11",
        title="Allow Substitution Code",
        description=(
            "C | Item #00895 | Table 0279 - Allow Substitution Codes | LEN:10"
        ),
    )

    ail_12: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ail_12",
            "filler_status_code",
            "AIL.12",
        ),
        serialization_alias="AIL.12",
        title="Filler Status Code",
        description="C | Item #00889 | Table 0278 - Filler status codes",
    )

    @field_validator("ail_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("ail_6", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        import re
        if re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    @field_validator("ail_7", "ail_9", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
