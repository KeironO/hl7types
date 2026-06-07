"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: PID
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.AD import AD
from ..datatypes.PN import PN
from ..datatypes.TS import TS


class PID(HL7Model):
    """HL7 v2 PID segment.

    Attributes
    ----------
    pid_1 : str | None
        PID.1 (opt) - Set ID - Patient ID (SI)

    pid_2 : str | None
        PID.2 (opt) - Patient ID (External ID) (CK)

    pid_3 : list[str]
        PID.3 (req, rep) - Patient ID (Internal ID) (CM)

    pid_4 : str | None
        PID.4 (opt) - Alternate Patient ID (ST)

    pid_5 : PN
        PID.5 (req) - Patient Name (PN)

    pid_6 : str | None
        PID.6 (opt) - Mother's Maiden Name (ST)

    pid_7 : TS | None
        PID.7 (opt) - Date of Birth (TS)

    pid_8 : str | None
        PID.8 (opt) - Sex (ID)

    pid_9 : list[PN] | None
        PID.9 (opt, rep) - Patient Alias (PN)

    pid_10 : str | None
        PID.10 (opt) - Race (ID)

    pid_11 : list[AD] | None
        PID.11 (opt, rep) - Patient Address (AD)

    pid_12 : str | None
        PID.12 (opt) - County code (ID)

    pid_13 : list[str] | None
        PID.13 (opt, rep) - Phone Number - Home (TN)

    pid_14 : list[str] | None
        PID.14 (opt, rep) - Phone Number - Business (TN)

    pid_15 : str | None
        PID.15 (opt) - Language - Patient (ST)

    pid_16 : str | None
        PID.16 (opt) - Marital Status (ID)

    pid_17 : str | None
        PID.17 (opt) - Religion (ID)

    pid_18 : str | None
        PID.18 (opt) - Patient Account Number (CK)

    pid_19 : str | None
        PID.19 (opt) - Social security number - patient (ST)

    pid_20 : str | None
        PID.20 (opt) - Driver's license number - patient (CM)

    pid_21 : str | None
        PID.21 (opt) - Mother's Identifier (CK)

    pid_22 : str | None
        PID.22 (opt) - Ethnic Group (ID)

    pid_23 : str | None
        PID.23 (opt) - Birth Place (ST)

    pid_24 : str | None
        PID.24 (opt) - Multiple Birth Indicator (ID)

    pid_25 : str | None
        PID.25 (opt) - Birth Order (NM)

    pid_26 : list[str] | None
        PID.26 (opt, rep) - Citizenship (ID)

    pid_27 : str | None
        PID.27 (opt) - Veterans Military Status (ST)
    """

    pid_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_1",
            "set_id_patient_id",
            "PID.1",
        ),
        serialization_alias="PID.1",
        title="Set ID - Patient ID",
        description="Item #104",
    )

    pid_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_2",
            "patient_id_external_id",
            "PID.2",
        ),
        serialization_alias="PID.2",
        title="Patient ID (External ID)",
        description="Item #105",
    )

    pid_3: List[str] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "pid_3",
            "patient_id_internal_id",
            "PID.3",
        ),
        serialization_alias="PID.3",
        title="Patient ID (Internal ID)",
        description="Item #106",
    )

    pid_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_4",
            "alternate_patient_id",
            "PID.4",
        ),
        serialization_alias="PID.4",
        title="Alternate Patient ID",
        description="Item #107",
    )

    pid_5: PN = Field(
        validation_alias=AliasChoices(
            "pid_5",
            "patient_name",
            "PID.5",
        ),
        serialization_alias="PID.5",
        title="Patient Name",
        description="Item #108",
    )

    pid_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_6",
            "mother_s_maiden_name",
            "PID.6",
        ),
        serialization_alias="PID.6",
        title="Mother's Maiden Name",
        description="Item #109",
    )

    pid_7: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_7",
            "date_of_birth",
            "PID.7",
        ),
        serialization_alias="PID.7",
        title="Date of Birth",
        description="Item #110",
    )

    pid_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_8",
            "sex",
            "PID.8",
        ),
        serialization_alias="PID.8",
        title="Sex",
        description="Item #111 | Table HL70001",
    )

    pid_9: Optional[List[PN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_9",
            "patient_alias",
            "PID.9",
        ),
        serialization_alias="PID.9",
        title="Patient Alias",
        description="Item #112",
    )

    pid_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_10",
            "race",
            "PID.10",
        ),
        serialization_alias="PID.10",
        title="Race",
        description="Item #113 | Table HL70005",
    )

    pid_11: Optional[List[AD]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_11",
            "patient_address",
            "PID.11",
        ),
        serialization_alias="PID.11",
        title="Patient Address",
        description="Item #114",
    )

    pid_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_12",
            "county_code",
            "PID.12",
        ),
        serialization_alias="PID.12",
        title="County code",
        description="Item #115",
    )

    pid_13: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_13",
            "phone_number_home",
            "PID.13",
        ),
        serialization_alias="PID.13",
        title="Phone Number - Home",
        description="Item #116",
    )

    pid_14: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_14",
            "phone_number_business",
            "PID.14",
        ),
        serialization_alias="PID.14",
        title="Phone Number - Business",
        description="Item #117",
    )

    pid_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_15",
            "language_patient",
            "PID.15",
        ),
        serialization_alias="PID.15",
        title="Language - Patient",
        description="Item #118",
    )

    pid_16: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_16",
            "marital_status",
            "PID.16",
        ),
        serialization_alias="PID.16",
        title="Marital Status",
        description="Item #119 | Table HL70002",
    )

    pid_17: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_17",
            "religion",
            "PID.17",
        ),
        serialization_alias="PID.17",
        title="Religion",
        description="Item #120 | Table HL70006",
    )

    pid_18: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_18",
            "patient_account_number",
            "PID.18",
        ),
        serialization_alias="PID.18",
        title="Patient Account Number",
        description="Item #121",
    )

    pid_19: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_19",
            "social_security_number_patient",
            "PID.19",
        ),
        serialization_alias="PID.19",
        title="Social security number - patient",
        description="Item #122",
    )

    pid_20: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_20",
            "driver_s_license_number_patient",
            "PID.20",
        ),
        serialization_alias="PID.20",
        title="Driver's license number - patient",
        description="Item #123",
    )

    pid_21: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_21",
            "mother_s_identifier",
            "PID.21",
        ),
        serialization_alias="PID.21",
        title="Mother's Identifier",
        description="Item #124",
    )

    pid_22: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_22",
            "ethnic_group",
            "PID.22",
        ),
        serialization_alias="PID.22",
        title="Ethnic Group",
        description="Item #125 | Table HL70189",
    )

    pid_23: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_23",
            "birth_place",
            "PID.23",
        ),
        serialization_alias="PID.23",
        title="Birth Place",
        description="Item #126",
    )

    pid_24: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_24",
            "multiple_birth_indicator",
            "PID.24",
        ),
        serialization_alias="PID.24",
        title="Multiple Birth Indicator",
        description="Item #127",
    )

    pid_25: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_25",
            "birth_order",
            "PID.25",
        ),
        serialization_alias="PID.25",
        title="Birth Order",
        description="Item #128",
    )

    pid_26: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_26",
            "citizenship",
            "PID.26",
        ),
        serialization_alias="PID.26",
        title="Citizenship",
        description="Item #129 | Table HL70171",
    )

    pid_27: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_27",
            "veterans_military_status",
            "PID.27",
        ),
        serialization_alias="PID.27",
        title="Veterans Military Status",
        description="Item #130",
    )

    @field_validator("pid_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("pid_25", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
