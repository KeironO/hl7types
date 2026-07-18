"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: CCR_I16.ROLE_PATHWAY
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.VAR import VAR

from .CCR_I16_ROLE_PATHWAY_OBJECT import CCR_I16_ROLE_PATHWAY_OBJECT

_CCR_I16_ROLE_PATHWAY_OBJECT = CCR_I16_ROLE_PATHWAY_OBJECT
_VAR = VAR


class CCR_I16_ROLE_PATHWAY(HL7Model):
    """HL7 v2 CCR_I16.ROLE_PATHWAY group.

    Attributes:
        ROLE_PATHWAY_OBJECT (CCR_I16_ROLE_PATHWAY_OBJECT): required
        VAR (Optional[List[VAR]]): Variance, optional
    """

    ROLE_PATHWAY_OBJECT: _CCR_I16_ROLE_PATHWAY_OBJECT = Field(
        title="ROLE_PATHWAY_OBJECT",
    )

    VAR: Optional[List[_VAR]] = Field(
        default=None,
        title="VAR",
        description="Variance",
    )

    model_config = ConfigDict(populate_by_name=True)
