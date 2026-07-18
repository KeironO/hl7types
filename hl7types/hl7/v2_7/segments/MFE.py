"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: MFE
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, ValidationInfo, field_validator
from hl7types.hl7 import HL7Model
from hl7types.hl7._validators import _apply_dt_fallback

from ..datatypes.XCN import XCN
from ..datatypes.varies import varies

_RE_DTM = re.compile(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?')


class MFE(HL7Model):
    """Master File Entry (S8.5.2).

    Attributes
    ----------
    mfe_1 : str
        MFE.1 - Record-Level Event Code (ID) R S8.5.2.1 | 0180 - Record-level Event Code

    mfe_2 : str | None
        MFE.2 - MFN Control ID (ST) C S8.5.2.2

    mfe_3 : str | None
        MFE.3 - Effective Date/Time (DTM) O S8.5.1.5

    mfe_4 : list[varies]
        MFE.4 - Primary Key Value - MFE (varies) R rep S8.5.2.4 | 9999 - no table for CE

    mfe_5 : list[str]
        MFE.5 - Primary Key Value Type (ID) R rep S8.5.2.5 | 0355 - Primary Key Value Type

    mfe_6 : str | None
        MFE.6 - Entered Date/Time (DTM) O S2.14.10.6

    mfe_7 : XCN | None
        MFE.7 - Entered By (XCN) O S2.14.10.5
    """

    mfe_1: str = Field(
        validation_alias=AliasChoices(
            "mfe_1",
            "record_level_event_code",
            "MFE.1",
        ),
        serialization_alias="MFE.1",
        title="Record-Level Event Code",
        description=(
            "R | Item #00664 | Table 0180 - Record-level Event Code | LEN:3"
        ),
    )

    mfe_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "mfe_2",
            "mfn_control_id",
            "MFE.2",
        ),
        serialization_alias="MFE.2",
        title="MFN Control ID",
        description="C | Item #00665",
    )

    mfe_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "mfe_3",
            "effective_date_time",
            "MFE.3",
        ),
        serialization_alias="MFE.3",
        title="Effective Date/Time",
        description="O | Item #00662",
    )

    mfe_4: List[varies] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "mfe_4",
            "primary_key_value_mfe",
            "MFE.4",
        ),
        serialization_alias="MFE.4",
        title="Primary Key Value - MFE",
        description="R | Item #00667 | Table 9999 - no table for CE",
    )

    mfe_5: List[str] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "mfe_5",
            "primary_key_value_type",
            "MFE.5",
        ),
        serialization_alias="MFE.5",
        title="Primary Key Value Type",
        description=(
            "R | Item #01319 | Table 0355 - Primary Key Value Type | LEN:3"
        ),
    )

    mfe_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "mfe_6",
            "entered_date_time",
            "MFE.6",
        ),
        serialization_alias="MFE.6",
        title="Entered Date/Time",
        description="O | Item #00661",
    )

    mfe_7: Optional[XCN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "mfe_7",
            "entered_by",
            "MFE.7",
        ),
        serialization_alias="MFE.7",
        title="Entered By",
        description="O | Item #00224",
    )

    @field_validator("mfe_3", "mfe_6", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        if _RE_DTM.fullmatch(v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = ConfigDict(populate_by_name=True)
