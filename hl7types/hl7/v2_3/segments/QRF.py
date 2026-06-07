"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: QRF
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.TQ import TQ
from ..datatypes.TS import TS


class QRF(HL7Model):
    """HL7 v2 QRF segment.

    Attributes
    ----------
    qrf_1 : list[str]
        QRF.1 (req, rep) - Where Subject Filter (ST)

    qrf_2 : TS | None
        QRF.2 (opt) - When Data Start Date/Time (TS)

    qrf_3 : TS | None
        QRF.3 (opt) - When Data End Date/Time (TS)

    qrf_4 : list[str] | None
        QRF.4 (opt, rep) - What User Qualifier (ST)

    qrf_5 : list[str] | None
        QRF.5 (opt, rep) - Other QRY Subject Filter (ST)

    qrf_6 : list[str] | None
        QRF.6 (opt, rep) - Which Date/Time Qualifier (ID)

    qrf_7 : list[str] | None
        QRF.7 (opt, rep) - Which Date/Time Status Qualifier (ID)

    qrf_8 : list[str] | None
        QRF.8 (opt, rep) - Date/Time Selection Qualifier (ID)

    qrf_9 : TQ | None
        QRF.9 (opt) - When Quantity/Timing Qualifier (TQ)
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
        description="Item #37",
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
        description="Item #38",
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
        description="Item #39",
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
        description="Item #40",
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
        description="Item #41",
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
        description="Item #42 | Table HL70156",
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
        description="Item #43 | Table HL70157",
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
        description="Item #44 | Table HL70158",
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
        description="Item #694",
    )

    model_config = {"populate_by_name": True}
