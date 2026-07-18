"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: QRD
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, ValidationInfo, field_validator
from hl7types.hl7 import HL7Model
from hl7types.hl7._validators import _apply_dt_fallback

from ..datatypes.CQ import CQ
from ..datatypes.CWE import CWE
from ..datatypes.VR import VR
from ..datatypes.XCN import XCN

_RE_DTM = re.compile(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?')


class QRD(HL7Model):
    """Original-Style Query Definition (S5.10.4.1).

    Attributes
    ----------
    qrd_1 : str
        QRD.1 - Query Date/Time (DTM) R S5.10.4.1.1

    qrd_2 : str
        QRD.2 - Query Format Code (ID) R S5.10.4.1.2 | 0106 - Query/response format code

    qrd_3 : str
        QRD.3 - Query Priority (ID) R S5.10.4.1.3 | 0091 - Query priority

    qrd_4 : str
        QRD.4 - Query ID (ST) R S5.10.4.1.4

    qrd_5 : str | None
        QRD.5 - Deferred Response Type (ID) O S5.10.4.1.5 | 0107 - Deferred response type

    qrd_6 : str | None
        QRD.6 - Deferred Response Date/Time (DTM) O S5.10.4.1.6

    qrd_7 : CQ
        QRD.7 - Quantity Limited Request (CQ) R S5.10.4.1.7 | 0126 - Quantity limited request

    qrd_8 : list[XCN]
        QRD.8 - Who Subject Filter (XCN) R rep S5.10.4.1.8

    qrd_9 : list[CWE]
        QRD.9 - What Subject Filter (CWE) R rep S5.10.4.1.9 | 0048 - What subject filter

    qrd_10 : list[CWE]
        QRD.10 - What Department Data Code (CWE) R rep S5.10.4.1.10

    qrd_11 : list[VR] | None
        QRD.11 - What Data Code Value Qual. (VR) O rep S5.10.4.1.11

    qrd_12 : str | None
        QRD.12 - Query Results Level (ID) O S5.10.4.1.12 | 0108 - Query results level
    """

    qrd_1: str = Field(
        validation_alias=AliasChoices(
            "qrd_1",
            "query_date_time",
            "QRD.1",
        ),
        serialization_alias="QRD.1",
        title="Query Date/Time",
        description="R | Item #00025 | LEN:24",
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

    qrd_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "qrd_6",
            "deferred_response_date_time",
            "QRD.6",
        ),
        serialization_alias="QRD.6",
        title="Deferred Response Date/Time",
        description="O | Item #00030 | LEN:24",
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

    qrd_9: List[CWE] = Field(
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

    qrd_10: List[CWE] = Field(
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

    @field_validator("qrd_1", "qrd_6", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        if _RE_DTM.fullmatch(v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = ConfigDict(populate_by_name=True)
