"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: EHC_E10.PRODUCT_SERVICE_GROUP
Type: Group
"""
from __future__ import annotations

from typing import List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.PSG import PSG

from .EHC_E10_PRODUCT_SERVICE_LINE_INFO import EHC_E10_PRODUCT_SERVICE_LINE_INFO

_EHC_E10_PRODUCT_SERVICE_LINE_INFO = EHC_E10_PRODUCT_SERVICE_LINE_INFO
_PSG = PSG


class EHC_E10_PRODUCT_SERVICE_GROUP(HL7Model):
    """HL7 v2 EHC_E10.PRODUCT_SERVICE_GROUP group.

    Attributes:
        PSG (PSG): required
        PRODUCT_SERVICE_LINE_INFO (List[EHC_E10_PRODUCT_SERVICE_LINE_INFO]): required
    """

    PSG: _PSG = Field(
        title="PSG",
        description="Required",
    )

    PRODUCT_SERVICE_LINE_INFO: List[_EHC_E10_PRODUCT_SERVICE_LINE_INFO] = Field(
        min_length=1,
        title="PRODUCT_SERVICE_LINE_INFO",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
