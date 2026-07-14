"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: EAR_U08
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.EQU import EQU
from ..segments.MSH import MSH
from ..segments.ROL import ROL

from ..groups.EAR_U08_COMMAND_RESPONSE import EAR_U08_COMMAND_RESPONSE

_EAR_U08_COMMAND_RESPONSE = EAR_U08_COMMAND_RESPONSE
_EQU = EQU
_MSH = MSH
_ROL = ROL


class EAR_U08(HL7Model):
    """EAR/ACK - Automated equipment response (S13).

    Attributes:
        MSH (MSH): Message Header, required
        EQU (EQU): Equipment Detail, required
        COMMAND_RESPONSE (List[EAR_U08_COMMAND_RESPONSE]): required
        ROL (Optional[ROL]): Role, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    EQU: _EQU = Field(
        title="EQU",
        description="Equipment Detail",
    )

    COMMAND_RESPONSE: List[_EAR_U08_COMMAND_RESPONSE] = Field(
        min_length=1,
        title="COMMAND_RESPONSE",
    )

    ROL: Optional[_ROL] = Field(
        default=None,
        title="ROL",
        description="Role",
    )

    model_config = {"populate_by_name": True}
