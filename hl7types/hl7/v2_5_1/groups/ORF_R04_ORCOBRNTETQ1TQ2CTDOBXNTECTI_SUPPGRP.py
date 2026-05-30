"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: ORF_R04.ORCOBRNTETQ1TQ2CTDOBXNTECTI_SUPPGRP
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.CTD import CTD
from ..segments.CTI import CTI
from ..segments.NTE import NTE
from ..segments.OBR import OBR
from ..segments.ORC import ORC

from .ORF_R04_OBXNTE_SUPPGRP import ORF_R04_OBXNTE_SUPPGRP
from .ORF_R04_TQ1TQ2_SUPPGRP import ORF_R04_TQ1TQ2_SUPPGRP

_CTD = CTD
_CTI = CTI
_NTE = NTE
_OBR = OBR
_ORC = ORC
_ORF_R04_OBXNTE_SUPPGRP = ORF_R04_OBXNTE_SUPPGRP
_ORF_R04_TQ1TQ2_SUPPGRP = ORF_R04_TQ1TQ2_SUPPGRP


class ORF_R04_ORCOBRNTETQ1TQ2CTDOBXNTECTI_SUPPGRP(HL7Model):
    """HL7 v2 ORF_R04.ORCOBRNTETQ1TQ2CTDOBXNTECTI_SUPPGRP group.

    Attributes:
        ORC (Optional[ORC]): optional
        OBR (OBR): required
        NTE (Optional[List[NTE]]): optional
        TQ1TQ2_SUPPGRP (Optional[List[ORF_R04_TQ1TQ2_SUPPGRP]]): optional
        CTD (Optional[CTD]): optional
        OBXNTE_SUPPGRP (List[ORF_R04_OBXNTE_SUPPGRP]): required
        CTI (Optional[List[CTI]]): optional
    """

    ORC: Optional[_ORC] = Field(
        default=None,
        title="ORC",
        description="Optional",
    )

    OBR: _OBR = Field(
        default=...,
        title="OBR",
        description="Required",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    TQ1TQ2_SUPPGRP: Optional[List[_ORF_R04_TQ1TQ2_SUPPGRP]] = Field(
        default=None,
        title="TQ1TQ2_SUPPGRP",
        description="Optional, repeating",
    )

    CTD: Optional[_CTD] = Field(
        default=None,
        title="CTD",
        description="Optional",
    )

    OBXNTE_SUPPGRP: List[_ORF_R04_OBXNTE_SUPPGRP] = Field(
        default=...,
        title="OBXNTE_SUPPGRP",
        description="Required, repeating",
    )

    CTI: Optional[List[_CTI]] = Field(
        default=None,
        title="CTI",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
