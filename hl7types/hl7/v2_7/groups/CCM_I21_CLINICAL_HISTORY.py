"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: CCM_I21.CLINICAL_HISTORY
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.CTI import CTI
from ..segments.ORC import ORC

from .CCM_I21_CLINICAL_HISTORY_DETAIL import CCM_I21_CLINICAL_HISTORY_DETAIL
from .CCM_I21_ROLE_CLINICAL_HISTORY import CCM_I21_ROLE_CLINICAL_HISTORY

_CCM_I21_CLINICAL_HISTORY_DETAIL = CCM_I21_CLINICAL_HISTORY_DETAIL
_CCM_I21_ROLE_CLINICAL_HISTORY = CCM_I21_ROLE_CLINICAL_HISTORY
_CTI = CTI
_ORC = ORC


class CCM_I21_CLINICAL_HISTORY(HL7Model):
    """HL7 v2 CCM_I21.CLINICAL_HISTORY group.

    Attributes:
        ORC (ORC): Common Order, required
        CLINICAL_HISTORY_DETAIL (Optional[List[CCM_I21_CLINICAL_HISTORY_DETAIL]]): optional
        ROLE_CLINICAL_HISTORY (Optional[List[CCM_I21_ROLE_CLINICAL_HISTORY]]): optional
        CTI (Optional[List[CTI]]): Clinical Trial Identification, optional
    """

    ORC: _ORC = Field(
        title="ORC",
        description="Common Order",
    )

    CLINICAL_HISTORY_DETAIL: Optional[List[_CCM_I21_CLINICAL_HISTORY_DETAIL]] = Field(
        default=None,
        title="CLINICAL_HISTORY_DETAIL",
    )

    ROLE_CLINICAL_HISTORY: Optional[List[_CCM_I21_ROLE_CLINICAL_HISTORY]] = Field(
        default=None,
        title="ROLE_CLINICAL_HISTORY",
    )

    CTI: Optional[List[_CTI]] = Field(
        default=None,
        title="CTI",
        description="Clinical Trial Identification",
    )

    model_config = ConfigDict(populate_by_name=True)
