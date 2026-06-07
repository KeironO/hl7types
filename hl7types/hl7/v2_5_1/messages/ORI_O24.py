"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
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
    """HL7 v2 ORI_O24 message.

    Attributes:
        MSH (MSH): required
        MSA (MSA): required
        ERR (Optional[List[ERR]]): optional
        SFT (Optional[List[SFT]]): optional
        NTE (Optional[List[NTE]]): optional
        RESPONSE (Optional[ORI_O24_RESPONSE]): optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Required",
    )

    MSA: _MSA = Field(
        title="MSA",
        description="Required",
    )

    ERR: Optional[List[_ERR]] = Field(
        default=None,
        title="ERR",
        description="Optional, repeating",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    RESPONSE: Optional[_ORI_O24_RESPONSE] = Field(
        default=None,
        title="RESPONSE",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
