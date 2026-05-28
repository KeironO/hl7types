"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: QRD
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field


class QRD(BaseModel):
    """HL7 v2 QRD segment."""

    qrd_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "qrd_1",
            "query_date_time",
            "QRD.1",
        ),
        serialization_alias="QRD.1",
        title="QUERY DATE/TIME",
        description="Item #156",
    )

    qrd_2: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "qrd_2",
            "query_format_code",
            "QRD.2",
        ),
        serialization_alias="QRD.2",
        title="QUERY FORMAT CODE",
        description="Item #158 | Table HL70106",
    )

    qrd_3: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "qrd_3",
            "query_priority",
            "QRD.3",
        ),
        serialization_alias="QRD.3",
        title="QUERY PRIORITY",
        description="Item #159 | Table HL70091",
    )

    qrd_4: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "qrd_4",
            "query_id",
            "QRD.4",
        ),
        serialization_alias="QRD.4",
        title="QUERY ID",
        description="Item #160",
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
        description="Item #161 | Table HL70107",
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
        description="Item #162",
    )

    qrd_7: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "qrd_7",
            "quantity_limited_request",
            "QRD.7",
        ),
        serialization_alias="QRD.7",
        title="QUANTITY LIMITED REQUEST",
        description="Item #164 | Table HL70126",
    )

    qrd_8: List[str] = Field(
        default=...,
        validation_alias=AliasChoices(
            "qrd_8",
            "who_subject_filter",
            "QRD.8",
        ),
        serialization_alias="QRD.8",
        title="WHO SUBJECT FILTER",
        description="Item #168",
    )

    qrd_9: List[str] = Field(
        default=...,
        validation_alias=AliasChoices(
            "qrd_9",
            "what_subject_filter",
            "QRD.9",
        ),
        serialization_alias="QRD.9",
        title="WHAT SUBJECT FILTER",
        description="Item #169 | Table HL70048",
    )

    qrd_10: List[str] = Field(
        default=...,
        validation_alias=AliasChoices(
            "qrd_10",
            "what_department_data_code",
            "QRD.10",
        ),
        serialization_alias="QRD.10",
        title="WHAT DEPARTMENT DATA CODE",
        description="Item #170",
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
        description="Item #171",
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
        description="Item #701 | Table HL70108",
    )

    model_config = {"populate_by_name": True}
