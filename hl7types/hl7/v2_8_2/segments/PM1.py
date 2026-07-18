"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: PM1
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE
from ..datatypes.CX import CX
from ..datatypes.XAD import XAD
from ..datatypes.XON import XON
from ..datatypes.XPN import XPN
from ..datatypes.XTN import XTN

_RE_DT = re.compile(r'(\d{4}([01]\d(\d{2})?)?)?')


class PM1(HL7Model):
    """Payer Master File (S8.8.17).

    Attributes
    ----------
    pm1_1 : CWE
        PM1.1 - Health Plan ID (CWE) R S6.5.1.14 | 0072 - Insurance Plan ID

    pm1_2 : list[CX]
        PM1.2 - Insurance Company ID (CX) R rep S6.5.6.3

    pm1_3 : list[XON] | None
        PM1.3 - Insurance Company Name (XON) O rep S6.5.6.4

    pm1_4 : list[XAD] | None
        PM1.4 - Insurance Company Address (XAD) O rep S6.5.6.5

    pm1_5 : list[XPN] | None
        PM1.5 - Insurance Co Contact Person (XPN) O rep S6.5.6.6

    pm1_6 : list[XTN] | None
        PM1.6 - Insurance Co Phone Number (XTN) O rep S6.5.6.7

    pm1_7 : str | None
        PM1.7 - Group Number (ST) O S6.5.6.8

    pm1_8 : list[XON] | None
        PM1.8 - Group Name (XON) O rep S6.5.6.9

    pm1_9 : str | None
        PM1.9 - Plan Effective Date (DT) O S6.5.6.12

    pm1_10 : str | None
        PM1.10 - Plan Expiration Date (DT) O S6.5.6.13

    pm1_11 : str | None
        PM1.11 - Patient DOB Required (ID) O S8.8.17.11 | 0136 - Yes/no Indicator

    pm1_12 : str | None
        PM1.12 - Patient Gender Required (ID) O S8.8.17.12 | 0136 - Yes/no Indicator

    pm1_13 : str | None
        PM1.13 - Patient Relationship Required (ID) O S8.8.17.13 | 0136 - Yes/no Indicator

    pm1_14 : str | None
        PM1.14 - Patient Signature Required (ID) O S8.8.17.14 | 0136 - Yes/no Indicator

    pm1_15 : str | None
        PM1.15 - Diagnosis Required (ID) O S8.8.17.15 | 0136 - Yes/no Indicator

    pm1_16 : str | None
        PM1.16 - Service Required (ID) O S8.8.17.16 | 0136 - Yes/no Indicator

    pm1_17 : str | None
        PM1.17 - Patient Name Required (ID) O S8.8.17.17 | 0136 - Yes/no Indicator

    pm1_18 : str | None
        PM1.18 - Patient Address Required (ID) O S8.8.17.18 | 0136 - Yes/no Indicator

    pm1_19 : str | None
        PM1.19 - Subscribers Name Required (ID) O S8.8.17.19 | 0136 - Yes/no Indicator

    pm1_20 : str | None
        PM1.20 - Workman's Comp Indicator (ID) O S8.8.17.20 | 0136 - Yes/no Indicator

    pm1_21 : str | None
        PM1.21 - Bill Type Required (ID) O S8.8.17.21 | 0136 - Yes/no Indicator

    pm1_22 : str | None
        PM1.22 - Commercial Carrier Name and Address Required (ID) O S8.8.17.22 | 0136 - Yes/no Indicator

    pm1_23 : str | None
        PM1.23 - Policy Number Pattern (ST) O S8.8.17.23

    pm1_24 : str | None
        PM1.24 - Group Number Pattern (ST) O S8.8.17.24
    """

    pm1_1: CWE = Field(
        validation_alias=AliasChoices(
            "pm1_1",
            "health_plan_id",
            "PM1.1",
        ),
        serialization_alias="PM1.1",
        title="Health Plan ID",
        description="R | Item #00368 | Table 0072 - Insurance Plan ID",
    )

    pm1_2: List[CX] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "pm1_2",
            "insurance_company_id",
            "PM1.2",
        ),
        serialization_alias="PM1.2",
        title="Insurance Company ID",
        description="R | Item #00428",
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
        description="O | Item #00429",
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
        description="O | Item #00430",
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
        description="O | Item #00431",
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
        description="O | Item #00432",
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
        description="O | Item #00433",
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
        description="O | Item #00434",
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
        description="O | Item #00437",
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
        description="O | Item #00438",
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
        description="O | Item #03454 | Table 0136 - Yes/no Indicator",
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
        description="O | Item #03455 | Table 0136 - Yes/no Indicator",
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
        description="O | Item #03456 | Table 0136 - Yes/no Indicator",
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
        description="O | Item #03457 | Table 0136 - Yes/no Indicator",
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
        description="O | Item #03458 | Table 0136 - Yes/no Indicator",
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
        description="O | Item #03459 | Table 0136 - Yes/no Indicator",
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
        description="O | Item #03460 | Table 0136 - Yes/no Indicator",
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
        description="O | Item #03461 | Table 0136 - Yes/no Indicator",
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
        description="O | Item #03462 | Table 0136 - Yes/no Indicator",
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
        description="O | Item #03463 | Table 0136 - Yes/no Indicator",
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
        description="O | Item #03464 | Table 0136 - Yes/no Indicator",
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
        description="O | Item #03465 | Table 0136 - Yes/no Indicator",
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
        description="O | Item #03466",
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
        description="O | Item #03467",
    )

    @field_validator("pm1_9", "pm1_10", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        if not _RE_DT.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    model_config = ConfigDict(populate_by_name=True)
