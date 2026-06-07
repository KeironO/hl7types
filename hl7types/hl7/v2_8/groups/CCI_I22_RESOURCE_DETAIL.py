"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: CCI_I22.RESOURCE_DETAIL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from .CCI_I22_RESOURCE_OBJECT import CCI_I22_RESOURCE_OBJECT
from .CCI_I22_RESOURCE_OBSERVATION import CCI_I22_RESOURCE_OBSERVATION

_CCI_I22_RESOURCE_OBJECT = CCI_I22_RESOURCE_OBJECT
_CCI_I22_RESOURCE_OBSERVATION = CCI_I22_RESOURCE_OBSERVATION


class CCI_I22_RESOURCE_DETAIL(HL7Model):
    """HL7 v2 CCI_I22.RESOURCE_DETAIL group.

    Attributes:
        RESOURCE_OBJECT (CCI_I22_RESOURCE_OBJECT): required
        RESOURCE_OBSERVATION (Optional[List[CCI_I22_RESOURCE_OBSERVATION]]): optional
    """

    RESOURCE_OBJECT: _CCI_I22_RESOURCE_OBJECT = Field(
        title="RESOURCE_OBJECT",
        description="Required",
    )

    RESOURCE_OBSERVATION: Optional[List[_CCI_I22_RESOURCE_OBSERVATION]] = Field(
        default=None,
        title="RESOURCE_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
