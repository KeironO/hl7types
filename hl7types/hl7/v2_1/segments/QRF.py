"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: QRF
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field
from hl7types.hl7 import HL7Model


class QRF(HL7Model):
    """QUERY FILTER (S5.3.4).

    Attributes
    ----------
    qrf_1 : list[str]
        QRF.1 - WHERE SUBJECT FILTER (ST) R rep

    qrf_2 : str | None
        QRF.2 - WHEN DATA START DATE/TIME (TS) O

    qrf_3 : str | None
        QRF.3 - WHEN DATA END DATE/TIME (TS) O

    qrf_4 : list[str] | None
        QRF.4 - WHAT USER QUALIFIER (ST) O rep

    qrf_5 : list[str] | None
        QRF.5 - OTHER QRY SUBJECT FILTER (ST) O rep
    """

    qrf_1: List[str] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "qrf_1",
            "where_subject_filter",
            "QRF.1",
        ),
        serialization_alias="QRF.1",
        title="WHERE SUBJECT FILTER",
        description="R | Item #00173 | LEN:20",
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
        description="O | Item #00174 | LEN:19",
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
        description="O | Item #00176 | LEN:19",
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
        description="O | Item #00178 | LEN:20",
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
        description="O | Item #00179 | LEN:20",
    )

    model_config = ConfigDict(populate_by_name=True)
