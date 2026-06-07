"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: OPR_O38.RESPONSE
Type: Group
"""
from __future__ import annotations

from typing import List
from pydantic import Field
from hl7types.hl7 import HL7Model

from .OPR_O38_ORDER import OPR_O38_ORDER

_OPR_O38_ORDER = OPR_O38_ORDER


class OPR_O38_RESPONSE(HL7Model):
    """HL7 v2 OPR_O38.RESPONSE group.

    Attributes:
        ORDER (List[OPR_O38_ORDER]): required
    """

    ORDER: List[_OPR_O38_ORDER] = Field(
        min_length=1,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
