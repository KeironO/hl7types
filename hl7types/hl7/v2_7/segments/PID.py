"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: PID
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CWE import CWE
from ..datatypes.CX import CX
from ..datatypes.HD import HD
from ..datatypes.XAD import XAD
from ..datatypes.XPN import XPN
from ..datatypes.XTN import XTN


class PID(BaseModel):
    """HL7 v2 PID segment.

    Attributes
    ----------
    pid_1 : str | None
        PID.1 (opt) - Set ID - PID (SI)

    pid_3 : list[CX]
        PID.3 (req, rep) - Patient Identifier List (CX)

    pid_5 : list[XPN]
        PID.5 (req, rep) - Patient Name (XPN)

    pid_6 : list[XPN] | None
        PID.6 (opt, rep) - Mother's Maiden Name (XPN)

    pid_7 : str | None
        PID.7 (opt) - Date/Time of Birth (DTM)

    pid_8 : CWE | None
        PID.8 (opt) - Administrative Sex (CWE)

    pid_10 : list[CWE] | None
        PID.10 (opt, rep) - Race (CWE)

    pid_11 : list[XAD] | None
        PID.11 (opt, rep) - Patient Address (XAD)

    pid_13 : list[XTN] | None
        PID.13 (opt, rep) - Phone Number - Home (XTN)

    pid_14 : list[XTN] | None
        PID.14 (opt, rep) - Phone Number - Business (XTN)

    pid_15 : CWE | None
        PID.15 (opt) - Primary Language (CWE)

    pid_16 : CWE | None
        PID.16 (opt) - Marital Status (CWE)

    pid_17 : CWE | None
        PID.17 (opt) - Religion (CWE)

    pid_18 : CX | None
        PID.18 (opt) - Patient Account Number (CX)

    pid_21 : list[CX] | None
        PID.21 (opt, rep) - Mother's Identifier (CX)

    pid_22 : list[CWE] | None
        PID.22 (opt, rep) - Ethnic Group (CWE)

    pid_23 : str | None
        PID.23 (opt) - Birth Place (ST)

    pid_24 : str | None
        PID.24 (opt) - Multiple Birth Indicator (ID)

    pid_25 : str | None
        PID.25 (opt) - Birth Order (NM)

    pid_26 : list[CWE] | None
        PID.26 (opt, rep) - Citizenship (CWE)

    pid_27 : CWE | None
        PID.27 (opt) - Veterans Military Status (CWE)

    pid_29 : str | None
        PID.29 (opt) - Patient Death Date and Time (DTM)

    pid_30 : str | None
        PID.30 (opt) - Patient Death Indicator (ID)

    pid_31 : str | None
        PID.31 (opt) - Identity Unknown Indicator (ID)

    pid_32 : list[CWE] | None
        PID.32 (opt, rep) - Identity Reliability Code (CWE)

    pid_33 : str | None
        PID.33 (opt) - Last Update Date/Time (DTM)

    pid_34 : HD | None
        PID.34 (opt) - Last Update Facility (HD)

    pid_35 : CWE | None
        PID.35 (opt) - Species Code (CWE)

    pid_36 : CWE | None
        PID.36 (opt) - Breed Code (CWE)

    pid_37 : str | None
        PID.37 (opt) - Strain (ST)

    pid_38 : list[CWE] | None
        PID.38 (opt, rep) - Production Class Code (CWE)

    pid_39 : list[CWE] | None
        PID.39 (opt, rep) - Tribal Citizenship (CWE)

    pid_40 : list[XTN] | None
        PID.40 (opt, rep) - Patient Telecommunication Information (XTN)
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
        description="Item #104",
    )

    pid_3: List[CX] = Field(
        default=...,
        validation_alias=AliasChoices(
            "pid_3",
            "patient_identifier_list",
            "PID.3",
        ),
        serialization_alias="PID.3",
        title="Patient Identifier List",
        description="Item #106",
    )

    pid_5: List[XPN] = Field(
        default=...,
        validation_alias=AliasChoices(
            "pid_5",
            "patient_name",
            "PID.5",
        ),
        serialization_alias="PID.5",
        title="Patient Name",
        description="Item #108 | Table HL70200",
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
        description="Item #109",
    )

    pid_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_7",
            "date_time_of_birth",
            "PID.7",
        ),
        serialization_alias="PID.7",
        title="Date/Time of Birth",
        description="Item #110",
    )

    pid_8: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_8",
            "administrative_sex",
            "PID.8",
        ),
        serialization_alias="PID.8",
        title="Administrative Sex",
        description="Item #111 | Table HL70001",
    )

    pid_10: Optional[List[CWE]] = Field(
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

    pid_15: Optional[CWE] = Field(
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

    pid_16: Optional[CWE] = Field(
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

    pid_17: Optional[CWE] = Field(
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
        description="Item #121 | Table HL70061",
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
        description="Item #124 | Table HL70061",
    )

    pid_22: Optional[List[CWE]] = Field(
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

    pid_26: Optional[List[CWE]] = Field(
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

    pid_27: Optional[CWE] = Field(
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

    pid_29: Optional[str] = Field(
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

    pid_31: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_31",
            "identity_unknown_indicator",
            "PID.31",
        ),
        serialization_alias="PID.31",
        title="Identity Unknown Indicator",
        description="Item #1535 | Table HL70136",
    )

    pid_32: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_32",
            "identity_reliability_code",
            "PID.32",
        ),
        serialization_alias="PID.32",
        title="Identity Reliability Code",
        description="Item #1536 | Table HL70445",
    )

    pid_33: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_33",
            "last_update_date_time",
            "PID.33",
        ),
        serialization_alias="PID.33",
        title="Last Update Date/Time",
        description="Item #1537",
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
        description="Item #1538",
    )

    pid_35: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_35",
            "species_code",
            "PID.35",
        ),
        serialization_alias="PID.35",
        title="Species Code",
        description="Item #1539 | Table HL70446",
    )

    pid_36: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_36",
            "breed_code",
            "PID.36",
        ),
        serialization_alias="PID.36",
        title="Breed Code",
        description="Item #1540 | Table HL70447",
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
        description="Item #1541",
    )

    pid_38: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_38",
            "production_class_code",
            "PID.38",
        ),
        serialization_alias="PID.38",
        title="Production Class Code",
        description="Item #1542 | Table HL70429",
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
        description="Item #1840 | Table HL70171",
    )

    pid_40: Optional[List[XTN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pid_40",
            "patient_telecommunication_information",
            "PID.40",
        ),
        serialization_alias="PID.40",
        title="Patient Telecommunication Information",
        description="Item #2289",
    )

    model_config = {"populate_by_name": True}
