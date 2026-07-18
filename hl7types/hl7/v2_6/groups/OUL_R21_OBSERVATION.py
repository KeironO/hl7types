"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: OUL_R21.OBSERVATION
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.OBX import OBX
from ..segments.SID import SID
from ..segments.TCD import TCD

_NTE = NTE
_OBX = OBX
_SID = SID
_TCD = TCD


class OUL_R21_OBSERVATION(HL7Model):
    """HL7 v2 OUL_R21.OBSERVATION group.

    Attributes:
        OBX (Optional[OBX]): Observation/Result, optional
        TCD (Optional[TCD]): Test Code Detail, optional
        SID (Optional[List[SID]]): Substance Identifier, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
    """

    OBX: Optional[_OBX] = Field(
        default=None,
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

    model_config = ConfigDict(populate_by_name=True)
