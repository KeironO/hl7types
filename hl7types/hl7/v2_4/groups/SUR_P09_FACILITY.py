"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: SUR_P09.FACILITY
Type: Group
"""
from __future__ import annotations

from typing import List
from pydantic import ConfigDict, Field
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
        FAC (FAC): Facility, required
        PRODUCT (List[SUR_P09_PRODUCT]): required
        PSH (PSH): Product Summary Header, required
        FACILITY_DETAIL (List[SUR_P09_FACILITY_DETAIL]): required
    """

    FAC: _FAC = Field(
        title="FAC",
        description="Facility",
    )

    PRODUCT: List[_SUR_P09_PRODUCT] = Field(
        min_length=1,
        title="PRODUCT",
    )

    PSH: _PSH = Field(
        title="PSH",
        description="Product Summary Header",
    )

    FACILITY_DETAIL: List[_SUR_P09_FACILITY_DETAIL] = Field(
        min_length=1,
        title="FACILITY_DETAIL",
    )

    model_config = ConfigDict(populate_by_name=True)
