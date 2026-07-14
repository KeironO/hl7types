"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: EHC_E20.AUTHORIZATION_REQUEST
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.CTD import CTD
from ..segments.IVC import IVC
from ..segments.LOC import LOC
from ..segments.ROL import ROL

from .EHC_E20_PAT_INFO import EHC_E20_PAT_INFO
from .EHC_E20_PSL_ITEM_INFO import EHC_E20_PSL_ITEM_INFO

_CTD = CTD
_EHC_E20_PAT_INFO = EHC_E20_PAT_INFO
_EHC_E20_PSL_ITEM_INFO = EHC_E20_PSL_ITEM_INFO
_IVC = IVC
_LOC = LOC
_ROL = ROL


class EHC_E20_AUTHORIZATION_REQUEST(HL7Model):
    """HL7 v2 EHC_E20.AUTHORIZATION_REQUEST group.

    Attributes:
        IVC (Optional[IVC]): Invoice Segment, optional
        CTD (Optional[List[CTD]]): Contact Data, optional
        LOC (Optional[List[LOC]]): Location Identification, optional
        ROL (Optional[List[ROL]]): Role, optional
        PAT_INFO (Optional[List[EHC_E20_PAT_INFO]]): optional
        PSL_ITEM_INFO (Optional[List[EHC_E20_PSL_ITEM_INFO]]): optional
    """

    IVC: Optional[_IVC] = Field(
        default=None,
        title="IVC",
        description="Invoice Segment",
    )

    CTD: Optional[List[_CTD]] = Field(
        default=None,
        title="CTD",
        description="Contact Data",
    )

    LOC: Optional[List[_LOC]] = Field(
        default=None,
        title="LOC",
        description="Location Identification",
    )

    ROL: Optional[List[_ROL]] = Field(
        default=None,
        title="ROL",
        description="Role",
    )

    PAT_INFO: Optional[List[_EHC_E20_PAT_INFO]] = Field(
        default=None,
        title="PAT_INFO",
    )

    PSL_ITEM_INFO: Optional[List[_EHC_E20_PSL_ITEM_INFO]] = Field(
        default=None,
        title="PSL_ITEM_INFO",
    )

    model_config = {"populate_by_name": True}
