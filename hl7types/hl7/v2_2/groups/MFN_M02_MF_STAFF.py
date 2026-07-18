"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: MFN_M02.MF_STAFF
Type: Group
"""
from __future__ import annotations

from typing import Optional, Any
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.MFE import MFE

_MFE = MFE


class MFN_M02_MF_STAFF(HL7Model):
    """HL7 v2 MFN_M02.MF_STAFF group.

    Attributes:
        MFE (MFE): MASTER FILE ENTRY, required
        anyzsegment (Optional[Any]): optional
    """

    MFE: _MFE = Field(
        title="MFE",
        description="MASTER FILE ENTRY",
    )

    anyzsegment: Optional[Any] = None

    model_config = ConfigDict(populate_by_name=True)
