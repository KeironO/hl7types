"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: DER_O44.DONOR_REGISTRATION
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.PV1 import PV1

_NTE = NTE
_PV1 = PV1


class DER_O44_DONOR_REGISTRATION(HL7Model):
    """HL7 v2 DER_O44.DONOR_REGISTRATION group.

    Attributes:
        PV1 (Optional[PV1]): optional
        NTE (Optional[List[NTE]]): optional
    """

    PV1: Optional[_PV1] = Field(
        default=None,
        title="PV1",
        description="Optional",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
