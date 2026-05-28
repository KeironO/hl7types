"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: SCV
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from .CWE import CWE


class SCV(BaseModel):
    """HL7 v2 SCV data type."""

    scv_1: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "scv_1",
            "parameter_class",
            "SCV.1",
        ),
        serialization_alias="SCV.1",
        title="Parameter Class",
    )

    scv_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "scv_2",
            "parameter_value",
            "SCV.2",
        ),
        serialization_alias="SCV.2",
        title="Parameter Value",
    )

    model_config = {"populate_by_name": True}
