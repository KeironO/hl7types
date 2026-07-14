"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: STF
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.CX import CX
from ..datatypes.DIN import DIN
from ..datatypes.DLN import DLN
from ..datatypes.JCC import JCC
from ..datatypes.TS import TS
from ..datatypes.XAD import XAD
from ..datatypes.XPN import XPN
from ..datatypes.XTN import XTN


class STF(HL7Model):
    """Staff Identification (S15.4.6).

    Attributes
    ----------
    stf_1 : CE | None
        STF.1 (opt) - Primary Key Value - STF (CE) S15.4.6.1 | 9999 - for unknown CE data elements

    stf_2 : list[CX] | None
        STF.2 (opt, rep) - Staff ID Code (CX) S15.4.6.2

    stf_3 : list[XPN] | None
        STF.3 (opt, rep) - Staff Name (XPN) S15.4.6.3

    stf_4 : list[str] | None
        STF.4 (opt, rep) - Staff Type (IS) S15.4.6.4 | 0182 - Staff type

    stf_5 : str | None
        STF.5 (opt) - Administrative Sex (IS) S15.4.6.5 | 0001 - Administrative sex

    stf_6 : TS | None
        STF.6 (opt) - Date/Time Of Birth (TS) S15.4.6.6

    stf_7 : str | None
        STF.7 (opt) - Active/Inactive Flag (ID) S15.4.6.7 | 0183 - Active/inactive

    stf_8 : list[CE] | None
        STF.8 (opt, rep) - Department (CE) S15.4.6.8 | 0184 - Department

    stf_9 : list[CE] | None
        STF.9 (opt, rep) - Hospital Service (CE) S15.4.6.9 | 0069 - Hospital service

    stf_10 : list[XTN] | None
        STF.10 (opt, rep) - Phone (XTN) S15.4.6.10

    stf_11 : list[XAD] | None
        STF.11 (opt, rep) - Office/Home Address (XAD) S15.4.6.11

    stf_12 : list[DIN] | None
        STF.12 (opt, rep) - Institution Activation Date (DIN) S15.4.6.12

    stf_13 : list[DIN] | None
        STF.13 (opt, rep) - Institution Inactivation Date (DIN) S15.4.6.13

    stf_14 : list[CE] | None
        STF.14 (opt, rep) - Backup Person ID (CE) S15.4.6.14

    stf_15 : list[str] | None
        STF.15 (opt, rep) - E-Mail Address (ST) S15.4.6.15

    stf_16 : CE | None
        STF.16 (opt) - Preferred Method of Contact (CE) S15.4.6.16 | 0185 - Preferred method of contact

    stf_17 : CE | None
        STF.17 (opt) - Marital Status (CE) S15.4.6.17 | 0002 - Marital status

    stf_18 : str | None
        STF.18 (opt) - Job Title (ST) S15.4.6.18

    stf_19 : JCC | None
        STF.19 (opt) - Job Code/Class (JCC) S15.4.6.19 | 0327 - Job code/class

    stf_20 : CE | None
        STF.20 (opt) - Employment Status Code (CE) S15.4.6.20 | 0066 - Employment status

    stf_21 : str | None
        STF.21 (opt) - Additional Insured on  Auto (ID) S15.4.6.21 | 0136 - Yes/no indicator

    stf_22 : DLN | None
        STF.22 (opt) - Driver's License Number - Staff (DLN) S15.4.6.22

    stf_23 : str | None
        STF.23 (opt) - Copy  Auto Ins (ID) S15.4.6.23 | 0136 - Yes/no indicator

    stf_24 : str | None
        STF.24 (opt) - Auto Ins. Expires (DT) S15.4.6.24

    stf_25 : str | None
        STF.25 (opt) - Date Last DMV Review (DT) S15.4.6.25

    stf_26 : str | None
        STF.26 (opt) - Date Next DMV Review (DT) S15.4.6.26

    stf_27 : CE | None
        STF.27 (opt) - Race (CE) S15.4.6.27 | 0005 - Race

    stf_28 : CE | None
        STF.28 (opt) - Ethnic Group (CE) S15.4.6.28 | 0189 - Ethnic group

    stf_29 : str | None
        STF.29 (opt) - Re-activation Approval Indicator (ID) S15.4.6.29 | 0136 - Yes/no indicator
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
        description="Item #671 | Table HL79999",
    )

    stf_2: Optional[List[CX]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_2",
            "staff_id_code",
            "STF.2",
        ),
        serialization_alias="STF.2",
        title="Staff ID Code",
        description="Item #672",
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
        description="Item #673",
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
        description="Item #674 | Table HL70182",
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
        description="Item #111 | Table HL70001",
    )

    stf_6: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_6",
            "date_time_of_birth",
            "STF.6",
        ),
        serialization_alias="STF.6",
        title="Date/Time Of Birth",
        description="Item #110",
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
        description="Item #675 | Table HL70183",
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
        description="Item #676 | Table HL70184",
    )

    stf_9: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_9",
            "hospital_service",
            "STF.9",
        ),
        serialization_alias="STF.9",
        title="Hospital Service",
        description="Item #677 | Table HL70069",
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
        description="Item #678",
    )

    stf_11: Optional[List[XAD]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_11",
            "office_home_address",
            "STF.11",
        ),
        serialization_alias="STF.11",
        title="Office/Home Address",
        description="Item #679",
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
        description="Item #680",
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
        description="Item #681",
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
        description="Item #682",
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
        description="Item #683",
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
        description="Item #684 | Table HL70185",
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
        description="Item #119 | Table HL70002",
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
        description="Item #785",
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
        description="Item #786 | Table HL70327",
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
        description="Item #1276 | Table HL70066",
    )

    stf_21: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_21",
            "additional_insured_on_auto",
            "STF.21",
        ),
        serialization_alias="STF.21",
        title="Additional Insured on  Auto",
        description="Item #1275 | Table HL70136",
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
        description="Item #1302",
    )

    stf_23: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_23",
            "copy_auto_ins",
            "STF.23",
        ),
        serialization_alias="STF.23",
        title="Copy  Auto Ins",
        description="Item #1229 | Table HL70136",
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
        description="Item #1232",
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
        description="Item #1298",
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
        description="Item #1234",
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
        description="Item #113 | Table HL70005",
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
        description="Item #125 | Table HL70189",
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
        description="Item #1596 | Table HL70136",
    )

    @field_validator("stf_24", "stf_25", "stf_26", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2})?)?)?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    model_config = {"populate_by_name": True}
