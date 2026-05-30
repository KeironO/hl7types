"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: CQU_I19.RESOURCE_DETAIL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.OBX import OBX

from .CQU_I19_RESOURCE_OBJECT import CQU_I19_RESOURCE_OBJECT

_CQU_I19_RESOURCE_OBJECT = CQU_I19_RESOURCE_OBJECT
_OBX = OBX


class CQU_I19_RESOURCE_DETAIL(HL7Model):
    """HL7 v2 CQU_I19.RESOURCE_DETAIL group.

    Attributes:
        RESOURCE_OBJECT (CQU_I19_RESOURCE_OBJECT): required
        OBX (Optional[List[OBX]]): optional
    """

    RESOURCE_OBJECT: _CQU_I19_RESOURCE_OBJECT = Field(
        default=...,
        title="RESOURCE_OBJECT",
        description="Required",
    )

    OBX: Optional[List[_OBX]] = Field(
        default=None,
        title="OBX",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
