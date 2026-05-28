"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: EHC_E13.REQUEST
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.CTD import CTD
from ..segments.NTE import NTE
from ..segments.OBR import OBR

from .EHC_E13_RESPONSE import EHC_E13_RESPONSE

_CTD = CTD
_EHC_E13_RESPONSE = EHC_E13_RESPONSE
_NTE = NTE
_OBR = OBR


class EHC_E13_REQUEST(BaseModel):
    """HL7 v2 EHC_E13.REQUEST group.

    Attributes:
        CTD (Optional[CTD]): optional
        OBR (OBR): required
        NTE (Optional[NTE]): optional
        RESPONSE (List[EHC_E13_RESPONSE]): required
    """

    CTD: Optional[_CTD] = Field(
        default=None,
        title="CTD",
        description="Optional",
    )

    OBR: _OBR = Field(
        default=...,
        title="OBR",
        description="Required",
    )

    NTE: Optional[_NTE] = Field(
        default=None,
        title="NTE",
        description="Optional",
    )

    RESPONSE: List[_EHC_E13_RESPONSE] = Field(
        default=...,
        title="RESPONSE",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
