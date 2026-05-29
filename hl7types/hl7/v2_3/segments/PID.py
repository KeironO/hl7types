"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: PID
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE
from ..datatypes.CX import CX
from ..datatypes.DLN import DLN
from ..datatypes.TS import TS
from ..datatypes.XAD import XAD
from ..datatypes.XPN import XPN
from ..datatypes.XTN import XTN


class PID(BaseModel):
    """HL7 v2 PID segment.

    Attributes
    ----------
    pid_1 : str | None
        PID.1 (opt) - Set ID - Patient ID (SI)

    pid_2 : CX | None
        PID.2 (opt) - Patient ID (External ID) (CX)

    pid_3 : list[CX]
        PID.3 (req, rep) - Patient ID (Internal ID) (CX)

    pid_4 : CX | None
        PID.4 (opt) - Alternate Patient ID (CX)

    pid_5 : XPN
        PID.5 (req) - Patient Name (XPN)

    pid_6 : XPN | None
        PID.6 (opt) - Mother's Maiden Name (XPN)

    pid_7 : TS | None
        PID.7 (opt) - Date of Birth (TS)

    pid_8 : str | None
        PID.8 (opt) - Sex (IS)

    pid_9 : list[XPN] | None
        PID.9 (opt, rep) - Patient Alias (XPN)

    pid_10 : str | None
        PID.10 (opt) - Race (IS)

    pid_11 : list[XAD] | None
        PID.11 (opt, rep) - Patient Address (XAD)

    pid_12 : str | None
        PID.12 (opt) - County Code (IS)

    pid_13 : list[XTN] | None
        PID.13 (opt, rep) - Phone Number - Home (XTN)

    pid_14 : list[XTN] | None
        PID.14 (opt, rep) - Phone Number - Business (XTN)

    pid_15 : CE | None
        PID.15 (opt) - Primary Language (CE)

    pid_16 : list[str] | None
        PID.16 (opt, rep) - Marital Status (IS)

    pid_17 : str | None
        PID.17 (opt) - Religion (IS)

    pid_18 : CX | None
        PID.18 (opt) - Patient Account Number (CX)

    pid_19 : str | None
        PID.19 (opt) - SSN Number - Patient (ST)

    pid_20 : DLN | None
        PID.20 (opt) - Driver's License Number (DLN)

    pid_21 : CX | None
        PID.21 (opt) - Mother's Identifier (CX)

    pid_22 : str | None
        PID.22 (opt) - Ethnic Group (IS)

    pid_23 : str | None
        PID.23 (opt) - Birth Place (ST)

    pid_24 : str | None
        PID.24 (opt) - Multiple Birth Indicator (ID)

    pid_25 : str | None
        PID.25 (opt) - Birth Order (NM)

    pid_26 : str | None
        PID.26 (opt) - Citizenship (IS)

    pid_27 : CE | None
        PID.27 (opt) - Veterans Military Status (CE)

    pid_28 : CE | None
        PID.28 (opt) - Nationality Code (CE)

    pid_29 : TS | None
        PID.29 (opt) - Patient Death Date and Time (TS)

    pid_30 : str | None
        PID.30 (opt) - Patient Death Indicator (ID)
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

    pid_2: Optional[CX] = Field(
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

    pid_3: List[CX] = Field(
        default=...,
        validation_alias=AliasChoices(
            "pid_3",
            "patient_id_internal_id",
            "PID.3",
        ),
        serialization_alias="PID.3",
        title="Patient ID (Internal ID)",
        description="Item #106",
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
        description="Item #107",
    )

    pid_5: XPN = Field(
        default=...,
        validation_alias=AliasChoices(
            "pid_5",
            "patient_name",
            "PID.5",
        ),
        serialization_alias="PID.5",
        title="Patient Name",
        description="Item #108",
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

    pid_9: Optional[List[XPN]] = Field(
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

    pid_11: Optional[List[XAD]] = Field(
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
        title="County Code",
        description="Item #115",
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
        description="Item #116",
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
        description="Item #117",
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
        description="Item #118 | Table HL70296",
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

    pid_18: Optional[CX] = Field(
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
            "ssn_number_patient",
            "PID.19",
        ),
        serialization_alias="PID.19",
        title="SSN Number - Patient",
        description="Item #122",
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
        description="Item #123",
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
        description="Item #127 | Table HL70136",
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

    pid_26: Optional[str] = Field(
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

    pid_27: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_27",
            "veterans_military_status",
            "PID.27",
        ),
        serialization_alias="PID.27",
        title="Veterans Military Status",
        description="Item #130 | Table HL70172",
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
        description="Item #739 | Table HL70212",
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
        description="Item #740",
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
        description="Item #741 | Table HL70136",
    )

    model_config = {"populate_by_name": True}
