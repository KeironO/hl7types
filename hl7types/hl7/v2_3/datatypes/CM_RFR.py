"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: CM_RFR
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from .TX import TX


class CM_RFR(BaseModel):
    """HL7 v2 CM_RFR data type.

    Attributes
    ----------
    cm_rfr_1 : str | None
        CM_RFR.1 (opt) - reference range (CM)

    cm_rfr_2 : str | None
        CM_RFR.2 (opt) - sex (IS)

    cm_rfr_3 : str | None
        CM_RFR.3 (opt) - age range (CM)

    cm_rfr_4 : str | None
        CM_RFR.4 (opt) - age gestation (CM)

    cm_rfr_5 : TX | None
        CM_RFR.5 (opt) - species (TX)

    cm_rfr_6 : str | None
        CM_RFR.6 (opt) - race/subspecies (ST)

    cm_rfr_7 : TX | None
        CM_RFR.7 (opt) - conditions (TX)
    """

    cm_rfr_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_rfr_1",
            "reference_range",
            "CM_RFR.1",
        ),
        serialization_alias="CM_RFR.1",
        title="reference range",
    )

    cm_rfr_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_rfr_2",
            "sex",
            "CM_RFR.2",
        ),
        serialization_alias="CM_RFR.2",
        title="sex",
    )

    cm_rfr_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_rfr_3",
            "age_range",
            "CM_RFR.3",
        ),
        serialization_alias="CM_RFR.3",
        title="age range",
    )

    cm_rfr_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_rfr_4",
            "age_gestation",
            "CM_RFR.4",
        ),
        serialization_alias="CM_RFR.4",
        title="age gestation",
    )

    cm_rfr_5: Optional[TX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_rfr_5",
            "species",
            "CM_RFR.5",
        ),
        serialization_alias="CM_RFR.5",
        title="species",
    )

    cm_rfr_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_rfr_6",
            "race_subspecies",
            "CM_RFR.6",
        ),
        serialization_alias="CM_RFR.6",
        title="race/subspecies",
    )

    cm_rfr_7: Optional[TX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_rfr_7",
            "conditions",
            "CM_RFR.7",
        ),
        serialization_alias="CM_RFR.7",
        title="conditions",
    )

    model_config = {"populate_by_name": True}
