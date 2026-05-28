"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: EHC_E21.PSL_ITEM_INFO
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.AUT import AUT
from ..segments.NTE import NTE
from ..segments.PSL import PSL

_AUT = AUT
_NTE = NTE
_PSL = PSL


class EHC_E21_PSL_ITEM_INFO(BaseModel):
    """HL7 v2 EHC_E21.PSL_ITEM_INFO group.

    Attributes:
        PSL (PSL): required
        NTE (Optional[List[NTE]]): optional
        AUT (Optional[AUT]): optional
    """

    PSL: _PSL = Field(
        default=...,
        title="PSL",
        description="Required",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    AUT: Optional[_AUT] = Field(
        default=None,
        title="AUT",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
