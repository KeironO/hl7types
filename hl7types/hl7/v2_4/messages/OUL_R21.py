"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: OUL_R21
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.DSC import DSC
from ..segments.MSH import MSH
from ..segments.NTE import NTE

from ..groups.OUL_R21_ORDER_OBSERVATION import OUL_R21_ORDER_OBSERVATION
from ..groups.OUL_R21_PATIENT import OUL_R21_PATIENT
from ..groups.OUL_R21_VISIT import OUL_R21_VISIT

_DSC = DSC
_MSH = MSH
_NTE = NTE
_OUL_R21_ORDER_OBSERVATION = OUL_R21_ORDER_OBSERVATION
_OUL_R21_PATIENT = OUL_R21_PATIENT
_OUL_R21_VISIT = OUL_R21_VISIT


class OUL_R21(HL7Model):
    """OUL - Unsolicited laboratory observation (S7).

    Attributes:
        MSH (MSH): Message Header, required
        NTE (Optional[NTE]): Notes and Comments, optional
        PATIENT (Optional[OUL_R21_PATIENT]): optional
        VISIT (Optional[OUL_R21_VISIT]): optional
        ORDER_OBSERVATION (List[OUL_R21_ORDER_OBSERVATION]): required
        DSC (Optional[DSC]): Continuation Pointer, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    NTE: Optional[_NTE] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    PATIENT: Optional[_OUL_R21_PATIENT] = Field(
        default=None,
        title="PATIENT",
    )

    VISIT: Optional[_OUL_R21_VISIT] = Field(
        default=None,
        title="VISIT",
    )

    ORDER_OBSERVATION: List[_OUL_R21_ORDER_OBSERVATION] = Field(
        min_length=1,
        title="ORDER_OBSERVATION",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Continuation Pointer",
    )

    model_config = {"populate_by_name": True}
