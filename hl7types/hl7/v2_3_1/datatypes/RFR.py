"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: RFR
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from .NR import NR
from .TX import TX


class RFR(BaseModel):
    """HL7 v2 RFR data type."""

    rfr_1: NR | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "rfr_1",
            "numeric_range",
            "RFR.1",
        ),
        serialization_alias="RFR.1",
        title="numeric range",
    )

    rfr_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "rfr_2",
            "administrative_sex",
            "RFR.2",
        ),
        serialization_alias="RFR.2",
        title="administrative sex",
    )

    rfr_3: NR | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "rfr_3",
            "age_range",
            "RFR.3",
        ),
        serialization_alias="RFR.3",
        title="age range",
    )

    rfr_4: NR | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "rfr_4",
            "gestational_age_range",
            "RFR.4",
        ),
        serialization_alias="RFR.4",
        title="gestational age range",
    )

    rfr_5: TX | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "rfr_5",
            "species",
            "RFR.5",
        ),
        serialization_alias="RFR.5",
        title="species",
    )

    rfr_6: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "rfr_6",
            "race_subspecies",
            "RFR.6",
        ),
        serialization_alias="RFR.6",
        title="race/subspecies",
    )

    rfr_7: TX | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "rfr_7",
            "conditions",
            "RFR.7",
        ),
        serialization_alias="RFR.7",
        title="conditions",
    )

    model_config = {"populate_by_name": True}
