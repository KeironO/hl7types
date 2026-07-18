"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: QRF
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..datatypes.TS import TS


class QRF(HL7Model):
    """QUERY FILTER (S2.10.5).

    Attributes
    ----------
    qrf_1 : list[str]
        QRF.1 - Where Subject Filter (ST) R rep S2.10.5.1

    qrf_2 : TS | None
        QRF.2 - When data start date / time (TS) NA S2.10.5.2

    qrf_3 : TS | None
        QRF.3 - When data end date / time (TS) NA S2.10.5.3

    qrf_4 : list[str] | None
        QRF.4 - What User Qualifier (ST) NA rep S2.10.5.4

    qrf_5 : list[str] | None
        QRF.5 - Other QRY Subject Filter (ST) NA rep S2.10.5.5

    qrf_6 : list[str] | None
        QRF.6 - Which date / time qualifier (ID) NA rep S2.10.5.6 | 0156 - DATE/TIME QUALIFIER

    qrf_7 : list[str] | None
        QRF.7 - Which date / time status qualifier (ID) NA rep S2.10.5.7 | 0157 - WHIHC DATE/TIME STATUS QUALIFIER

    qrf_8 : list[str] | None
        QRF.8 - Date / time selection qualifier (ID) NA rep S2.10.5.8 | 0158 - DATE/TIME SELECTION QUALIFIER
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
        title="When data start date / time",
        description="NA | Item #00038",
    )

    qrf_3: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "qrf_3",
            "when_data_end_date_time",
            "QRF.3",
        ),
        serialization_alias="QRF.3",
        title="When data end date / time",
        description="NA | Item #00039",
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
        description="NA | Item #00040 | LEN:20",
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
        description="NA | Item #00041 | LEN:20",
    )

    qrf_6: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "qrf_6",
            "which_date_time_qualifier",
            "QRF.6",
        ),
        serialization_alias="QRF.6",
        title="Which date / time qualifier",
        description=(
            "NA | Item #00042 | Table 0156 - DATE/TIME QUALIFIER | LEN:12"
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
        title="Which date / time status qualifier",
        description=(
            "NA | Item #00043 | Table 0157 - WHIHC DATE/TIME STATUS QUALIFIER | "
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
        title="Date / time selection qualifier",
        description=(
            "NA | Item #00044 | Table 0158 - DATE/TIME SELECTION QUALIFIER | "
            "LEN:12"
        ),
    )

    model_config = ConfigDict(populate_by_name=True)
