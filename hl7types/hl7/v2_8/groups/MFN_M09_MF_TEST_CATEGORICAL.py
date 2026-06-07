"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: MFN_M09.MF_TEST_CATEGORICAL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MFE import MFE
from ..segments.OM1 import OM1
from ..segments.PRT import PRT

from .MFN_M09_MF_TEST_CAT_DETAIL import MFN_M09_MF_TEST_CAT_DETAIL

_MFE = MFE
_MFN_M09_MF_TEST_CAT_DETAIL = MFN_M09_MF_TEST_CAT_DETAIL
_OM1 = OM1
_PRT = PRT


class MFN_M09_MF_TEST_CATEGORICAL(HL7Model):
    """HL7 v2 MFN_M09.MF_TEST_CATEGORICAL group.

    Attributes:
        MFE (MFE): required
        OM1 (OM1): required
        PRT (Optional[List[PRT]]): optional
        MF_TEST_CAT_DETAIL (Optional[MFN_M09_MF_TEST_CAT_DETAIL]): optional
    """

    MFE: _MFE = Field(
        title="MFE",
        description="Required",
    )

    OM1: _OM1 = Field(
        title="OM1",
        description="Required",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    MF_TEST_CAT_DETAIL: Optional[_MFN_M09_MF_TEST_CAT_DETAIL] = Field(
        default=None,
        title="MF_TEST_CAT_DETAIL",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
