"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: PPR_PC1.ORDER_DETAIL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.VAR import VAR

from .PPR_PC1_CHOICE import PPR_PC1_CHOICE
from .PPR_PC1_ORDER_OBSERVATION import PPR_PC1_ORDER_OBSERVATION

_NTE = NTE
_PPR_PC1_CHOICE = PPR_PC1_CHOICE
_PPR_PC1_ORDER_OBSERVATION = PPR_PC1_ORDER_OBSERVATION
_VAR = VAR


class PPR_PC1_ORDER_DETAIL(HL7Model):
    """HL7 v2 PPR_PC1.ORDER_DETAIL group.

    Attributes:
        CHOICE (PPR_PC1_CHOICE): required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        VAR (Optional[List[VAR]]): Variance, optional
        ORDER_OBSERVATION (Optional[List[PPR_PC1_ORDER_OBSERVATION]]): optional
    """

    CHOICE: _PPR_PC1_CHOICE = Field(
        title="CHOICE",
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

    model_config = ConfigDict(populate_by_name=True)
