"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: EHC_E01.PRODUCT_SERVICE_SECTION
Type: Group
"""
from __future__ import annotations

from typing import List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.PSS import PSS

from .EHC_E01_PRODUCT_SERVICE_GROUP import EHC_E01_PRODUCT_SERVICE_GROUP

_EHC_E01_PRODUCT_SERVICE_GROUP = EHC_E01_PRODUCT_SERVICE_GROUP
_PSS = PSS


class EHC_E01_PRODUCT_SERVICE_SECTION(HL7Model):
    """HL7 v2 EHC_E01.PRODUCT_SERVICE_SECTION group.

    Attributes:
        PSS (PSS): required
        PRODUCT_SERVICE_GROUP (List[EHC_E01_PRODUCT_SERVICE_GROUP]): required
    """

    PSS: _PSS = Field(
        title="PSS",
        description="Required",
    )

    PRODUCT_SERVICE_GROUP: List[_EHC_E01_PRODUCT_SERVICE_GROUP] = Field(
        min_length=1,
        title="PRODUCT_SERVICE_GROUP",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
