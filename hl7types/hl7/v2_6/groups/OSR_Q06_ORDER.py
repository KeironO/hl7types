"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: OSR_Q06.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.CTI import CTI
from ..segments.NTE import NTE
from ..segments.ORC import ORC

from .OSR_Q06_CHOICE import OSR_Q06_CHOICE
from .OSR_Q06_TIMING import OSR_Q06_TIMING

_CTI = CTI
_NTE = NTE
_ORC = ORC
_OSR_Q06_CHOICE = OSR_Q06_CHOICE
_OSR_Q06_TIMING = OSR_Q06_TIMING


class OSR_Q06_ORDER(HL7Model):
    """HL7 v2 OSR_Q06.ORDER group.

    Attributes:
        ORC (ORC): Common Order, required
        TIMING (Optional[List[OSR_Q06_TIMING]]): optional
        CHOICE (OSR_Q06_CHOICE): required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        CTI (Optional[List[CTI]]): Clinical Trial Identification, optional
    """

    ORC: _ORC = Field(
        title="ORC",
        description="Common Order",
    )

    TIMING: Optional[List[_OSR_Q06_TIMING]] = Field(
        default=None,
        title="TIMING",
    )

    CHOICE: _OSR_Q06_CHOICE = Field(
        title="CHOICE",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    CTI: Optional[List[_CTI]] = Field(
        default=None,
        title="CTI",
        description="Clinical Trial Identification",
    )

    model_config = ConfigDict(populate_by_name=True)
