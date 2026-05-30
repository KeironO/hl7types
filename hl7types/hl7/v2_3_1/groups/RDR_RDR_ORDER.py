"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: RDR_RDR.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ORC import ORC

from .RDR_RDR_DISPENSE import RDR_RDR_DISPENSE
from .RDR_RDR_ENCODING import RDR_RDR_ENCODING

_ORC = ORC
_RDR_RDR_DISPENSE = RDR_RDR_DISPENSE
_RDR_RDR_ENCODING = RDR_RDR_ENCODING


class RDR_RDR_ORDER(HL7Model):
    """HL7 v2 RDR_RDR.ORDER group.

    Attributes:
        ORC (ORC): required
        ENCODING (Optional[RDR_RDR_ENCODING]): optional
        DISPENSE (List[RDR_RDR_DISPENSE]): required
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    ENCODING: Optional[_RDR_RDR_ENCODING] = Field(
        default=None,
        title="ENCODING",
        description="Optional",
    )

    DISPENSE: List[_RDR_RDR_DISPENSE] = Field(
        default=...,
        title="DISPENSE",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
