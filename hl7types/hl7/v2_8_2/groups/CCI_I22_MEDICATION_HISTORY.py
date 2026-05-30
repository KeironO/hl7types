"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: CCI_I22.MEDICATION_HISTORY
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.CTI import CTI
from ..segments.ORC import ORC

from .CCI_I22_MEDICATION_ADMINISTRATION_DETAIL import CCI_I22_MEDICATION_ADMINISTRATION_DETAIL
from .CCI_I22_MEDICATION_ENCODING_DETAIL import CCI_I22_MEDICATION_ENCODING_DETAIL
from .CCI_I22_MEDICATION_ORDER_DETAIL import CCI_I22_MEDICATION_ORDER_DETAIL

_CCI_I22_MEDICATION_ADMINISTRATION_DETAIL = CCI_I22_MEDICATION_ADMINISTRATION_DETAIL
_CCI_I22_MEDICATION_ENCODING_DETAIL = CCI_I22_MEDICATION_ENCODING_DETAIL
_CCI_I22_MEDICATION_ORDER_DETAIL = CCI_I22_MEDICATION_ORDER_DETAIL
_CTI = CTI
_ORC = ORC


class CCI_I22_MEDICATION_HISTORY(HL7Model):
    """HL7 v2 CCI_I22.MEDICATION_HISTORY group.

    Attributes:
        ORC (ORC): required
        MEDICATION_ORDER_DETAIL (Optional[CCI_I22_MEDICATION_ORDER_DETAIL]): optional
        MEDICATION_ENCODING_DETAIL (Optional[CCI_I22_MEDICATION_ENCODING_DETAIL]): optional
        MEDICATION_ADMINISTRATION_DETAIL (Optional[List[CCI_I22_MEDICATION_ADMINISTRATION_DETAIL]]): optional
        CTI (Optional[List[CTI]]): optional
    """

    ORC: _ORC = Field(
        default=...,
        title="ORC",
        description="Required",
    )

    MEDICATION_ORDER_DETAIL: Optional[_CCI_I22_MEDICATION_ORDER_DETAIL] = Field(
        default=None,
        title="MEDICATION_ORDER_DETAIL",
        description="Optional",
    )

    MEDICATION_ENCODING_DETAIL: Optional[_CCI_I22_MEDICATION_ENCODING_DETAIL] = Field(
        default=None,
        title="MEDICATION_ENCODING_DETAIL",
        description="Optional",
    )

    MEDICATION_ADMINISTRATION_DETAIL: Optional[List[_CCI_I22_MEDICATION_ADMINISTRATION_DETAIL]] = Field(
        default=None,
        title="MEDICATION_ADMINISTRATION_DETAIL",
        description="Optional, repeating",
    )

    CTI: Optional[List[_CTI]] = Field(
        default=None,
        title="CTI",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
