"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: NPU
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.PL import PL


class NPU(BaseModel):
    """HL7 v2 NPU segment."""

    npu_1: PL = Field(
        default=...,
        validation_alias=AliasChoices(
            "npu_1",
            "bed_location",
            "NPU.1",
        ),
        serialization_alias="NPU.1",
        title="Bed Location",
        description="Item #209",
    )

    npu_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "npu_2",
            "bed_status",
            "NPU.2",
        ),
        serialization_alias="NPU.2",
        title="Bed Status",
        description="Item #170 | Table HL70116",
    )

    model_config = {"populate_by_name": True}
