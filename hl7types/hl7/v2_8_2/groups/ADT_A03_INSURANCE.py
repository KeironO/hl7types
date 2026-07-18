"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: ADT_A03.INSURANCE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.AUT import AUT
from ..segments.IN1 import IN1
from ..segments.IN2 import IN2
from ..segments.IN3 import IN3
from ..segments.RF1 import RF1
from ..segments.ROL import ROL

_AUT = AUT
_IN1 = IN1
_IN2 = IN2
_IN3 = IN3
_RF1 = RF1
_ROL = ROL


class ADT_A03_INSURANCE(HL7Model):
    """HL7 v2 ADT_A03.INSURANCE group.

    Attributes:
        IN1 (IN1): Insurance, required
        IN2 (Optional[IN2]): Insurance Additional Information, optional
        IN3 (Optional[List[IN3]]): Insurance Additional Information, Certification, optional
        ROL (Optional[List[ROL]]): Role, optional
        AUT (Optional[List[AUT]]): Authorization Information, optional
        RF1 (Optional[List[RF1]]): Referral Information, optional
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

    ROL: Optional[List[_ROL]] = Field(
        default=None,
        title="ROL",
        description="Role",
    )

    AUT: Optional[List[_AUT]] = Field(
        default=None,
        title="AUT",
        description="Authorization Information",
    )

    RF1: Optional[List[_RF1]] = Field(
        default=None,
        title="RF1",
        description="Referral Information",
    )

    model_config = ConfigDict(populate_by_name=True)
