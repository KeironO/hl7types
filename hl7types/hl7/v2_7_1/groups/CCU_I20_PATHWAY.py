"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: CCU_I20.PATHWAY
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.OBX import OBX
from ..segments.PTH import PTH
from ..segments.VAR import VAR

from .CCU_I20_ROLE_PATHWAY import CCU_I20_ROLE_PATHWAY

_CCU_I20_ROLE_PATHWAY = CCU_I20_ROLE_PATHWAY
_OBX = OBX
_PTH = PTH
_VAR = VAR


class CCU_I20_PATHWAY(HL7Model):
    """HL7 v2 CCU_I20.PATHWAY group.

    Attributes:
        PTH (PTH): Pathway, required
        VAR (Optional[List[VAR]]): Variance, optional
        ROLE_PATHWAY (Optional[List[CCU_I20_ROLE_PATHWAY]]): optional
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

    ROLE_PATHWAY: Optional[List[_CCU_I20_ROLE_PATHWAY]] = Field(
        default=None,
        title="ROLE_PATHWAY",
    )

    OBX: Optional[List[_OBX]] = Field(
        default=None,
        title="OBX",
        description="Observation/Result",
    )

    model_config = {"populate_by_name": True}
