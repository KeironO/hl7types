"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: PTR_PCF.ORDER_OBSERVATION
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.OBX import OBX
from ..segments.VAR import VAR

_NTE = NTE
_OBX = OBX
_VAR = VAR


class PTR_PCF_ORDER_OBSERVATION(HL7Model):
    """HL7 v2 PTR_PCF.ORDER_OBSERVATION group.

    Attributes:
        OBX (OBX): Observation/Result, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        VAR (Optional[List[VAR]]): Variance, optional
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

    VAR: Optional[List[_VAR]] = Field(
        default=None,
        title="VAR",
        description="Variance",
    )

    model_config = {"populate_by_name": True}
