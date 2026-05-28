"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: EHC_E10.PRODUCT_SERVICE_GROUP
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.PSG import PSG
from .EHC_E10_PRODUCT_SERVICE_LINE_INFO import EHC_E10_PRODUCT_SERVICE_LINE_INFO

_EHC_E10_PRODUCT_SERVICE_LINE_INFO = EHC_E10_PRODUCT_SERVICE_LINE_INFO
_PSG = PSG


class EHC_E10_PRODUCT_SERVICE_GROUP(BaseModel):
    """HL7 v2 EHC_E10.PRODUCT_SERVICE_GROUP group.

    Attributes:
        PSG (PSG): required
        PRODUCT_SERVICE_LINE_INFO (List[EHC_E10_PRODUCT_SERVICE_LINE_INFO]): required
    """

    PSG: _PSG = Field(
        default=...,
        title="PSG",
        description="Required",
    )

    PRODUCT_SERVICE_LINE_INFO: list[_EHC_E10_PRODUCT_SERVICE_LINE_INFO] = Field(
        default=...,
        title="PRODUCT_SERVICE_LINE_INFO",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
