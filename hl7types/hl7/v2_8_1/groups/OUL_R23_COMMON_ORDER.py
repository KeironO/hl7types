"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: OUL_R23.COMMON_ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ORC import ORC
from ..segments.PRT import PRT

from .OUL_R23_ORDER_DOCUMENT import OUL_R23_ORDER_DOCUMENT

_ORC = ORC
_OUL_R23_ORDER_DOCUMENT = OUL_R23_ORDER_DOCUMENT
_PRT = PRT


class OUL_R23_COMMON_ORDER(HL7Model):
    """HL7 v2 OUL_R23.COMMON_ORDER group.

    Attributes:
        ORC (ORC): required
        PRT (Optional[List[PRT]]): optional
        ORDER_DOCUMENT (Optional[OUL_R23_ORDER_DOCUMENT]): optional
    """

    ORC: _ORC = Field(
        title="ORC",
        description="Required",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    ORDER_DOCUMENT: Optional[_OUL_R23_ORDER_DOCUMENT] = Field(
        default=None,
        title="ORDER_DOCUMENT",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
