"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: SUR_P09.FACPSHPDCPSHFACPDCNTEED_SUPPGRP
Type: Group
"""
from __future__ import annotations

from typing import Optional, List, Any
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.FAC import FAC
from ..segments.PSH import PSH

from .SUR_P09_FACPDCNTE_SUPPGRP import SUR_P09_FACPDCNTE_SUPPGRP
from .SUR_P09_PSHPDC_SUPPGRP import SUR_P09_PSHPDC_SUPPGRP

_FAC = FAC
_PSH = PSH
_SUR_P09_FACPDCNTE_SUPPGRP = SUR_P09_FACPDCNTE_SUPPGRP
_SUR_P09_PSHPDC_SUPPGRP = SUR_P09_PSHPDC_SUPPGRP


class SUR_P09_FACPSHPDCPSHFACPDCNTEED_SUPPGRP(HL7Model):
    """HL7 v2 SUR_P09.FACPSHPDCPSHFACPDCNTEED_SUPPGRP group.

    Attributes:
        FAC (FAC): required
        PSHPDC_SUPPGRP (List[SUR_P09_PSHPDC_SUPPGRP]): required
        PSH (PSH): required
        FACPDCNTE_SUPPGRP (List[SUR_P09_FACPDCNTE_SUPPGRP]): required
        ed (Any): required
    """

    FAC: _FAC = Field(
        default=...,
        title="FAC",
        description="Required",
    )

    PSHPDC_SUPPGRP: List[_SUR_P09_PSHPDC_SUPPGRP] = Field(
        default=...,
        title="PSHPDC_SUPPGRP",
        description="Required, repeating",
    )

    PSH: _PSH = Field(
        default=...,
        title="PSH",
        description="Required",
    )

    FACPDCNTE_SUPPGRP: List[_SUR_P09_FACPDCNTE_SUPPGRP] = Field(
        default=...,
        title="FACPDCNTE_SUPPGRP",
        description="Required, repeating",
    )

    ed: Any

    model_config = {"populate_by_name": True}
