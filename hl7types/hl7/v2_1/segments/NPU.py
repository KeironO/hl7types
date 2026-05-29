"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: NPU
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class NPU(BaseModel):
    """HL7 v2 NPU segment.

    Attributes
    ----------
    npu_1 : str
        NPU.1 (req) - BED LOCATION (ID)

    npu_2 : str | None
        NPU.2 (opt) - BED STATUS (ID)
    """

    npu_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "npu_1",
            "bed_location",
            "NPU.1",
        ),
        serialization_alias="NPU.1",
        title="BED LOCATION",
        description="Item #785 | Table HL70079",
    )

    npu_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "npu_2",
            "bed_status",
            "NPU.2",
        ),
        serialization_alias="NPU.2",
        title="BED STATUS",
        description="Item #671 | Table HL70116",
    )

    model_config = {"populate_by_name": True}
