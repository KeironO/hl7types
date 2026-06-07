"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: CQU_I19.MEDICATION_HISTORY
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.CTI import CTI
from ..segments.ORC import ORC

from .CQU_I19_MEDICATION_ADMINISTRATION_DETAIL import CQU_I19_MEDICATION_ADMINISTRATION_DETAIL
from .CQU_I19_MEDICATION_ENCODING_DETAIL import CQU_I19_MEDICATION_ENCODING_DETAIL
from .CQU_I19_MEDICATION_ORDER_DETAIL import CQU_I19_MEDICATION_ORDER_DETAIL

_CQU_I19_MEDICATION_ADMINISTRATION_DETAIL = CQU_I19_MEDICATION_ADMINISTRATION_DETAIL
_CQU_I19_MEDICATION_ENCODING_DETAIL = CQU_I19_MEDICATION_ENCODING_DETAIL
_CQU_I19_MEDICATION_ORDER_DETAIL = CQU_I19_MEDICATION_ORDER_DETAIL
_CTI = CTI
_ORC = ORC


class CQU_I19_MEDICATION_HISTORY(HL7Model):
    """HL7 v2 CQU_I19.MEDICATION_HISTORY group.

    Attributes:
        ORC (ORC): required
        MEDICATION_ORDER_DETAIL (Optional[CQU_I19_MEDICATION_ORDER_DETAIL]): optional
        MEDICATION_ENCODING_DETAIL (Optional[CQU_I19_MEDICATION_ENCODING_DETAIL]): optional
        MEDICATION_ADMINISTRATION_DETAIL (Optional[List[CQU_I19_MEDICATION_ADMINISTRATION_DETAIL]]): optional
        CTI (Optional[List[CTI]]): optional
    """

    ORC: _ORC = Field(
        title="ORC",
        description="Required",
    )

    MEDICATION_ORDER_DETAIL: Optional[_CQU_I19_MEDICATION_ORDER_DETAIL] = Field(
        default=None,
        title="MEDICATION_ORDER_DETAIL",
        description="Optional",
    )

    MEDICATION_ENCODING_DETAIL: Optional[_CQU_I19_MEDICATION_ENCODING_DETAIL] = Field(
        default=None,
        title="MEDICATION_ENCODING_DETAIL",
        description="Optional",
    )

    MEDICATION_ADMINISTRATION_DETAIL: Optional[List[_CQU_I19_MEDICATION_ADMINISTRATION_DETAIL]] = Field(
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
