"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: QRD
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field
from hl7types.hl7 import HL7Model


class QRD(HL7Model):
    """QUERY DEFINITION (S5.3.3).

    Attributes
    ----------
    qrd_1 : str
        QRD.1 - QUERY DATE/TIME (TS) R S5-6

    qrd_2 : str
        QRD.2 - QUERY FORMAT CODE (ID) R | 0106 - QUERY FORMAT CODE

    qrd_3 : str
        QRD.3 - QUERY PRIORITY (ID) R | 0091 - QUERY PRIORITY

    qrd_4 : str
        QRD.4 - QUERY ID (ST) R

    qrd_5 : str | None
        QRD.5 - DEFERRED RESPONSE TYPE (ID) O | 0107 - DEFERRED RESPONSE TYPE

    qrd_6 : str | None
        QRD.6 - DEFERRED RESPONSE DATE/TIME (TS) O

    qrd_7 : str
        QRD.7 - QUANTITY LIMITED REQUEST (CQ) R | 0126 - QUANTITY LIMITED REQUEST

    qrd_8 : list[str]
        QRD.8 - WHO SUBJECT FILTER (ST) R rep

    qrd_9 : list[str]
        QRD.9 - WHAT SUBJECT FILTER (ID) R rep | 0048 - WHAT SUBJECT FILTER

    qrd_10 : list[str]
        QRD.10 - WHAT DEPARTMENT DATA CODE (ST) R rep

    qrd_11 : list[str] | None
        QRD.11 - WHAT DATA CODE VALUE QUAL. (ST) O rep

    qrd_12 : str | None
        QRD.12 - QUERY RESULTS LEVEL (ID) O | 0108 - QUERY RESULTS LEVEL
    """

    qrd_1: str = Field(
        validation_alias=AliasChoices(
            "qrd_1",
            "query_date_time",
            "QRD.1",
        ),
        serialization_alias="QRD.1",
        title="QUERY DATE/TIME",
        description="R | Item #00156 | LEN:19",
    )

    qrd_2: str = Field(
        validation_alias=AliasChoices(
            "qrd_2",
            "query_format_code",
            "QRD.2",
        ),
        serialization_alias="QRD.2",
        title="QUERY FORMAT CODE",
        description="R | Item #00158 | Table 0106 - QUERY FORMAT CODE | LEN:1",
    )

    qrd_3: str = Field(
        validation_alias=AliasChoices(
            "qrd_3",
            "query_priority",
            "QRD.3",
        ),
        serialization_alias="QRD.3",
        title="QUERY PRIORITY",
        description="R | Item #00159 | Table 0091 - QUERY PRIORITY | LEN:1",
    )

    qrd_4: str = Field(
        validation_alias=AliasChoices(
            "qrd_4",
            "query_id",
            "QRD.4",
        ),
        serialization_alias="QRD.4",
        title="QUERY ID",
        description="R | Item #00160 | LEN:10",
    )

    qrd_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "qrd_5",
            "deferred_response_type",
            "QRD.5",
        ),
        serialization_alias="QRD.5",
        title="DEFERRED RESPONSE TYPE",
        description=(
            "O | Item #00161 | Table 0107 - DEFERRED RESPONSE TYPE | LEN:1"
        ),
    )

    qrd_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "qrd_6",
            "deferred_response_date_time",
            "QRD.6",
        ),
        serialization_alias="QRD.6",
        title="DEFERRED RESPONSE DATE/TIME",
        description="O | Item #00162 | LEN:19",
    )

    qrd_7: str = Field(
        validation_alias=AliasChoices(
            "qrd_7",
            "quantity_limited_request",
            "QRD.7",
        ),
        serialization_alias="QRD.7",
        title="QUANTITY LIMITED REQUEST",
        description=(
            "R | Item #00164 | Table 0126 - QUANTITY LIMITED REQUEST | LEN:5"
        ),
    )

    qrd_8: List[str] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "qrd_8",
            "who_subject_filter",
            "QRD.8",
        ),
        serialization_alias="QRD.8",
        title="WHO SUBJECT FILTER",
        description="R | Item #00168 | LEN:20",
    )

    qrd_9: List[str] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "qrd_9",
            "what_subject_filter",
            "QRD.9",
        ),
        serialization_alias="QRD.9",
        title="WHAT SUBJECT FILTER",
        description=(
            "R | Item #00169 | Table 0048 - WHAT SUBJECT FILTER | LEN:3"
        ),
    )

    qrd_10: List[str] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "qrd_10",
            "what_department_data_code",
            "QRD.10",
        ),
        serialization_alias="QRD.10",
        title="WHAT DEPARTMENT DATA CODE",
        description="R | Item #00170 | LEN:20",
    )

    qrd_11: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "qrd_11",
            "what_data_code_value_qual",
            "QRD.11",
        ),
        serialization_alias="QRD.11",
        title="WHAT DATA CODE VALUE QUAL.",
        description="O | Item #00171 | LEN:20",
    )

    qrd_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "qrd_12",
            "query_results_level",
            "QRD.12",
        ),
        serialization_alias="QRD.12",
        title="QUERY RESULTS LEVEL",
        description=(
            "O | Item #00701 | Table 0108 - QUERY RESULTS LEVEL | LEN:1"
        ),
    )

    model_config = ConfigDict(populate_by_name=True)
