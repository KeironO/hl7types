"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: CSU_C09.STUDY_PHARM
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from .CSU_C09_COMMON_ORDER import CSU_C09_COMMON_ORDER
from .CSU_C09_RX_ADMIN import CSU_C09_RX_ADMIN

_CSU_C09_COMMON_ORDER = CSU_C09_COMMON_ORDER
_CSU_C09_RX_ADMIN = CSU_C09_RX_ADMIN


class CSU_C09_STUDY_PHARM(HL7Model):
    """HL7 v2 CSU_C09.STUDY_PHARM group.

    Attributes:
        COMMON_ORDER (Optional[CSU_C09_COMMON_ORDER]): optional
        RX_ADMIN (List[CSU_C09_RX_ADMIN]): required
    """

    COMMON_ORDER: Optional[_CSU_C09_COMMON_ORDER] = Field(
        default=None,
        title="COMMON_ORDER",
        description="Optional",
    )

    RX_ADMIN: List[_CSU_C09_RX_ADMIN] = Field(
        default=...,
        title="RX_ADMIN",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
