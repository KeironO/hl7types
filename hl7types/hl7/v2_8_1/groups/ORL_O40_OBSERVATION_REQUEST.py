"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: ORL_O40.OBSERVATION_REQUEST
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.OBR import OBR
from ..segments.PRT import PRT

from .ORL_O40_SPECIMEN_SHIPMENT import ORL_O40_SPECIMEN_SHIPMENT

_OBR = OBR
_ORL_O40_SPECIMEN_SHIPMENT = ORL_O40_SPECIMEN_SHIPMENT
_PRT = PRT


class ORL_O40_OBSERVATION_REQUEST(HL7Model):
    """HL7 v2 ORL_O40.OBSERVATION_REQUEST group.

    Attributes:
        OBR (OBR): required
        PRT (Optional[List[PRT]]): optional
        SPECIMEN_SHIPMENT (Optional[List[ORL_O40_SPECIMEN_SHIPMENT]]): optional
    """

    OBR: _OBR = Field(
        title="OBR",
        description="Required",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    SPECIMEN_SHIPMENT: Optional[List[_ORL_O40_SPECIMEN_SHIPMENT]] = Field(
        default=None,
        title="SPECIMEN_SHIPMENT",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
