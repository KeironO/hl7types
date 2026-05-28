"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: ICD
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from .TS import TS


class ICD(BaseModel):
    """HL7 v2 ICD data type."""

    icd_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "icd_1",
            "certification_patient_type",
            "ICD.1",
        ),
        serialization_alias="ICD.1",
        title="Certification Patient Type",
    )

    icd_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "icd_2",
            "certification_required",
            "ICD.2",
        ),
        serialization_alias="ICD.2",
        title="Certification Required",
    )

    icd_3: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "icd_3",
            "date_time_certification_required",
            "ICD.3",
        ),
        serialization_alias="ICD.3",
        title="Date/Time Certification Required",
    )

    model_config = {"populate_by_name": True}
