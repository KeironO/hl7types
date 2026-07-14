"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: PGL_PC6.PROBLEM_ROLE
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


class PGL_PC6_PROBLEM_ROLE(HL7Model):
    """HL7 v2 PGL_PC6.PROBLEM_ROLE group.

    Attributes:
        ROL (ROL): Role, required
        VAR (Optional[List[VAR]]): Variance, optional
    """

    ROL: _ROL = Field(
        title="ROL",
        description="Role",
    )

    VAR: Optional[List[_VAR]] = Field(
        default=None,
        title="VAR",
        description="Variance",
    )

    model_config = {"populate_by_name": True}
