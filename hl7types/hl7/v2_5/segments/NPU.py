"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: NPU
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.PL import PL


class NPU(HL7Model):
    """Bed Status Update (S3.4.8).

    Attributes
    ----------
    npu_1 : PL
        NPU.1 - Bed Location (PL) R S3.4.8.1

    npu_2 : str | None
        NPU.2 - Bed Status (IS) O S3.4.3.40 | 0116 - Bed Status
    """

    npu_1: PL = Field(
        validation_alias=AliasChoices(
            "npu_1",
            "bed_location",
            "NPU.1",
        ),
        serialization_alias="NPU.1",
        title="Bed Location",
        description="R | Item #00209",
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
        description="O | Item #00170 | Table 0116 - Bed Status | LEN:1",
    )

    model_config = {"populate_by_name": True}
