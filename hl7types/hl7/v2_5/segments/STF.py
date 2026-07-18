"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: STF
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.CWE import CWE
from ..datatypes.CX import CX
from ..datatypes.DIN import DIN
from ..datatypes.DLN import DLN
from ..datatypes.DR import DR
from ..datatypes.JCC import JCC
from ..datatypes.TS import TS
from ..datatypes.XAD import XAD
from ..datatypes.XPN import XPN
from ..datatypes.XTN import XTN

_RE_DT = re.compile(r'(\d{4}([01]\d(\d{2})?)?)?')


class STF(HL7Model):
    """Staff Identification (S15.4.8).

    Attributes
    ----------
    stf_1 : CE | None
        STF.1 - Primary Key Value - STF (CE) C S15.4.8.1 | 9999 - no table for CE

    stf_2 : list[CX] | None
        STF.2 - Staff Identifier List (CX) O rep S15.4.8.2

    stf_3 : list[XPN] | None
        STF.3 - Staff Name (XPN) O rep S15.4.8.3

    stf_4 : list[str] | None
        STF.4 - Staff Type (IS) O rep S15.4.8.4 | 0182 - Staff type

    stf_5 : str | None
        STF.5 - Administrative Sex (IS) O S3.4.2.8 | 0001 - Administrative Sex

    stf_6 : TS | None
        STF.6 - Date/Time of Birth (TS) O S3.4.2.7

    stf_7 : str | None
        STF.7 - Active/Inactive Flag (ID) O S8.9.5.6 | 0183 - Active/Inactive

    stf_8 : list[CE] | None
        STF.8 - Department (CE) O rep S8.10.3.3 | 0184 - Department

    stf_9 : list[CE] | None
        STF.9 - Hospital Service - STF (CE) O rep S15.4.8.9 | 0069 - Hospital Service

    stf_10 : list[XTN] | None
        STF.10 - Phone (XTN) O rep S15.4.7.12

    stf_11 : list[XAD] | None
        STF.11 - Office/Home Address/Birthplace (XAD) O rep S15.4.7.11

    stf_12 : list[DIN] | None
        STF.12 - Institution Activation Date (DIN) O rep S15.4.8.12 | 0537 - Institution

    stf_13 : list[DIN] | None
        STF.13 - Institution Inactivation Date (DIN) O rep S15.4.8.13 | 0537 - Institution

    stf_14 : list[CE] | None
        STF.14 - Backup Person ID (CE) O rep S15.4.8.14

    stf_15 : list[str] | None
        STF.15 - E-Mail Address (ST) O rep S15.4.8.15

    stf_16 : CE | None
        STF.16 - Preferred Method of Contact (CE) O S11.6.3.6 | 0185 - Preferred method of contact

    stf_17 : CE | None
        STF.17 - Marital Status (CE) O S3.4.2.16 | 0002 - Marital Status

    stf_18 : str | None
        STF.18 - Job Title (ST) O S6.5.5.49

    stf_19 : JCC | None
        STF.19 - Job Code/Class (JCC) O S6.5.5.50

    stf_20 : CE | None
        STF.20 - Employment Status Code (CE) O S15.4.5.10 | 0066 - Employment Status

    stf_21 : str | None
        STF.21 - Additional Insured on Auto (ID) O S15.4.8.21 | 0136 - Yes/no indicator

    stf_22 : DLN | None
        STF.22 - Driver's License Number - Staff (DLN) O S15.4.8.22

    stf_23 : str | None
        STF.23 - Copy Auto Ins (ID) O S15.4.8.23 | 0136 - Yes/no indicator

    stf_24 : str | None
        STF.24 - Auto Ins. Expires (DT) O S15.4.8.24

    stf_25 : str | None
        STF.25 - Date Last DMV Review (DT) O S15.4.8.25

    stf_26 : str | None
        STF.26 - Date Next DMV Review (DT) O S15.4.8.26

    stf_27 : CE | None
        STF.27 - Race (CE) O S3.4.2.10 | 0005 - Race

    stf_28 : CE | None
        STF.28 - Ethnic Group (CE) O S3.4.2.22 | 0189 - Ethnic Group

    stf_29 : str | None
        STF.29 - Re-activation Approval Indicator (ID) O S15.4.8.29 | 0136 - Yes/no indicator

    stf_30 : list[CE] | None
        STF.30 - Citizenship (CE) O rep S3.4.2.26 | 0171 - Citizenship

    stf_31 : TS | None
        STF.31 - Death Date and Time (TS) O S15.4.8.31

    stf_32 : str | None
        STF.32 - Death Indicator (ID) O S15.4.8.32 | 0136 - Yes/no indicator

    stf_33 : CWE | None
        STF.33 - Institution Relationship Type Code (CWE) O S15.4.8.33 | 0538 - Institution Relationship Type

    stf_34 : DR | None
        STF.34 - Institution Relationship Period (DR) O S15.4.8.34

    stf_35 : str | None
        STF.35 - Expected Return Date (DT) O S15.4.8.35

    stf_36 : list[CWE] | None
        STF.36 - Cost Center Code (CWE) O rep S15.4.8.36 | 0539 - Cost Center Code

    stf_37 : str | None
        STF.37 - Generic Classification Indicator (ID) O S15.4.8.37 | 0136 - Yes/no indicator

    stf_38 : CWE | None
        STF.38 - Inactive Reason Code (CWE) O S15.4.8.38 | 0540 - Inactive Reason Code
    """

    stf_1: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_1",
            "primary_key_value_stf",
            "STF.1",
        ),
        serialization_alias="STF.1",
        title="Primary Key Value - STF",
        description="C | Item #00671 | Table 9999 - no table for CE",
    )

    stf_2: Optional[List[CX]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_2",
            "staff_identifier_list",
            "STF.2",
        ),
        serialization_alias="STF.2",
        title="Staff Identifier List",
        description="O | Item #00672",
    )

    stf_3: Optional[List[XPN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_3",
            "staff_name",
            "STF.3",
        ),
        serialization_alias="STF.3",
        title="Staff Name",
        description="O | Item #00673",
    )

    stf_4: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_4",
            "staff_type",
            "STF.4",
        ),
        serialization_alias="STF.4",
        title="Staff Type",
        description="O | Item #00674 | Table 0182 - Staff type | LEN:2",
    )

    stf_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_5",
            "administrative_sex",
            "STF.5",
        ),
        serialization_alias="STF.5",
        title="Administrative Sex",
        description="O | Item #00111 | Table 0001 - Administrative Sex | LEN:1",
    )

    stf_6: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_6",
            "date_time_of_birth",
            "STF.6",
        ),
        serialization_alias="STF.6",
        title="Date/Time of Birth",
        description="O | Item #00110",
    )

    stf_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_7",
            "active_inactive_flag",
            "STF.7",
        ),
        serialization_alias="STF.7",
        title="Active/Inactive Flag",
        description="O | Item #00675 | Table 0183 - Active/Inactive | LEN:1",
    )

    stf_8: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_8",
            "department",
            "STF.8",
        ),
        serialization_alias="STF.8",
        title="Department",
        description="O | Item #00676 | Table 0184 - Department",
    )

    stf_9: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_9",
            "hospital_service_stf",
            "STF.9",
        ),
        serialization_alias="STF.9",
        title="Hospital Service - STF",
        description="O | Item #00677 | Table 0069 - Hospital Service",
    )

    stf_10: Optional[List[XTN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_10",
            "phone",
            "STF.10",
        ),
        serialization_alias="STF.10",
        title="Phone",
        description="O | Item #00678",
    )

    stf_11: Optional[List[XAD]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_11",
            "office_home_address_birthplace",
            "STF.11",
        ),
        serialization_alias="STF.11",
        title="Office/Home Address/Birthplace",
        description="O | Item #00679",
    )

    stf_12: Optional[List[DIN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_12",
            "institution_activation_date",
            "STF.12",
        ),
        serialization_alias="STF.12",
        title="Institution Activation Date",
        description="O | Item #00680 | Table 0537 - Institution",
    )

    stf_13: Optional[List[DIN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_13",
            "institution_inactivation_date",
            "STF.13",
        ),
        serialization_alias="STF.13",
        title="Institution Inactivation Date",
        description="O | Item #00681 | Table 0537 - Institution",
    )

    stf_14: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_14",
            "backup_person_id",
            "STF.14",
        ),
        serialization_alias="STF.14",
        title="Backup Person ID",
        description="O | Item #00682",
    )

    stf_15: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_15",
            "e_mail_address",
            "STF.15",
        ),
        serialization_alias="STF.15",
        title="E-Mail Address",
        description="O | Item #00683 | LEN:40",
    )

    stf_16: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_16",
            "preferred_method_of_contact",
            "STF.16",
        ),
        serialization_alias="STF.16",
        title="Preferred Method of Contact",
        description=(
            "O | Item #00684 | Table 0185 - Preferred method of contact"
        ),
    )

    stf_17: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_17",
            "marital_status",
            "STF.17",
        ),
        serialization_alias="STF.17",
        title="Marital Status",
        description="O | Item #00119 | Table 0002 - Marital Status",
    )

    stf_18: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_18",
            "job_title",
            "STF.18",
        ),
        serialization_alias="STF.18",
        title="Job Title",
        description="O | Item #00785 | LEN:20",
    )

    stf_19: Optional[JCC] = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_19",
            "job_code_class",
            "STF.19",
        ),
        serialization_alias="STF.19",
        title="Job Code/Class",
        description="O | Item #00786",
    )

    stf_20: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_20",
            "employment_status_code",
            "STF.20",
        ),
        serialization_alias="STF.20",
        title="Employment Status Code",
        description="O | Item #01276 | Table 0066 - Employment Status",
    )

    stf_21: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_21",
            "additional_insured_on_auto",
            "STF.21",
        ),
        serialization_alias="STF.21",
        title="Additional Insured on Auto",
        description="O | Item #01275 | Table 0136 - Yes/no indicator | LEN:1",
    )

    stf_22: Optional[DLN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_22",
            "driver_s_license_number_staff",
            "STF.22",
        ),
        serialization_alias="STF.22",
        title="Driver's License Number - Staff",
        description="O | Item #01302",
    )

    stf_23: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_23",
            "copy_auto_ins",
            "STF.23",
        ),
        serialization_alias="STF.23",
        title="Copy Auto Ins",
        description="O | Item #01229 | Table 0136 - Yes/no indicator | LEN:1",
    )

    stf_24: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_24",
            "auto_ins_expires",
            "STF.24",
        ),
        serialization_alias="STF.24",
        title="Auto Ins. Expires",
        description="O | Item #01232 | LEN:8",
    )

    stf_25: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_25",
            "date_last_dmv_review",
            "STF.25",
        ),
        serialization_alias="STF.25",
        title="Date Last DMV Review",
        description="O | Item #01298 | LEN:8",
    )

    stf_26: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_26",
            "date_next_dmv_review",
            "STF.26",
        ),
        serialization_alias="STF.26",
        title="Date Next DMV Review",
        description="O | Item #01234 | LEN:8",
    )

    stf_27: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_27",
            "race",
            "STF.27",
        ),
        serialization_alias="STF.27",
        title="Race",
        description="O | Item #00113 | Table 0005 - Race",
    )

    stf_28: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_28",
            "ethnic_group",
            "STF.28",
        ),
        serialization_alias="STF.28",
        title="Ethnic Group",
        description="O | Item #00125 | Table 0189 - Ethnic Group",
    )

    stf_29: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_29",
            "re_activation_approval_indicator",
            "STF.29",
        ),
        serialization_alias="STF.29",
        title="Re-activation Approval Indicator",
        description="O | Item #01596 | Table 0136 - Yes/no indicator | LEN:1",
    )

    stf_30: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_30",
            "citizenship",
            "STF.30",
        ),
        serialization_alias="STF.30",
        title="Citizenship",
        description="O | Item #00129 | Table 0171 - Citizenship",
    )

    stf_31: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_31",
            "death_date_and_time",
            "STF.31",
        ),
        serialization_alias="STF.31",
        title="Death Date and Time",
        description="O | Item #01886",
    )

    stf_32: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_32",
            "death_indicator",
            "STF.32",
        ),
        serialization_alias="STF.32",
        title="Death Indicator",
        description="O | Item #01887 | Table 0136 - Yes/no indicator | LEN:1",
    )

    stf_33: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_33",
            "institution_relationship_type_code",
            "STF.33",
        ),
        serialization_alias="STF.33",
        title="Institution Relationship Type Code",
        description=(
            "O | Item #01888 | Table 0538 - Institution Relationship Type"
        ),
    )

    stf_34: Optional[DR] = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_34",
            "institution_relationship_period",
            "STF.34",
        ),
        serialization_alias="STF.34",
        title="Institution Relationship Period",
        description="O | Item #01889",
    )

    stf_35: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_35",
            "expected_return_date",
            "STF.35",
        ),
        serialization_alias="STF.35",
        title="Expected Return Date",
        description="O | Item #01890 | LEN:8",
    )

    stf_36: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_36",
            "cost_center_code",
            "STF.36",
        ),
        serialization_alias="STF.36",
        title="Cost Center Code",
        description="O | Item #01891 | Table 0539 - Cost Center Code",
    )

    stf_37: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_37",
            "generic_classification_indicator",
            "STF.37",
        ),
        serialization_alias="STF.37",
        title="Generic Classification Indicator",
        description="O | Item #01892 | Table 0136 - Yes/no indicator | LEN:1",
    )

    stf_38: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_38",
            "inactive_reason_code",
            "STF.38",
        ),
        serialization_alias="STF.38",
        title="Inactive Reason Code",
        description="O | Item #01893 | Table 0540 - Inactive Reason Code",
    )

    @field_validator("stf_24", "stf_25", "stf_26", "stf_35", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        if not _RE_DT.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    model_config = ConfigDict(populate_by_name=True)
