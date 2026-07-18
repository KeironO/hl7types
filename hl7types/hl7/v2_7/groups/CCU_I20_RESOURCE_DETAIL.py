"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: CCU_I20.RESOURCE_DETAIL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.OBX import OBX

from .CCU_I20_RESOURCE_OBJECT import CCU_I20_RESOURCE_OBJECT

_CCU_I20_RESOURCE_OBJECT = CCU_I20_RESOURCE_OBJECT
_OBX = OBX


class CCU_I20_RESOURCE_DETAIL(HL7Model):
    """HL7 v2 CCU_I20.RESOURCE_DETAIL group.

    Attributes:
        RESOURCE_OBJECT (CCU_I20_RESOURCE_OBJECT): required
        OBX (Optional[List[OBX]]): Observation/Result, optional
    """

    RESOURCE_OBJECT: _CCU_I20_RESOURCE_OBJECT = Field(
        title="RESOURCE_OBJECT",
    )

    OBX: Optional[List[_OBX]] = Field(
        default=None,
        title="OBX",
        description="Observation/Result",
    )

    model_config = ConfigDict(populate_by_name=True)
