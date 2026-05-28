"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: MFN_M18.MF_PAYER
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.MFE import MFE

from .MFN_M18_PAYER_MF_ENTRY import MFN_M18_PAYER_MF_ENTRY

_MFE = MFE
_MFN_M18_PAYER_MF_ENTRY = MFN_M18_PAYER_MF_ENTRY


class MFN_M18_MF_PAYER(BaseModel):
    """HL7 v2 MFN_M18.MF_PAYER group.

    Attributes:
        MFE (MFE): required
        PAYER_MF_ENTRY (List[MFN_M18_PAYER_MF_ENTRY]): required
    """

    MFE: _MFE = Field(
        default=...,
        title="MFE",
        description="Required",
    )

    PAYER_MF_ENTRY: List[_MFN_M18_PAYER_MF_ENTRY] = Field(
        default=...,
        title="PAYER_MF_ENTRY",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
