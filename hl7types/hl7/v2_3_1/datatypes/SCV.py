"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: SCV
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class SCV(BaseModel):
    """HL7 v2 SCV data type.

    Attributes
    ----------
    scv_1 : str | None
        SCV.1 (opt) - parameter class (IS)

    scv_2 : str | None
        SCV.2 (opt) - parameter value (IS)
    """

    scv_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "scv_1",
            "parameter_class",
            "SCV.1",
        ),
        serialization_alias="SCV.1",
        title="parameter class",
    )

    scv_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "scv_2",
            "parameter_value",
            "SCV.2",
        ),
        serialization_alias="SCV.2",
        title="parameter value",
    )

    model_config = {"populate_by_name": True}
