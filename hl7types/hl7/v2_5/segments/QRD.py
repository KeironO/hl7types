"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: QRD
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE
from ..datatypes.CQ import CQ
from ..datatypes.TS import TS
from ..datatypes.VR import VR
from ..datatypes.XCN import XCN


class QRD(BaseModel):
    """HL7 v2 QRD segment."""

    qrd_1: TS = Field(
        default=...,
        validation_alias=AliasChoices(
            "qrd_1",
            "query_date_time",
            "QRD.1",
        ),
        serialization_alias="QRD.1",
        title="Query Date/Time",
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

    qrd_5: str | None = Field(
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

    qrd_6: TS | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "qrd_6",
            "deferred_response_date_time",
            "QRD.6",
        ),
        serialization_alias="QRD.6",
        title="Deferred Response Date/Time",
        description="Item #30",
    )

    qrd_7: CQ = Field(
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

    qrd_8: list[XCN] = Field(
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

    qrd_9: list[CE] = Field(
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

    qrd_10: list[CE] = Field(
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

    qrd_11: list[VR] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "qrd_11",
            "what_data_code_value_qual",
            "QRD.11",
        ),
        serialization_alias="QRD.11",
        title="What Data Code Value Qual.",
        description="Item #35",
    )

    qrd_12: str | None = Field(
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
