"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: QRF
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.TQ import TQ
from ..datatypes.TS import TS

_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class QRF(HL7Model):
    """Original style query filter (S5.10.5.4).

    Attributes
    ----------
    qrf_1 : list[str]
        QRF.1 - Where Subject Filter (ST) R rep S5.10.5.4.1

    qrf_2 : TS | None
        QRF.2 - When Data Start Date/Time (TS) O S5.10.5.4.2

    qrf_3 : TS | None
        QRF.3 - When Data End Date/Time (TS) O S5.10.5.4.3

    qrf_4 : list[str] | None
        QRF.4 - What User Qualifier (ST) O rep S5.10.5.4.4

    qrf_5 : list[str] | None
        QRF.5 - Other QRY Subject Filter (ST) O rep S5.10.5.4.5

    qrf_6 : list[str] | None
        QRF.6 - Which Date/Time Qualifier (ID) O rep S5.10.5.4.6 | 0156 - Which date/time qualifier

    qrf_7 : list[str] | None
        QRF.7 - Which Date/Time Status Qualifier (ID) O rep S5.10.5.4.7 | 0157 - Which date/time status qualifier

    qrf_8 : list[str] | None
        QRF.8 - Date/Time Selection Qualifier (ID) O rep S5.10.5.4.8 | 0158 - Date/time selection qualifier

    qrf_9 : TQ | None
        QRF.9 - When Quantity/Timing Qualifier (TQ) O S5.10.5.4.9

    qrf_10 : str | None
        QRF.10 - Search Confidence Threshold (NM) O S5.10.5.4.1
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

    qrf_2: Optional[TS] = Field(
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

    qrf_3: Optional[TS] = Field(
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

    @field_validator("qrf_10", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
