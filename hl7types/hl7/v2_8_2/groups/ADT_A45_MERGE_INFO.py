"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: ADT_A45.MERGE_INFO
Type: Group
"""
from __future__ import annotations

from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.MRG import MRG
from ..segments.PV1 import PV1

_MRG = MRG
_PV1 = PV1


class ADT_A45_MERGE_INFO(HL7Model):
    """HL7 v2 ADT_A45.MERGE_INFO group.

    Attributes:
        MRG (MRG): Merge Patient Information, required
        PV1 (PV1): Patient Visit, required
    """

    MRG: _MRG = Field(
        title="MRG",
        description="Merge Patient Information",
    )

    PV1: _PV1 = Field(
        title="PV1",
        description="Patient Visit",
    )

    model_config = ConfigDict(populate_by_name=True)
