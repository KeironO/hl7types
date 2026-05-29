"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: QRD
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.TS import TS


class QRD(BaseModel):
    """HL7 v2 QRD segment.

    Attributes
    ----------
    qrd_1 : TS
        QRD.1 (req) - Query date / time (TS)

    qrd_2 : str
        QRD.2 (req) - Query Format Code (ID)

    qrd_3 : str
        QRD.3 (req) - Query Priority (ID)

    qrd_4 : str
        QRD.4 (req) - Query ID (ST)

    qrd_5 : str | None
        QRD.5 (opt) - Deferred Response Type (ID)

    qrd_6 : TS | None
        QRD.6 (opt) - Deferred response date / time (TS)

    qrd_7 : str
        QRD.7 (req) - Quantity Limited Request (CQ)

    qrd_8 : list[str]
        QRD.8 (req, rep) - Who Subject Filter (ST)

    qrd_9 : list[str]
        QRD.9 (req, rep) - What Subject Filter (ID)

    qrd_10 : list[str]
        QRD.10 (req, rep) - What Department Data Code (ST)

    qrd_11 : list[str] | None
        QRD.11 (opt, rep) - What data code value qualifier (CM)

    qrd_12 : str | None
        QRD.12 (opt) - Query Results Level (ID)
    """

    qrd_1: TS = Field(
        default=...,
        validation_alias=AliasChoices(
            "qrd_1",
            "query_date_time",
            "QRD.1",
        ),
        serialization_alias="QRD.1",
        title="Query date / time",
        description="Item #25",
    )

    qrd_2: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "qrd_2",
            "query_format_code",
            "QRD.2",
        ),
        serialization_alias="QRD.2",
        title="Query Format Code",
        description="Item #26 | Table HL70106",
    )

    qrd_3: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "qrd_3",
            "query_priority",
            "QRD.3",
        ),
        serialization_alias="QRD.3",
        title="Query Priority",
        description="Item #27 | Table HL70091",
    )

    qrd_4: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "qrd_4",
            "query_id",
            "QRD.4",
        ),
        serialization_alias="QRD.4",
        title="Query ID",
        description="Item #28",
    )

    qrd_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "qrd_5",
            "deferred_response_type",
            "QRD.5",
        ),
        serialization_alias="QRD.5",
        title="Deferred Response Type",
        description="Item #29 | Table HL70107",
    )

    qrd_6: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "qrd_6",
            "deferred_response_date_time",
            "QRD.6",
        ),
        serialization_alias="QRD.6",
        title="Deferred response date / time",
        description="Item #30",
    )

    qrd_7: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "qrd_7",
            "quantity_limited_request",
            "QRD.7",
        ),
        serialization_alias="QRD.7",
        title="Quantity Limited Request",
        description="Item #31 | Table HL70126",
    )

    qrd_8: List[str] = Field(
        default=...,
        validation_alias=AliasChoices(
            "qrd_8",
            "who_subject_filter",
            "QRD.8",
        ),
        serialization_alias="QRD.8",
        title="Who Subject Filter",
        description="Item #32",
    )

    qrd_9: List[str] = Field(
        default=...,
        validation_alias=AliasChoices(
            "qrd_9",
            "what_subject_filter",
            "QRD.9",
        ),
        serialization_alias="QRD.9",
        title="What Subject Filter",
        description="Item #33 | Table HL70048",
    )

    qrd_10: List[str] = Field(
        default=...,
        validation_alias=AliasChoices(
            "qrd_10",
            "what_department_data_code",
            "QRD.10",
        ),
        serialization_alias="QRD.10",
        title="What Department Data Code",
        description="Item #34",
    )

    qrd_11: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "qrd_11",
            "what_data_code_value_qualifier",
            "QRD.11",
        ),
        serialization_alias="QRD.11",
        title="What data code value qualifier",
        description="Item #35",
    )

    qrd_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "qrd_12",
            "query_results_level",
            "QRD.12",
        ),
        serialization_alias="QRD.12",
        title="Query Results Level",
        description="Item #36 | Table HL70108",
    )

    model_config = {"populate_by_name": True}
