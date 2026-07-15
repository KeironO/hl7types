"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: PID
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.CWE import CWE
from ..datatypes.CX import CX
from ..datatypes.DLN import DLN
from ..datatypes.HD import HD
from ..datatypes.TS import TS
from ..datatypes.XAD import XAD
from ..datatypes.XPN import XPN
from ..datatypes.XTN import XTN


class PID(HL7Model):
    """Patient Identification (S3.4.2).

    Attributes
    ----------
    pid_1 : str | None
        PID.1 - Set ID - PID (SI) O S3.4.2.1

    pid_2 : CX | None
        PID.2 - Patient ID (CX) O S3.4.2.2

    pid_3 : list[CX]
        PID.3 - Patient Identifier List (CX) R rep S3.4.2.3

    pid_4 : list[CX] | None
        PID.4 - Alternate Patient ID - PID (CX) O rep S3.4.2.4

    pid_5 : list[XPN]
        PID.5 - Patient Name (XPN) R rep S3.4.2.5

    pid_6 : list[XPN] | None
        PID.6 - Mother's Maiden Name (XPN) O rep S3.4.2.6

    pid_7 : TS | None
        PID.7 - Date/Time of Birth (TS) O S3.4.2.7

    pid_8 : str | None
        PID.8 - Administrative Sex (IS) O S3.4.2.8 | 0001 - Administrative Sex

    pid_9 : list[XPN] | None
        PID.9 - Patient Alias (XPN) O rep S3.4.2.9

    pid_10 : list[CE] | None
        PID.10 - Race (CE) O rep S3.4.2.10 | 0005 - Race

    pid_11 : list[XAD] | None
        PID.11 - Patient Address (XAD) O rep S3.4.2.11

    pid_12 : str | None
        PID.12 - County Code (IS) O S3.4.2.12 | 0289 - County/parish

    pid_13 : list[XTN] | None
        PID.13 - Phone Number - Home (XTN) O rep S3.4.2.13

    pid_14 : list[XTN] | None
        PID.14 - Phone Number - Business (XTN) O rep S3.4.2.14

    pid_15 : CE | None
        PID.15 - Primary Language (CE) O S3.4.2.15 | 0296 - Primary Language

    pid_16 : CE | None
        PID.16 - Marital Status (CE) O S3.4.2.16 | 0002 - Marital Status

    pid_17 : CE | None
        PID.17 - Religion (CE) O S3.4.2.17 | 0006 - Religion

    pid_18 : CX | None
        PID.18 - Patient Account Number (CX) O S3.4.2.18

    pid_19 : str | None
        PID.19 - SSN Number - Patient (ST) O S3.4.2.19

    pid_20 : DLN | None
        PID.20 - Driver's License Number - Patient (DLN) O S3.4.2.20

    pid_21 : list[CX] | None
        PID.21 - Mother's Identifier (CX) O rep S3.4.2.21

    pid_22 : list[CE] | None
        PID.22 - Ethnic Group (CE) O rep S3.4.2.22 | 0189 - Ethnic Group

    pid_23 : str | None
        PID.23 - Birth Place (ST) O S3.4.2.23

    pid_24 : str | None
        PID.24 - Multiple Birth Indicator (ID) O S3.4.2.24 | 0136 - Yes/no indicator

    pid_25 : str | None
        PID.25 - Birth Order (NM) O S3.4.2.25

    pid_26 : list[CE] | None
        PID.26 - Citizenship (CE) O rep S3.4.2.26 | 0171 - Citizenship

    pid_27 : CE | None
        PID.27 - Veterans Military Status (CE) O S3.4.2.27 | 0172 - Veterans Military Status

    pid_28 : CE | None
        PID.28 - Nationality (CE) O S3.4.2.28 | 0212 - Nationality

    pid_29 : TS | None
        PID.29 - Patient Death Date and Time (TS) O S3.4.2.29

    pid_30 : str | None
        PID.30 - Patient Death Indicator (ID) O S3.4.2.30 | 0136 - Yes/no indicator

    pid_31 : str | None
        PID.31 - Identity Unknown Indicator (ID) O S3.4.2.31 | 0136 - Yes/no indicator

    pid_32 : list[str] | None
        PID.32 - Identity Reliability Code (IS) O rep S3.4.2.32 | 0445 - Identity Reliability Code

    pid_33 : TS | None
        PID.33 - Last Update Date/Time (TS) O S3.4.2.33

    pid_34 : HD | None
        PID.34 - Last Update Facility (HD) O S3.4.2.34

    pid_35 : CE | None
        PID.35 - Species Code (CE) C S3.4.2.35 | 0446 - Species Code

    pid_36 : CE | None
        PID.36 - Breed Code (CE) C S3.4.2.36 | 0447 - Breed Code

    pid_37 : str | None
        PID.37 - Strain (ST) O S3.4.2.37

    pid_38 : CE | None
        PID.38 - Production Class Code (CE) O S3.4.2.38 | 0429 - Production Class Code

    pid_39 : list[CWE] | None
        PID.39 - Tribal Citizenship (CWE) O rep S3.4.2.39 | 0171 - Citizenship
    """

    pid_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_1",
            "set_id_pid",
            "PID.1",
        ),
        serialization_alias="PID.1",
        title="Set ID - PID",
        description="O | Item #00104 | LEN:4",
    )

    pid_2: Optional[CX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_2",
            "patient_id",
            "PID.2",
        ),
        serialization_alias="PID.2",
        title="Patient ID",
        description="O | Item #00105",
    )

    pid_3: List[CX] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "pid_3",
            "patient_identifier_list",
            "PID.3",
        ),
        serialization_alias="PID.3",
        title="Patient Identifier List",
        description="R | Item #00106",
    )

    pid_4: Optional[List[CX]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_4",
            "alternate_patient_id_pid",
            "PID.4",
        ),
        serialization_alias="PID.4",
        title="Alternate Patient ID - PID",
        description="O | Item #00107",
    )

    pid_5: List[XPN] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "pid_5",
            "patient_name",
            "PID.5",
        ),
        serialization_alias="PID.5",
        title="Patient Name",
        description="R | Item #00108",
    )

    pid_6: Optional[List[XPN]] = Field(
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
            "date_time_of_birth",
            "PID.7",
        ),
        serialization_alias="PID.7",
        title="Date/Time of Birth",
        description="O | Item #00110",
    )

    pid_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_8",
            "administrative_sex",
            "PID.8",
        ),
        serialization_alias="PID.8",
        title="Administrative Sex",
        description="O | Item #00111 | Table 0001 - Administrative Sex | LEN:1",
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

    pid_10: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_10",
            "race",
            "PID.10",
        ),
        serialization_alias="PID.10",
        title="Race",
        description="O | Item #00113 | Table 0005 - Race",
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
        description="O | Item #00115 | Table 0289 - County/parish | LEN:4",
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
        description="O | Item #00118 | Table 0296 - Primary Language",
    )

    pid_16: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_16",
            "marital_status",
            "PID.16",
        ),
        serialization_alias="PID.16",
        title="Marital Status",
        description="O | Item #00119 | Table 0002 - Marital Status",
    )

    pid_17: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_17",
            "religion",
            "PID.17",
        ),
        serialization_alias="PID.17",
        title="Religion",
        description="O | Item #00120 | Table 0006 - Religion",
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
            "driver_s_license_number_patient",
            "PID.20",
        ),
        serialization_alias="PID.20",
        title="Driver's License Number - Patient",
        description="O | Item #00123",
    )

    pid_21: Optional[List[CX]] = Field(
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

    pid_22: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_22",
            "ethnic_group",
            "PID.22",
        ),
        serialization_alias="PID.22",
        title="Ethnic Group",
        description="O | Item #00125 | Table 0189 - Ethnic Group",
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
        description="O | Item #00126 | LEN:250",
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
        description="O | Item #00127 | Table 0136 - Yes/no indicator | LEN:1",
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

    pid_26: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_26",
            "citizenship",
            "PID.26",
        ),
        serialization_alias="PID.26",
        title="Citizenship",
        description="O | Item #00129 | Table 0171 - Citizenship",
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
            "nationality",
            "PID.28",
        ),
        serialization_alias="PID.28",
        title="Nationality",
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
        description="O | Item #00740",
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
        description="O | Item #00741 | Table 0136 - Yes/no indicator | LEN:1",
    )

    pid_31: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_31",
            "identity_unknown_indicator",
            "PID.31",
        ),
        serialization_alias="PID.31",
        title="Identity Unknown Indicator",
        description="O | Item #01535 | Table 0136 - Yes/no indicator | LEN:1",
    )

    pid_32: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_32",
            "identity_reliability_code",
            "PID.32",
        ),
        serialization_alias="PID.32",
        title="Identity Reliability Code",
        description=(
            "O | Item #01536 | Table 0445 - Identity Reliability Code | LEN:20"
        ),
    )

    pid_33: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_33",
            "last_update_date_time",
            "PID.33",
        ),
        serialization_alias="PID.33",
        title="Last Update Date/Time",
        description="O | Item #01537",
    )

    pid_34: Optional[HD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_34",
            "last_update_facility",
            "PID.34",
        ),
        serialization_alias="PID.34",
        title="Last Update Facility",
        description="O | Item #01538",
    )

    pid_35: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_35",
            "species_code",
            "PID.35",
        ),
        serialization_alias="PID.35",
        title="Species Code",
        description="C | Item #01539 | Table 0446 - Species Code",
    )

    pid_36: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_36",
            "breed_code",
            "PID.36",
        ),
        serialization_alias="PID.36",
        title="Breed Code",
        description="C | Item #01540 | Table 0447 - Breed Code",
    )

    pid_37: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_37",
            "strain",
            "PID.37",
        ),
        serialization_alias="PID.37",
        title="Strain",
        description="O | Item #01541 | LEN:80",
    )

    pid_38: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_38",
            "production_class_code",
            "PID.38",
        ),
        serialization_alias="PID.38",
        title="Production Class Code",
        description="O | Item #01542 | Table 0429 - Production Class Code",
    )

    pid_39: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_39",
            "tribal_citizenship",
            "PID.39",
        ),
        serialization_alias="PID.39",
        title="Tribal Citizenship",
        description="O | Item #01840 | Table 0171 - Citizenship",
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
