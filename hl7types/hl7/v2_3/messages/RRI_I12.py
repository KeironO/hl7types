"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: RRI_I12
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.ACC import ACC
from ..segments.AL1 import AL1
from ..segments.DG1 import DG1
from ..segments.DRG import DRG
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.PID import PID
from ..segments.RF1 import RF1

from ..groups.RRI_I12_AUTHORIZATION import RRI_I12_AUTHORIZATION
from ..groups.RRI_I12_PROCEDURE import RRI_I12_PROCEDURE
from ..groups.RRI_I12_PROVIDER import RRI_I12_PROVIDER
from ..groups.RRI_I12_RESULTS import RRI_I12_RESULTS
from ..groups.RRI_I12_VISIT import RRI_I12_VISIT

_ACC = ACC
_AL1 = AL1
_DG1 = DG1
_DRG = DRG
_MSA = MSA
_MSH = MSH
_NTE = NTE
_PID = PID
_RF1 = RF1
_RRI_I12_AUTHORIZATION = RRI_I12_AUTHORIZATION
_RRI_I12_PROCEDURE = RRI_I12_PROCEDURE
_RRI_I12_PROVIDER = RRI_I12_PROVIDER
_RRI_I12_RESULTS = RRI_I12_RESULTS
_RRI_I12_VISIT = RRI_I12_VISIT


class RRI_I12(HL7Model):
    """REF/RRI -  Patient referral.

    Attributes:
        MSH (MSH): Message header segment, required
        MSA (Optional[MSA]): Message acknowledgement segment, optional
        RF1 (Optional[RF1]): Referral Information Segment, optional
        AUTHORIZATION (Optional[RRI_I12_AUTHORIZATION]): optional
        PROVIDER (List[RRI_I12_PROVIDER]): required
        PID (PID): Patient Identification, required
        ACC (Optional[ACC]): Accident, optional
        DG1 (Optional[List[DG1]]): Diagnosis, optional
        DRG (Optional[List[DRG]]): Diagnosis Related Group, optional
        AL1 (Optional[List[AL1]]): Patient allergy information, optional
        PROCEDURE (Optional[List[RRI_I12_PROCEDURE]]): optional
        RESULTS (Optional[List[RRI_I12_RESULTS]]): optional
        VISIT (Optional[RRI_I12_VISIT]): optional
        NTE (Optional[List[NTE]]): Notes and comments segment, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message header segment",
    )

    MSA: Optional[_MSA] = Field(
        default=None,
        title="MSA",
        description="Message acknowledgement segment",
    )

    RF1: Optional[_RF1] = Field(
        default=None,
        title="RF1",
        description="Referral Information Segment",
    )

    AUTHORIZATION: Optional[_RRI_I12_AUTHORIZATION] = Field(
        default=None,
        title="AUTHORIZATION",
    )

    PROVIDER: List[_RRI_I12_PROVIDER] = Field(
        min_length=1,
        title="PROVIDER",
    )

    PID: _PID = Field(
        title="PID",
        description="Patient Identification",
    )

    ACC: Optional[_ACC] = Field(
        default=None,
        title="ACC",
        description="Accident",
    )

    DG1: Optional[List[_DG1]] = Field(
        default=None,
        title="DG1",
        description="Diagnosis",
    )

    DRG: Optional[List[_DRG]] = Field(
        default=None,
        title="DRG",
        description="Diagnosis Related Group",
    )

    AL1: Optional[List[_AL1]] = Field(
        default=None,
        title="AL1",
        description="Patient allergy information",
    )

    PROCEDURE: Optional[List[_RRI_I12_PROCEDURE]] = Field(
        default=None,
        title="PROCEDURE",
    )

    RESULTS: Optional[List[_RRI_I12_RESULTS]] = Field(
        default=None,
        title="RESULTS",
    )

    VISIT: Optional[_RRI_I12_VISIT] = Field(
        default=None,
        title="VISIT",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and comments segment",
    )

    model_config = ConfigDict(populate_by_name=True)
