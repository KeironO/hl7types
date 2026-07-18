"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: CCR_I16.RESOURCE_DETAIL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.OBX import OBX

from .CCR_I16_RESOURCE_OBJECT import CCR_I16_RESOURCE_OBJECT

_CCR_I16_RESOURCE_OBJECT = CCR_I16_RESOURCE_OBJECT
_OBX = OBX


class CCR_I16_RESOURCE_DETAIL(HL7Model):
    """HL7 v2 CCR_I16.RESOURCE_DETAIL group.

    Attributes:
        RESOURCE_OBJECT (CCR_I16_RESOURCE_OBJECT): required
        OBX (Optional[List[OBX]]): Observation/Result, optional
    """

    RESOURCE_OBJECT: _CCR_I16_RESOURCE_OBJECT = Field(
        title="RESOURCE_OBJECT",
    )

    OBX: Optional[List[_OBX]] = Field(
        default=None,
        title="OBX",
        description="Observation/Result",
    )

    model_config = ConfigDict(populate_by_name=True)
