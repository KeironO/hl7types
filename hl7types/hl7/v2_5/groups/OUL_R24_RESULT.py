"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: OUL_R24.RESULT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.OBX import OBX
from ..segments.SID import SID
from ..segments.TCD import TCD

_NTE = NTE
_OBX = OBX
_SID = SID
_TCD = TCD


class OUL_R24_RESULT(HL7Model):
    """HL7 v2 OUL_R24.RESULT group.

    Attributes:
        OBX (OBX): Observation/Result, required
        TCD (Optional[TCD]): Test Code Detail, optional
        SID (Optional[List[SID]]): Substance Identifier, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
    """

    OBX: _OBX = Field(
        title="OBX",
        description="Observation/Result",
    )

    TCD: Optional[_TCD] = Field(
        default=None,
        title="TCD",
        description="Test Code Detail",
    )

    SID: Optional[List[_SID]] = Field(
        default=None,
        title="SID",
        description="Substance Identifier",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    model_config = {"populate_by_name": True}
