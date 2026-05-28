"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: OUL_R24
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.DSC import DSC
from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.SFT import SFT

from ..groups.OUL_R24_ORDER import OUL_R24_ORDER
from ..groups.OUL_R24_PIDPD1NTE_SUPPGRP import OUL_R24_PIDPD1NTE_SUPPGRP
from ..groups.OUL_R24_PV1PV2_SUPPGRP import OUL_R24_PV1PV2_SUPPGRP

_DSC = DSC
_MSH = MSH
_NTE = NTE
_OUL_R24_ORDER = OUL_R24_ORDER
_OUL_R24_PIDPD1NTE_SUPPGRP = OUL_R24_PIDPD1NTE_SUPPGRP
_OUL_R24_PV1PV2_SUPPGRP = OUL_R24_PV1PV2_SUPPGRP
_SFT = SFT


class OUL_R24(BaseModel):
    """HL7 v2 OUL_R24 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        NTE (Optional[NTE]): optional
        PIDPD1NTE_SUPPGRP (Optional[OUL_R24_PIDPD1NTE_SUPPGRP]): optional
        PV1PV2_SUPPGRP (Optional[OUL_R24_PV1PV2_SUPPGRP]): optional
        ORDER (List[OUL_R24_ORDER]): required
        DSC (Optional[DSC]): optional
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    NTE: Optional[_NTE] = Field(
        default=None,
        title="NTE",
        description="Optional",
    )

    PIDPD1NTE_SUPPGRP: Optional[_OUL_R24_PIDPD1NTE_SUPPGRP] = Field(
        default=None,
        title="PIDPD1NTE_SUPPGRP",
        description="Optional",
    )

    PV1PV2_SUPPGRP: Optional[_OUL_R24_PV1PV2_SUPPGRP] = Field(
        default=None,
        title="PV1PV2_SUPPGRP",
        description="Optional",
    )

    ORDER: List[_OUL_R24_ORDER] = Field(
        default=...,
        title="ORDER",
        description="Required, repeating",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
