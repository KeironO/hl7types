"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: CM_PCF
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from .TS import TS


class CM_PCF(HL7Model):
    """HL7 v2 CM_PCF data type.

    Attributes
    ----------
    cm_pcf_1 : str | None
        CM_PCF.1 (opt) - pre-certification patient type (ID)

    cm_pcf_2 : str | None
        CM_PCF.2 (opt) - pre-certication required (ID)

    cm_pcf_3 : TS | None
        CM_PCF.3 (opt) - pre-certification window (TS)
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
            "pre_certication_required",
            "CM_PCF.2",
        ),
        serialization_alias="CM_PCF.2",
        title="pre-certication required",
    )

    cm_pcf_3: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_pcf_3",
            "pre_certification_window",
            "CM_PCF.3",
        ),
        serialization_alias="CM_PCF.3",
        title="pre-certification window",
    )

    model_config = {"populate_by_name": True}
