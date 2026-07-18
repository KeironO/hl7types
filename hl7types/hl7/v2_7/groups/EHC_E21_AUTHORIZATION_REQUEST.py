"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: EHC_E21.AUTHORIZATION_REQUEST
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.IVC import IVC

from .EHC_E21_PSL_ITEM_INFO import EHC_E21_PSL_ITEM_INFO

_EHC_E21_PSL_ITEM_INFO = EHC_E21_PSL_ITEM_INFO
_IVC = IVC


class EHC_E21_AUTHORIZATION_REQUEST(HL7Model):
    """HL7 v2 EHC_E21.AUTHORIZATION_REQUEST group.

    Attributes:
        IVC (Optional[IVC]): Invoice Segment, optional
        PSL_ITEM_INFO (Optional[List[EHC_E21_PSL_ITEM_INFO]]): optional
    """

    IVC: Optional[_IVC] = Field(
        default=None,
        title="IVC",
        description="Invoice Segment",
    )

    PSL_ITEM_INFO: Optional[List[_EHC_E21_PSL_ITEM_INFO]] = Field(
        default=None,
        title="PSL_ITEM_INFO",
    )

    model_config = ConfigDict(populate_by_name=True)
