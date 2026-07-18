"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: DER_O44.DONOR_ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.OBR import OBR

_NTE = NTE
_OBR = OBR


class DER_O44_DONOR_ORDER(HL7Model):
    """HL7 v2 DER_O44.DONOR_ORDER group.

    Attributes:
        OBR (OBR): Observation Request, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
    """

    OBR: _OBR = Field(
        title="OBR",
        description="Observation Request",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    model_config = ConfigDict(populate_by_name=True)
