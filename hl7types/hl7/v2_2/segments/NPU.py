"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: NPU
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model


class NPU(HL7Model):
    """BED STATUS UPDATE (S3.3.7).

    Attributes
    ----------
    npu_1 : str
        NPU.1 - Bed Location (CM) R S3.3.7.1 | 0079 - LOCATION

    npu_2 : str | None
        NPU.2 - Bed Status (ID) NA S3.3.7.2 | 0116 - BED STATUS
    """

    npu_1: str = Field(
        validation_alias=AliasChoices(
            "npu_1",
            "bed_location",
            "NPU.1",
        ),
        serialization_alias="NPU.1",
        title="Bed Location",
        description="R | Item #00209 | Table 0079 - LOCATION",
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
        description="NA | Item #00170 | Table 0116 - BED STATUS | LEN:1",
    )

    model_config = {"populate_by_name": True}
