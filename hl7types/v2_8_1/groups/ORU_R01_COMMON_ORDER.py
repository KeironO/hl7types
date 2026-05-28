"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: ORU_R01.COMMON_ORDER
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.ORC import ORC
from ..segments.PRT import PRT

from .ORU_R01_ORDER_DOCUMENT import ORU_R01_ORDER_DOCUMENT

_ORC = ORC
_ORU_R01_ORDER_DOCUMENT = ORU_R01_ORDER_DOCUMENT
_PRT = PRT


class ORU_R01_COMMON_ORDER(BaseModel):
    """HL7 v2 ORU_R01.COMMON_ORDER group.

    Attributes:
        ORC (ORC): required
        PRT (Optional[List[PRT]]): optional
        ORDER_DOCUMENT (Optional[ORU_R01_ORDER_DOCUMENT]): optional
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

    ORDER_DOCUMENT: Optional[_ORU_R01_ORDER_DOCUMENT] = Field(
        default=None,
        title="ORDER_DOCUMENT",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
