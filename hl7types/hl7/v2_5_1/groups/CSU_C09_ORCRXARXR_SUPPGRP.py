"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: CSU_C09.ORCRXARXR_SUPPGRP
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.ORC import ORC

from .CSU_C09_RXARXR_SUPPGRP import CSU_C09_RXARXR_SUPPGRP

_CSU_C09_RXARXR_SUPPGRP = CSU_C09_RXARXR_SUPPGRP
_ORC = ORC


class CSU_C09_ORCRXARXR_SUPPGRP(HL7Model):
    """HL7 v2 CSU_C09.ORCRXARXR_SUPPGRP group.

    Attributes:
        ORC (Optional[ORC]): Common Order, optional
        RXARXR_SUPPGRP (List[CSU_C09_RXARXR_SUPPGRP]): required
    """

    ORC: Optional[_ORC] = Field(
        default=None,
        title="ORC",
        description="Common Order",
    )

    RXARXR_SUPPGRP: List[_CSU_C09_RXARXR_SUPPGRP] = Field(
        min_length=1,
        title="RXARXR_SUPPGRP",
    )

    model_config = ConfigDict(populate_by_name=True)
