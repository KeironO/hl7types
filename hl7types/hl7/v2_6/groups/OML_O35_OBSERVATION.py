"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: OML_O35.OBSERVATION
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.OBX import OBX
from ..segments.TCD import TCD

_NTE = NTE
_OBX = OBX
_TCD = TCD


class OML_O35_OBSERVATION(HL7Model):
    """HL7 v2 OML_O35.OBSERVATION group.

    Attributes:
        OBX (OBX): required
        TCD (Optional[TCD]): optional
        NTE (Optional[List[NTE]]): optional
    """

    OBX: _OBX = Field(
        title="OBX",
        description="Required",
    )

    TCD: Optional[_TCD] = Field(
        default=None,
        title="TCD",
        description="Optional",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
