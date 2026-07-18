"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: CCR_I16.CLINICAL_ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.CTI import CTI
from ..segments.ORC import ORC

from .CCR_I16_CLINICAL_ORDER_DETAIL import CCR_I16_CLINICAL_ORDER_DETAIL
from .CCR_I16_CLINICAL_ORDER_TIMING import CCR_I16_CLINICAL_ORDER_TIMING

_CCR_I16_CLINICAL_ORDER_DETAIL = CCR_I16_CLINICAL_ORDER_DETAIL
_CCR_I16_CLINICAL_ORDER_TIMING = CCR_I16_CLINICAL_ORDER_TIMING
_CTI = CTI
_ORC = ORC


class CCR_I16_CLINICAL_ORDER(HL7Model):
    """HL7 v2 CCR_I16.CLINICAL_ORDER group.

    Attributes:
        ORC (ORC): Common Order, required
        CLINICAL_ORDER_TIMING (Optional[List[CCR_I16_CLINICAL_ORDER_TIMING]]): optional
        CLINICAL_ORDER_DETAIL (List[CCR_I16_CLINICAL_ORDER_DETAIL]): required
        CTI (Optional[List[CTI]]): Clinical Trial Identification, optional
    """

    ORC: _ORC = Field(
        title="ORC",
        description="Common Order",
    )

    CLINICAL_ORDER_TIMING: Optional[List[_CCR_I16_CLINICAL_ORDER_TIMING]] = Field(
        default=None,
        title="CLINICAL_ORDER_TIMING",
    )

    CLINICAL_ORDER_DETAIL: List[_CCR_I16_CLINICAL_ORDER_DETAIL] = Field(
        min_length=1,
        title="CLINICAL_ORDER_DETAIL",
    )

    CTI: Optional[List[_CTI]] = Field(
        default=None,
        title="CTI",
        description="Clinical Trial Identification",
    )

    model_config = ConfigDict(populate_by_name=True)
