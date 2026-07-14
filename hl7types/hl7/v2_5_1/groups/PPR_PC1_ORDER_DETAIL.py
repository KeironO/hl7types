"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: PPR_PC1.ORDER_DETAIL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.VAR import VAR

from .PPR_PC1_OBR_SUPPGRP import PPR_PC1_OBR_SUPPGRP
from .PPR_PC1_ORDER_OBSERVATION import PPR_PC1_ORDER_OBSERVATION

_NTE = NTE
_PPR_PC1_OBR_SUPPGRP = PPR_PC1_OBR_SUPPGRP
_PPR_PC1_ORDER_OBSERVATION = PPR_PC1_ORDER_OBSERVATION
_VAR = VAR


class PPR_PC1_ORDER_DETAIL(HL7Model):
    """HL7 v2 PPR_PC1.ORDER_DETAIL group.

    Attributes:
        OBR_SUPPGRP (PPR_PC1_OBR_SUPPGRP): required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        VAR (Optional[List[VAR]]): Variance, optional
        ORDER_OBSERVATION (Optional[List[PPR_PC1_ORDER_OBSERVATION]]): optional
    """

    OBR_SUPPGRP: _PPR_PC1_OBR_SUPPGRP = Field(
        title="OBR_SUPPGRP",
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

    ORDER_OBSERVATION: Optional[List[_PPR_PC1_ORDER_OBSERVATION]] = Field(
        default=None,
        title="ORDER_OBSERVATION",
    )

    model_config = {"populate_by_name": True}
