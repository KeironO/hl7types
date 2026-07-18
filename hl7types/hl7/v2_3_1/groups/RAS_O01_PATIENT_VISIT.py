"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: RAS_O01.PATIENT_VISIT
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.PV1 import PV1
from ..segments.PV2 import PV2

_PV1 = PV1
_PV2 = PV2


class RAS_O01_PATIENT_VISIT(HL7Model):
    """HL7 v2 RAS_O01.PATIENT_VISIT group.

    Attributes:
        PV1 (PV1): PV1 - patient visit segment-, required
        PV2 (Optional[PV2]): PV2 - patient visit - additional information segment, optional
    """

    PV1: _PV1 = Field(
        title="PV1",
        description="PV1 - patient visit segment-",
    )

    PV2: Optional[_PV2] = Field(
        default=None,
        title="PV2",
        description="PV2 - patient visit - additional information segment",
    )

    model_config = ConfigDict(populate_by_name=True)
