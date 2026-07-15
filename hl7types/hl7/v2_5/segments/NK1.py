"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: NK1
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.CX import CX
from ..datatypes.JCC import JCC
from ..datatypes.TS import TS
from ..datatypes.XAD import XAD
from ..datatypes.XON import XON
from ..datatypes.XPN import XPN
from ..datatypes.XTN import XTN


class NK1(HL7Model):
    """Next of Kin / Associated Parties (S3.4.5).

    Attributes
    ----------
    nk1_1 : str
        NK1.1 - Set ID - NK1 (SI) R S3.4.5.1

    nk1_2 : list[XPN] | None
        NK1.2 - Name (XPN) O rep S3.4.5.2

    nk1_3 : CE | None
        NK1.3 - Relationship (CE) O S3.4.5.3 | 0063 - Relationship

    nk1_4 : list[XAD] | None
        NK1.4 - Address (XAD) O rep S3.4.5.4

    nk1_5 : list[XTN] | None
        NK1.5 - Phone Number (XTN) O rep S3.4.5.5

    nk1_6 : list[XTN] | None
        NK1.6 - Business Phone Number (XTN) O rep S3.4.5.6

    nk1_7 : CE | None
        NK1.7 - Contact Role (CE) O S3.4.5.7 | 0131 - Contact Role

    nk1_8 : str | None
        NK1.8 - Start Date (DT) O S3.4.5.8

    nk1_9 : str | None
        NK1.9 - End Date (DT) O S3.4.5.9

    nk1_10 : str | None
        NK1.10 - Next of Kin / Associated Parties Job Title (ST) O S3.4.5.10

    nk1_11 : JCC | None
        NK1.11 - Next of Kin / Associated Parties Job Code/Class (JCC) O S3.4.5.11

    nk1_12 : CX | None
        NK1.12 - Next of Kin / Associated Parties Employee Number (CX) O S3.4.5.12

    nk1_13 : list[XON] | None
        NK1.13 - Organization Name - NK1 (XON) O rep S3.4.5.13

    nk1_14 : CE | None
        NK1.14 - Marital Status (CE) O S3.4.2.16 | 0002 - Marital Status

    nk1_15 : str | None
        NK1.15 - Administrative Sex (IS) O S3.4.2.8 | 0001 - Administrative Sex

    nk1_16 : TS | None
        NK1.16 - Date/Time of Birth (TS) O S3.4.2.7

    nk1_17 : list[str] | None
        NK1.17 - Living Dependency (IS) O rep S3.4.5.17 | 0223 - Living Dependency

    nk1_18 : list[str] | None
        NK1.18 - Ambulatory Status (IS) O rep S3.4.3.15 | 0009 - Ambulatory Status

    nk1_19 : list[CE] | None
        NK1.19 - Citizenship (CE) O rep S3.4.2.26 | 0171 - Citizenship

    nk1_20 : CE | None
        NK1.20 - Primary Language (CE) O S3.4.2.15 | 0296 - Primary Language

    nk1_21 : str | None
        NK1.21 - Living Arrangement (IS) O S3.4.5.21 | 0220 - Living Arrangement

    nk1_22 : CE | None
        NK1.22 - Publicity Code (CE) O S3.4.5.22 | 0215 - Publicity Code

    nk1_23 : str | None
        NK1.23 - Protection Indicator (ID) O S3.4.5.23 | 0136 - Yes/no indicator

    nk1_24 : str | None
        NK1.24 - Student Indicator (IS) O S3.4.5.24 | 0231 - Student Status

    nk1_25 : CE | None
        NK1.25 - Religion (CE) O S3.4.2.17 | 0006 - Religion

    nk1_26 : list[XPN] | None
        NK1.26 - Mother's Maiden Name (XPN) O rep S3.4.2.6

    nk1_27 : CE | None
        NK1.27 - Nationality (CE) O S3.4.2.28 | 0212 - Nationality

    nk1_28 : list[CE] | None
        NK1.28 - Ethnic Group (CE) O rep S3.4.2.22 | 0189 - Ethnic Group

    nk1_29 : list[CE] | None
        NK1.29 - Contact Reason (CE) O rep S3.4.5.29 | 0222 - Contact Reason

    nk1_30 : list[XPN] | None
        NK1.30 - Contact Person's Name (XPN) O rep S3.4.5.30

    nk1_31 : list[XTN] | None
        NK1.31 - Contact Person's Telephone Number (XTN) O rep S3.4.5.31

    nk1_32 : list[XAD] | None
        NK1.32 - Contact Person's Address (XAD) O rep S3.4.5.32

    nk1_33 : list[CX] | None
        NK1.33 - Next of Kin/Associated Party's Identifiers (CX) O rep S3.4.5.33

    nk1_34 : str | None
        NK1.34 - Job Status (IS) O S3.4.5.34 | 0311 - Job Status

    nk1_35 : list[CE] | None
        NK1.35 - Race (CE) O rep S3.4.2.10 | 0005 - Race

    nk1_36 : str | None
        NK1.36 - Handicap (IS) O S3.4.5.36 | 0295 - Handicap

    nk1_37 : str | None
        NK1.37 - Contact Person Social Security Number (ST) O S3.4.5.37

    nk1_38 : str | None
        NK1.38 - Next of Kin Birth Place (ST) O S3.4.5.38

    nk1_39 : str | None
        NK1.39 - VIP Indicator (IS) O S3.4.3.16 | 0099 - VIP Indicator
    """

    nk1_1: str = Field(
        validation_alias=AliasChoices(
            "nk1_1",
            "set_id_nk1",
            "NK1.1",
        ),
        serialization_alias="NK1.1",
        title="Set ID - NK1",
        description="R | Item #00190 | LEN:4",
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
        description="O | Item #00191",
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
        description="O | Item #00192 | Table 0063 - Relationship",
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
        description="O | Item #00193",
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
        description="O | Item #00194",
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
        description="O | Item #00195",
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
        description="O | Item #00196 | Table 0131 - Contact Role",
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
        description="O | Item #00197 | LEN:8",
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
        description="O | Item #00198 | LEN:8",
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
        description="O | Item #00199 | LEN:60",
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
        description="O | Item #00200",
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
        description="O | Item #00201",
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
        description="O | Item #00202",
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
        description="O | Item #00119 | Table 0002 - Marital Status",
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
        description="O | Item #00111 | Table 0001 - Administrative Sex | LEN:1",
    )

    nk1_16: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_16",
            "date_time_of_birth",
            "NK1.16",
        ),
        serialization_alias="NK1.16",
        title="Date/Time of Birth",
        description="O | Item #00110",
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
        description="O | Item #00755 | Table 0223 - Living Dependency | LEN:2",
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
        description="O | Item #00145 | Table 0009 - Ambulatory Status | LEN:2",
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
        description="O | Item #00129 | Table 0171 - Citizenship",
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
        description="O | Item #00118 | Table 0296 - Primary Language",
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
        description="O | Item #00742 | Table 0220 - Living Arrangement | LEN:2",
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
        description="O | Item #00743 | Table 0215 - Publicity Code",
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
        description="O | Item #00744 | Table 0136 - Yes/no indicator | LEN:1",
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
        description="O | Item #00745 | Table 0231 - Student Status | LEN:2",
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
        description="O | Item #00120 | Table 0006 - Religion",
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
        description="O | Item #00109",
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
        description="O | Item #00739 | Table 0212 - Nationality",
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
        description="O | Item #00125 | Table 0189 - Ethnic Group",
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
        description="O | Item #00747 | Table 0222 - Contact Reason",
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
        description="O | Item #00748",
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
        description="O | Item #00749",
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
        description="O | Item #00750",
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
        description="O | Item #00751",
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
        description="O | Item #00752 | Table 0311 - Job Status | LEN:2",
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
        description="O | Item #00113 | Table 0005 - Race",
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
        description="O | Item #00753 | Table 0295 - Handicap | LEN:2",
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
        description="O | Item #00754 | LEN:16",
    )

    nk1_38: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_38",
            "next_of_kin_birth_place",
            "NK1.38",
        ),
        serialization_alias="NK1.38",
        title="Next of Kin Birth Place",
        description="O | Item #01905 | LEN:250",
    )

    nk1_39: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_39",
            "vip_indicator",
            "NK1.39",
        ),
        serialization_alias="NK1.39",
        title="VIP Indicator",
        description="O | Item #00146 | Table 0099 - VIP Indicator | LEN:2",
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
