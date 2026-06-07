"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: ORP_O10
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

from ..groups.ORP_O10_RESPONSE import ORP_O10_RESPONSE

_ERR = ERR
_MSA = MSA
_MSH = MSH
_NTE = NTE
_ORP_O10_RESPONSE = ORP_O10_RESPONSE


class ORP_O10(HL7Model):
    """HL7 v2 ORP_O10 message.

    Attributes:
        MSH (MSH): required
        MSA (MSA): required
        ERR (Optional[ERR]): optional
        NTE (Optional[List[NTE]]): optional
        RESPONSE (Optional[ORP_O10_RESPONSE]): optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Required",
    )

    MSA: _MSA = Field(
        title="MSA",
        description="Required",
    )

    ERR: Optional[_ERR] = Field(
        default=None,
        title="ERR",
        description="Optional",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    RESPONSE: Optional[_ORP_O10_RESPONSE] = Field(
        default=None,
        title="RESPONSE",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
