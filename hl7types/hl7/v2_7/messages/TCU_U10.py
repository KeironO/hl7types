"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: TCU_U10
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.EQU import EQU
from ..segments.MSH import MSH
from ..segments.ROL import ROL
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.TCU_U10_TEST_CONFIGURATION import TCU_U10_TEST_CONFIGURATION

_EQU = EQU
_MSH = MSH
_ROL = ROL
_SFT = SFT
_TCU_U10_TEST_CONFIGURATION = TCU_U10_TEST_CONFIGURATION
_UAC = UAC


class TCU_U10(HL7Model):
    """TCU/ACK - Automated equipment test code settings update (S13.3.10).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        EQU (EQU): Equipment Detail, required
        TEST_CONFIGURATION (List[TCU_U10_TEST_CONFIGURATION]): required
        ROL (Optional[ROL]): Role, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Software Segment",
    )

    UAC: Optional[_UAC] = Field(
        default=None,
        title="UAC",
        description="User Authentication Credential Segment",
    )

    EQU: _EQU = Field(
        title="EQU",
        description="Equipment Detail",
    )

    TEST_CONFIGURATION: List[_TCU_U10_TEST_CONFIGURATION] = Field(
        min_length=1,
        title="TEST_CONFIGURATION",
    )

    ROL: Optional[_ROL] = Field(
        default=None,
        title="ROL",
        description="Role",
    )

    model_config = ConfigDict(populate_by_name=True)
