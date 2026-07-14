"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: ORI_O24
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.SFT import SFT

from ..groups.ORI_O24_RESPONSE import ORI_O24_RESPONSE

_ERR = ERR
_MSA = MSA
_MSH = MSH
_NTE = NTE
_ORI_O24_RESPONSE = ORI_O24_RESPONSE
_SFT = SFT


class ORI_O24(HL7Model):
    """ORI - Imaging order response message to any OMI (S4.4.13).

    Attributes:
        MSH (MSH): Message Header, required
        MSA (MSA): Message Acknowledgment, required
        ERR (Optional[List[ERR]]): Error, optional
        SFT (Optional[List[SFT]]): Software Segment, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        RESPONSE (Optional[ORI_O24_RESPONSE]): optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    MSA: _MSA = Field(
        title="MSA",
        description="Message Acknowledgment",
    )

    ERR: Optional[List[_ERR]] = Field(
        default=None,
        title="ERR",
        description="Error",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Software Segment",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    RESPONSE: Optional[_ORI_O24_RESPONSE] = Field(
        default=None,
        title="RESPONSE",
    )

    model_config = {"populate_by_name": True}
