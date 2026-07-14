"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: SQR_S25.GENERAL_RESOURCE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.AIG import AIG
from ..segments.NTE import NTE

_AIG = AIG
_NTE = NTE


class SQR_S25_GENERAL_RESOURCE(HL7Model):
    """HL7 v2 SQR_S25.GENERAL_RESOURCE group.

    Attributes:
        AIG (AIG): Appointment Information - General Resource, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
    """

    AIG: _AIG = Field(
        title="AIG",
        description="Appointment Information - General Resource",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    model_config = {"populate_by_name": True}
