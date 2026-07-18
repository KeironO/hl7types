"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: ORL_O22.SPECIMEN
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.SAC import SAC
from ..segments.SPM import SPM

_SAC = SAC
_SPM = SPM


class ORL_O22_SPECIMEN(HL7Model):
    """HL7 v2 ORL_O22.SPECIMEN group.

    Attributes:
        SPM (SPM): Specimen, required
        SAC (Optional[List[SAC]]): Specimen Container detail, optional
    """

    SPM: _SPM = Field(
        title="SPM",
        description="Specimen",
    )

    SAC: Optional[List[_SAC]] = Field(
        default=None,
        title="SAC",
        description="Specimen Container detail",
    )

    model_config = ConfigDict(populate_by_name=True)
