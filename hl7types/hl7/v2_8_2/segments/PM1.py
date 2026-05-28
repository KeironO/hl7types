"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: PM1
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CWE import CWE
from ..datatypes.CX import CX
from ..datatypes.XAD import XAD
from ..datatypes.XON import XON
from ..datatypes.XPN import XPN
from ..datatypes.XTN import XTN


class PM1(BaseModel):
    """HL7 v2 PM1 segment."""

    pm1_1: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "pm1_1",
            "health_plan_id",
            "PM1.1",
        ),
        serialization_alias="PM1.1",
        title="Health Plan ID",
        description="Item #368 | Table HL70072",
    )

    pm1_2: list[CX] = Field(
        default=...,
        validation_alias=AliasChoices(
            "pm1_2",
            "insurance_company_id",
            "PM1.2",
        ),
        serialization_alias="PM1.2",
        title="Insurance Company ID",
        description="Item #428",
    )

    pm1_3: list[XON] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pm1_3",
            "insurance_company_name",
            "PM1.3",
        ),
        serialization_alias="PM1.3",
        title="Insurance Company Name",
        description="Item #429",
    )

    pm1_4: list[XAD] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pm1_4",
            "insurance_company_address",
            "PM1.4",
        ),
        serialization_alias="PM1.4",
        title="Insurance Company Address",
        description="Item #430",
    )

    pm1_5: list[XPN] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pm1_5",
            "insurance_co_contact_person",
            "PM1.5",
        ),
        serialization_alias="PM1.5",
        title="Insurance Co Contact Person",
        description="Item #431",
    )

    pm1_6: list[XTN] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pm1_6",
            "insurance_co_phone_number",
            "PM1.6",
        ),
        serialization_alias="PM1.6",
        title="Insurance Co Phone Number",
        description="Item #432",
    )

    pm1_7: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pm1_7",
            "group_number",
            "PM1.7",
        ),
        serialization_alias="PM1.7",
        title="Group Number",
        description="Item #433",
    )

    pm1_8: list[XON] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pm1_8",
            "group_name",
            "PM1.8",
        ),
        serialization_alias="PM1.8",
        title="Group Name",
        description="Item #434",
    )

    pm1_9: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pm1_9",
            "plan_effective_date",
            "PM1.9",
        ),
        serialization_alias="PM1.9",
        title="Plan Effective Date",
        description="Item #437",
    )

    pm1_10: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pm1_10",
            "plan_expiration_date",
            "PM1.10",
        ),
        serialization_alias="PM1.10",
        title="Plan Expiration Date",
        description="Item #438",
    )

    pm1_11: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pm1_11",
            "patient_dob_required",
            "PM1.11",
        ),
        serialization_alias="PM1.11",
        title="Patient DOB Required",
        description="Item #3454 | Table HL70136",
    )

    pm1_12: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pm1_12",
            "patient_gender_required",
            "PM1.12",
        ),
        serialization_alias="PM1.12",
        title="Patient Gender Required",
        description="Item #3455 | Table HL70136",
    )

    pm1_13: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pm1_13",
            "patient_relationship_required",
            "PM1.13",
        ),
        serialization_alias="PM1.13",
        title="Patient Relationship Required",
        description="Item #3456 | Table HL70136",
    )

    pm1_14: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pm1_14",
            "patient_signature_required",
            "PM1.14",
        ),
        serialization_alias="PM1.14",
        title="Patient Signature Required",
        description="Item #3457 | Table HL70136",
    )

    pm1_15: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pm1_15",
            "diagnosis_required",
            "PM1.15",
        ),
        serialization_alias="PM1.15",
        title="Diagnosis Required",
        description="Item #3458 | Table HL70136",
    )

    pm1_16: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pm1_16",
            "service_required",
            "PM1.16",
        ),
        serialization_alias="PM1.16",
        title="Service Required",
        description="Item #3459 | Table HL70136",
    )

    pm1_17: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pm1_17",
            "patient_name_required",
            "PM1.17",
        ),
        serialization_alias="PM1.17",
        title="Patient Name Required",
        description="Item #3460 | Table HL70136",
    )

    pm1_18: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pm1_18",
            "patient_address_required",
            "PM1.18",
        ),
        serialization_alias="PM1.18",
        title="Patient Address Required",
        description="Item #3461 | Table HL70136",
    )

    pm1_19: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pm1_19",
            "subscribers_name_required",
            "PM1.19",
        ),
        serialization_alias="PM1.19",
        title="Subscribers Name Required",
        description="Item #3462 | Table HL70136",
    )

    pm1_20: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pm1_20",
            "workman_s_comp_indicator",
            "PM1.20",
        ),
        serialization_alias="PM1.20",
        title="Workman's Comp Indicator",
        description="Item #3463 | Table HL70136",
    )

    pm1_21: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pm1_21",
            "bill_type_required",
            "PM1.21",
        ),
        serialization_alias="PM1.21",
        title="Bill Type Required",
        description="Item #3464 | Table HL70136",
    )

    pm1_22: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pm1_22",
            "commercial_carrier_name_and_address_required",
            "PM1.22",
        ),
        serialization_alias="PM1.22",
        title="Commercial Carrier Name and Address Required",
        description="Item #3465 | Table HL70136",
    )

    pm1_23: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pm1_23",
            "policy_number_pattern",
            "PM1.23",
        ),
        serialization_alias="PM1.23",
        title="Policy Number Pattern",
        description="Item #3466",
    )

    pm1_24: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pm1_24",
            "group_number_pattern",
            "PM1.24",
        ),
        serialization_alias="PM1.24",
        title="Group Number Pattern",
        description="Item #3467",
    )

    model_config = {"populate_by_name": True}
