"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: PEX_P07.PEX_CAUSE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.PCR import PCR
from ..segments.PRB import PRB

from .PEX_P07_ASSOCIATED_PERSON import PEX_P07_ASSOCIATED_PERSON
from .PEX_P07_OBSERVATION import PEX_P07_OBSERVATION
from .PEX_P07_RX_ADMINISTRATION import PEX_P07_RX_ADMINISTRATION
from .PEX_P07_RX_ORDER import PEX_P07_RX_ORDER
from .PEX_P07_STUDY import PEX_P07_STUDY

_NTE = NTE
_PCR = PCR
_PEX_P07_ASSOCIATED_PERSON = PEX_P07_ASSOCIATED_PERSON
_PEX_P07_OBSERVATION = PEX_P07_OBSERVATION
_PEX_P07_RX_ADMINISTRATION = PEX_P07_RX_ADMINISTRATION
_PEX_P07_RX_ORDER = PEX_P07_RX_ORDER
_PEX_P07_STUDY = PEX_P07_STUDY
_PRB = PRB


class PEX_P07_PEX_CAUSE(HL7Model):
    """HL7 v2 PEX_P07.PEX_CAUSE group.

    Attributes:
        PCR (PCR): required
        RX_ORDER (Optional[PEX_P07_RX_ORDER]): optional
        RX_ADMINISTRATION (Optional[List[PEX_P07_RX_ADMINISTRATION]]): optional
        PRB (Optional[List[PRB]]): optional
        OBSERVATION (Optional[List[PEX_P07_OBSERVATION]]): optional
        NTE (Optional[List[NTE]]): optional
        ASSOCIATED_PERSON (Optional[PEX_P07_ASSOCIATED_PERSON]): optional
        STUDY (Optional[List[PEX_P07_STUDY]]): optional
    """

    PCR: _PCR = Field(
        title="PCR",
        description="Required",
    )

    RX_ORDER: Optional[_PEX_P07_RX_ORDER] = Field(
        default=None,
        title="RX_ORDER",
        description="Optional",
    )

    RX_ADMINISTRATION: Optional[List[_PEX_P07_RX_ADMINISTRATION]] = Field(
        default=None,
        title="RX_ADMINISTRATION",
        description="Optional, repeating",
    )

    PRB: Optional[List[_PRB]] = Field(
        default=None,
        title="PRB",
        description="Optional, repeating",
    )

    OBSERVATION: Optional[List[_PEX_P07_OBSERVATION]] = Field(
        default=None,
        title="OBSERVATION",
        description="Optional, repeating",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    ASSOCIATED_PERSON: Optional[_PEX_P07_ASSOCIATED_PERSON] = Field(
        default=None,
        title="ASSOCIATED_PERSON",
        description="Optional",
    )

    STUDY: Optional[List[_PEX_P07_STUDY]] = Field(
        default=None,
        title="STUDY",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
