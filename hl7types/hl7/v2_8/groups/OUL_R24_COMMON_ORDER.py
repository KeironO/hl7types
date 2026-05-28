"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: OUL_R24.COMMON_ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.ORC import ORC
from ..segments.PRT import PRT

from .OUL_R24_ORDER_DOCUMENT import OUL_R24_ORDER_DOCUMENT

_ORC = ORC
_OUL_R24_ORDER_DOCUMENT = OUL_R24_ORDER_DOCUMENT
_PRT = PRT


class OUL_R24_COMMON_ORDER(BaseModel):
    """HL7 v2 OUL_R24.COMMON_ORDER group.

    Attributes:
        ORC (ORC): required
        PRT (Optional[List[PRT]]): optional
        ORDER_DOCUMENT (Optional[OUL_R24_ORDER_DOCUMENT]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    ORDER_DOCUMENT: Optional[_OUL_R24_ORDER_DOCUMENT] = Field(
        default=None,
        title="ORDER_DOCUMENT",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
