"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: QRF
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model


class QRF(HL7Model):
    """HL7 v2 QRF segment.

    Attributes
    ----------
    qrf_1 : list[str]
        QRF.1 (req, rep) - WHERE SUBJECT FILTER (ST)

    qrf_2 : str | None
        QRF.2 (opt) - WHEN DATA START DATE/TIME (TS)

    qrf_3 : str | None
        QRF.3 (opt) - WHEN DATA END DATE/TIME (TS)

    qrf_4 : list[str] | None
        QRF.4 (opt, rep) - WHAT USER QUALIFIER (ST)

    qrf_5 : list[str] | None
        QRF.5 (opt, rep) - OTHER QRY SUBJECT FILTER (ST)
    """

    qrf_1: List[str] = Field(
        default=...,
        validation_alias=AliasChoices(
            "qrf_1",
            "where_subject_filter",
            "QRF.1",
        ),
        serialization_alias="QRF.1",
        title="WHERE SUBJECT FILTER",
        description="Item #173",
    )

    qrf_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "qrf_2",
            "when_data_start_date_time",
            "QRF.2",
        ),
        serialization_alias="QRF.2",
        title="WHEN DATA START DATE/TIME",
        description="Item #174",
    )

    qrf_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "qrf_3",
            "when_data_end_date_time",
            "QRF.3",
        ),
        serialization_alias="QRF.3",
        title="WHEN DATA END DATE/TIME",
        description="Item #176",
    )

    qrf_4: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "qrf_4",
            "what_user_qualifier",
            "QRF.4",
        ),
        serialization_alias="QRF.4",
        title="WHAT USER QUALIFIER",
        description="Item #178",
    )

    qrf_5: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "qrf_5",
            "other_qry_subject_filter",
            "QRF.5",
        ),
        serialization_alias="QRF.5",
        title="OTHER QRY SUBJECT FILTER",
        description="Item #179",
    )

    model_config = {"populate_by_name": True}
