"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: RSP_Z82.VISIT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.AL1 import AL1
from ..segments.PV1 import PV1
from ..segments.PV2 import PV2

_AL1 = AL1
_PV1 = PV1
_PV2 = PV2


class RSP_Z82_VISIT(HL7Model):
    """HL7 v2 RSP_Z82.VISIT group.

    Attributes:
        AL1 (List[AL1]): Patient Allergy Information, required
        PV1 (PV1): Patient Visit, required
        PV2 (Optional[PV2]): Patient Visit - Additional Information, optional
    """

    AL1: List[_AL1] = Field(
        min_length=1,
        title="AL1",
        description="Patient Allergy Information",
    )

    PV1: _PV1 = Field(
        title="PV1",
        description="Patient Visit",
    )

    PV2: Optional[_PV2] = Field(
        default=None,
        title="PV2",
        description="Patient Visit - Additional Information",
    )

    model_config = ConfigDict(populate_by_name=True)
