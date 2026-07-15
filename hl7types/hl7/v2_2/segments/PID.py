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
    """PATIENT IDENTIFICATION (S3.3.2).

    Attributes
    ----------
    pid_1 : str | None
        PID.1 - Set ID - Patient ID (SI) NA S3.3.2.1

    pid_2 : str | None
        PID.2 - Patient ID (External ID) (CK) NA S3.3.2.2

    pid_3 : list[str]
        PID.3 - Patient ID (Internal ID) (CM) R rep S3.3.2.3

    pid_4 : str | None
        PID.4 - Alternate Patient ID (ST) NA S3.3.2.4

    pid_5 : PN
        PID.5 - Patient Name (PN) R S3.3.2.5

    pid_6 : str | None
        PID.6 - Mother's Maiden Name (ST) NA S3.3.2.6

    pid_7 : TS | None
        PID.7 - Date of Birth (TS) NA S3.3.2.7

    pid_8 : str | None
        PID.8 - Sex (ID) NA S3.3.2.8 | 0001 - SEX

    pid_9 : list[PN] | None
        PID.9 - Patient Alias (PN) NA rep S3.3.2.9

    pid_10 : str | None
        PID.10 - Race (ID) NA S3.3.2.10 | 0005 - RACE

    pid_11 : list[AD] | None
        PID.11 - Patient Address (AD) NA rep S3.3.2.11

    pid_12 : str | None
        PID.12 - County code (ID) NA S3.3.2.12

    pid_13 : list[str] | None
        PID.13 - Phone Number - Home (TN) NA rep S3.3.2.13

    pid_14 : list[str] | None
        PID.14 - Phone Number - Business (TN) NA rep S3.3.2.14

    pid_15 : str | None
        PID.15 - Language - Patient (ST) NA S3.3.2.15

    pid_16 : str | None
        PID.16 - Marital Status (ID) NA S3.3.2.16 | 0002 - MARITAL STATUS

    pid_17 : str | None
        PID.17 - Religion (ID) NA S3.3.2.17 | 0006 - RELIGION

    pid_18 : str | None
        PID.18 - Patient Account Number (CK) NA S3.3.2.18

    pid_19 : str | None
        PID.19 - Social security number - patient (ST) NA S3.3.2.19

    pid_20 : str | None
        PID.20 - Driver's license number - patient (CM) NA S3.3.2.20

    pid_21 : str | None
        PID.21 - Mother's Identifier (CK) NA S3.3.2.21

    pid_22 : str | None
        PID.22 - Ethnic Group (ID) NA S3.3.2.22 | 0189 - Ethnic Group

    pid_23 : str | None
        PID.23 - Birth Place (ST) NA S3.3.2.23

    pid_24 : str | None
        PID.24 - Multiple Birth Indicator (ID) NA S3.3.2.24

    pid_25 : str | None
        PID.25 - Birth Order (NM) NA S3.3.2.25

    pid_26 : list[str] | None
        PID.26 - Citizenship (ID) NA rep S3.3.2.26 | 0171 - Country Code

    pid_27 : str | None
        PID.27 - Veterans Military Status (ST) NA S3.3.2.27
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
        description="NA | Item #00104 | LEN:4",
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
        description="NA | Item #00105 | LEN:16",
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
        description="R | Item #00106",
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
        description="NA | Item #00107 | LEN:12",
    )

    pid_5: PN = Field(
        validation_alias=AliasChoices(
            "pid_5",
            "patient_name",
            "PID.5",
        ),
        serialization_alias="PID.5",
        title="Patient Name",
        description="R | Item #00108",
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
        description="NA | Item #00109 | LEN:30",
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
        description="NA | Item #00110",
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
        description="NA | Item #00111 | Table 0001 - SEX | LEN:1",
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
        description="NA | Item #00112",
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
        description="NA | Item #00113 | Table 0005 - RACE | LEN:1",
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
        description="NA | Item #00114",
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
        description="NA | Item #00115 | LEN:4",
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
        description="NA | Item #00116 | LEN:40",
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
        description="NA | Item #00117 | LEN:40",
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
        description="NA | Item #00118 | LEN:25",
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
        description="NA | Item #00119 | Table 0002 - MARITAL STATUS | LEN:1",
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
        description="NA | Item #00120 | Table 0006 - RELIGION | LEN:3",
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
        description="NA | Item #00121 | LEN:20",
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
        description="NA | Item #00122 | LEN:16",
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
        description="NA | Item #00123",
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
        description="NA | Item #00124 | LEN:20",
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
        description="NA | Item #00125 | Table 0189 - Ethnic Group | LEN:1",
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
        description="NA | Item #00126 | LEN:25",
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
        description="NA | Item #00127 | LEN:2",
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
        description="NA | Item #00128 | LEN:2",
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
        description="NA | Item #00129 | Table 0171 - Country Code | LEN:3",
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
        description="NA | Item #00130 | LEN:60",
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
