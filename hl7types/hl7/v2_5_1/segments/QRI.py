"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: QRI
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator

from ..datatypes.CE import CE


class QRI(HL7Model):
    """HL7 v2 QRI segment.

    Attributes
    ----------
    qri_1 : str | None
        QRI.1 (opt) - Candidate Confidence (NM)

    qri_2 : list[str] | None
        QRI.2 (opt, rep) - Match Reason Code (IS)

    qri_3 : CE | None
        QRI.3 (opt) - Algorithm Descriptor (CE)
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

    qri_3: Optional[CE] = Field(
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

    @field_validator("qri_1", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
