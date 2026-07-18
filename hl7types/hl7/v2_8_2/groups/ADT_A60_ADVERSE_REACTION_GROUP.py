"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: ADT_A60.ADVERSE_REACTION_GROUP
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.IAM import IAM
from ..segments.IAR import IAR
from ..segments.NTE import NTE

_IAM = IAM
_IAR = IAR
_NTE = NTE


class ADT_A60_ADVERSE_REACTION_GROUP(HL7Model):
    """HL7 v2 ADT_A60.ADVERSE_REACTION_GROUP group.

    Attributes:
        IAM (IAM): Patient Adverse Reaction Information, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        IAR (Optional[List[IAR]]): allergy reaction, optional
    """

    IAM: _IAM = Field(
        title="IAM",
        description="Patient Adverse Reaction Information",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    IAR: Optional[List[_IAR]] = Field(
        default=None,
        title="IAR",
        description="allergy reaction",
    )

    model_config = ConfigDict(populate_by_name=True)
