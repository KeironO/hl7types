"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: OUL_R23
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.DSC import DSC
from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.SFT import SFT

from ..groups.OUL_R23_PATIENT import OUL_R23_PATIENT
from ..groups.OUL_R23_SPECIMEN import OUL_R23_SPECIMEN
from ..groups.OUL_R23_VISIT import OUL_R23_VISIT

_DSC = DSC
_MSH = MSH
_NTE = NTE
_OUL_R23_PATIENT = OUL_R23_PATIENT
_OUL_R23_SPECIMEN = OUL_R23_SPECIMEN
_OUL_R23_VISIT = OUL_R23_VISIT
_SFT = SFT


class OUL_R23(HL7Model):
    """HL7 v2 OUL_R23 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        NTE (Optional[NTE]): optional
        PATIENT (Optional[OUL_R23_PATIENT]): optional
        VISIT (Optional[OUL_R23_VISIT]): optional
        SPECIMEN (List[OUL_R23_SPECIMEN]): required
        DSC (Optional[DSC]): optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Required",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    NTE: Optional[_NTE] = Field(
        default=None,
        title="NTE",
        description="Optional",
    )

    PATIENT: Optional[_OUL_R23_PATIENT] = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    VISIT: Optional[_OUL_R23_VISIT] = Field(
        default=None,
        title="VISIT",
        description="Optional",
    )

    SPECIMEN: List[_OUL_R23_SPECIMEN] = Field(
        min_length=1,
        title="SPECIMEN",
        description="Required, repeating",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
