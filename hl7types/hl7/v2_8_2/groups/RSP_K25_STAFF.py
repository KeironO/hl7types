"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: RSP_K25.STAFF
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.AFF import AFF
from ..segments.CER import CER
from ..segments.EDU import EDU
from ..segments.LAN import LAN
from ..segments.NK1 import NK1
from ..segments.ORG import ORG
from ..segments.PRA import PRA
from ..segments.PRT import PRT
from ..segments.ROL import ROL
from ..segments.STF import STF

_AFF = AFF
_CER = CER
_EDU = EDU
_LAN = LAN
_NK1 = NK1
_ORG = ORG
_PRA = PRA
_PRT = PRT
_ROL = ROL
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
        NK1 (Optional[List[NK1]]): Next of Kin / Associated Parties, optional
        PRT (Optional[List[PRT]]): Participation Information, optional
        ROL (Optional[List[ROL]]): Role, optional
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

    NK1: Optional[List[_NK1]] = Field(
        default=None,
        title="NK1",
        description="Next of Kin / Associated Parties",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Participation Information",
    )

    ROL: Optional[List[_ROL]] = Field(
        default=None,
        title="ROL",
        description="Role",
    )

    model_config = ConfigDict(populate_by_name=True)
