"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: PRR_PC5.ORDER_DETAIL
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.VAR import VAR

from .PRR_PC5_OBRanyHL7Segment_SUPPGRP import PRR_PC5_OBRanyHL7Segment_SUPPGRP
from .PRR_PC5_ORDER_OBSERVATION import PRR_PC5_ORDER_OBSERVATION

_NTE = NTE
_PRR_PC5_OBRanyHL7Segment_SUPPGRP = PRR_PC5_OBRanyHL7Segment_SUPPGRP
_PRR_PC5_ORDER_OBSERVATION = PRR_PC5_ORDER_OBSERVATION
_VAR = VAR


class PRR_PC5_ORDER_DETAIL(BaseModel):
    """HL7 v2 PRR_PC5.ORDER_DETAIL group.

    Attributes:
        OBRanyHL7Segment_SUPPGRP (PRR_PC5_OBRanyHL7Segment_SUPPGRP): required
        NTE (Optional[List[NTE]]): optional
        VAR (Optional[List[VAR]]): optional
        ORDER_OBSERVATION (Optional[List[PRR_PC5_ORDER_OBSERVATION]]): optional
    """

    OBRanyHL7Segment_SUPPGRP: _PRR_PC5_OBRanyHL7Segment_SUPPGRP = Field(
        default=...,
        title="OBRanyHL7Segment_SUPPGRP",
        description="Required",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    VAR: Optional[List[_VAR]] = Field(
        default=None,
        title="VAR",
        description="Optional, repeating",
    )

    ORDER_OBSERVATION: Optional[List[_PRR_PC5_ORDER_OBSERVATION]] = Field(
        default=None,
        title="ORDER_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
