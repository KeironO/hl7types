"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: NPU
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model


class NPU(HL7Model):
    """NON-PATIENT UPDATE (S3.3.5).

    Attributes
    ----------
    npu_1 : str
        NPU.1 (req) - BED LOCATION (ID) S3-22 | 0079 - LOCATION

    npu_2 : str | None
        NPU.2 (opt) - BED STATUS (ID) | 0116 - BED STATUS
    """

    npu_1: str = Field(
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
