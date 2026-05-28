"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: MFE
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.XCN import XCN
from ..datatypes.varies import varies


class MFE(BaseModel):
    """HL7 v2 MFE segment."""

    mfe_1: str = Field(
        default=...,
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

    mfe_4: List[varies] = Field(
        default=...,
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
        default=...,
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

    model_config = {"populate_by_name": True}
