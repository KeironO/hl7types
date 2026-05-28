"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: RFR
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from .CWE import CWE
from .NR import NR
from .TX import TX


class RFR(BaseModel):
    """HL7 v2 RFR data type."""

    rfr_1: NR = Field(
        default=...,
        validation_alias=AliasChoices(
            "rfr_1",
            "numeric_range",
            "RFR.1",
        ),
        serialization_alias="RFR.1",
        title="Numeric Range",
    )

    rfr_2: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rfr_2",
            "administrative_sex",
            "RFR.2",
        ),
        serialization_alias="RFR.2",
        title="Administrative Sex",
    )

    rfr_3: Optional[NR] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rfr_3",
            "age_range",
            "RFR.3",
        ),
        serialization_alias="RFR.3",
        title="Age Range",
    )

    rfr_4: Optional[NR] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rfr_4",
            "gestational_age_range",
            "RFR.4",
        ),
        serialization_alias="RFR.4",
        title="Gestational Age Range",
    )

    rfr_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rfr_5",
            "species",
            "RFR.5",
        ),
        serialization_alias="RFR.5",
        title="Species",
    )

    rfr_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rfr_6",
            "race_subspecies",
            "RFR.6",
        ),
        serialization_alias="RFR.6",
        title="Race/subspecies",
    )

    rfr_7: Optional[TX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rfr_7",
            "conditions",
            "RFR.7",
        ),
        serialization_alias="RFR.7",
        title="Conditions",
    )

    model_config = {"populate_by_name": True}
