"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: DFT_P11.VISIT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.PV1 import PV1
from ..segments.PV2 import PV2
from ..segments.ROL import ROL

_PV1 = PV1
_PV2 = PV2
_ROL = ROL


class DFT_P11_VISIT(HL7Model):
    """HL7 v2 DFT_P11.VISIT group.

    Attributes:
        PV1 (PV1): Patient Visit, required
        PV2 (Optional[PV2]): Patient Visit - Additional Information, optional
        ROL (Optional[List[ROL]]): Role, optional
    """

    PV1: _PV1 = Field(
        title="PV1",
        description="Patient Visit",
    )

    PV2: Optional[_PV2] = Field(
        default=None,
        title="PV2",
        description="Patient Visit - Additional Information",
    )

    ROL: Optional[List[_ROL]] = Field(
        default=None,
        title="ROL",
        description="Role",
    )

    model_config = ConfigDict(populate_by_name=True)
