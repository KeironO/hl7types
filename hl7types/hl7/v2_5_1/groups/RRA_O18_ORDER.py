"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: RRA_O18.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ORC import ORC

from .RRA_O18_ADMINISTRATION import RRA_O18_ADMINISTRATION
from .RRA_O18_TIMING import RRA_O18_TIMING

_ORC = ORC
_RRA_O18_ADMINISTRATION = RRA_O18_ADMINISTRATION
_RRA_O18_TIMING = RRA_O18_TIMING


class RRA_O18_ORDER(HL7Model):
    """HL7 v2 RRA_O18.ORDER group.

    Attributes:
        ORC (ORC): required
        TIMING (Optional[List[RRA_O18_TIMING]]): optional
        ADMINISTRATION (Optional[RRA_O18_ADMINISTRATION]): optional
    """

    ORC: _ORC = Field(
        title="ORC",
        description="Required",
    )

    TIMING: Optional[List[_RRA_O18_TIMING]] = Field(
        default=None,
        title="TIMING",
        description="Optional, repeating",
    )

    ADMINISTRATION: Optional[_RRA_O18_ADMINISTRATION] = Field(
        default=None,
        title="ADMINISTRATION",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
