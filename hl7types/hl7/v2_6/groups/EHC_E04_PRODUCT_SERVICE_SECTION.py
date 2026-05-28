"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: EHC_E04.PRODUCT_SERVICE_SECTION
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.PSS import PSS
from .EHC_E04_PRODUCT_SERVICE_GROUP import EHC_E04_PRODUCT_SERVICE_GROUP

_EHC_E04_PRODUCT_SERVICE_GROUP = EHC_E04_PRODUCT_SERVICE_GROUP
_PSS = PSS


class EHC_E04_PRODUCT_SERVICE_SECTION(BaseModel):
    """HL7 v2 EHC_E04.PRODUCT_SERVICE_SECTION group.

    Attributes:
        PSS (PSS): required
        PRODUCT_SERVICE_GROUP (Optional[List[EHC_E04_PRODUCT_SERVICE_GROUP]]): optional
    """

    PSS: _PSS = Field(
        default=...,
        title="PSS",
        description="Required",
    )

    PRODUCT_SERVICE_GROUP: list[_EHC_E04_PRODUCT_SERVICE_GROUP] | None = Field(
        default=None,
        title="PRODUCT_SERVICE_GROUP",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
