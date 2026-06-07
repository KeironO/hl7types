"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: RSP_E22.AUTHORIZATION_INFO
Type: Group
"""
from __future__ import annotations

from typing import List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.IVC import IVC
from ..segments.PSG import PSG

from .RSP_E22_PSL_ITEM_INFO import RSP_E22_PSL_ITEM_INFO

_IVC = IVC
_PSG = PSG
_RSP_E22_PSL_ITEM_INFO = RSP_E22_PSL_ITEM_INFO


class RSP_E22_AUTHORIZATION_INFO(HL7Model):
    """HL7 v2 RSP_E22.AUTHORIZATION_INFO group.

    Attributes:
        IVC (IVC): required
        PSG (PSG): required
        PSL_ITEM_INFO (List[RSP_E22_PSL_ITEM_INFO]): required
    """

    IVC: _IVC = Field(
        title="IVC",
        description="Required",
    )

    PSG: _PSG = Field(
        title="PSG",
        description="Required",
    )

    PSL_ITEM_INFO: List[_RSP_E22_PSL_ITEM_INFO] = Field(
        min_length=1,
        title="PSL_ITEM_INFO",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
