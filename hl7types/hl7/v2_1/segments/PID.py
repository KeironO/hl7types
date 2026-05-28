"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: PID
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field


class PID(BaseModel):
    """HL7 v2 PID segment."""

    pid_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_1",
            "set_id_patient_id",
            "PID.1",
        ),
        serialization_alias="PID.1",
        title="SET ID - PATIENT ID",
        description="Item #572",
    )

    pid_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_2",
            "patient_id_external_external_id",
            "PID.2",
        ),
        serialization_alias="PID.2",
        title="PATIENT ID EXTERNAL (EXTERNAL ID)",
        description="Item #581 | Table HL70061",
    )

    pid_3: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "pid_3",
            "patient_id_internal_internal_id",
            "PID.3",
        ),
        serialization_alias="PID.3",
        title="PATIENT ID INTERNAL (INTERNAL ID)",
        description="Item #34 | Table HL70061",
    )

    pid_4: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_4",
            "alternate_patient_id",
            "PID.4",
        ),
        serialization_alias="PID.4",
        title="ALTERNATE PATIENT ID",
        description="Item #38",
    )

    pid_5: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "pid_5",
            "patient_name",
            "PID.5",
        ),
        serialization_alias="PID.5",
        title="PATIENT NAME",
        description="Item #41",
    )

    pid_6: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_6",
            "mother_s_maiden_name",
            "PID.6",
        ),
        serialization_alias="PID.6",
        title="MOTHER'S MAIDEN NAME",
        description="Item #582",
    )

    pid_7: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_7",
            "date_of_birth",
            "PID.7",
        ),
        serialization_alias="PID.7",
        title="DATE OF BIRTH",
        description="Item #43",
    )

    pid_8: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_8",
            "sex",
            "PID.8",
        ),
        serialization_alias="PID.8",
        title="SEX",
        description="Item #42 | Table HL70001",
    )

    pid_9: list[str] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_9",
            "patient_alias",
            "PID.9",
        ),
        serialization_alias="PID.9",
        title="PATIENT ALIAS",
        description="Item #597",
    )

    pid_10: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_10",
            "ethnic_group",
            "PID.10",
        ),
        serialization_alias="PID.10",
        title="ETHNIC GROUP",
        description="Item #44 | Table HL70005",
    )

    pid_11: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_11",
            "patient_address",
            "PID.11",
        ),
        serialization_alias="PID.11",
        title="PATIENT ADDRESS",
        description="Item #20",
    )

    pid_12: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_12",
            "county_code",
            "PID.12",
        ),
        serialization_alias="PID.12",
        title="COUNTY CODE",
        description="Item #26",
    )

    pid_13: list[str] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_13",
            "phone_number_home",
            "PID.13",
        ),
        serialization_alias="PID.13",
        title="PHONE NUMBER - HOME",
        description="Item #49",
    )

    pid_14: list[str] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_14",
            "phone_number_business",
            "PID.14",
        ),
        serialization_alias="PID.14",
        title="PHONE NUMBER - BUSINESS",
        description="Item #50",
    )

    pid_15: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_15",
            "language_patient",
            "PID.15",
        ),
        serialization_alias="PID.15",
        title="LANGUAGE - PATIENT",
        description="Item #464",
    )

    pid_16: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_16",
            "marital_status",
            "PID.16",
        ),
        serialization_alias="PID.16",
        title="MARITAL STATUS",
        description="Item #46 | Table HL70002",
    )

    pid_17: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_17",
            "religion",
            "PID.17",
        ),
        serialization_alias="PID.17",
        title="RELIGION",
        description="Item #45 | Table HL70006",
    )

    pid_18: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_18",
            "patient_account_number",
            "PID.18",
        ),
        serialization_alias="PID.18",
        title="PATIENT ACCOUNT NUMBER",
        description="Item #35 | Table HL70061",
    )

    pid_19: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_19",
            "ssn_number_patient",
            "PID.19",
        ),
        serialization_alias="PID.19",
        title="SSN NUMBER - PATIENT",
        description="Item #457",
    )

    pid_20: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_20",
            "driver_s_lic_num_patient",
            "PID.20",
        ),
        serialization_alias="PID.20",
        title="DRIVER'S LIC NUM - PATIENT",
        description="Item #453",
    )

    model_config = {"populate_by_name": True}
