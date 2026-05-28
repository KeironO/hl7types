"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: CM_RFR
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from .CE import CE


class CM_RFR(BaseModel):
    """HL7 v2 CM_RFR data type."""

    cm_rfr_1: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_rfr_1",
            "reference_range",
            "CM_RFR.1",
        ),
        serialization_alias="CM_RFR.1",
        title="Reference Range",
    )

    cm_rfr_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_rfr_2",
            "sex",
            "CM_RFR.2",
        ),
        serialization_alias="CM_RFR.2",
        title="Sex",
    )

    cm_rfr_3: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_rfr_3",
            "age_range",
            "CM_RFR.3",
        ),
        serialization_alias="CM_RFR.3",
        title="Age Range",
    )

    cm_rfr_4: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_rfr_4",
            "gestational_age_range",
            "CM_RFR.4",
        ),
        serialization_alias="CM_RFR.4",
        title="Gestational Age Range",
    )

    cm_rfr_5: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_rfr_5",
            "species",
            "CM_RFR.5",
        ),
        serialization_alias="CM_RFR.5",
        title="Species",
    )

    cm_rfr_6: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_rfr_6",
            "race_subspecies",
            "CM_RFR.6",
        ),
        serialization_alias="CM_RFR.6",
        title="Race / Subspecies",
    )

    cm_rfr_7: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_rfr_7",
            "text_condition",
            "CM_RFR.7",
        ),
        serialization_alias="CM_RFR.7",
        title="Text Condition",
    )

    model_config = {"populate_by_name": True}
