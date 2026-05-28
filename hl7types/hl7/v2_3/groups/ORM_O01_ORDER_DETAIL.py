"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: ORM_O01.ORDER_DETAIL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.DG1 import DG1
from ..segments.NTE import NTE

from .ORM_O01_CHOICE import ORM_O01_CHOICE
from .ORM_O01_OBSERVATION import ORM_O01_OBSERVATION

_DG1 = DG1
_NTE = NTE
_ORM_O01_CHOICE = ORM_O01_CHOICE
_ORM_O01_OBSERVATION = ORM_O01_OBSERVATION


class ORM_O01_ORDER_DETAIL(BaseModel):
    """HL7 v2 ORM_O01.ORDER_DETAIL group.

    Attributes:
        CHOICE (ORM_O01_CHOICE): required
        NTE (Optional[List[NTE]]): optional
        DG1 (Optional[List[DG1]]): optional
        OBSERVATION (Optional[List[ORM_O01_OBSERVATION]]): optional
    """

    CHOICE: _ORM_O01_CHOICE = Field(
        default=...,
        title="CHOICE",
        description="Required",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    DG1: Optional[List[_DG1]] = Field(
        default=None,
        title="DG1",
        description="Optional, repeating",
    )

    OBSERVATION: Optional[List[_ORM_O01_OBSERVATION]] = Field(
        default=None,
        title="OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
