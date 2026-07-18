"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: ORG_O20.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.CTI import CTI
from ..segments.NTE import NTE
from ..segments.ORC import ORC

from .ORG_O20_OBSERVATION_GROUP import ORG_O20_OBSERVATION_GROUP
from .ORG_O20_SPECIMEN import ORG_O20_SPECIMEN
from .ORG_O20_TIMING import ORG_O20_TIMING

_CTI = CTI
_NTE = NTE
_ORC = ORC
_ORG_O20_OBSERVATION_GROUP = ORG_O20_OBSERVATION_GROUP
_ORG_O20_SPECIMEN = ORG_O20_SPECIMEN
_ORG_O20_TIMING = ORG_O20_TIMING


class ORG_O20_ORDER(HL7Model):
    """HL7 v2 ORG_O20.ORDER group.

    Attributes:
        ORC (ORC): Common Order, required
        TIMING (Optional[List[ORG_O20_TIMING]]): optional
        OBSERVATION_GROUP (Optional[ORG_O20_OBSERVATION_GROUP]): optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        CTI (Optional[List[CTI]]): Clinical Trial Identification, optional
        SPECIMEN (Optional[List[ORG_O20_SPECIMEN]]): optional
    """

    ORC: _ORC = Field(
        title="ORC",
        description="Common Order",
    )

    TIMING: Optional[List[_ORG_O20_TIMING]] = Field(
        default=None,
        title="TIMING",
    )

    OBSERVATION_GROUP: Optional[_ORG_O20_OBSERVATION_GROUP] = Field(
        default=None,
        title="OBSERVATION_GROUP",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    CTI: Optional[List[_CTI]] = Field(
        default=None,
        title="CTI",
        description="Clinical Trial Identification",
    )

    SPECIMEN: Optional[List[_ORG_O20_SPECIMEN]] = Field(
        default=None,
        title="SPECIMEN",
    )

    model_config = ConfigDict(populate_by_name=True)
