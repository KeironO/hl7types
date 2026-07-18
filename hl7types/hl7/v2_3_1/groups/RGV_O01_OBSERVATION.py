"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: RGV_O01.OBSERVATION
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.OBX import OBX

_NTE = NTE
_OBX = OBX


class RGV_O01_OBSERVATION(HL7Model):
    """HL7 v2 RGV_O01.OBSERVATION group.

    Attributes:
        OBX (Optional[OBX]): OBX - observation/result segment, optional
        NTE (Optional[List[NTE]]): NTE - notes and comments segment, optional
    """

    OBX: Optional[_OBX] = Field(
        default=None,
        title="OBX",
        description="OBX - observation/result segment",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="NTE - notes and comments segment",
    )

    model_config = ConfigDict(populate_by_name=True)
