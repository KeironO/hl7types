"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: ADT_A45.MERGE_INFO
Type: Group
"""
from __future__ import annotations

from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MRG import MRG
from ..segments.PV1 import PV1

_MRG = MRG
_PV1 = PV1


class ADT_A45_MERGE_INFO(HL7Model):
    """HL7 v2 ADT_A45.MERGE_INFO group.

    Attributes:
        MRG (MRG): required
        PV1 (PV1): required
    """

    MRG: _MRG = Field(
        title="MRG",
        description="Required",
    )

    PV1: _PV1 = Field(
        title="PV1",
        description="Required",
    )

    model_config = {"populate_by_name": True}
