"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: QRI
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE

_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class QRI(HL7Model):
    """Query Response Instance (S5.5.5).

    Attributes
    ----------
    qri_1 : str | None
        QRI.1 - Candidate Confidence (NM) O S5.5.5.1

    qri_2 : list[str] | None
        QRI.2 - Match Reason Code (IS) O rep S5.5.5.2 | 0392 - Match reason

    qri_3 : CE | None
        QRI.3 - Algorithm Descriptor (CE) O S5.5.5.3 | 0393 - Match algorithms
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
        description="O | Item #01436 | LEN:10",
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
        description="O | Item #01437 | Table 0392 - Match reason | LEN:2",
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
        description="O | Item #01438 | Table 0393 - Match algorithms",
    )

    @field_validator("qri_1", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
