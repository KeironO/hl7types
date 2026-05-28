"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: PMU_B07.CERTIFICATE
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.CER import CER
from ..segments.PRT import PRT
from ..segments.ROL import ROL

_CER = CER
_PRT = PRT
_ROL = ROL


class PMU_B07_CERTIFICATE(BaseModel):
    """HL7 v2 PMU_B07.CERTIFICATE group.

    Attributes:
        CER (CER): required
        PRT (Optional[List[PRT]]): optional
        ROL (Optional[List[ROL]]): optional
    """

    CER: _CER = Field(
        default=...,
        title="CER",
        description="Required",
    )

    PRT: list[_PRT] | None = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    ROL: list[_ROL] | None = Field(
        default=None,
        title="ROL",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
