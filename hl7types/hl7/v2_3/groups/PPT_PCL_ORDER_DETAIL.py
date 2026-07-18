"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: PPT_PCL.ORDER_DETAIL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segments.VAR import VAR

from .PPT_PCL_ORDER_OBSERVATION import PPT_PCL_ORDER_OBSERVATION

_NTE = NTE
_OBR = OBR
_PPT_PCL_ORDER_OBSERVATION = PPT_PCL_ORDER_OBSERVATION
_VAR = VAR


class PPT_PCL_ORDER_DETAIL(HL7Model):
    """HL7 v2 PPT_PCL.ORDER_DETAIL group.

    Attributes:
        OBR (OBR): Observation request segment, required
        NTE (Optional[List[NTE]]): Notes and comments segment, optional
        VAR (Optional[List[VAR]]): Variance, optional
        ORDER_OBSERVATION (Optional[List[PPT_PCL_ORDER_OBSERVATION]]): optional
    """

    OBR: _OBR = Field(
        title="OBR",
        description="Observation request segment",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and comments segment",
    )

    VAR: Optional[List[_VAR]] = Field(
        default=None,
        title="VAR",
        description="Variance",
    )

    ORDER_OBSERVATION: Optional[List[_PPT_PCL_ORDER_OBSERVATION]] = Field(
        default=None,
        title="ORDER_OBSERVATION",
    )

    model_config = ConfigDict(populate_by_name=True)
