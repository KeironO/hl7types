"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: RRA_O02.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ORC import ORC

from .RRA_O02_ADMINISTRATION import RRA_O02_ADMINISTRATION

_ORC = ORC
_RRA_O02_ADMINISTRATION = RRA_O02_ADMINISTRATION


class RRA_O02_ORDER(HL7Model):
    """HL7 v2 RRA_O02.ORDER group.

    Attributes:
        ORC (ORC): required
        ADMINISTRATION (Optional[List[RRA_O02_ADMINISTRATION]]): optional
    """

    ORC: _ORC = Field(
        title="ORC",
        description="Required",
    )

    ADMINISTRATION: Optional[List[_RRA_O02_ADMINISTRATION]] = Field(
        default=None,
        title="ADMINISTRATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
