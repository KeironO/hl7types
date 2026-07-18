"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: QRF
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, ValidationInfo, field_validator
from hl7types.hl7 import HL7Model
from hl7types.hl7._validators import _apply_dt_fallback

from ..datatypes.TQ import TQ

_RE_DTM = re.compile(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?')
_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class QRF(HL7Model):
    """Original style query filter (S5.10.4.2).

    Attributes
    ----------
    qrf_1 : list[str]
        QRF.1 - Where Subject Filter (ST) R rep S5.10.4.2.1

    qrf_2 : str | None
        QRF.2 - When Data Start Date/Time (DTM) O S5.10.4.2.2

    qrf_3 : str | None
        QRF.3 - When Data End Date/Time (DTM) O S5.10.4.2.3

    qrf_4 : list[str] | None
        QRF.4 - What User Qualifier (ST) O rep S5.10.4.2.4

    qrf_5 : list[str] | None
        QRF.5 - Other QRY Subject Filter (ST) O rep S5.10.4.2.5

    qrf_6 : list[str] | None
        QRF.6 - Which Date/Time Qualifier (ID) O rep S5.10.4.2.6 | 0156 - Which date/time qualifier

    qrf_7 : list[str] | None
        QRF.7 - Which Date/Time Status Qualifier (ID) O rep S5.10.4.2.7 | 0157 - Which date/time status qualifier

    qrf_8 : list[str] | None
        QRF.8 - Date/Time Selection Qualifier (ID) O rep S5.10.4.2.8 | 0158 - Date/time selection qualifier

    qrf_9 : TQ | None
        QRF.9 - When Quantity/Timing Qualifier (TQ) O S5.10.4.2.9

    qrf_10 : str | None
        QRF.10 - Search Confidence Threshold (NM) O S5.10.4.2.10
    """

    qrf_1: List[str] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "qrf_1",
            "where_subject_filter",
            "QRF.1",
        ),
        serialization_alias="QRF.1",
        title="Where Subject Filter",
        description="R | Item #00037 | LEN:20",
    )

    qrf_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "qrf_2",
            "when_data_start_date_time",
            "QRF.2",
        ),
        serialization_alias="QRF.2",
        title="When Data Start Date/Time",
        description="O | Item #00038",
    )

    qrf_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "qrf_3",
            "when_data_end_date_time",
            "QRF.3",
        ),
        serialization_alias="QRF.3",
        title="When Data End Date/Time",
        description="O | Item #00039",
    )

    qrf_4: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "qrf_4",
            "what_user_qualifier",
            "QRF.4",
        ),
        serialization_alias="QRF.4",
        title="What User Qualifier",
        description="O | Item #00040 | LEN:60",
    )

    qrf_5: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "qrf_5",
            "other_qry_subject_filter",
            "QRF.5",
        ),
        serialization_alias="QRF.5",
        title="Other QRY Subject Filter",
        description="O | Item #00041 | LEN:60",
    )

    qrf_6: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "qrf_6",
            "which_date_time_qualifier",
            "QRF.6",
        ),
        serialization_alias="QRF.6",
        title="Which Date/Time Qualifier",
        description=(
            "O | Item #00042 | Table 0156 - Which date/time qualifier | LEN:12"
        ),
    )

    qrf_7: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "qrf_7",
            "which_date_time_status_qualifier",
            "QRF.7",
        ),
        serialization_alias="QRF.7",
        title="Which Date/Time Status Qualifier",
        description=(
            "O | Item #00043 | Table 0157 - Which date/time status qualifier | "
            "LEN:12"
        ),
    )

    qrf_8: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "qrf_8",
            "date_time_selection_qualifier",
            "QRF.8",
        ),
        serialization_alias="QRF.8",
        title="Date/Time Selection Qualifier",
        description=(
            "O | Item #00044 | Table 0158 - Date/time selection qualifier | "
            "LEN:12"
        ),
    )

    qrf_9: Optional[TQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "qrf_9",
            "when_quantity_timing_qualifier",
            "QRF.9",
        ),
        serialization_alias="QRF.9",
        title="When Quantity/Timing Qualifier",
        description="O | Item #00694",
    )

    qrf_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "qrf_10",
            "search_confidence_threshold",
            "QRF.10",
        ),
        serialization_alias="QRF.10",
        title="Search Confidence Threshold",
        description="O | Item #01442 | LEN:10",
    )

    @field_validator("qrf_2", "qrf_3", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        if _RE_DTM.fullmatch(v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    @field_validator("qrf_10", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
