"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: RSP_K25.STAFF
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.AFF import AFF
from ..segments.CER import CER
from ..segments.EDU import EDU
from ..segments.LAN import LAN
from ..segments.ORG import ORG
from ..segments.PRA import PRA
from ..segments.STF import STF

_AFF = AFF
_CER = CER
_EDU = EDU
_LAN = LAN
_ORG = ORG
_PRA = PRA
_STF = STF


class RSP_K25_STAFF(HL7Model):
    """HL7 v2 RSP_K25.STAFF group.

    Attributes:
        STF (STF): Staff Identification, required
        PRA (Optional[List[PRA]]): Practitioner Detail, optional
        ORG (Optional[List[ORG]]): Practitioner Organization Unit, optional
        AFF (Optional[List[AFF]]): Professional Affiliation, optional
        LAN (Optional[List[LAN]]): Language Detail, optional
        EDU (Optional[List[EDU]]): Educational Detail, optional
        CER (Optional[List[CER]]): Certificate Detail, optional
    """

    STF: _STF = Field(
        title="STF",
        description="Staff Identification",
    )

    PRA: Optional[List[_PRA]] = Field(
        default=None,
        title="PRA",
        description="Practitioner Detail",
    )

    ORG: Optional[List[_ORG]] = Field(
        default=None,
        title="ORG",
        description="Practitioner Organization Unit",
    )

    AFF: Optional[List[_AFF]] = Field(
        default=None,
        title="AFF",
        description="Professional Affiliation",
    )

    LAN: Optional[List[_LAN]] = Field(
        default=None,
        title="LAN",
        description="Language Detail",
    )

    EDU: Optional[List[_EDU]] = Field(
        default=None,
        title="EDU",
        description="Educational Detail",
    )

    CER: Optional[List[_CER]] = Field(
        default=None,
        title="CER",
        description="Certificate Detail",
    )

    model_config = {"populate_by_name": True}
