"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: EHC_E21.AUTHORIZATION_REQUEST
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.IVC import IVC

from .EHC_E21_PSL_ITEM_INFO import EHC_E21_PSL_ITEM_INFO

_EHC_E21_PSL_ITEM_INFO = EHC_E21_PSL_ITEM_INFO
_IVC = IVC


class EHC_E21_AUTHORIZATION_REQUEST(HL7Model):
    """HL7 v2 EHC_E21.AUTHORIZATION_REQUEST group.

    Attributes:
        IVC (Optional[IVC]): optional
        PSL_ITEM_INFO (Optional[List[EHC_E21_PSL_ITEM_INFO]]): optional
    """

    IVC: Optional[_IVC] = Field(
        default=None,
        title="IVC",
        description="Optional",
    )

    PSL_ITEM_INFO: Optional[List[_EHC_E21_PSL_ITEM_INFO]] = Field(
        default=None,
        title="PSL_ITEM_INFO",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
