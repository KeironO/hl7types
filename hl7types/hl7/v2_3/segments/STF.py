"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: STF
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.AD import AD
from ..datatypes.CE import CE
from ..datatypes.DLN import DLN
from ..datatypes.JCC import JCC
from ..datatypes.TS import TS
from ..datatypes.XPN import XPN


class STF(BaseModel):
    """HL7 v2 STF segment."""

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

    stf_2: list[CE] | None = Field(
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

    stf_3: XPN | None = Field(
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

    stf_4: list[str] | None = Field(
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

    stf_5: str | None = Field(
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

    stf_6: TS | None = Field(
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

    stf_7: str | None = Field(
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

    stf_8: list[CE] | None = Field(
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

    stf_9: list[CE] | None = Field(
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

    stf_10: list[str] | None = Field(
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

    stf_11: list[AD] | None = Field(
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

    stf_12: list[str] | None = Field(
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

    stf_13: list[str] | None = Field(
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

    stf_14: list[CE] | None = Field(
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

    stf_15: list[str] | None = Field(
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

    stf_16: CE | None = Field(
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

    stf_17: list[str] | None = Field(
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

    stf_18: str | None = Field(
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

    stf_19: JCC | None = Field(
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

    stf_20: str | None = Field(
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

    stf_21: str | None = Field(
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

    stf_22: DLN | None = Field(
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

    stf_23: str | None = Field(
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

    stf_24: str | None = Field(
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

    stf_25: str | None = Field(
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

    stf_26: str | None = Field(
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
