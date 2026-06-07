"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: BAR_P02.PATIENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.DB1 import DB1
from ..segments.PD1 import PD1
from ..segments.PID import PID
from ..segments.PV1 import PV1

_DB1 = DB1
_PD1 = PD1
_PID = PID
_PV1 = PV1


class BAR_P02_PATIENT(HL7Model):
    """HL7 v2 BAR_P02.PATIENT group.

    Attributes:
        PID (PID): required
        PD1 (Optional[PD1]): optional
        PV1 (Optional[PV1]): optional
        DB1 (Optional[List[DB1]]): optional
    """

    PID: _PID = Field(
        title="PID",
        description="Required",
    )

    PD1: Optional[_PD1] = Field(
        default=None,
        title="PD1",
        description="Optional",
    )

    PV1: Optional[_PV1] = Field(
        default=None,
        title="PV1",
        description="Optional",
    )

    DB1: Optional[List[_DB1]] = Field(
        default=None,
        title="DB1",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
