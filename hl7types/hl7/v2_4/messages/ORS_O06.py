"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: ORS_O06
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

from ..groups.ORS_O06_RSPONSE import ORS_O06_RSPONSE

_ERR = ERR
_MSA = MSA
_MSH = MSH
_NTE = NTE
_ORS_O06_RSPONSE = ORS_O06_RSPONSE


class ORS_O06(HL7Model):
    """ORS - Stock requisition acknowledgement (S4).

    Attributes:
        MSH (MSH): Message Header, required
        MSA (MSA): Message Acknowledgment, required
        ERR (Optional[ERR]): Error, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        RSPONSE (Optional[ORS_O06_RSPONSE]): optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    MSA: _MSA = Field(
        title="MSA",
        description="Message Acknowledgment",
    )

    ERR: Optional[_ERR] = Field(
        default=None,
        title="ERR",
        description="Error",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    RSPONSE: Optional[_ORS_O06_RSPONSE] = Field(
        default=None,
        title="RSPONSE",
    )

    model_config = {"populate_by_name": True}
