"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: CCR_I16.MEDICATION_HISTORY
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.CTI import CTI
from ..segments.ORC import ORC

from .CCR_I16_MEDICATION_ADMINISTRATION_DETAIL import CCR_I16_MEDICATION_ADMINISTRATION_DETAIL
from .CCR_I16_MEDICATION_ENCODING_DETAIL import CCR_I16_MEDICATION_ENCODING_DETAIL
from .CCR_I16_MEDICATION_ORDER_DETAIL import CCR_I16_MEDICATION_ORDER_DETAIL

_CCR_I16_MEDICATION_ADMINISTRATION_DETAIL = CCR_I16_MEDICATION_ADMINISTRATION_DETAIL
_CCR_I16_MEDICATION_ENCODING_DETAIL = CCR_I16_MEDICATION_ENCODING_DETAIL
_CCR_I16_MEDICATION_ORDER_DETAIL = CCR_I16_MEDICATION_ORDER_DETAIL
_CTI = CTI
_ORC = ORC


class CCR_I16_MEDICATION_HISTORY(HL7Model):
    """HL7 v2 CCR_I16.MEDICATION_HISTORY group.

    Attributes:
        ORC (ORC): Common Order, required
        MEDICATION_ORDER_DETAIL (Optional[CCR_I16_MEDICATION_ORDER_DETAIL]): optional
        MEDICATION_ENCODING_DETAIL (Optional[CCR_I16_MEDICATION_ENCODING_DETAIL]): optional
        MEDICATION_ADMINISTRATION_DETAIL (Optional[List[CCR_I16_MEDICATION_ADMINISTRATION_DETAIL]]): optional
        CTI (Optional[List[CTI]]): Clinical Trial Identification, optional
    """

    ORC: _ORC = Field(
        title="ORC",
        description="Common Order",
    )

    MEDICATION_ORDER_DETAIL: Optional[_CCR_I16_MEDICATION_ORDER_DETAIL] = Field(
        default=None,
        title="MEDICATION_ORDER_DETAIL",
    )

    MEDICATION_ENCODING_DETAIL: Optional[_CCR_I16_MEDICATION_ENCODING_DETAIL] = Field(
        default=None,
        title="MEDICATION_ENCODING_DETAIL",
    )

    MEDICATION_ADMINISTRATION_DETAIL: Optional[List[_CCR_I16_MEDICATION_ADMINISTRATION_DETAIL]] = Field(
        default=None,
        title="MEDICATION_ADMINISTRATION_DETAIL",
    )

    CTI: Optional[List[_CTI]] = Field(
        default=None,
        title="CTI",
        description="Clinical Trial Identification",
    )

    model_config = {"populate_by_name": True}
