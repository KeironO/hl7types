"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: ICD
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator

from .CWE import CWE


class ICD(HL7Model):
    """HL7 v2 ICD data type.

    Attributes
    ----------
    icd_1 : CWE | None
        ICD.1 (opt) - Certification Patient Type (CWE)

    icd_2 : str
        ICD.2 (req) - Certification Required (ID)

    icd_3 : str | None
        ICD.3 (opt) - Date/Time Certification Required (DTM)
    """

    icd_1: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "icd_1",
            "certification_patient_type",
            "ICD.1",
        ),
        serialization_alias="ICD.1",
        title="Certification Patient Type",
    )

    icd_2: str = Field(
        default=...,
        max_length=1,
        validation_alias=AliasChoices(
            "icd_2",
            "certification_required",
            "ICD.2",
        ),
        serialization_alias="ICD.2",
        title="Certification Required",
    )

    icd_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "icd_3",
            "date_time_certification_required",
            "ICD.3",
        ),
        serialization_alias="ICD.3",
        title="Date/Time Certification Required",
    )

    @field_validator("icd_3", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 datetime")
        return v

    model_config = {"populate_by_name": True}
