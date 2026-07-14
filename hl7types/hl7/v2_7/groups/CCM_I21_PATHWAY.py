"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: CCM_I21.PATHWAY
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.OBX import OBX
from ..segments.PTH import PTH
from ..segments.VAR import VAR

from .CCM_I21_ROLE_PATHWAY import CCM_I21_ROLE_PATHWAY

_CCM_I21_ROLE_PATHWAY = CCM_I21_ROLE_PATHWAY
_OBX = OBX
_PTH = PTH
_VAR = VAR


class CCM_I21_PATHWAY(HL7Model):
    """HL7 v2 CCM_I21.PATHWAY group.

    Attributes:
        PTH (PTH): Pathway, required
        VAR (Optional[List[VAR]]): Variance, optional
        ROLE_PATHWAY (Optional[List[CCM_I21_ROLE_PATHWAY]]): optional
        OBX (Optional[List[OBX]]): Observation/Result, optional
    """

    PTH: _PTH = Field(
        title="PTH",
        description="Pathway",
    )

    VAR: Optional[List[_VAR]] = Field(
        default=None,
        title="VAR",
        description="Variance",
    )

    ROLE_PATHWAY: Optional[List[_CCM_I21_ROLE_PATHWAY]] = Field(
        default=None,
        title="ROLE_PATHWAY",
    )

    OBX: Optional[List[_OBX]] = Field(
        default=None,
        title="OBX",
        description="Observation/Result",
    )

    model_config = {"populate_by_name": True}
