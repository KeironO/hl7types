"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: NK1
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator

from ..datatypes.CE import CE
from ..datatypes.CX import CX
from ..datatypes.JCC import JCC
from ..datatypes.TS import TS
from ..datatypes.XAD import XAD
from ..datatypes.XON import XON
from ..datatypes.XPN import XPN
from ..datatypes.XTN import XTN


class NK1(HL7Model):
    """HL7 v2 NK1 segment.

    Attributes
    ----------
    nk1_1 : str
        NK1.1 (req) - Set ID - NK1 (SI)

    nk1_2 : list[XPN] | None
        NK1.2 (opt, rep) - Name (XPN)

    nk1_3 : CE | None
        NK1.3 (opt) - Relationship (CE)

    nk1_4 : list[XAD] | None
        NK1.4 (opt, rep) - Address (XAD)

    nk1_5 : list[XTN] | None
        NK1.5 (opt, rep) - Phone Number (XTN)

    nk1_6 : list[XTN] | None
        NK1.6 (opt, rep) - Business Phone Number (XTN)

    nk1_7 : CE | None
        NK1.7 (opt) - Contact Role (CE)

    nk1_8 : str | None
        NK1.8 (opt) - Start Date (DT)

    nk1_9 : str | None
        NK1.9 (opt) - End Date (DT)

    nk1_10 : str | None
        NK1.10 (opt) - Next of Kin / Associated Parties Job Title (ST)

    nk1_11 : JCC | None
        NK1.11 (opt) - Next of Kin / Associated Parties Job Code/Class (JCC)

    nk1_12 : CX | None
        NK1.12 (opt) - Next of Kin / Associated Parties Employee Number (CX)

    nk1_13 : list[XON] | None
        NK1.13 (opt, rep) - Organization Name - NK1 (XON)

    nk1_14 : CE | None
        NK1.14 (opt) - Marital Status (CE)

    nk1_15 : str | None
        NK1.15 (opt) - Administrative Sex (IS)

    nk1_16 : TS | None
        NK1.16 (opt) - Date/Time Of Birth (TS)

    nk1_17 : list[str] | None
        NK1.17 (opt, rep) - Living Dependency (IS)

    nk1_18 : list[str] | None
        NK1.18 (opt, rep) - Ambulatory Status (IS)

    nk1_19 : list[CE] | None
        NK1.19 (opt, rep) - Citizenship (CE)

    nk1_20 : CE | None
        NK1.20 (opt) - Primary Language (CE)

    nk1_21 : str | None
        NK1.21 (opt) - Living Arrangement (IS)

    nk1_22 : CE | None
        NK1.22 (opt) - Publicity Code (CE)

    nk1_23 : str | None
        NK1.23 (opt) - Protection Indicator (ID)

    nk1_24 : str | None
        NK1.24 (opt) - Student Indicator (IS)

    nk1_25 : CE | None
        NK1.25 (opt) - Religion (CE)

    nk1_26 : list[XPN] | None
        NK1.26 (opt, rep) - Mother's Maiden Name (XPN)

    nk1_27 : CE | None
        NK1.27 (opt) - Nationality (CE)

    nk1_28 : list[CE] | None
        NK1.28 (opt, rep) - Ethnic Group (CE)

    nk1_29 : list[CE] | None
        NK1.29 (opt, rep) - Contact Reason (CE)

    nk1_30 : list[XPN] | None
        NK1.30 (opt, rep) - Contact Person's Name (XPN)

    nk1_31 : list[XTN] | None
        NK1.31 (opt, rep) - Contact Person's Telephone Number (XTN)

    nk1_32 : list[XAD] | None
        NK1.32 (opt, rep) - Contact Person's Address (XAD)

    nk1_33 : list[CX] | None
        NK1.33 (opt, rep) - Next of Kin/Associated Party's Identifiers (CX)

    nk1_34 : str | None
        NK1.34 (opt) - Job Status (IS)

    nk1_35 : list[CE] | None
        NK1.35 (opt, rep) - Race (CE)

    nk1_36 : str | None
        NK1.36 (opt) - Handicap (IS)

    nk1_37 : str | None
        NK1.37 (opt) - Contact Person Social Security Number (ST)
    """

    nk1_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "nk1_1",
            "set_id_nk1",
            "NK1.1",
        ),
        serialization_alias="NK1.1",
        title="Set ID - NK1",
        description="Item #190",
    )

    nk1_2: Optional[List[XPN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_2",
            "name",
            "NK1.2",
        ),
        serialization_alias="NK1.2",
        title="Name",
        description="Item #191",
    )

    nk1_3: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_3",
            "relationship",
            "NK1.3",
        ),
        serialization_alias="NK1.3",
        title="Relationship",
        description="Item #192 | Table HL70063",
    )

    nk1_4: Optional[List[XAD]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_4",
            "address",
            "NK1.4",
        ),
        serialization_alias="NK1.4",
        title="Address",
        description="Item #193",
    )

    nk1_5: Optional[List[XTN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_5",
            "phone_number",
            "NK1.5",
        ),
        serialization_alias="NK1.5",
        title="Phone Number",
        description="Item #194",
    )

    nk1_6: Optional[List[XTN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_6",
            "business_phone_number",
            "NK1.6",
        ),
        serialization_alias="NK1.6",
        title="Business Phone Number",
        description="Item #195",
    )

    nk1_7: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_7",
            "contact_role",
            "NK1.7",
        ),
        serialization_alias="NK1.7",
        title="Contact Role",
        description="Item #196 | Table HL70131",
    )

    nk1_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_8",
            "start_date",
            "NK1.8",
        ),
        serialization_alias="NK1.8",
        title="Start Date",
        description="Item #197",
    )

    nk1_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_9",
            "end_date",
            "NK1.9",
        ),
        serialization_alias="NK1.9",
        title="End Date",
        description="Item #198",
    )

    nk1_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_10",
            "next_of_kin_associated_parties_job_title",
            "NK1.10",
        ),
        serialization_alias="NK1.10",
        title="Next of Kin / Associated Parties Job Title",
        description="Item #199",
    )

    nk1_11: Optional[JCC] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_11",
            "next_of_kin_associated_parties_job_code_class",
            "NK1.11",
        ),
        serialization_alias="NK1.11",
        title="Next of Kin / Associated Parties Job Code/Class",
        description="Item #200 | Table HL70327",
    )

    nk1_12: Optional[CX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_12",
            "next_of_kin_associated_parties_employee_number",
            "NK1.12",
        ),
        serialization_alias="NK1.12",
        title="Next of Kin / Associated Parties Employee Number",
        description="Item #201",
    )

    nk1_13: Optional[List[XON]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_13",
            "organization_name_nk1",
            "NK1.13",
        ),
        serialization_alias="NK1.13",
        title="Organization Name - NK1",
        description="Item #202",
    )

    nk1_14: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_14",
            "marital_status",
            "NK1.14",
        ),
        serialization_alias="NK1.14",
        title="Marital Status",
        description="Item #119 | Table HL70002",
    )

    nk1_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_15",
            "administrative_sex",
            "NK1.15",
        ),
        serialization_alias="NK1.15",
        title="Administrative Sex",
        description="Item #111 | Table HL70001",
    )

    nk1_16: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_16",
            "date_time_of_birth",
            "NK1.16",
        ),
        serialization_alias="NK1.16",
        title="Date/Time Of Birth",
        description="Item #110",
    )

    nk1_17: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_17",
            "living_dependency",
            "NK1.17",
        ),
        serialization_alias="NK1.17",
        title="Living Dependency",
        description="Item #755 | Table HL70223",
    )

    nk1_18: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_18",
            "ambulatory_status",
            "NK1.18",
        ),
        serialization_alias="NK1.18",
        title="Ambulatory Status",
        description="Item #145 | Table HL70009",
    )

    nk1_19: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_19",
            "citizenship",
            "NK1.19",
        ),
        serialization_alias="NK1.19",
        title="Citizenship",
        description="Item #129 | Table HL70171",
    )

    nk1_20: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_20",
            "primary_language",
            "NK1.20",
        ),
        serialization_alias="NK1.20",
        title="Primary Language",
        description="Item #118 | Table HL70296",
    )

    nk1_21: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_21",
            "living_arrangement",
            "NK1.21",
        ),
        serialization_alias="NK1.21",
        title="Living Arrangement",
        description="Item #742 | Table HL70220",
    )

    nk1_22: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_22",
            "publicity_code",
            "NK1.22",
        ),
        serialization_alias="NK1.22",
        title="Publicity Code",
        description="Item #743 | Table HL70215",
    )

    nk1_23: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_23",
            "protection_indicator",
            "NK1.23",
        ),
        serialization_alias="NK1.23",
        title="Protection Indicator",
        description="Item #744 | Table HL70136",
    )

    nk1_24: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_24",
            "student_indicator",
            "NK1.24",
        ),
        serialization_alias="NK1.24",
        title="Student Indicator",
        description="Item #745 | Table HL70231",
    )

    nk1_25: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_25",
            "religion",
            "NK1.25",
        ),
        serialization_alias="NK1.25",
        title="Religion",
        description="Item #120 | Table HL70006",
    )

    nk1_26: Optional[List[XPN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_26",
            "mother_s_maiden_name",
            "NK1.26",
        ),
        serialization_alias="NK1.26",
        title="Mother's Maiden Name",
        description="Item #109",
    )

    nk1_27: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_27",
            "nationality",
            "NK1.27",
        ),
        serialization_alias="NK1.27",
        title="Nationality",
        description="Item #739 | Table HL70212",
    )

    nk1_28: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_28",
            "ethnic_group",
            "NK1.28",
        ),
        serialization_alias="NK1.28",
        title="Ethnic Group",
        description="Item #125 | Table HL70189",
    )

    nk1_29: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_29",
            "contact_reason",
            "NK1.29",
        ),
        serialization_alias="NK1.29",
        title="Contact Reason",
        description="Item #747 | Table HL70222",
    )

    nk1_30: Optional[List[XPN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_30",
            "contact_person_s_name",
            "NK1.30",
        ),
        serialization_alias="NK1.30",
        title="Contact Person's Name",
        description="Item #748",
    )

    nk1_31: Optional[List[XTN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_31",
            "contact_person_s_telephone_number",
            "NK1.31",
        ),
        serialization_alias="NK1.31",
        title="Contact Person's Telephone Number",
        description="Item #749",
    )

    nk1_32: Optional[List[XAD]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_32",
            "contact_person_s_address",
            "NK1.32",
        ),
        serialization_alias="NK1.32",
        title="Contact Person's Address",
        description="Item #750",
    )

    nk1_33: Optional[List[CX]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_33",
            "next_of_kin_associated_party_s_identifiers",
            "NK1.33",
        ),
        serialization_alias="NK1.33",
        title="Next of Kin/Associated Party's Identifiers",
        description="Item #751",
    )

    nk1_34: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_34",
            "job_status",
            "NK1.34",
        ),
        serialization_alias="NK1.34",
        title="Job Status",
        description="Item #752 | Table HL70311",
    )

    nk1_35: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_35",
            "race",
            "NK1.35",
        ),
        serialization_alias="NK1.35",
        title="Race",
        description="Item #113 | Table HL70005",
    )

    nk1_36: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_36",
            "handicap",
            "NK1.36",
        ),
        serialization_alias="NK1.36",
        title="Handicap",
        description="Item #753 | Table HL70295",
    )

    nk1_37: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_37",
            "contact_person_social_security_number",
            "NK1.37",
        ),
        serialization_alias="NK1.37",
        title="Contact Person Social Security Number",
        description="Item #754",
    )

    @field_validator("nk1_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("nk1_8", "nk1_9", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2})?)?)?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    model_config = {"populate_by_name": True}
