"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: QRD
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.CQ import CQ
from ..datatypes.TS import TS
from ..datatypes.VR import VR
from ..datatypes.XCN import XCN


class QRD(HL7Model):
    """Original-Style Query Definition (S5.10.5.3).

    Attributes
    ----------
    qrd_1 : TS
        QRD.1 - Query Date/Time (TS) R S5.10.5.3.1

    qrd_2 : str
        QRD.2 - Query Format Code (ID) R S5.10.5.3.2 | 0106 - Query/response format code

    qrd_3 : str
        QRD.3 - Query Priority (ID) R S5.10.5.3.3 | 0091 - Query priority

    qrd_4 : str
        QRD.4 - Query ID (ST) R S5.10.5.3.4

    qrd_5 : str | None
        QRD.5 - Deferred Response Type (ID) O S5.10.5.3.5 | 0107 - Deferred response type

    qrd_6 : TS | None
        QRD.6 - Deferred Response Date/Time (TS) O S5.10.5.3.6

    qrd_7 : CQ
        QRD.7 - Quantity Limited Request (CQ) R S5.10.5.3.7 | 0126 - Quantity limited request

    qrd_8 : list[XCN]
        QRD.8 - Who Subject Filter (XCN) R rep S5.10.5.3.8

    qrd_9 : list[CE]
        QRD.9 - What Subject Filter (CE) R rep S5.10.5.3.9 | 0048 - What subject filter

    qrd_10 : list[CE]
        QRD.10 - What Department Data Code (CE) R rep S5.10.5.3.1

    qrd_11 : list[VR] | None
        QRD.11 - What Data Code Value Qual. (VR) O rep S5.10.5.3.1

    qrd_12 : str | None
        QRD.12 - Query Results Level (ID) O S5.10.5.3.1 | 0108 - Query results level
    """

    qrd_1: TS = Field(
        validation_alias=AliasChoices(
            "qrd_1",
            "query_date_time",
            "QRD.1",
        ),
        serialization_alias="QRD.1",
        title="Query Date/Time",
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
        description=(
            "R | Item #00026 | Table 0106 - Query/response format code | LEN:1"
        ),
    )

    qrd_3: str = Field(
        validation_alias=AliasChoices(
            "qrd_3",
            "query_priority",
            "QRD.3",
        ),
        serialization_alias="QRD.3",
        title="Query Priority",
        description="R | Item #00027 | Table 0091 - Query priority | LEN:1",
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
            "O | Item #00029 | Table 0107 - Deferred response type | LEN:1"
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
        title="Deferred Response Date/Time",
        description="O | Item #00030",
    )

    qrd_7: CQ = Field(
        validation_alias=AliasChoices(
            "qrd_7",
            "quantity_limited_request",
            "QRD.7",
        ),
        serialization_alias="QRD.7",
        title="Quantity Limited Request",
        description="R | Item #00031 | Table 0126 - Quantity limited request",
    )

    qrd_8: List[XCN] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "qrd_8",
            "who_subject_filter",
            "QRD.8",
        ),
        serialization_alias="QRD.8",
        title="Who Subject Filter",
        description="R | Item #00032",
    )

    qrd_9: List[CE] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "qrd_9",
            "what_subject_filter",
            "QRD.9",
        ),
        serialization_alias="QRD.9",
        title="What Subject Filter",
        description="R | Item #00033 | Table 0048 - What subject filter",
    )

    qrd_10: List[CE] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "qrd_10",
            "what_department_data_code",
            "QRD.10",
        ),
        serialization_alias="QRD.10",
        title="What Department Data Code",
        description="R | Item #00034",
    )

    qrd_11: Optional[List[VR]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "qrd_11",
            "what_data_code_value_qual",
            "QRD.11",
        ),
        serialization_alias="QRD.11",
        title="What Data Code Value Qual.",
        description="O | Item #00035",
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
            "O | Item #00036 | Table 0108 - Query results level | LEN:1"
        ),
    )

    model_config = {"populate_by_name": True}
