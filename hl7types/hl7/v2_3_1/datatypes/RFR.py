"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: RFR
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from .NR import NR
from .TX import TX


class RFR(HL7Model):
    """HL7 v2 RFR data type.

    Attributes
    ----------
    rfr_1 : NR | None
        RFR.1 (opt) - numeric range (NR)

    rfr_2 : str | None
        RFR.2 (opt) - administrative sex (IS)

    rfr_3 : NR | None
        RFR.3 (opt) - age range (NR)

    rfr_4 : NR | None
        RFR.4 (opt) - gestational age range (NR)

    rfr_5 : TX | None
        RFR.5 (opt) - species (TX)

    rfr_6 : str | None
        RFR.6 (opt) - race/subspecies (ST)

    rfr_7 : TX | None
        RFR.7 (opt) - conditions (TX)
    """

    rfr_1: Optional[NR] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rfr_1",
            "numeric_range",
            "RFR.1",
        ),
        serialization_alias="RFR.1",
        title="numeric range",
    )

    rfr_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rfr_2",
            "administrative_sex",
            "RFR.2",
        ),
        serialization_alias="RFR.2",
        title="administrative sex",
    )

    rfr_3: Optional[NR] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rfr_3",
            "age_range",
            "RFR.3",
        ),
        serialization_alias="RFR.3",
        title="age range",
    )

    rfr_4: Optional[NR] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rfr_4",
            "gestational_age_range",
            "RFR.4",
        ),
        serialization_alias="RFR.4",
        title="gestational age range",
    )

    rfr_5: Optional[TX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rfr_5",
            "species",
            "RFR.5",
        ),
        serialization_alias="RFR.5",
        title="species",
    )

    rfr_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rfr_6",
            "race_subspecies",
            "RFR.6",
        ),
        serialization_alias="RFR.6",
        title="race/subspecies",
    )

    rfr_7: Optional[TX] = Field(
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
