"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: BAR_P01.INSURANCE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.IN1 import IN1
from ..segments.IN2 import IN2
from ..segments.IN3 import IN3
from ..segments.PRT import PRT
from ..segments.ROL import ROL

_IN1 = IN1
_IN2 = IN2
_IN3 = IN3
_PRT = PRT
_ROL = ROL


class BAR_P01_INSURANCE(HL7Model):
    """HL7 v2 BAR_P01.INSURANCE group.

    Attributes:
        IN1 (IN1): Insurance, required
        IN2 (Optional[IN2]): Insurance Additional Information, optional
        IN3 (Optional[List[IN3]]): Insurance Additional Information, Certification, optional
        PRT (Optional[List[PRT]]): Participation Information, optional
        ROL (Optional[List[ROL]]): Role, optional
    """

    IN1: _IN1 = Field(
        title="IN1",
        description="Insurance",
    )

    IN2: Optional[_IN2] = Field(
        default=None,
        title="IN2",
        description="Insurance Additional Information",
    )

    IN3: Optional[List[_IN3]] = Field(
        default=None,
        title="IN3",
        description="Insurance Additional Information, Certification",
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
