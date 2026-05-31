"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: EHC_E24.AUTHORIZATION_RESPONSE_INFO
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.IVC import IVC

from .EHC_E24_PSL_ITEM_INFO import EHC_E24_PSL_ITEM_INFO

_EHC_E24_PSL_ITEM_INFO = EHC_E24_PSL_ITEM_INFO
_IVC = IVC


class EHC_E24_AUTHORIZATION_RESPONSE_INFO(HL7Model):
    """HL7 v2 EHC_E24.AUTHORIZATION_RESPONSE_INFO group.

    Attributes:
        IVC (Optional[IVC]): optional
        PSL_ITEM_INFO (Optional[List[EHC_E24_PSL_ITEM_INFO]]): optional
    """

    IVC: Optional[_IVC] = Field(
        default=None,
        title="IVC",
        description="Optional",
    )

    PSL_ITEM_INFO: Optional[List[_EHC_E24_PSL_ITEM_INFO]] = Field(
        default=None,
        title="PSL_ITEM_INFO",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
