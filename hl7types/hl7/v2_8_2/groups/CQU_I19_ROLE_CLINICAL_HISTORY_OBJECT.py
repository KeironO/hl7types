"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: CQU_I19.ROLE_CLINICAL_HISTORY_OBJECT
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.PRD import PRD
from ..segments.ROL import ROL

_PRD = PRD
_ROL = ROL


class CQU_I19_ROLE_CLINICAL_HISTORY_OBJECT(HL7Model):
    """HL7 v2 CQU_I19.ROLE_CLINICAL_HISTORY_OBJECT group.

    Attributes:
        ROL (Optional[ROL]): Role, optional
        PRD (Optional[PRD]): Provider Data, optional
    """

    ROL: Optional[_ROL] = Field(
        default=None,
        title="ROL",
        description="Role",
    )

    PRD: Optional[_PRD] = Field(
        default=None,
        title="PRD",
        description="Provider Data",
    )

    model_config = ConfigDict(populate_by_name=True)
