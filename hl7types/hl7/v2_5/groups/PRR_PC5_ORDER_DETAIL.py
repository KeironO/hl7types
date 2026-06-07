"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: PRR_PC5.ORDER_DETAIL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.VAR import VAR

from .PRR_PC5_CHOICE import PRR_PC5_CHOICE
from .PRR_PC5_ORDER_OBSERVATION import PRR_PC5_ORDER_OBSERVATION

_NTE = NTE
_PRR_PC5_CHOICE = PRR_PC5_CHOICE
_PRR_PC5_ORDER_OBSERVATION = PRR_PC5_ORDER_OBSERVATION
_VAR = VAR


class PRR_PC5_ORDER_DETAIL(HL7Model):
    """HL7 v2 PRR_PC5.ORDER_DETAIL group.

    Attributes:
        CHOICE (PRR_PC5_CHOICE): required
        NTE (Optional[List[NTE]]): optional
        VAR (Optional[List[VAR]]): optional
        ORDER_OBSERVATION (Optional[List[PRR_PC5_ORDER_OBSERVATION]]): optional
    """

    CHOICE: _PRR_PC5_CHOICE = Field(
        title="CHOICE",
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
