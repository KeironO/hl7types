"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: MFE
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.XCN import XCN
from ..datatypes.varies import varies


class MFE(HL7Model):
    """HL7 v2 MFE segment.

    Attributes
    ----------
    mfe_1 : str
        MFE.1 (req) - Record-Level Event Code (ID)

    mfe_2 : str | None
        MFE.2 (opt) - MFN Control ID (ST)

    mfe_3 : str | None
        MFE.3 (opt) - Effective Date/Time (DTM)

    mfe_4 : list[varies] | None
        MFE.4 (req, rep) - Primary Key Value - MFE (varies) [optional: varies has no required components]

    mfe_5 : list[str]
        MFE.5 (req, rep) - Primary Key Value Type (ID)

    mfe_6 : str | None
        MFE.6 (opt) - Entered Date/Time (DTM)

    mfe_7 : XCN | None
        MFE.7 (opt) - Entered By (XCN)
    """

    mfe_1: str = Field(
        validation_alias=AliasChoices(
            "mfe_1",
            "record_level_event_code",
            "MFE.1",
        ),
        serialization_alias="MFE.1",
        title="Record-Level Event Code",
        description="Item #664 | Table HL70180",
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
        description="Item #665",
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
        description="Item #662",
    )

    mfe_4: Optional[List[varies]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "mfe_4",
            "primary_key_value_mfe",
            "MFE.4",
        ),
        serialization_alias="MFE.4",
        title="Primary Key Value - MFE",
        description="Item #667 | Table HL79999",
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
        description="Item #1319 | Table HL70355",
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
        description="Item #661",
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
        description="Item #224",
    )

    @field_validator("mfe_3", "mfe_6", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 datetime")
        return v

    model_config = {"populate_by_name": True}
