"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: ORM_O01.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.BLG import BLG
from ..segments.CTI import CTI
from ..segments.ORC import ORC

from .ORM_O01_ORDER_DETAIL import ORM_O01_ORDER_DETAIL

_BLG = BLG
_CTI = CTI
_ORC = ORC
_ORM_O01_ORDER_DETAIL = ORM_O01_ORDER_DETAIL


class ORM_O01_ORDER(HL7Model):
    """HL7 v2 ORM_O01.ORDER group.

    Attributes:
        ORC (ORC): ORC - common order segment, required
        ORDER_DETAIL (Optional[ORM_O01_ORDER_DETAIL]): optional
        CTI (Optional[List[CTI]]): CTI - clinical trial identification segment, optional
        BLG (Optional[BLG]): BLG - billing segment, optional
    """

    ORC: _ORC = Field(
        title="ORC",
        description="ORC - common order segment",
    )

    ORDER_DETAIL: Optional[_ORM_O01_ORDER_DETAIL] = Field(
        default=None,
        title="ORDER_DETAIL",
    )

    CTI: Optional[List[_CTI]] = Field(
        default=None,
        title="CTI",
        description="CTI - clinical trial identification segment",
    )

    BLG: Optional[_BLG] = Field(
        default=None,
        title="BLG",
        description="BLG - billing segment",
    )

    model_config = ConfigDict(populate_by_name=True)
