"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: DLN
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class DLN(BaseModel):
    """HL7 v2 DLN data type."""

    dln_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dln_1",
            "license_number",
            "DLN.1",
        ),
        serialization_alias="DLN.1",
        title="License Number",
    )

    dln_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dln_2",
            "issuing_state_province_country",
            "DLN.2",
        ),
        serialization_alias="DLN.2",
        title="Issuing State, Province, Country",
    )

    dln_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dln_3",
            "expiration_date",
            "DLN.3",
        ),
        serialization_alias="DLN.3",
        title="Expiration Date",
    )

    model_config = {"populate_by_name": True}
