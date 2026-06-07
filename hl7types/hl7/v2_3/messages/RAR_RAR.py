"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: RAR_RAR
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.DSC import DSC
from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH

from ..groups.RAR_RAR_DEFINITION import RAR_RAR_DEFINITION

_DSC = DSC
_ERR = ERR
_MSA = MSA
_MSH = MSH
_RAR_RAR_DEFINITION = RAR_RAR_DEFINITION


class RAR_RAR(HL7Model):
    """HL7 v2 RAR_RAR message.

    Attributes:
        MSH (MSH): required
        MSA (MSA): required
        ERR (Optional[ERR]): optional
        DEFINITION (List[RAR_RAR_DEFINITION]): required
        DSC (Optional[DSC]): optional
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

    DEFINITION: List[_RAR_RAR_DEFINITION] = Field(
        min_length=1,
        title="DEFINITION",
        description="Required, repeating",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
