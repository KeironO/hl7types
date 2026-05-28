"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: ORL_O22.GENERAL_ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from .ORL_O22_CONTAINER import ORL_O22_CONTAINER
from .ORL_O22_ORDER import ORL_O22_ORDER

_ORL_O22_CONTAINER = ORL_O22_CONTAINER
_ORL_O22_ORDER = ORL_O22_ORDER


class ORL_O22_GENERAL_ORDER(BaseModel):
    """HL7 v2 ORL_O22.GENERAL_ORDER group.

    Attributes:
        CONTAINER (Optional[ORL_O22_CONTAINER]): optional
        ORDER (Optional[List[ORL_O22_ORDER]]): optional
    """

    CONTAINER: Optional[_ORL_O22_CONTAINER] = Field(
        default=None,
        title="CONTAINER",
        description="Optional",
    )

    ORDER: Optional[List[_ORL_O22_ORDER]] = Field(
        default=None,
        title="ORDER",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
