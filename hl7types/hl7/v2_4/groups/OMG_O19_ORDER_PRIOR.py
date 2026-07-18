"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: OMG_O19.ORDER_PRIOR
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.CTD import CTD
from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segments.ORC import ORC

from .OMG_O19_OBSERVATION_PRIOR import OMG_O19_OBSERVATION_PRIOR

_CTD = CTD
_NTE = NTE
_OBR = OBR
_OMG_O19_OBSERVATION_PRIOR = OMG_O19_OBSERVATION_PRIOR
_ORC = ORC


class OMG_O19_ORDER_PRIOR(HL7Model):
    """HL7 v2 OMG_O19.ORDER_PRIOR group.

    Attributes:
        ORC (Optional[ORC]): Common Order, optional
        OBR (OBR): Observation Request, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        CTD (Optional[CTD]): Contact Data, optional
        OBSERVATION_PRIOR (List[OMG_O19_OBSERVATION_PRIOR]): required
    """

    ORC: Optional[_ORC] = Field(
        default=None,
        title="ORC",
        description="Common Order",
    )

    OBR: _OBR = Field(
        title="OBR",
        description="Observation Request",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    CTD: Optional[_CTD] = Field(
        default=None,
        title="CTD",
        description="Contact Data",
    )

    OBSERVATION_PRIOR: List[_OMG_O19_OBSERVATION_PRIOR] = Field(
        min_length=1,
        title="OBSERVATION_PRIOR",
    )

    model_config = ConfigDict(populate_by_name=True)
