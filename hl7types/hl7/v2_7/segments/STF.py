"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: STF
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CWE import CWE
from ..datatypes.CX import CX
from ..datatypes.DIN import DIN
from ..datatypes.DLN import DLN
from ..datatypes.DR import DR
from ..datatypes.ED import ED
from ..datatypes.JCC import JCC
from ..datatypes.XAD import XAD
from ..datatypes.XPN import XPN
from ..datatypes.XTN import XTN


class STF(BaseModel):
    """HL7 v2 STF segment."""

    stf_1: Optional[CWE] = Field(
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
            "staff_identifier_list",
            "STF.2",
        ),
        serialization_alias="STF.2",
        title="Staff Identifier List",
        description="Item #672 | Table HL70061",
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

    stf_4: Optional[List[CWE]] = Field(
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

    stf_5: Optional[CWE] = Field(
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

    stf_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_6",
            "date_time_of_birth",
            "STF.6",
        ),
        serialization_alias="STF.6",
        title="Date/Time of Birth",
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

    stf_8: Optional[List[CWE]] = Field(
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

    stf_9: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_9",
            "hospital_service_stf",
            "STF.9",
        ),
        serialization_alias="STF.9",
        title="Hospital Service - STF",
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
            "office_home_address_birthplace",
            "STF.11",
        ),
        serialization_alias="STF.11",
        title="Office/Home Address/Birthplace",
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
        description="Item #680 | Table HL70537",
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
        description="Item #681 | Table HL70537",
    )

    stf_14: Optional[List[CWE]] = Field(
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

    stf_16: Optional[CWE] = Field(
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

    stf_17: Optional[CWE] = Field(
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

    stf_20: Optional[CWE] = Field(
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
        title="Additional Insured on Auto",
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
        title="Auto Ins Expires",
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

    stf_27: Optional[CWE] = Field(
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

    stf_28: Optional[CWE] = Field(
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

    stf_30: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_30",
            "citizenship",
            "STF.30",
        ),
        serialization_alias="STF.30",
        title="Citizenship",
        description="Item #129 | Table HL70171",
    )

    stf_31: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_31",
            "date_time_of_death",
            "STF.31",
        ),
        serialization_alias="STF.31",
        title="Date/Time of Death",
        description="Item #1886",
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
        description="Item #1887 | Table HL70136",
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
        description="Item #1888 | Table HL70538",
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
        description="Item #1889",
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
        description="Item #1890",
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
        description="Item #1891 | Table HL70539",
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
        description="Item #1892 | Table HL70136",
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
        description="Item #1893 | Table HL70540",
    )

    stf_39: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_39",
            "generic_resource_type_or_category",
            "STF.39",
        ),
        serialization_alias="STF.39",
        title="Generic resource type or category",
        description="Item #2184 | Table HL70771",
    )

    stf_40: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_40",
            "religion",
            "STF.40",
        ),
        serialization_alias="STF.40",
        title="Religion",
        description="Item #120 | Table HL70006",
    )

    stf_41: Optional[ED] = Field(
        default=None,
        validation_alias=AliasChoices(
            "stf_41",
            "signature",
            "STF.41",
        ),
        serialization_alias="STF.41",
        title="Signature",
        description="Item #1861",
    )

    model_config = {"populate_by_name": True}
