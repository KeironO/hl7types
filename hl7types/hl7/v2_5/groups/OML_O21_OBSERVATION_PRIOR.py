"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: OML_O21.OBSERVATION_PRIOR
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.OBX import OBX

_NTE = NTE
_OBX = OBX


class OML_O21_OBSERVATION_PRIOR(HL7Model):
    """HL7 v2 OML_O21.OBSERVATION_PRIOR group.

    Attributes:
        OBX (OBX): Observation/Result, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
    """

    OBX: _OBX = Field(
        title="OBX",
        description="Observation/Result",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    model_config = {"populate_by_name": True}
