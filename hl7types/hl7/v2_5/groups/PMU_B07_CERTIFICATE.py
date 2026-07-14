"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: PMU_B07.CERTIFICATE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.CER import CER
from ..segments.ROL import ROL

_CER = CER
_ROL = ROL


class PMU_B07_CERTIFICATE(HL7Model):
    """HL7 v2 PMU_B07.CERTIFICATE group.

    Attributes:
        CER (CER): Certificate Detail, required
        ROL (Optional[List[ROL]]): Role, optional
    """

    CER: _CER = Field(
        title="CER",
        description="Certificate Detail",
    )

    ROL: Optional[List[_ROL]] = Field(
        default=None,
        title="ROL",
        description="Role",
    )

    model_config = {"populate_by_name": True}
