"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: CCI_I22.CLINICAL_HISTORY_DETAIL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.OBX import OBX

from .CCI_I22_CLINICAL_HISTORY_OBJECT import CCI_I22_CLINICAL_HISTORY_OBJECT

_CCI_I22_CLINICAL_HISTORY_OBJECT = CCI_I22_CLINICAL_HISTORY_OBJECT
_OBX = OBX


class CCI_I22_CLINICAL_HISTORY_DETAIL(HL7Model):
    """HL7 v2 CCI_I22.CLINICAL_HISTORY_DETAIL group.

    Attributes:
        CLINICAL_HISTORY_OBJECT (CCI_I22_CLINICAL_HISTORY_OBJECT): required
        OBX (Optional[List[OBX]]): optional
    """

    CLINICAL_HISTORY_OBJECT: _CCI_I22_CLINICAL_HISTORY_OBJECT = Field(
        default=...,
        title="CLINICAL_HISTORY_OBJECT",
        description="Required",
    )

    OBX: Optional[List[_OBX]] = Field(
        default=None,
        title="OBX",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
