"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: QRI
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE


class QRI(BaseModel):
    """HL7 v2 QRI segment."""

    qri_1: str | None = Field(
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

    qri_2: list[str] | None = Field(
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

    qri_3: CE | None = Field(
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
