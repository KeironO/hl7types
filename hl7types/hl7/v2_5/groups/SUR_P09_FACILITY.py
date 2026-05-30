"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: SUR_P09.FACILITY
Type: Group
"""
from __future__ import annotations

from typing import Optional, List, Any
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.FAC import FAC
from ..segments.PSH import PSH

from .SUR_P09_FACILITY_DETAIL import SUR_P09_FACILITY_DETAIL
from .SUR_P09_PRODUCT import SUR_P09_PRODUCT

_FAC = FAC
_PSH = PSH
_SUR_P09_FACILITY_DETAIL = SUR_P09_FACILITY_DETAIL
_SUR_P09_PRODUCT = SUR_P09_PRODUCT


class SUR_P09_FACILITY(HL7Model):
    """HL7 v2 SUR_P09.FACILITY group.

    Attributes:
        FAC (FAC): required
        PRODUCT (List[SUR_P09_PRODUCT]): required
        PSH (PSH): required
        FACILITY_DETAIL (List[SUR_P09_FACILITY_DETAIL]): required
        ed (Any): required
    """

    FAC: _FAC = Field(
        default=...,
        title="FAC",
        description="Required",
    )

    PRODUCT: List[_SUR_P09_PRODUCT] = Field(
        default=...,
        title="PRODUCT",
        description="Required, repeating",
    )

    PSH: _PSH = Field(
        default=...,
        title="PSH",
        description="Required",
    )

    FACILITY_DETAIL: List[_SUR_P09_FACILITY_DETAIL] = Field(
        default=...,
        title="FACILITY_DETAIL",
        description="Required, repeating",
    )

    ed: Any

    model_config = {"populate_by_name": True}
