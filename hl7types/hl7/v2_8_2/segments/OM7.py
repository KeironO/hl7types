"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: OM7
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CWE import CWE
from ..datatypes.PL import PL
from ..datatypes.TX import TX
from ..datatypes.XCN import XCN


class OM7(BaseModel):
    """HL7 v2 OM7 segment."""

    om7_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "om7_1",
            "sequence_number_test_observation_master_file",
            "OM7.1",
        ),
        serialization_alias="OM7.1",
        title="Sequence Number - Test/Observation Master File",
        description="Item #586",
    )

    om7_2: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "om7_2",
            "universal_service_identifier",
            "OM7.2",
        ),
        serialization_alias="OM7.2",
        title="Universal Service Identifier",
        description="Item #238",
    )

    om7_3: list[CWE] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "om7_3",
            "category_identifier",
            "OM7.3",
        ),
        serialization_alias="OM7.3",
        title="Category Identifier",
        description="Item #1481 | Table HL70412",
    )

    om7_4: TX | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "om7_4",
            "category_description",
            "OM7.4",
        ),
        serialization_alias="OM7.4",
        title="Category Description",
        description="Item #1482",
    )

    om7_5: list[str] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "om7_5",
            "category_synonym",
            "OM7.5",
        ),
        serialization_alias="OM7.5",
        title="Category Synonym",
        description="Item #1483",
    )

    om7_6: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "om7_6",
            "effective_test_service_start_date_time",
            "OM7.6",
        ),
        serialization_alias="OM7.6",
        title="Effective Test/Service Start Date/Time",
        description="Item #1484",
    )

    om7_7: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "om7_7",
            "effective_test_service_end_date_time",
            "OM7.7",
        ),
        serialization_alias="OM7.7",
        title="Effective Test/Service End Date/Time",
        description="Item #1485",
    )

    om7_8: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "om7_8",
            "test_service_default_duration_quantity",
            "OM7.8",
        ),
        serialization_alias="OM7.8",
        title="Test/Service Default Duration Quantity",
        description="Item #1486",
    )

    om7_9: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "om7_9",
            "test_service_default_duration_units",
            "OM7.9",
        ),
        serialization_alias="OM7.9",
        title="Test/Service Default Duration Units",
        description="Item #1487 | Table HL79999",
    )

    om7_10: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "om7_10",
            "test_service_default_frequency",
            "OM7.10",
        ),
        serialization_alias="OM7.10",
        title="Test/Service Default Frequency",
        description="Item #1488",
    )

    om7_11: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "om7_11",
            "consent_indicator",
            "OM7.11",
        ),
        serialization_alias="OM7.11",
        title="Consent Indicator",
        description="Item #1489 | Table HL70136",
    )

    om7_12: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "om7_12",
            "consent_identifier",
            "OM7.12",
        ),
        serialization_alias="OM7.12",
        title="Consent Identifier",
        description="Item #1490 | Table HL70413",
    )

    om7_13: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "om7_13",
            "consent_effective_start_date_time",
            "OM7.13",
        ),
        serialization_alias="OM7.13",
        title="Consent Effective Start Date/Time",
        description="Item #1491",
    )

    om7_14: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "om7_14",
            "consent_effective_end_date_time",
            "OM7.14",
        ),
        serialization_alias="OM7.14",
        title="Consent Effective End Date/Time",
        description="Item #1492",
    )

    om7_15: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "om7_15",
            "consent_interval_quantity",
            "OM7.15",
        ),
        serialization_alias="OM7.15",
        title="Consent Interval Quantity",
        description="Item #1493",
    )

    om7_16: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "om7_16",
            "consent_interval_units",
            "OM7.16",
        ),
        serialization_alias="OM7.16",
        title="Consent Interval Units",
        description="Item #1494 | Table HL70414",
    )

    om7_17: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "om7_17",
            "consent_waiting_period_quantity",
            "OM7.17",
        ),
        serialization_alias="OM7.17",
        title="Consent Waiting Period Quantity",
        description="Item #1495",
    )

    om7_18: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "om7_18",
            "consent_waiting_period_units",
            "OM7.18",
        ),
        serialization_alias="OM7.18",
        title="Consent Waiting Period Units",
        description="Item #1496 | Table HL70414",
    )

    om7_19: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "om7_19",
            "effective_date_time_of_change",
            "OM7.19",
        ),
        serialization_alias="OM7.19",
        title="Effective Date/Time of Change",
        description="Item #607",
    )

    om7_20: XCN | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "om7_20",
            "entered_by",
            "OM7.20",
        ),
        serialization_alias="OM7.20",
        title="Entered By",
        description="Item #224",
    )

    om7_21: list[PL] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "om7_21",
            "orderable_at_location",
            "OM7.21",
        ),
        serialization_alias="OM7.21",
        title="Orderable-at Location",
        description="Item #1497",
    )

    om7_22: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "om7_22",
            "formulary_status",
            "OM7.22",
        ),
        serialization_alias="OM7.22",
        title="Formulary Status",
        description="Item #1498 | Table HL70473",
    )

    om7_23: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "om7_23",
            "special_order_indicator",
            "OM7.23",
        ),
        serialization_alias="OM7.23",
        title="Special Order Indicator",
        description="Item #1499 | Table HL70136",
    )

    om7_24: list[CWE] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "om7_24",
            "primary_key_value_cdm",
            "OM7.24",
        ),
        serialization_alias="OM7.24",
        title="Primary Key Value - CDM",
        description="Item #1306",
    )

    model_config = {"populate_by_name": True}
