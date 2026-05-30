"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: PPT_PCL.PATHWAY_ROLE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ROL import ROL
from ..segments.VAR import VAR

_ROL = ROL
_VAR = VAR


class PPT_PCL_PATHWAY_ROLE(HL7Model):
    """HL7 v2 PPT_PCL.PATHWAY_ROLE group.

    Attributes:
        ROL (ROL): required
        VAR (Optional[List[VAR]]): optional
    """

    ROL: _ROL = Field(
        default=...,
        title="ROL",
        description="Required",
    )

    VAR: Optional[List[_VAR]] = Field(
        default=None,
        title="VAR",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
