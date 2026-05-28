"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: SUR_P09.FACILITY
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.ED import ED
from ..segments.FAC import FAC
from ..segments.PSH import PSH
from .SUR_P09_FACILITY_DETAIL import SUR_P09_FACILITY_DETAIL
from .SUR_P09_PRODUCT import SUR_P09_PRODUCT

_ED = ED
_FAC = FAC
_PSH = PSH
_SUR_P09_FACILITY_DETAIL = SUR_P09_FACILITY_DETAIL
_SUR_P09_PRODUCT = SUR_P09_PRODUCT


class SUR_P09_FACILITY(BaseModel):
    """HL7 v2 SUR_P09.FACILITY group.

    Attributes:
        FAC (FAC): required
        PRODUCT (List[SUR_P09_PRODUCT]): required
        PSH (PSH): required
        FACILITY_DETAIL (List[SUR_P09_FACILITY_DETAIL]): required
        ED (ED): required
    """

    FAC: _FAC = Field(
        default=...,
        title="FAC",
        description="Required",
    )

    PRODUCT: list[_SUR_P09_PRODUCT] = Field(
        default=...,
        title="PRODUCT",
        description="Required, repeating",
    )

    PSH: _PSH = Field(
        default=...,
        title="PSH",
        description="Required",
    )

    FACILITY_DETAIL: list[_SUR_P09_FACILITY_DETAIL] = Field(
        default=...,
        title="FACILITY_DETAIL",
        description="Required, repeating",
    )

    ED: _ED = Field(
        default=...,
        title="ED",
        description="Required",
    )

    model_config = {"populate_by_name": True}
