"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: RSP_O34.DONATION
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.DON import DON
from ..segments.NTE import NTE
from ..segments.OBX import OBX

_DON = DON
_NTE = NTE
_OBX = OBX


class RSP_O34_DONATION(HL7Model):
    """HL7 v2 RSP_O34.DONATION group.

    Attributes:
        DON (DON): Donation, required
        OBX (Optional[List[OBX]]): Observation/Result, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
    """

    DON: _DON = Field(
        title="DON",
        description="Donation",
    )

    OBX: Optional[List[_OBX]] = Field(
        default=None,
        title="OBX",
        description="Observation/Result",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    model_config = {"populate_by_name": True}
