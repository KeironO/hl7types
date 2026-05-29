"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: STF
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.AD import AD
from ..datatypes.CE import CE
from ..datatypes.DLN import DLN
from ..datatypes.JCC import JCC
from ..datatypes.TS import TS
from ..datatypes.XPN import XPN


class STF(BaseModel):
    """HL7 v2 STF segment.

    Attributes
    ----------
    stf_1 : CE
        STF.1 (req) - STF - Primary Key Value (CE)

    stf_2 : list[CE] | None
        STF.2 (opt, rep) - Staff ID Code (CE)

    stf_3 : XPN | None
        STF.3 (opt) - Staff Name (XPN)

    stf_4 : list[str] | None
        STF.4 (opt, rep) - Staff Type (ID)

    stf_5 : str | None
        STF.5 (opt) - Sex (IS)

    stf_6 : TS | None
        STF.6 (opt) - Date of Birth (TS)

    stf_7 : str | None
        STF.7 (opt) - Active/Inactive Flag (ID)

    stf_8 : list[CE] | None
        STF.8 (opt, rep) - Department (CE)

    stf_9 : list[CE] | None
        STF.9 (opt, rep) - Service (CE)

    stf_10 : list[str] | None
        STF.10 (opt, rep) - Phone (TN)

    stf_11 : list[AD] | None
        STF.11 (opt, rep) - Office/Home Address (AD)

    stf_12 : list[str] | None
        STF.12 (opt, rep) - Activation Date (CM)

    stf_13 : list[str] | None
        STF.13 (opt, rep) - Inactivation Date (CM)

    stf_14 : list[CE] | None
        STF.14 (opt, rep) - Backup Person ID (CE)

    stf_15 : list[str] | None
        STF.15 (opt, rep) - E-mail Address (ST)

    stf_16 : CE | None
        STF.16 (opt) - Preferred Method of Contact (CE)

    stf_17 : list[str] | None
        STF.17 (opt, rep) - Marital Status (IS)

    stf_18 : str | None
        STF.18 (opt) - Job Title (ST)

    stf_19 : JCC | None
        STF.19 (opt) - Job Code/Class (JCC)

    stf_20 : str | None
        STF.20 (opt) - Employment Status (IS)

    stf_21 : str | None
        STF.21 (opt) - Additional Insured on Auto (ID)

    stf_22 : DLN | None
        STF.22 (opt) - Driver's License Number (DLN)

    stf_23 : str | None
        STF.23 (opt) - Copy Auto Ins (ID)

    stf_24 : str | None
        STF.24 (opt) - Auto Ins. Expires (DT)

    stf_25 : str | None
        STF.25 (opt) - Date Last DMV Review (DT)

    stf_26 : str | None
        STF.26 (opt) - Date Next DMV Review (DT)
    """

    stf_1: CE = Field(
        default=...,
        validation_alias=AliasChoices(
            "stf_1",
            "stf_primary_key_value",
            "STF.1",
        ),
        serialization_alias="STF.1",
        title="STF - Primary Key Value",
        description="Item #671",
    )

    stf_2: Optional[List[CE]] = Field(
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

    stf_3: Optional[XPN] = Field(
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
            "sex",
            "STF.5",
        ),
        serialization_alias="STF.5",
        title="Sex",
        description="Item #111 | Table HL70001",
    )

    stf_6: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_6",
            "date_of_birth",
            "STF.6",
        ),
        serialization_alias="STF.6",
        title="Date of Birth",
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
            "service",
            "STF.9",
        ),
        serialization_alias="STF.9",
        title="Service",
        description="Item #677",
    )

    stf_10: Optional[List[str]] = Field(
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

    stf_11: Optional[List[AD]] = Field(
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

    stf_12: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_12",
            "activation_date",
            "STF.12",
        ),
        serialization_alias="STF.12",
        title="Activation Date",
        description="Item #680",
    )

    stf_13: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_13",
            "inactivation_date",
            "STF.13",
        ),
        serialization_alias="STF.13",
        title="Inactivation Date",
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
        title="E-mail Address",
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

    stf_17: Optional[List[str]] = Field(
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
        description="Item #786",
    )

    stf_20: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_20",
            "employment_status",
            "STF.20",
        ),
        serialization_alias="STF.20",
        title="Employment Status",
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
        title="Additional Insured on Auto",
        description="Item #1275 | Table HL70136",
    )

    stf_22: Optional[DLN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_22",
            "driver_s_license_number",
            "STF.22",
        ),
        serialization_alias="STF.22",
        title="Driver's License Number",
        description="Item #123",
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
        description="Item #1297",
    )

    model_config = {"populate_by_name": True}
