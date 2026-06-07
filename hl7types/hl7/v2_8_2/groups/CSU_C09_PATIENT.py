"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: CSU_C09.PATIENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ARV import ARV
from ..segments.CSR import CSR
from ..segments.NTE import NTE
from ..segments.PD1 import PD1
from ..segments.PID import PID
from ..segments.PRT import PRT

from .CSU_C09_STUDY_PHASE import CSU_C09_STUDY_PHASE
from .CSU_C09_VISIT import CSU_C09_VISIT

_ARV = ARV
_CSR = CSR
_CSU_C09_STUDY_PHASE = CSU_C09_STUDY_PHASE
_CSU_C09_VISIT = CSU_C09_VISIT
_NTE = NTE
_PD1 = PD1
_PID = PID
_PRT = PRT


class CSU_C09_PATIENT(HL7Model):
    """HL7 v2 CSU_C09.PATIENT group.

    Attributes:
        PID (PID): required
        PD1 (Optional[PD1]): optional
        PRT (Optional[List[PRT]]): optional
        ARV (Optional[List[ARV]]): optional
        NTE (Optional[List[NTE]]): optional
        VISIT (Optional[CSU_C09_VISIT]): optional
        CSR (CSR): required
        STUDY_PHASE (List[CSU_C09_STUDY_PHASE]): required
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

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    ARV: Optional[List[_ARV]] = Field(
        default=None,
        title="ARV",
        description="Optional, repeating",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    VISIT: Optional[_CSU_C09_VISIT] = Field(
        default=None,
        title="VISIT",
        description="Optional",
    )

    CSR: _CSR = Field(
        title="CSR",
        description="Required",
    )

    STUDY_PHASE: List[_CSU_C09_STUDY_PHASE] = Field(
        min_length=1,
        title="STUDY_PHASE",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
