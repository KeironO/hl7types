"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: DFT_P03.FINANCIAL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.FT1 import FT1

from .DFT_P03_FINANCIAL_PROCEDURE import DFT_P03_FINANCIAL_PROCEDURE

_DFT_P03_FINANCIAL_PROCEDURE = DFT_P03_FINANCIAL_PROCEDURE
_FT1 = FT1


class DFT_P03_FINANCIAL(HL7Model):
    """HL7 v2 DFT_P03.FINANCIAL group.

    Attributes:
        FT1 (FT1): FT1 - financial transaction segment, required
        FINANCIAL_PROCEDURE (Optional[List[DFT_P03_FINANCIAL_PROCEDURE]]): optional
    """

    FT1: _FT1 = Field(
        title="FT1",
        description="FT1 - financial transaction segment",
    )

    FINANCIAL_PROCEDURE: Optional[List[_DFT_P03_FINANCIAL_PROCEDURE]] = Field(
        default=None,
        title="FINANCIAL_PROCEDURE",
    )

    model_config = ConfigDict(populate_by_name=True)
