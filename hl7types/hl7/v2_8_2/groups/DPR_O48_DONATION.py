"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: DPR_O48.DONATION
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.DON import DON
from ..segments.NTE import NTE
from ..segments.OBX import OBX

from .DPR_O48_BLOOD_UNIT import DPR_O48_BLOOD_UNIT

_DON = DON
_DPR_O48_BLOOD_UNIT = DPR_O48_BLOOD_UNIT
_NTE = NTE
_OBX = OBX


class DPR_O48_DONATION(HL7Model):
    """HL7 v2 DPR_O48.DONATION group.

    Attributes:
        DON (DON): Donation, required
        OBX (Optional[List[OBX]]): Observation/Result, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        BLOOD_UNIT (Optional[DPR_O48_BLOOD_UNIT]): optional
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

    BLOOD_UNIT: Optional[_DPR_O48_BLOOD_UNIT] = Field(
        default=None,
        title="BLOOD_UNIT",
    )

    model_config = ConfigDict(populate_by_name=True)
