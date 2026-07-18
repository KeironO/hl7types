"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: EHC_E01.PRODUCT_SERVICE_SECTION
Type: Group
"""
from __future__ import annotations

from typing import List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.PSS import PSS

from .EHC_E01_PRODUCT_SERVICE_GROUP import EHC_E01_PRODUCT_SERVICE_GROUP

_EHC_E01_PRODUCT_SERVICE_GROUP = EHC_E01_PRODUCT_SERVICE_GROUP
_PSS = PSS


class EHC_E01_PRODUCT_SERVICE_SECTION(HL7Model):
    """HL7 v2 EHC_E01.PRODUCT_SERVICE_SECTION group.

    Attributes:
        PSS (PSS): Product/Service Section, required
        PRODUCT_SERVICE_GROUP (List[EHC_E01_PRODUCT_SERVICE_GROUP]): required
    """

    PSS: _PSS = Field(
        title="PSS",
        description="Product/Service Section",
    )

    PRODUCT_SERVICE_GROUP: List[_EHC_E01_PRODUCT_SERVICE_GROUP] = Field(
        min_length=1,
        title="PRODUCT_SERVICE_GROUP",
    )

    model_config = ConfigDict(populate_by_name=True)
