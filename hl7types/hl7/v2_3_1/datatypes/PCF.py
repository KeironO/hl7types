"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: PCF
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from .TS import TS


class PCF(BaseModel):
    """HL7 v2 PCF data type.

    Attributes
    ----------
    pcf_1 : str | None
        PCF.1 (opt) - pre-certification patient type (IS)

    pcf_2 : str | None
        PCF.2 (opt) - pre-certification required (ID)

    pcf_3 : TS | None
        PCF.3 (opt) - pre-certification window (TS)
    """

    pcf_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pcf_1",
            "pre_certification_patient_type",
            "PCF.1",
        ),
        serialization_alias="PCF.1",
        title="pre-certification patient type",
    )

    pcf_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pcf_2",
            "pre_certification_required",
            "PCF.2",
        ),
        serialization_alias="PCF.2",
        title="pre-certification required",
    )

    pcf_3: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pcf_3",
            "pre_certification_window",
            "PCF.3",
        ),
        serialization_alias="PCF.3",
        title="pre-certification window",
    )

    model_config = {"populate_by_name": True}
