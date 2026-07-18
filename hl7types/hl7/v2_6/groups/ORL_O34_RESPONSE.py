"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: ORL_O34.RESPONSE
Type: Group
"""
from __future__ import annotations

from typing import List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.PID import PID

from .ORL_O34_SPECIMEN import ORL_O34_SPECIMEN

_ORL_O34_SPECIMEN = ORL_O34_SPECIMEN
_PID = PID


class ORL_O34_RESPONSE(HL7Model):
    """HL7 v2 ORL_O34.RESPONSE group.

    Attributes:
        PID (PID): Patient Identification, required
        SPECIMEN (List[ORL_O34_SPECIMEN]): required
    """

    PID: _PID = Field(
        title="PID",
        description="Patient Identification",
    )

    SPECIMEN: List[_ORL_O34_SPECIMEN] = Field(
        min_length=1,
        title="SPECIMEN",
    )

    model_config = ConfigDict(populate_by_name=True)
