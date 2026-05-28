"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: ORS_O06
Type: Message
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.NTE import NTE

from ..groups.ORS_O06_RSPONSE import ORS_O06_RSPONSE

_ERR = ERR
_MSA = MSA
_MSH = MSH
_NTE = NTE
_ORS_O06_RSPONSE = ORS_O06_RSPONSE


class ORS_O06(BaseModel):
    """HL7 v2 ORS_O06 message.

    Attributes:
        MSH (MSH): required
        MSA (MSA): required
        ERR (Optional[ERR]): optional
        NTE (Optional[List[NTE]]): optional
        RSPONSE (Optional[ORS_O06_RSPONSE]): optional
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    MSA: _MSA = Field(
        default=...,
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

    RSPONSE: Optional[_ORS_O06_RSPONSE] = Field(
        default=None,
        title="RSPONSE",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
