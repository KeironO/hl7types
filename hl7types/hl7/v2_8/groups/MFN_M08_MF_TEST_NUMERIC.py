"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: MFN_M08.MF_TEST_NUMERIC
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MFE import MFE
from ..segments.OM1 import OM1
from ..segments.OM2 import OM2
from ..segments.OM3 import OM3
from ..segments.OM4 import OM4
from ..segments.PRT import PRT

_MFE = MFE
_OM1 = OM1
_OM2 = OM2
_OM3 = OM3
_OM4 = OM4
_PRT = PRT


class MFN_M08_MF_TEST_NUMERIC(HL7Model):
    """HL7 v2 MFN_M08.MF_TEST_NUMERIC group.

    Attributes:
        MFE (MFE): required
        OM1 (OM1): required
        PRT (Optional[List[PRT]]): optional
        OM2 (Optional[OM2]): optional
        OM3 (Optional[OM3]): optional
        OM4 (Optional[List[OM4]]): optional
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

    OM2: Optional[_OM2] = Field(
        default=None,
        title="OM2",
        description="Optional",
    )

    OM3: Optional[_OM3] = Field(
        default=None,
        title="OM3",
        description="Optional",
    )

    OM4: Optional[List[_OM4]] = Field(
        default=None,
        title="OM4",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
