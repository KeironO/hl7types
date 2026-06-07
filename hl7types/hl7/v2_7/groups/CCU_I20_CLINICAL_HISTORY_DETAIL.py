"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: CCU_I20.CLINICAL_HISTORY_DETAIL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.OBX import OBX

from .CCU_I20_CLINICAL_HISTORY_OBJECT import CCU_I20_CLINICAL_HISTORY_OBJECT

_CCU_I20_CLINICAL_HISTORY_OBJECT = CCU_I20_CLINICAL_HISTORY_OBJECT
_OBX = OBX


class CCU_I20_CLINICAL_HISTORY_DETAIL(HL7Model):
    """HL7 v2 CCU_I20.CLINICAL_HISTORY_DETAIL group.

    Attributes:
        CLINICAL_HISTORY_OBJECT (CCU_I20_CLINICAL_HISTORY_OBJECT): required
        OBX (Optional[List[OBX]]): optional
    """

    CLINICAL_HISTORY_OBJECT: _CCU_I20_CLINICAL_HISTORY_OBJECT = Field(
        title="CLINICAL_HISTORY_OBJECT",
        description="Required",
    )

    OBX: Optional[List[_OBX]] = Field(
        default=None,
        title="OBX",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
