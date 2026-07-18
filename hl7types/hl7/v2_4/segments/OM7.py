"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: OM7
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.PL import PL
from ..datatypes.TS import TS
from ..datatypes.XCN import XCN

_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class OM7(HL7Model):
    """Additional Basic Attributes (S8.8.9).

    Attributes
    ----------
    om7_1 : str
        OM7.1 - Sequence Number - Test/ Observation Master File (NM) R S8.8.9.1

    om7_2 : CE
        OM7.2 - Universal Service Identifier (CE) R S13.4.10.1

    om7_3 : list[CE] | None
        OM7.3 - Category Identifier (CE) O rep S8.8.9.3 | 0412 - Category identifier

    om7_4 : str | None
        OM7.4 - Category Description (TX) O S8.8.9.4

    om7_5 : list[str] | None
        OM7.5 - Category Synonym (ST) O rep S8.8.9.5

    om7_6 : TS | None
        OM7.6 - Effective Test/Service Start Date/Time (TS) O S8.8.9.6

    om7_7 : TS | None
        OM7.7 - Effective Test/Service End Date/Time (TS) O S8.8.9.7

    om7_8 : str | None
        OM7.8 - Test/Service Default Duration Quantity (NM) O S8.8.9.8

    om7_9 : CE | None
        OM7.9 - Test/Service Default Duration Units (CE) O S8.8.9.9 | 9999 - for unknown CE data elements

    om7_10 : str | None
        OM7.10 - Test/Service Default Frequency (IS) O S8.8.9.10 | 0335 - Repeat pattern

    om7_11 : str | None
        OM7.11 - Consent Indicator (ID) O S8.8.9.11 | 0136 - Yes/no indicator

    om7_12 : CE | None
        OM7.12 - Consent Identifier (CE) O S8.8.9.12 | 0413 - Consent identifier

    om7_13 : TS | None
        OM7.13 - Consent Effective Start Date/Time (TS) O S8.8.9.13

    om7_14 : TS | None
        OM7.14 - Consent Effective End Date/Time (TS) O S8.8.9.14

    om7_15 : str | None
        OM7.15 - Consent Interval Quantity (NM) O S8.8.9.15

    om7_16 : CE | None
        OM7.16 - Consent Interval Units (CE) C S8.8.9.16 | 0414 - Units of time

    om7_17 : str | None
        OM7.17 - Consent Waiting Period Quantity (NM) O S8.8.9.17

    om7_18 : CE | None
        OM7.18 - Consent Waiting Period Units (CE) C S8.8.9.18 | 0414 - Units of time

    om7_19 : TS | None
        OM7.19 - Effective Date/Time of Change (TS) O S8.8.9.19

    om7_20 : XCN | None
        OM7.20 - Entered By (XCN) O S8.8.9.20

    om7_21 : list[PL] | None
        OM7.21 - Orderable-at Location (PL) O rep S8.8.9.21

    om7_22 : str | None
        OM7.22 - Formulary Status (IS) O S8.8.9.22 | 0473 - Formulary status

    om7_23 : str | None
        OM7.23 - Special Order Indicator (ID) O S8.8.9.23 | 0136 - Yes/no indicator

    om7_24 : list[CE] | None
        OM7.24 - Primary Key Value - CDM (CE) O rep S8.10.2.1 | 0132 - Transaction code
    """

    om7_1: str = Field(
        validation_alias=AliasChoices(
            "om7_1",
            "sequence_number_test_observation_master_file",
            "OM7.1",
        ),
        serialization_alias="OM7.1",
        title="Sequence Number - Test/ Observation Master File",
        description="R | Item #00586 | LEN:4",
    )

    om7_2: CE = Field(
        validation_alias=AliasChoices(
            "om7_2",
            "universal_service_identifier",
            "OM7.2",
        ),
        serialization_alias="OM7.2",
        title="Universal Service Identifier",
        description="R | Item #00238",
    )

    om7_3: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om7_3",
            "category_identifier",
            "OM7.3",
        ),
        serialization_alias="OM7.3",
        title="Category Identifier",
        description="O | Item #01481 | Table 0412 - Category identifier",
    )

    om7_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om7_4",
            "category_description",
            "OM7.4",
        ),
        serialization_alias="OM7.4",
        title="Category Description",
        description="O | Item #01482",
    )

    om7_5: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om7_5",
            "category_synonym",
            "OM7.5",
        ),
        serialization_alias="OM7.5",
        title="Category Synonym",
        description="O | Item #01483 | LEN:200",
    )

    om7_6: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om7_6",
            "effective_test_service_start_date_time",
            "OM7.6",
        ),
        serialization_alias="OM7.6",
        title="Effective Test/Service Start Date/Time",
        description="O | Item #01484",
    )

    om7_7: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om7_7",
            "effective_test_service_end_date_time",
            "OM7.7",
        ),
        serialization_alias="OM7.7",
        title="Effective Test/Service End Date/Time",
        description="O | Item #01485",
    )

    om7_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om7_8",
            "test_service_default_duration_quantity",
            "OM7.8",
        ),
        serialization_alias="OM7.8",
        title="Test/Service Default Duration Quantity",
        description="O | Item #01486 | LEN:5",
    )

    om7_9: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om7_9",
            "test_service_default_duration_units",
            "OM7.9",
        ),
        serialization_alias="OM7.9",
        title="Test/Service Default Duration Units",
        description=(
            "O | Item #01487 | Table 9999 - for unknown CE data elements"
        ),
    )

    om7_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om7_10",
            "test_service_default_frequency",
            "OM7.10",
        ),
        serialization_alias="OM7.10",
        title="Test/Service Default Frequency",
        description="O | Item #01488 | Table 0335 - Repeat pattern | LEN:60",
    )

    om7_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om7_11",
            "consent_indicator",
            "OM7.11",
        ),
        serialization_alias="OM7.11",
        title="Consent Indicator",
        description="O | Item #01489 | Table 0136 - Yes/no indicator | LEN:1",
    )

    om7_12: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om7_12",
            "consent_identifier",
            "OM7.12",
        ),
        serialization_alias="OM7.12",
        title="Consent Identifier",
        description="O | Item #01490 | Table 0413 - Consent identifier",
    )

    om7_13: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om7_13",
            "consent_effective_start_date_time",
            "OM7.13",
        ),
        serialization_alias="OM7.13",
        title="Consent Effective Start Date/Time",
        description="O | Item #01491",
    )

    om7_14: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om7_14",
            "consent_effective_end_date_time",
            "OM7.14",
        ),
        serialization_alias="OM7.14",
        title="Consent Effective End Date/Time",
        description="O | Item #01492",
    )

    om7_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om7_15",
            "consent_interval_quantity",
            "OM7.15",
        ),
        serialization_alias="OM7.15",
        title="Consent Interval Quantity",
        description="O | Item #01493 | LEN:5",
    )

    om7_16: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om7_16",
            "consent_interval_units",
            "OM7.16",
        ),
        serialization_alias="OM7.16",
        title="Consent Interval Units",
        description="C | Item #01494 | Table 0414 - Units of time",
    )

    om7_17: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om7_17",
            "consent_waiting_period_quantity",
            "OM7.17",
        ),
        serialization_alias="OM7.17",
        title="Consent Waiting Period Quantity",
        description="O | Item #01495 | LEN:5",
    )

    om7_18: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om7_18",
            "consent_waiting_period_units",
            "OM7.18",
        ),
        serialization_alias="OM7.18",
        title="Consent Waiting Period Units",
        description="C | Item #01496 | Table 0414 - Units of time",
    )

    om7_19: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om7_19",
            "effective_date_time_of_change",
            "OM7.19",
        ),
        serialization_alias="OM7.19",
        title="Effective Date/Time of Change",
        description="O | Item #00607",
    )

    om7_20: Optional[XCN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om7_20",
            "entered_by",
            "OM7.20",
        ),
        serialization_alias="OM7.20",
        title="Entered By",
        description="O | Item #00224",
    )

    om7_21: Optional[List[PL]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om7_21",
            "orderable_at_location",
            "OM7.21",
        ),
        serialization_alias="OM7.21",
        title="Orderable-at Location",
        description="O | Item #01497",
    )

    om7_22: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om7_22",
            "formulary_status",
            "OM7.22",
        ),
        serialization_alias="OM7.22",
        title="Formulary Status",
        description="O | Item #01498 | Table 0473 - Formulary status | LEN:1",
    )

    om7_23: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om7_23",
            "special_order_indicator",
            "OM7.23",
        ),
        serialization_alias="OM7.23",
        title="Special Order Indicator",
        description="O | Item #01499 | Table 0136 - Yes/no indicator | LEN:1",
    )

    om7_24: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om7_24",
            "primary_key_value_cdm",
            "OM7.24",
        ),
        serialization_alias="OM7.24",
        title="Primary Key Value - CDM",
        description="O | Item #01306 | Table 0132 - Transaction code",
    )

    @field_validator("om7_1", "om7_8", "om7_15", "om7_17", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
