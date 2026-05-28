"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: MFN_M16.MATERIAL_ITEM_RECORD
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.ITM import ITM
from ..segments.MFE import MFE
from ..segments.NTE import NTE

from .MFN_M16_MATERIAL_LOCATION import MFN_M16_MATERIAL_LOCATION
from .MFN_M16_PURCHASING_VENDOR import MFN_M16_PURCHASING_VENDOR
from .MFN_M16_STERILIZATION import MFN_M16_STERILIZATION

_ITM = ITM
_MFE = MFE
_MFN_M16_MATERIAL_LOCATION = MFN_M16_MATERIAL_LOCATION
_MFN_M16_PURCHASING_VENDOR = MFN_M16_PURCHASING_VENDOR
_MFN_M16_STERILIZATION = MFN_M16_STERILIZATION
_NTE = NTE


class MFN_M16_MATERIAL_ITEM_RECORD(BaseModel):
    """HL7 v2 MFN_M16.MATERIAL_ITEM_RECORD group.

    Attributes:
        MFE (MFE): required
        ITM (ITM): required
        NTE (Optional[List[NTE]]): optional
        STERILIZATION (Optional[List[MFN_M16_STERILIZATION]]): optional
        PURCHASING_VENDOR (Optional[List[MFN_M16_PURCHASING_VENDOR]]): optional
        MATERIAL_LOCATION (Optional[List[MFN_M16_MATERIAL_LOCATION]]): optional
    """

    MFE: _MFE = Field(
        default=...,
        title="MFE",
        description="Required",
    )

    ITM: _ITM = Field(
        default=...,
        title="ITM",
        description="Required",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    STERILIZATION: Optional[List[_MFN_M16_STERILIZATION]] = Field(
        default=None,
        title="STERILIZATION",
        description="Optional, repeating",
    )

    PURCHASING_VENDOR: Optional[List[_MFN_M16_PURCHASING_VENDOR]] = Field(
        default=None,
        title="PURCHASING_VENDOR",
        description="Optional, repeating",
    )

    MATERIAL_LOCATION: Optional[List[_MFN_M16_MATERIAL_LOCATION]] = Field(
        default=None,
        title="MATERIAL_LOCATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
