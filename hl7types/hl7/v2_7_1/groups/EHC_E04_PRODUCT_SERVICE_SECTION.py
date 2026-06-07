"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: EHC_E04.PRODUCT_SERVICE_SECTION
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.PSS import PSS

from .EHC_E04_PRODUCT_SERVICE_GROUP import EHC_E04_PRODUCT_SERVICE_GROUP

_EHC_E04_PRODUCT_SERVICE_GROUP = EHC_E04_PRODUCT_SERVICE_GROUP
_PSS = PSS


class EHC_E04_PRODUCT_SERVICE_SECTION(HL7Model):
    """HL7 v2 EHC_E04.PRODUCT_SERVICE_SECTION group.

    Attributes:
        PSS (PSS): required
        PRODUCT_SERVICE_GROUP (Optional[List[EHC_E04_PRODUCT_SERVICE_GROUP]]): optional
    """

    PSS: _PSS = Field(
        title="PSS",
        description="Required",
    )

    PRODUCT_SERVICE_GROUP: Optional[List[_EHC_E04_PRODUCT_SERVICE_GROUP]] = Field(
        default=None,
        title="PRODUCT_SERVICE_GROUP",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
