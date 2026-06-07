"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: RRE_O02.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ORC import ORC

from .RRE_O02_ENCODING import RRE_O02_ENCODING

_ORC = ORC
_RRE_O02_ENCODING = RRE_O02_ENCODING


class RRE_O02_ORDER(HL7Model):
    """HL7 v2 RRE_O02.ORDER group.

    Attributes:
        ORC (ORC): required
        ENCODING (Optional[RRE_O02_ENCODING]): optional
    """

    ORC: _ORC = Field(
        title="ORC",
        description="Required",
    )

    ENCODING: Optional[_RRE_O02_ENCODING] = Field(
        default=None,
        title="ENCODING",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
