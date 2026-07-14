"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: EHC_E01.PROCEDURE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.PR1 import PR1
from ..segments.ROL import ROL

_NTE = NTE
_PR1 = PR1
_ROL = ROL


class EHC_E01_PROCEDURE(HL7Model):
    """HL7 v2 EHC_E01.PROCEDURE group.

    Attributes:
        PR1 (PR1): Procedures, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        ROL (Optional[List[ROL]]): Role, optional
    """

    PR1: _PR1 = Field(
        title="PR1",
        description="Procedures",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    ROL: Optional[List[_ROL]] = Field(
        default=None,
        title="ROL",
        description="Role",
    )

    model_config = {"populate_by_name": True}
