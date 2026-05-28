"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: ACC
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CWE import CWE
from ..datatypes.XAD import XAD
from ..datatypes.XCN import XCN


class ACC(BaseModel):
    """HL7 v2 ACC segment."""

    acc_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "acc_1",
            "accident_date_time",
            "ACC.1",
        ),
        serialization_alias="ACC.1",
        title="Accident Date/Time",
        description="Item #527",
    )

    acc_2: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "acc_2",
            "accident_code",
            "ACC.2",
        ),
        serialization_alias="ACC.2",
        title="Accident Code",
        description="Item #528 | Table HL70050",
    )

    acc_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "acc_3",
            "accident_location",
            "ACC.3",
        ),
        serialization_alias="ACC.3",
        title="Accident Location",
        description="Item #529",
    )

    acc_4: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "acc_4",
            "auto_accident_state",
            "ACC.4",
        ),
        serialization_alias="ACC.4",
        title="Auto Accident State",
        description="Item #812 | Table HL70347",
    )

    acc_5: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "acc_5",
            "accident_job_related_indicator",
            "ACC.5",
        ),
        serialization_alias="ACC.5",
        title="Accident Job Related Indicator",
        description="Item #813 | Table HL70136",
    )

    acc_6: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "acc_6",
            "accident_death_indicator",
            "ACC.6",
        ),
        serialization_alias="ACC.6",
        title="Accident Death Indicator",
        description="Item #814 | Table HL70136",
    )

    acc_7: XCN | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "acc_7",
            "entered_by",
            "ACC.7",
        ),
        serialization_alias="ACC.7",
        title="Entered By",
        description="Item #224",
    )

    acc_8: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "acc_8",
            "accident_description",
            "ACC.8",
        ),
        serialization_alias="ACC.8",
        title="Accident Description",
        description="Item #1503",
    )

    acc_9: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "acc_9",
            "brought_in_by",
            "ACC.9",
        ),
        serialization_alias="ACC.9",
        title="Brought In By",
        description="Item #1504",
    )

    acc_10: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "acc_10",
            "police_notified_indicator",
            "ACC.10",
        ),
        serialization_alias="ACC.10",
        title="Police Notified Indicator",
        description="Item #1505 | Table HL70136",
    )

    acc_11: XAD | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "acc_11",
            "accident_address",
            "ACC.11",
        ),
        serialization_alias="ACC.11",
        title="Accident Address",
        description="Item #1853",
    )

    acc_12: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "acc_12",
            "degree_of_patient_liability",
            "ACC.12",
        ),
        serialization_alias="ACC.12",
        title="Degree of patient liability",
        description="Item #2374",
    )

    model_config = {"populate_by_name": True}
