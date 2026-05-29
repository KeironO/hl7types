"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: DTN
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from .CWE import CWE


class DTN(BaseModel):
    """HL7 v2 DTN data type.

    Attributes
    ----------
    dtn_1 : CWE
        DTN.1 (req) - Day Type (CWE)

    dtn_2 : str
        DTN.2 (req) - Number of Days (NM)
    """

    dtn_1: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "dtn_1",
            "day_type",
            "DTN.1",
        ),
        serialization_alias="DTN.1",
        title="Day Type",
    )

    dtn_2: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "dtn_2",
            "number_of_days",
            "DTN.2",
        ),
        serialization_alias="DTN.2",
        title="Number of Days",
    )

    model_config = {"populate_by_name": True}
