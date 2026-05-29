"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: CM_PCF
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from .TS import TS


class CM_PCF(BaseModel):
    """HL7 v2 CM_PCF data type.

    Attributes
    ----------
    cm_pcf_1 : str | None
        CM_PCF.1 (opt) - pre-certification patient type (IS)

    cm_pcf_2 : str | None
        CM_PCF.2 (opt) - pre-certification required (ID)

    cm_pcf_3 : TS | None
        CM_PCF.3 (opt) - pre-certification windwow (TS)
    """

    cm_pcf_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_pcf_1",
            "pre_certification_patient_type",
            "CM_PCF.1",
        ),
        serialization_alias="CM_PCF.1",
        title="pre-certification patient type",
    )

    cm_pcf_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_pcf_2",
            "pre_certification_required",
            "CM_PCF.2",
        ),
        serialization_alias="CM_PCF.2",
        title="pre-certification required",
    )

    cm_pcf_3: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_pcf_3",
            "pre_certification_windwow",
            "CM_PCF.3",
        ),
        serialization_alias="CM_PCF.3",
        title="pre-certification windwow",
    )

    model_config = {"populate_by_name": True}
