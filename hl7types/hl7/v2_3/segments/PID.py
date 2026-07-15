"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: PID
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.CX import CX
from ..datatypes.DLN import DLN
from ..datatypes.TS import TS
from ..datatypes.XAD import XAD
from ..datatypes.XPN import XPN
from ..datatypes.XTN import XTN


class PID(HL7Model):
    """Patient Identification (S3.3.2).

    Attributes
    ----------
    pid_1 : str | None
        PID.1 - Set ID - Patient ID (SI) O S3.3.2.1

    pid_2 : CX | None
        PID.2 - Patient ID (External ID) (CX) O S3.3.2.2

    pid_3 : list[CX]
        PID.3 - Patient ID (Internal ID) (CX) R rep S3.3.2.3

    pid_4 : CX | None
        PID.4 - Alternate Patient ID (CX) O S3.3.2.4

    pid_5 : XPN
        PID.5 - Patient Name (XPN) R S3.3.2.5

    pid_6 : XPN | None
        PID.6 - Mother's Maiden Name (XPN) O S3.3.2.6

    pid_7 : TS | None
        PID.7 - Date of Birth (TS) O S3.3.2

    pid_8 : str | None
        PID.8 - Sex (IS) NA S3.3.2 | 0001 - Sex

    pid_9 : list[XPN] | None
        PID.9 - Patient Alias (XPN) O rep S3.3.2

    pid_10 : str | None
        PID.10 - Race (IS) NA S3.3.2 | 0005 - Race

    pid_11 : list[XAD] | None
        PID.11 - Patient Address (XAD) O rep S3.3.2.11

    pid_12 : str | None
        PID.12 - County Code (IS) O S3.3.2.12

    pid_13 : list[XTN] | None
        PID.13 - Phone Number - Home (XTN) O rep S3.3.2.13

    pid_14 : list[XTN] | None
        PID.14 - Phone Number - Business (XTN) O rep S3.3.2.14

    pid_15 : CE | None
        PID.15 - Primary Language (CE) O S3.3.2 | 0296 - Language

    pid_16 : list[str] | None
        PID.16 - Marital Status (IS) NA rep S3.3.2 | 0002 - Marital Status

    pid_17 : str | None
        PID.17 - Religion (IS) O S3.3.2 | 0006 - Religion

    pid_18 : CX | None
        PID.18 - Patient Account Number (CX) O S3.3.2.18

    pid_19 : str | None
        PID.19 - SSN Number - Patient (ST) O S3.3.2.19

    pid_20 : DLN | None
        PID.20 - Driver's License Number (DLN) O S3.3.2.20

    pid_21 : CX | None
        PID.21 - Mother's Identifier (CX) O S3.3.2.21

    pid_22 : str | None
        PID.22 - Ethnic Group (IS) O S3.3.2 | 0189 - Ethnic Group

    pid_23 : str | None
        PID.23 - Birth Place (ST) O S3.3.2.23

    pid_24 : str | None
        PID.24 - Multiple Birth Indicator (ID) O S3.3.2.24 | 0136 - Yes/No Indicator

    pid_25 : str | None
        PID.25 - Birth Order (NM) O S3.3.2.25

    pid_26 : str | None
        PID.26 - Citizenship (IS) O S3.3.2 | 0171 - Country Code

    pid_27 : CE | None
        PID.27 - Veterans Military Status (CE) O S3.3.2.27 | 0172 - Veterans Military Status

    pid_28 : CE | None
        PID.28 - Nationality Code (CE) O S3.3.2 | 0212 - Nationality

    pid_29 : TS | None
        PID.29 - Patient Death Date and Time (TS) NA S3.3.2.29

    pid_30 : str | None
        PID.30 - Patient Death Indicator (ID) O S3.3.2.30 | 0136 - Yes/No Indicator
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
        description="O | Item #00104 | LEN:4",
    )

    pid_2: Optional[CX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_2",
            "patient_id_external_id",
            "PID.2",
        ),
        serialization_alias="PID.2",
        title="Patient ID (External ID)",
        description="O | Item #00105",
    )

    pid_3: List[CX] = Field(
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

    pid_4: Optional[CX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_4",
            "alternate_patient_id",
            "PID.4",
        ),
        serialization_alias="PID.4",
        title="Alternate Patient ID",
        description="O | Item #00107",
    )

    pid_5: XPN = Field(
        validation_alias=AliasChoices(
            "pid_5",
            "patient_name",
            "PID.5",
        ),
        serialization_alias="PID.5",
        title="Patient Name",
        description="R | Item #00108",
    )

    pid_6: Optional[XPN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_6",
            "mother_s_maiden_name",
            "PID.6",
        ),
        serialization_alias="PID.6",
        title="Mother's Maiden Name",
        description="O | Item #00109",
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
        description="O | Item #00110",
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
        description="NA | Item #00111 | Table 0001 - Sex | LEN:1",
    )

    pid_9: Optional[List[XPN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_9",
            "patient_alias",
            "PID.9",
        ),
        serialization_alias="PID.9",
        title="Patient Alias",
        description="O | Item #00112",
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
        description="NA | Item #00113 | Table 0005 - Race | LEN:1",
    )

    pid_11: Optional[List[XAD]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_11",
            "patient_address",
            "PID.11",
        ),
        serialization_alias="PID.11",
        title="Patient Address",
        description="O | Item #00114",
    )

    pid_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_12",
            "county_code",
            "PID.12",
        ),
        serialization_alias="PID.12",
        title="County Code",
        description="O | Item #00115 | LEN:4",
    )

    pid_13: Optional[List[XTN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_13",
            "phone_number_home",
            "PID.13",
        ),
        serialization_alias="PID.13",
        title="Phone Number - Home",
        description="O | Item #00116",
    )

    pid_14: Optional[List[XTN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_14",
            "phone_number_business",
            "PID.14",
        ),
        serialization_alias="PID.14",
        title="Phone Number - Business",
        description="O | Item #00117",
    )

    pid_15: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_15",
            "primary_language",
            "PID.15",
        ),
        serialization_alias="PID.15",
        title="Primary Language",
        description="O | Item #00118 | Table 0296 - Language",
    )

    pid_16: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_16",
            "marital_status",
            "PID.16",
        ),
        serialization_alias="PID.16",
        title="Marital Status",
        description="NA | Item #00119 | Table 0002 - Marital Status | LEN:1",
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
        description="O | Item #00120 | Table 0006 - Religion | LEN:3",
    )

    pid_18: Optional[CX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_18",
            "patient_account_number",
            "PID.18",
        ),
        serialization_alias="PID.18",
        title="Patient Account Number",
        description="O | Item #00121",
    )

    pid_19: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_19",
            "ssn_number_patient",
            "PID.19",
        ),
        serialization_alias="PID.19",
        title="SSN Number - Patient",
        description="O | Item #00122 | LEN:16",
    )

    pid_20: Optional[DLN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_20",
            "driver_s_license_number",
            "PID.20",
        ),
        serialization_alias="PID.20",
        title="Driver's License Number",
        description="O | Item #00123",
    )

    pid_21: Optional[CX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_21",
            "mother_s_identifier",
            "PID.21",
        ),
        serialization_alias="PID.21",
        title="Mother's Identifier",
        description="O | Item #00124",
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
        description="O | Item #00125 | Table 0189 - Ethnic Group | LEN:1",
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
        description="O | Item #00126 | LEN:60",
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
        description="O | Item #00127 | Table 0136 - Yes/No Indicator | LEN:2",
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
        description="O | Item #00128 | LEN:2",
    )

    pid_26: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_26",
            "citizenship",
            "PID.26",
        ),
        serialization_alias="PID.26",
        title="Citizenship",
        description="O | Item #00129 | Table 0171 - Country Code | LEN:4",
    )

    pid_27: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_27",
            "veterans_military_status",
            "PID.27",
        ),
        serialization_alias="PID.27",
        title="Veterans Military Status",
        description="O | Item #00130 | Table 0172 - Veterans Military Status",
    )

    pid_28: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_28",
            "nationality_code",
            "PID.28",
        ),
        serialization_alias="PID.28",
        title="Nationality Code",
        description="O | Item #00739 | Table 0212 - Nationality",
    )

    pid_29: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_29",
            "patient_death_date_and_time",
            "PID.29",
        ),
        serialization_alias="PID.29",
        title="Patient Death Date and Time",
        description="NA | Item #00740",
    )

    pid_30: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_30",
            "patient_death_indicator",
            "PID.30",
        ),
        serialization_alias="PID.30",
        title="Patient Death Indicator",
        description="O | Item #00741 | Table 0136 - Yes/No Indicator | LEN:1",
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
