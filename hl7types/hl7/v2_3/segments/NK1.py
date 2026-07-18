"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: NK1
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.CX import CX
from ..datatypes.JCC import JCC
from ..datatypes.TS import TS
from ..datatypes.XAD import XAD
from ..datatypes.XON import XON
from ..datatypes.XPN import XPN
from ..datatypes.XTN import XTN

_RE_SI = re.compile(r'\d*')
_RE_DT = re.compile(r'(\d{4}([01]\d(\d{2})?)?)?')


class NK1(HL7Model):
    """Next of kin (S3.3.5).

    Attributes
    ----------
    nk1_1 : str
        NK1.1 - Set ID - Next of Kin (SI) R S3.3.5.1

    nk1_2 : list[XPN] | None
        NK1.2 - Name (XPN) O rep S3.3.5.2

    nk1_3 : CE | None
        NK1.3 - Relationship (CE) O S3.3.5.3 | 0063 - Relationship

    nk1_4 : list[XAD] | None
        NK1.4 - Address (XAD) O rep S3.3.5.4

    nk1_5 : list[XTN] | None
        NK1.5 - Phone Number (XTN) O rep S3.3.5.5

    nk1_6 : list[XTN] | None
        NK1.6 - Business Phone Number (XTN) O rep S3.3.5.6

    nk1_7 : CE | None
        NK1.7 - Contact Role (CE) R S3.3.5.7 | 0131 - Contact Role

    nk1_8 : str | None
        NK1.8 - Start Date (DT) O S3.3.5.8

    nk1_9 : str | None
        NK1.9 - End Date (DT) O S3.3.5.9

    nk1_10 : str | None
        NK1.10 - Next of Kin/Associated Parties Job Title (ST) O S3.3.5.10

    nk1_11 : JCC | None
        NK1.11 - Next of Kin Job/Associated Parties Code/Class (JCC) O S3.3.5.11

    nk1_12 : CX | None
        NK1.12 - Next of Kin/Associated Parties Employee Number (CX) O S3.3.5.12

    nk1_13 : list[XON] | None
        NK1.13 - Organization Name (XON) O rep S3.3.5.13

    nk1_14 : list[str] | None
        NK1.14 - Marital Status (IS) NA rep S3.3.2 | 0002 - Marital Status

    nk1_15 : str | None
        NK1.15 - Sex (IS) NA S3.3.2 | 0001 - Sex

    nk1_16 : TS | None
        NK1.16 - Date of Birth (TS) O S3.3.2

    nk1_17 : str | None
        NK1.17 - Living Dependency (IS) O S3.3.5 | 0223 - Living Dependency

    nk1_18 : str | None
        NK1.18 - Ambulatory Status (IS) O S3.3.3 | 0009 - Ambulatory Status

    nk1_19 : str | None
        NK1.19 - Citizenship (IS) O S3.3.2 | 0171 - Country Code

    nk1_20 : CE | None
        NK1.20 - Primary Language (CE) O S3.3.2 | 0296 - Language

    nk1_21 : str | None
        NK1.21 - Living Arrangement (IS) O S3.3.5 | 0220 - Living Arrangements

    nk1_22 : CE | None
        NK1.22 - Publicity Indicator (CE) O S3.3.5 | 0215 - Publicity Code

    nk1_23 : str | None
        NK1.23 - Protection Indicator (ID) O S3.3.5 | 0136 - Yes/No Indicator

    nk1_24 : str | None
        NK1.24 - Student Indicator (IS) O S3.3.5 | 0231 - Student Status

    nk1_25 : str | None
        NK1.25 - Religion (IS) O S3.3.2 | 0006 - Religion

    nk1_26 : XPN | None
        NK1.26 - Mother’s Maiden Name (XPN) O S3.3.5

    nk1_27 : CE | None
        NK1.27 - Nationality Code (CE) O S3.3.2 | 0212 - Nationality

    nk1_28 : str | None
        NK1.28 - Ethnic Group (IS) O S3.3.2 | 0189 - Ethnic Group

    nk1_29 : CE | None
        NK1.29 - Contact Reason (CE) O S3.3.5 | 0222 - Contact Reason

    nk1_30 : list[XPN] | None
        NK1.30 - Contact Person's Name (XPN) O rep S3.3.5

    nk1_31 : list[XTN] | None
        NK1.31 - Contact Person’s Telephone Number (XTN) O rep S3.3.5

    nk1_32 : list[XAD] | None
        NK1.32 - Contact Person’s Address (XAD) NA rep S3.3.5

    nk1_33 : list[CX] | None
        NK1.33 - Associated Party’s Identifiers (CX) NA rep S3.3.5.33

    nk1_34 : str | None
        NK1.34 - Job Status (IS) O S3.3.5 | 0311 - Job Status

    nk1_35 : str | None
        NK1.35 - Race (IS) NA S3.3.2 | 0005 - Race

    nk1_36 : str | None
        NK1.36 - Handicap (IS) O S3.3.5 | 0295 - Handicap

    nk1_37 : str | None
        NK1.37 - Contact Person Social Security Number (ST) NA S3.3.5.37
    """

    nk1_1: str = Field(
        validation_alias=AliasChoices(
            "nk1_1",
            "set_id_next_of_kin",
            "NK1.1",
        ),
        serialization_alias="NK1.1",
        title="Set ID - Next of Kin",
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
        description="R | Item #00196 | Table 0131 - Contact Role",
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
        title="Next of Kin/Associated Parties Job Title",
        description="O | Item #00199 | LEN:60",
    )

    nk1_11: Optional[JCC] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_11",
            "next_of_kin_job_associated_parties_code_class",
            "NK1.11",
        ),
        serialization_alias="NK1.11",
        title="Next of Kin Job/Associated Parties Code/Class",
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
        title="Next of Kin/Associated Parties Employee Number",
        description="O | Item #00201",
    )

    nk1_13: Optional[List[XON]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_13",
            "organization_name",
            "NK1.13",
        ),
        serialization_alias="NK1.13",
        title="Organization Name",
        description="O | Item #00202",
    )

    nk1_14: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_14",
            "marital_status",
            "NK1.14",
        ),
        serialization_alias="NK1.14",
        title="Marital Status",
        description="NA | Item #00119 | Table 0002 - Marital Status | LEN:1",
    )

    nk1_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_15",
            "sex",
            "NK1.15",
        ),
        serialization_alias="NK1.15",
        title="Sex",
        description="NA | Item #00111 | Table 0001 - Sex | LEN:1",
    )

    nk1_16: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_16",
            "date_of_birth",
            "NK1.16",
        ),
        serialization_alias="NK1.16",
        title="Date of Birth",
        description="O | Item #00110",
    )

    nk1_17: Optional[str] = Field(
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

    nk1_18: Optional[str] = Field(
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

    nk1_19: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_19",
            "citizenship",
            "NK1.19",
        ),
        serialization_alias="NK1.19",
        title="Citizenship",
        description="O | Item #00129 | Table 0171 - Country Code | LEN:4",
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
        description="O | Item #00118 | Table 0296 - Language",
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
        description=(
            "O | Item #00742 | Table 0220 - Living Arrangements | LEN:2"
        ),
    )

    nk1_22: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_22",
            "publicity_indicator",
            "NK1.22",
        ),
        serialization_alias="NK1.22",
        title="Publicity Indicator",
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
        description="O | Item #00744 | Table 0136 - Yes/No Indicator | LEN:1",
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

    nk1_25: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_25",
            "religion",
            "NK1.25",
        ),
        serialization_alias="NK1.25",
        title="Religion",
        description="O | Item #00120 | Table 0006 - Religion | LEN:3",
    )

    nk1_26: Optional[XPN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_26",
            "mother_s_maiden_name",
            "NK1.26",
        ),
        serialization_alias="NK1.26",
        title="Mother’s Maiden Name",
        description="O | Item #00746",
    )

    nk1_27: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_27",
            "nationality_code",
            "NK1.27",
        ),
        serialization_alias="NK1.27",
        title="Nationality Code",
        description="O | Item #00739 | Table 0212 - Nationality",
    )

    nk1_28: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_28",
            "ethnic_group",
            "NK1.28",
        ),
        serialization_alias="NK1.28",
        title="Ethnic Group",
        description="O | Item #00125 | Table 0189 - Ethnic Group | LEN:1",
    )

    nk1_29: Optional[CE] = Field(
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
        title="Contact Person’s Telephone Number",
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
        title="Contact Person’s Address",
        description="NA | Item #00750",
    )

    nk1_33: Optional[List[CX]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_33",
            "associated_party_s_identifiers",
            "NK1.33",
        ),
        serialization_alias="NK1.33",
        title="Associated Party’s Identifiers",
        description="NA | Item #00751",
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

    nk1_35: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_35",
            "race",
            "NK1.35",
        ),
        serialization_alias="NK1.35",
        title="Race",
        description="NA | Item #00113 | Table 0005 - Race | LEN:1",
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
        description="NA | Item #00754 | LEN:16",
    )

    @field_validator("nk1_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        if not _RE_SI.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("nk1_8", "nk1_9", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        if not _RE_DT.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    model_config = ConfigDict(populate_by_name=True)
