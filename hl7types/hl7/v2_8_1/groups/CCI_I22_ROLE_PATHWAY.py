"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: CCI_I22.ROLE_PATHWAY
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.VAR import VAR

from .CCI_I22_ROLE_PATHWAY_OBJECT import CCI_I22_ROLE_PATHWAY_OBJECT

_CCI_I22_ROLE_PATHWAY_OBJECT = CCI_I22_ROLE_PATHWAY_OBJECT
_VAR = VAR


class CCI_I22_ROLE_PATHWAY(HL7Model):
    """HL7 v2 CCI_I22.ROLE_PATHWAY group.

    Attributes:
        ROLE_PATHWAY_OBJECT (CCI_I22_ROLE_PATHWAY_OBJECT): required
        VAR (Optional[List[VAR]]): optional
    """

    ROLE_PATHWAY_OBJECT: _CCI_I22_ROLE_PATHWAY_OBJECT = Field(
        title="ROLE_PATHWAY_OBJECT",
        description="Required",
    )

    VAR: Optional[List[_VAR]] = Field(
        default=None,
        title="VAR",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
