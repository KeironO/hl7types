"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: ADT_A06.INSURANCE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.IN1 import IN1
from ..segments.IN2 import IN2
from ..segments.IN3 import IN3
from ..segments.ROL import ROL

_IN1 = IN1
_IN2 = IN2
_IN3 = IN3
_ROL = ROL


class ADT_A06_INSURANCE(HL7Model):
    """HL7 v2 ADT_A06.INSURANCE group.

    Attributes:
        IN1 (IN1): Insurance, required
        IN2 (Optional[IN2]): Insurance Additional Information, optional
        IN3 (Optional[List[IN3]]): Insurance Additional Information, Certification, optional
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

    ROL: Optional[List[_ROL]] = Field(
        default=None,
        title="ROL",
        description="Role",
    )

    model_config = ConfigDict(populate_by_name=True)
