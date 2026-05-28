"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: CSU_C09.STUDY_PHARM
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.ORC import ORC
from .CSU_C09_RX_ADMIN import CSU_C09_RX_ADMIN

_CSU_C09_RX_ADMIN = CSU_C09_RX_ADMIN
_ORC = ORC


class CSU_C09_STUDY_PHARM(BaseModel):
    """HL7 v2 CSU_C09.STUDY_PHARM group.

    Attributes:
        ORC (Optional[ORC]): optional
        RX_ADMIN (List[CSU_C09_RX_ADMIN]): required
    """

    ORC: _ORC | None = Field(
        default=None,
        title="ORC",
        description="Optional",
    )

    RX_ADMIN: list[_CSU_C09_RX_ADMIN] = Field(
        default=...,
        title="RX_ADMIN",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
