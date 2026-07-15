"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: PID
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model


class PID(HL7Model):
    """PATIENT IDENTIFICATION (S3.3.3).

    Attributes
    ----------
    pid_1 : str | None
        PID.1 - SET ID - PATIENT ID (SI) O S3-14

    pid_2 : str | None
        PID.2 - PATIENT ID EXTERNAL (EXTERNAL ID) (CK) O | 0061 - CHECK DIGIT SCHEME

    pid_3 : str
        PID.3 - PATIENT ID INTERNAL (INTERNAL ID) (CK) R | 0061 - CHECK DIGIT SCHEME

    pid_4 : str | None
        PID.4 - ALTERNATE PATIENT ID (ST) O

    pid_5 : str
        PID.5 - PATIENT NAME (PN) R

    pid_6 : str | None
        PID.6 - MOTHER'S MAIDEN NAME (ST) O

    pid_7 : str | None
        PID.7 - DATE OF BIRTH (DT) O

    pid_8 : str | None
        PID.8 - SEX (ID) O | 0001 - SEX

    pid_9 : list[str] | None
        PID.9 - PATIENT ALIAS (PN) O rep

    pid_10 : str | None
        PID.10 - ETHNIC GROUP (ID) O | 0005 - ETHNIC GROUP

    pid_11 : str | None
        PID.11 - PATIENT ADDRESS (AD) O

    pid_12 : str | None
        PID.12 - COUNTY CODE (ID) O

    pid_13 : list[str] | None
        PID.13 - PHONE NUMBER - HOME (TN) O rep

    pid_14 : list[str] | None
        PID.14 - PHONE NUMBER - BUSINESS (TN) O rep

    pid_15 : str | None
        PID.15 - LANGUAGE - PATIENT (ST) O

    pid_16 : str | None
        PID.16 - MARITAL STATUS (ID) O | 0002 - MARITAL STATUS

    pid_17 : str | None
        PID.17 - RELIGION (ID) O | 0006 - RELIGION

    pid_18 : str | None
        PID.18 - PATIENT ACCOUNT NUMBER (CK) O | 0061 - CHECK DIGIT SCHEME

    pid_19 : str | None
        PID.19 - SSN NUMBER - PATIENT (ST) O

    pid_20 : str | None
        PID.20 - DRIVER'S LIC NUM - PATIENT (CM) O
    """

    pid_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_1",
            "set_id_patient_id",
            "PID.1",
        ),
        serialization_alias="PID.1",
        title="SET ID - PATIENT ID",
        description="O | Item #00572 | LEN:4",
    )

    pid_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_2",
            "patient_id_external_external_id",
            "PID.2",
        ),
        serialization_alias="PID.2",
        title="PATIENT ID EXTERNAL (EXTERNAL ID)",
        description=(
            "O | Item #00581 | Table 0061 - CHECK DIGIT SCHEME | LEN:16"
        ),
    )

    pid_3: str = Field(
        validation_alias=AliasChoices(
            "pid_3",
            "patient_id_internal_internal_id",
            "PID.3",
        ),
        serialization_alias="PID.3",
        title="PATIENT ID INTERNAL (INTERNAL ID)",
        description=(
            "R | Item #00034 | Table 0061 - CHECK DIGIT SCHEME | LEN:16"
        ),
    )

    pid_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_4",
            "alternate_patient_id",
            "PID.4",
        ),
        serialization_alias="PID.4",
        title="ALTERNATE PATIENT ID",
        description="O | Item #00038 | LEN:12",
    )

    pid_5: str = Field(
        validation_alias=AliasChoices(
            "pid_5",
            "patient_name",
            "PID.5",
        ),
        serialization_alias="PID.5",
        title="PATIENT NAME",
        description="R | Item #00041 | LEN:48",
    )

    pid_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_6",
            "mother_s_maiden_name",
            "PID.6",
        ),
        serialization_alias="PID.6",
        title="MOTHER'S MAIDEN NAME",
        description="O | Item #00582 | LEN:30",
    )

    pid_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_7",
            "date_of_birth",
            "PID.7",
        ),
        serialization_alias="PID.7",
        title="DATE OF BIRTH",
        description="O | Item #00043 | LEN:8",
    )

    pid_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_8",
            "sex",
            "PID.8",
        ),
        serialization_alias="PID.8",
        title="SEX",
        description="O | Item #00042 | Table 0001 - SEX | LEN:1",
    )

    pid_9: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_9",
            "patient_alias",
            "PID.9",
        ),
        serialization_alias="PID.9",
        title="PATIENT ALIAS",
        description="O | Item #00597 | LEN:48",
    )

    pid_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_10",
            "ethnic_group",
            "PID.10",
        ),
        serialization_alias="PID.10",
        title="ETHNIC GROUP",
        description="O | Item #00044 | Table 0005 - ETHNIC GROUP | LEN:1",
    )

    pid_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_11",
            "patient_address",
            "PID.11",
        ),
        serialization_alias="PID.11",
        title="PATIENT ADDRESS",
        description="O | Item #00020 | LEN:106",
    )

    pid_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_12",
            "county_code",
            "PID.12",
        ),
        serialization_alias="PID.12",
        title="COUNTY CODE",
        description="O | Item #00026 | LEN:4",
    )

    pid_13: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_13",
            "phone_number_home",
            "PID.13",
        ),
        serialization_alias="PID.13",
        title="PHONE NUMBER - HOME",
        description="O | Item #00049 | LEN:40",
    )

    pid_14: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_14",
            "phone_number_business",
            "PID.14",
        ),
        serialization_alias="PID.14",
        title="PHONE NUMBER - BUSINESS",
        description="O | Item #00050 | LEN:40",
    )

    pid_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_15",
            "language_patient",
            "PID.15",
        ),
        serialization_alias="PID.15",
        title="LANGUAGE - PATIENT",
        description="O | Item #00464 | LEN:25",
    )

    pid_16: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_16",
            "marital_status",
            "PID.16",
        ),
        serialization_alias="PID.16",
        title="MARITAL STATUS",
        description="O | Item #00046 | Table 0002 - MARITAL STATUS | LEN:1",
    )

    pid_17: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_17",
            "religion",
            "PID.17",
        ),
        serialization_alias="PID.17",
        title="RELIGION",
        description="O | Item #00045 | Table 0006 - RELIGION | LEN:3",
    )

    pid_18: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_18",
            "patient_account_number",
            "PID.18",
        ),
        serialization_alias="PID.18",
        title="PATIENT ACCOUNT NUMBER",
        description=(
            "O | Item #00035 | Table 0061 - CHECK DIGIT SCHEME | LEN:20"
        ),
    )

    pid_19: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_19",
            "ssn_number_patient",
            "PID.19",
        ),
        serialization_alias="PID.19",
        title="SSN NUMBER - PATIENT",
        description="O | Item #00457 | LEN:16",
    )

    pid_20: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_20",
            "driver_s_lic_num_patient",
            "PID.20",
        ),
        serialization_alias="PID.20",
        title="DRIVER'S LIC NUM - PATIENT",
        description="O | Item #00453 | LEN:25",
    )

    @field_validator("pid_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("pid_7", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2})?)?)?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    model_config = {"populate_by_name": True}
