"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: MFN_M15.MF_INV_ITEM
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field

from ..segments.IIM import IIM
from ..segments.MFE import MFE

_IIM = IIM
_MFE = MFE


class MFN_M15_MF_INV_ITEM(BaseModel):
    """HL7 v2 MFN_M15.MF_INV_ITEM group.

    Attributes:
        MFE (MFE): required
        IIM (IIM): required
    """

    MFE: _MFE = Field(
        default=...,
        title="MFE",
        description="Required",
    )

    IIM: _IIM = Field(
        default=...,
        title="IIM",
        description="Required",
    )

    model_config = {"populate_by_name": True}
