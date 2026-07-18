"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: PMU_B04
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.EVN import EVN
from ..segments.MSH import MSH
from ..segments.ORG import ORG
from ..segments.PRA import PRA
from ..segments.STF import STF

_EVN = EVN
_MSH = MSH
_ORG = ORG
_PRA = PRA
_STF = STF


class PMU_B04(HL7Model):
    """PMU/ACK - Active practicing person (S15).

    Attributes:
        MSH (MSH): Message Header, required
        EVN (EVN): Event Type, required
        STF (STF): Staff Identification, required
        PRA (Optional[List[PRA]]): Practitioner Detail, optional
        ORG (Optional[ORG]): Practitioner Organization Unit, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    EVN: _EVN = Field(
        title="EVN",
        description="Event Type",
    )

    STF: _STF = Field(
        title="STF",
        description="Staff Identification",
    )

    PRA: Optional[List[_PRA]] = Field(
        default=None,
        title="PRA",
        description="Practitioner Detail",
    )

    ORG: Optional[_ORG] = Field(
        default=None,
        title="ORG",
        description="Practitioner Organization Unit",
    )

    model_config = ConfigDict(populate_by_name=True)
