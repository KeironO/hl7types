"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: NPU
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.PL import PL


class NPU(HL7Model):
    """HL7 v2 NPU segment.

    Attributes
    ----------
    npu_1 : PL
        NPU.1 (req) - Bed Location (PL)

    npu_2 : str | None
        NPU.2 (opt) - Bed Status (IS)
    """

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

    npu_2: Optional[str] = Field(
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
