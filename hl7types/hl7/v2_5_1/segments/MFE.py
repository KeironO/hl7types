"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: MFE
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.TS import TS


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

    mfe_2: str | None = Field(
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

    mfe_3: TS | None = Field(
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

    mfe_4: list[str] = Field(
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

    mfe_5: list[str] = Field(
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

    model_config = {"populate_by_name": True}
