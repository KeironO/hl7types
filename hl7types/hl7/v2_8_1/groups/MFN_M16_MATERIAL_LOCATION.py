"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: MFN_M16.MATERIAL_LOCATION
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ILT import ILT
from ..segments.IVT import IVT
from ..segments.NTE import NTE

_ILT = ILT
_IVT = IVT
_NTE = NTE


class MFN_M16_MATERIAL_LOCATION(HL7Model):
    """HL7 v2 MFN_M16.MATERIAL_LOCATION group.

    Attributes:
        IVT (IVT): required
        ILT (Optional[List[ILT]]): optional
        NTE (Optional[List[NTE]]): optional
    """

    IVT: _IVT = Field(
        default=...,
        title="IVT",
        description="Required",
    )

    ILT: Optional[List[_ILT]] = Field(
        default=None,
        title="ILT",
        description="Optional, repeating",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
