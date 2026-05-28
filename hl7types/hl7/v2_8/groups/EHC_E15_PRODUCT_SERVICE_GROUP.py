"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: EHC_E15.PRODUCT_SERVICE_GROUP
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.PSG import PSG
from .EHC_E15_PSL_ITEM_INFO import EHC_E15_PSL_ITEM_INFO

_EHC_E15_PSL_ITEM_INFO = EHC_E15_PSL_ITEM_INFO
_PSG = PSG


class EHC_E15_PRODUCT_SERVICE_GROUP(BaseModel):
    """HL7 v2 EHC_E15.PRODUCT_SERVICE_GROUP group.

    Attributes:
        PSG (PSG): required
        PSL_ITEM_INFO (List[EHC_E15_PSL_ITEM_INFO]): required
    """

    PSG: _PSG = Field(
        default=...,
        title="PSG",
        description="Required",
    )

    PSL_ITEM_INFO: list[_EHC_E15_PSL_ITEM_INFO] = Field(
        default=...,
        title="PSL_ITEM_INFO",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
