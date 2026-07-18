"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: MFN_M15.MF_INV_ITEM
Type: Group
"""
from __future__ import annotations

from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.IIM import IIM
from ..segments.MFE import MFE

_IIM = IIM
_MFE = MFE


class MFN_M15_MF_INV_ITEM(HL7Model):
    """HL7 v2 MFN_M15.MF_INV_ITEM group.

    Attributes:
        MFE (MFE): Master File Entry, required
        IIM (IIM): Inventory Item Master, required
    """

    MFE: _MFE = Field(
        title="MFE",
        description="Master File Entry",
    )

    IIM: _IIM = Field(
        title="IIM",
        description="Inventory Item Master",
    )

    model_config = ConfigDict(populate_by_name=True)
