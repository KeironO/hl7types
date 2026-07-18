"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: EHC_E15.PRODUCT_SERVICE_GROUP
Type: Group
"""
from __future__ import annotations

from typing import List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.PSG import PSG

from .EHC_E15_PSL_ITEM_INFO import EHC_E15_PSL_ITEM_INFO

_EHC_E15_PSL_ITEM_INFO = EHC_E15_PSL_ITEM_INFO
_PSG = PSG


class EHC_E15_PRODUCT_SERVICE_GROUP(HL7Model):
    """HL7 v2 EHC_E15.PRODUCT_SERVICE_GROUP group.

    Attributes:
        PSG (PSG): Product/Service Group, required
        PSL_ITEM_INFO (List[EHC_E15_PSL_ITEM_INFO]): required
    """

    PSG: _PSG = Field(
        title="PSG",
        description="Product/Service Group",
    )

    PSL_ITEM_INFO: List[_EHC_E15_PSL_ITEM_INFO] = Field(
        min_length=1,
        title="PSL_ITEM_INFO",
    )

    model_config = ConfigDict(populate_by_name=True)
