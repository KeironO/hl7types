"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: EHC_E15.PRODUCT_SERVICE_SECTION
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.PSS import PSS

from .EHC_E15_PRODUCT_SERVICE_GROUP import EHC_E15_PRODUCT_SERVICE_GROUP

_EHC_E15_PRODUCT_SERVICE_GROUP = EHC_E15_PRODUCT_SERVICE_GROUP
_PSS = PSS


class EHC_E15_PRODUCT_SERVICE_SECTION(BaseModel):
    """HL7 v2 EHC_E15.PRODUCT_SERVICE_SECTION group.

    Attributes:
        PSS (PSS): required
        PRODUCT_SERVICE_GROUP (List[EHC_E15_PRODUCT_SERVICE_GROUP]): required
    """

    PSS: _PSS = Field(
        default=...,
        title="PSS",
        description="Required",
    )

    PRODUCT_SERVICE_GROUP: List[_EHC_E15_PRODUCT_SERVICE_GROUP] = Field(
        default=...,
        title="PRODUCT_SERVICE_GROUP",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
