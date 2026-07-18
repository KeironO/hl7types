"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: CTI
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE
from ..datatypes.EI import EI


class CTI(HL7Model):
    """Clinical Trial Identification (S7.8.4).

    Attributes
    ----------
    cti_1 : EI
        CTI.1 - Sponsor Study ID (EI) R S7.8.1.1

    cti_2 : CWE | None
        CTI.2 - Study Phase Identifier (CWE) C S8.11.3.2

    cti_3 : CWE | None
        CTI.3 - Study Scheduled Time Point (CWE) O S7.8.3.1 | 9999 - no table for CE
    """

    cti_1: EI = Field(
        validation_alias=AliasChoices(
            "cti_1",
            "sponsor_study_id",
            "CTI.1",
        ),
        serialization_alias="CTI.1",
        title="Sponsor Study ID",
        description="R | Item #01011",
    )

    cti_2: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cti_2",
            "study_phase_identifier",
            "CTI.2",
        ),
        serialization_alias="CTI.2",
        title="Study Phase Identifier",
        description="C | Item #01022",
    )

    cti_3: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cti_3",
            "study_scheduled_time_point",
            "CTI.3",
        ),
        serialization_alias="CTI.3",
        title="Study Scheduled Time Point",
        description="O | Item #01055 | Table 9999 - no table for CE",
    )

    model_config = ConfigDict(populate_by_name=True)
