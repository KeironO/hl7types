"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: EHC_E12.REQUEST
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.CTD import CTD
from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segments.OBX import OBX

_CTD = CTD
_NTE = NTE
_OBR = OBR
_OBX = OBX


class EHC_E12_REQUEST(HL7Model):
    """HL7 v2 EHC_E12.REQUEST group.

    Attributes:
        CTD (Optional[CTD]): Contact Data, optional
        OBR (OBR): Observation Request, required
        NTE (Optional[NTE]): Notes and Comments, optional
        OBX (Optional[List[OBX]]): Observation/Result, optional
    """

    CTD: Optional[_CTD] = Field(
        default=None,
        title="CTD",
        description="Contact Data",
    )

    OBR: _OBR = Field(
        title="OBR",
        description="Observation Request",
    )

    NTE: Optional[_NTE] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    OBX: Optional[List[_OBX]] = Field(
        default=None,
        title="OBX",
        description="Observation/Result",
    )

    model_config = {"populate_by_name": True}
