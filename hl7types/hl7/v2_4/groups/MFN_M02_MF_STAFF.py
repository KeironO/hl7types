"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: MFN_M02.MF_STAFF
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.MFE import MFE
from ..segments.ORG import ORG
from ..segments.PRA import PRA
from ..segments.STF import STF

_MFE = MFE
_ORG = ORG
_PRA = PRA
_STF = STF


class MFN_M02_MF_STAFF(HL7Model):
    """HL7 v2 MFN_M02.MF_STAFF group.

    Attributes:
        MFE (MFE): Master File Entry, required
        STF (STF): Staff Identification, required
        PRA (Optional[PRA]): Practitioner Detail, optional
        ORG (Optional[ORG]): Practitioner Organization Unit, optional
    """

    MFE: _MFE = Field(
        title="MFE",
        description="Master File Entry",
    )

    STF: _STF = Field(
        title="STF",
        description="Staff Identification",
    )

    PRA: Optional[_PRA] = Field(
        default=None,
        title="PRA",
        description="Practitioner Detail",
    )

    ORG: Optional[_ORG] = Field(
        default=None,
        title="ORG",
        description="Practitioner Organization Unit",
    )

    model_config = ConfigDict(populate_by_name=True)
