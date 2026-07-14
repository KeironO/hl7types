"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: OSR_Q06.OBSERVATION
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.CTI import CTI
from ..segments.NTE import NTE
from ..segments.ORC import ORC

from .OSR_Q06_CHOICE import OSR_Q06_CHOICE

_CTI = CTI
_NTE = NTE
_ORC = ORC
_OSR_Q06_CHOICE = OSR_Q06_CHOICE


class OSR_Q06_OBSERVATION(HL7Model):
    """HL7 v2 OSR_Q06.OBSERVATION group.

    Attributes:
        ORC (ORC): ORC - common order segment, required
        CHOICE (OSR_Q06_CHOICE): required
        NTE (Optional[List[NTE]]): NTE - notes and comments segment, optional
        CTI (Optional[List[CTI]]): CTI - clinical trial identification segment, optional
    """

    ORC: _ORC = Field(
        title="ORC",
        description="ORC - common order segment",
    )

    CHOICE: _OSR_Q06_CHOICE = Field(
        title="CHOICE",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="NTE - notes and comments segment",
    )

    CTI: Optional[List[_CTI]] = Field(
        default=None,
        title="CTI",
        description="CTI - clinical trial identification segment",
    )

    model_config = {"populate_by_name": True}
