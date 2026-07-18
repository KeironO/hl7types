"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: PMU_B07.CERTIFICATE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.CER import CER
from ..segments.PRT import PRT
from ..segments.ROL import ROL

_CER = CER
_PRT = PRT
_ROL = ROL


class PMU_B07_CERTIFICATE(HL7Model):
    """HL7 v2 PMU_B07.CERTIFICATE group.

    Attributes:
        CER (CER): Certificate Detail, required
        PRT (Optional[List[PRT]]): Participation Information, optional
        ROL (Optional[List[ROL]]): Role, optional
    """

    CER: _CER = Field(
        title="CER",
        description="Certificate Detail",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Participation Information",
    )

    ROL: Optional[List[_ROL]] = Field(
        default=None,
        title="ROL",
        description="Role",
    )

    model_config = ConfigDict(populate_by_name=True)
