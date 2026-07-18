"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: SUR_P09.FACPSHPDCPSHFACPDCNTEED_SUPPGRP
Type: Group
"""
from __future__ import annotations

from typing import List, Any
from pydantic import ConfigDict, Field
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
        FAC (FAC): Facility, required
        PSHPDC_SUPPGRP (List[SUR_P09_PSHPDC_SUPPGRP]): required
        PSH (PSH): Product Summary Header, required
        FACPDCNTE_SUPPGRP (List[SUR_P09_FACPDCNTE_SUPPGRP]): required
        ed (Any): Encapsulated Data (wrong segment), required
    """

    FAC: _FAC = Field(
        title="FAC",
        description="Facility",
    )

    PSHPDC_SUPPGRP: List[_SUR_P09_PSHPDC_SUPPGRP] = Field(
        min_length=1,
        title="PSHPDC_SUPPGRP",
    )

    PSH: _PSH = Field(
        title="PSH",
        description="Product Summary Header",
    )

    FACPDCNTE_SUPPGRP: List[_SUR_P09_FACPDCNTE_SUPPGRP] = Field(
        min_length=1,
        title="FACPDCNTE_SUPPGRP",
    )

    ed: Any

    model_config = ConfigDict(populate_by_name=True)
