"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: PM1
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator

from ..datatypes.CWE import CWE
from ..datatypes.CX import CX
from ..datatypes.XAD import XAD
from ..datatypes.XON import XON
from ..datatypes.XPN import XPN
from ..datatypes.XTN import XTN


class PM1(HL7Model):
    """HL7 v2 PM1 segment.

    Attributes
    ----------
    pm1_1 : CWE
        PM1.1 (req) - Health Plan ID (CWE)

    pm1_2 : list[CX]
        PM1.2 (req, rep) - Insurance Company ID (CX)

    pm1_3 : list[XON] | None
        PM1.3 (opt, rep) - Insurance Company Name (XON)

    pm1_4 : list[XAD] | None
        PM1.4 (opt, rep) - Insurance Company Address (XAD)

    pm1_5 : list[XPN] | None
        PM1.5 (opt, rep) - Insurance Co Contact Person (XPN)

    pm1_6 : list[XTN] | None
        PM1.6 (opt, rep) - Insurance Co Phone Number (XTN)

    pm1_7 : str | None
        PM1.7 (opt) - Group Number (ST)

    pm1_8 : list[XON] | None
        PM1.8 (opt, rep) - Group Name (XON)

    pm1_9 : str | None
        PM1.9 (opt) - Plan Effective Date (DT)

    pm1_10 : str | None
        PM1.10 (opt) - Plan Expiration Date (DT)

    pm1_11 : str | None
        PM1.11 (opt) - Patient DOB Required (ID)

    pm1_12 : str | None
        PM1.12 (opt) - Patient Gender Required (ID)

    pm1_13 : str | None
        PM1.13 (opt) - Patient Relationship Required (ID)

    pm1_14 : str | None
        PM1.14 (opt) - Patient Signature Required (ID)

    pm1_15 : str | None
        PM1.15 (opt) - Diagnosis Required (ID)

    pm1_16 : str | None
        PM1.16 (opt) - Service Required (ID)

    pm1_17 : str | None
        PM1.17 (opt) - Patient Name Required (ID)

    pm1_18 : str | None
        PM1.18 (opt) - Patient Address Required (ID)

    pm1_19 : str | None
        PM1.19 (opt) - Subscribers Name Required (ID)

    pm1_20 : str | None
        PM1.20 (opt) - Workman's Comp Indicator (ID)

    pm1_21 : str | None
        PM1.21 (opt) - Bill Type Required (ID)

    pm1_22 : str | None
        PM1.22 (opt) - Commercial Carrier Name and Address Required (ID)

    pm1_23 : str | None
        PM1.23 (opt) - Policy Number Pattern (ST)

    pm1_24 : str | None
        PM1.24 (opt) - Group Number Pattern (ST)
    """

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

    pm1_2: List[CX] = Field(
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

    pm1_3: Optional[List[XON]] = Field(
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

    pm1_4: Optional[List[XAD]] = Field(
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

    pm1_5: Optional[List[XPN]] = Field(
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

    pm1_6: Optional[List[XTN]] = Field(
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

    pm1_7: Optional[str] = Field(
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

    pm1_8: Optional[List[XON]] = Field(
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

    pm1_9: Optional[str] = Field(
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

    pm1_10: Optional[str] = Field(
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

    pm1_11: Optional[str] = Field(
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

    pm1_12: Optional[str] = Field(
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

    pm1_13: Optional[str] = Field(
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

    pm1_14: Optional[str] = Field(
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

    pm1_15: Optional[str] = Field(
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

    pm1_16: Optional[str] = Field(
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

    pm1_17: Optional[str] = Field(
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

    pm1_18: Optional[str] = Field(
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

    pm1_19: Optional[str] = Field(
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

    pm1_20: Optional[str] = Field(
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

    pm1_21: Optional[str] = Field(
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

    pm1_22: Optional[str] = Field(
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

    pm1_23: Optional[str] = Field(
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

    pm1_24: Optional[str] = Field(
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

    @field_validator("pm1_9", "pm1_10", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2})?)?)?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    model_config = {"populate_by_name": True}
