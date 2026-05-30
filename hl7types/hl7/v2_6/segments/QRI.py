"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: QRI
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE


class QRI(HL7Model):
    """HL7 v2 QRI segment.

    Attributes
    ----------
    qri_1 : str | None
        QRI.1 (opt) - Candidate Confidence (NM)

    qri_2 : list[str] | None
        QRI.2 (opt, rep) - Match Reason Code (IS)

    qri_3 : CWE | None
        QRI.3 (opt) - Algorithm Descriptor (CWE)
    """

    qri_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "qri_1",
            "candidate_confidence",
            "QRI.1",
        ),
        serialization_alias="QRI.1",
        title="Candidate Confidence",
        description="Item #1436",
    )

    qri_2: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "qri_2",
            "match_reason_code",
            "QRI.2",
        ),
        serialization_alias="QRI.2",
        title="Match Reason Code",
        description="Item #1437 | Table HL70392",
    )

    qri_3: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "qri_3",
            "algorithm_descriptor",
            "QRI.3",
        ),
        serialization_alias="QRI.3",
        title="Algorithm Descriptor",
        description="Item #1438 | Table HL70393",
    )

    model_config = {"populate_by_name": True}
