"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: QRD
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.TS import TS


class QRD(HL7Model):
    """QUERY DEFINITION (S2.10.4).

    Attributes
    ----------
    qrd_1 : TS
        QRD.1 - Query date / time (TS) R S2.10.4.1

    qrd_2 : str
        QRD.2 - Query Format Code (ID) R S2.10.4.2 | 0106 - QUERY FORMAT CODE

    qrd_3 : str
        QRD.3 - Query Priority (ID) R S2.10.4.3 | 0091 - QUERY PRIORITY

    qrd_4 : str
        QRD.4 - Query ID (ST) R S2.10.4.4

    qrd_5 : str | None
        QRD.5 - Deferred Response Type (ID) NA S2.10.4.5 | 0107 - DEFERRED RESPONSE TYPE

    qrd_6 : TS | None
        QRD.6 - Deferred response date / time (TS) NA S2.10.4.6

    qrd_7 : str
        QRD.7 - Quantity Limited Request (CQ) R S2.10.4.7 | 0126 - QUANTITY LIMITED REQUEST

    qrd_8 : list[str]
        QRD.8 - Who Subject Filter (ST) R rep S2.10.4.8

    qrd_9 : list[str]
        QRD.9 - What Subject Filter (ID) R rep S2.10.4.9 | 0048 - WHAT SUBJECT FILTER

    qrd_10 : list[str]
        QRD.10 - What Department Data Code (ST) R rep S2.10.4.10

    qrd_11 : list[str] | None
        QRD.11 - What data code value qualifier (CM) NA rep S2.10.4.11

    qrd_12 : str | None
        QRD.12 - Query Results Level (ID) NA S2.10.4.12 | 0108 - QUERY RESULTS LEVEL
    """

    qrd_1: TS = Field(
        validation_alias=AliasChoices(
            "qrd_1",
            "query_date_time",
            "QRD.1",
        ),
        serialization_alias="QRD.1",
        title="Query date / time",
        description="R | Item #00025",
    )

    qrd_2: str = Field(
        validation_alias=AliasChoices(
            "qrd_2",
            "query_format_code",
            "QRD.2",
        ),
        serialization_alias="QRD.2",
        title="Query Format Code",
        description="R | Item #00026 | Table 0106 - QUERY FORMAT CODE | LEN:1",
    )

    qrd_3: str = Field(
        validation_alias=AliasChoices(
            "qrd_3",
            "query_priority",
            "QRD.3",
        ),
        serialization_alias="QRD.3",
        title="Query Priority",
        description="R | Item #00027 | Table 0091 - QUERY PRIORITY | LEN:1",
    )

    qrd_4: str = Field(
        validation_alias=AliasChoices(
            "qrd_4",
            "query_id",
            "QRD.4",
        ),
        serialization_alias="QRD.4",
        title="Query ID",
        description="R | Item #00028 | LEN:10",
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
        description=(
            "NA | Item #00029 | Table 0107 - DEFERRED RESPONSE TYPE | LEN:1"
        ),
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
        description="NA | Item #00030",
    )

    qrd_7: str = Field(
        validation_alias=AliasChoices(
            "qrd_7",
            "quantity_limited_request",
            "QRD.7",
        ),
        serialization_alias="QRD.7",
        title="Quantity Limited Request",
        description="R | Item #00031 | Table 0126 - QUANTITY LIMITED REQUEST",
    )

    qrd_8: List[str] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "qrd_8",
            "who_subject_filter",
            "QRD.8",
        ),
        serialization_alias="QRD.8",
        title="Who Subject Filter",
        description="R | Item #00032 | LEN:20",
    )

    qrd_9: List[str] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "qrd_9",
            "what_subject_filter",
            "QRD.9",
        ),
        serialization_alias="QRD.9",
        title="What Subject Filter",
        description=(
            "R | Item #00033 | Table 0048 - WHAT SUBJECT FILTER | LEN:3"
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
        title="What Department Data Code",
        description="R | Item #00034 | LEN:20",
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
        description="NA | Item #00035",
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
        description=(
            "NA | Item #00036 | Table 0108 - QUERY RESULTS LEVEL | LEN:1"
        ),
    )

    model_config = {"populate_by_name": True}
