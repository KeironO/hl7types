"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: AUT
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CP import CP
from ..datatypes.CQ import CQ
from ..datatypes.CWE import CWE
from ..datatypes.EI import EI
from ..datatypes.MO import MO
from ..datatypes.XCN import XCN
from ..datatypes.XON import XON
from ..datatypes.XTN import XTN


class AUT(BaseModel):
    """HL7 v2 AUT segment."""

    aut_1: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_1",
            "authorizing_payor_plan_id",
            "AUT.1",
        ),
        serialization_alias="AUT.1",
        title="Authorizing Payor, Plan ID",
        description="Item #1146 | Table HL70072",
    )

    aut_2: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "aut_2",
            "authorizing_payor_company_id",
            "AUT.2",
        ),
        serialization_alias="AUT.2",
        title="Authorizing Payor, Company ID",
        description="Item #1147 | Table HL70285",
    )

    aut_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_3",
            "authorizing_payor_company_name",
            "AUT.3",
        ),
        serialization_alias="AUT.3",
        title="Authorizing Payor, Company Name",
        description="Item #1148",
    )

    aut_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_4",
            "authorization_effective_date",
            "AUT.4",
        ),
        serialization_alias="AUT.4",
        title="Authorization Effective Date",
        description="Item #1149",
    )

    aut_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_5",
            "authorization_expiration_date",
            "AUT.5",
        ),
        serialization_alias="AUT.5",
        title="Authorization Expiration Date",
        description="Item #1150",
    )

    aut_6: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_6",
            "authorization_identifier",
            "AUT.6",
        ),
        serialization_alias="AUT.6",
        title="Authorization Identifier",
        description="Item #1151",
    )

    aut_7: Optional[CP] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_7",
            "reimbursement_limit",
            "AUT.7",
        ),
        serialization_alias="AUT.7",
        title="Reimbursement Limit",
        description="Item #1152",
    )

    aut_8: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_8",
            "requested_number_of_treatments",
            "AUT.8",
        ),
        serialization_alias="AUT.8",
        title="Requested Number of Treatments",
        description="Item #1153",
    )

    aut_9: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_9",
            "authorized_number_of_treatments",
            "AUT.9",
        ),
        serialization_alias="AUT.9",
        title="Authorized Number of Treatments",
        description="Item #1154",
    )

    aut_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_10",
            "process_date",
            "AUT.10",
        ),
        serialization_alias="AUT.10",
        title="Process Date",
        description="Item #1145",
    )

    aut_11: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_11",
            "requested_discipline_s",
            "AUT.11",
        ),
        serialization_alias="AUT.11",
        title="Requested Discipline(s)",
        description="Item #2375",
    )

    aut_12: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_12",
            "authorized_discipline_s",
            "AUT.12",
        ),
        serialization_alias="AUT.12",
        title="Authorized Discipline(s)",
        description="Item #2376",
    )

    aut_13: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "aut_13",
            "authorization_referral_type",
            "AUT.13",
        ),
        serialization_alias="AUT.13",
        title="Authorization Referral Type",
        description="Item #3413",
    )

    aut_14: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_14",
            "approval_status",
            "AUT.14",
        ),
        serialization_alias="AUT.14",
        title="Approval Status",
        description="Item #3414",
    )

    aut_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_15",
            "planned_treatment_stop_date",
            "AUT.15",
        ),
        serialization_alias="AUT.15",
        title="Planned Treatment Stop Date",
        description="Item #3415",
    )

    aut_16: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_16",
            "clinical_service",
            "AUT.16",
        ),
        serialization_alias="AUT.16",
        title="Clinical Service",
        description="Item #3416",
    )

    aut_17: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_17",
            "reason_text",
            "AUT.17",
        ),
        serialization_alias="AUT.17",
        title="Reason Text",
        description="Item #3417",
    )

    aut_18: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_18",
            "number_of_authorized_treatments_units",
            "AUT.18",
        ),
        serialization_alias="AUT.18",
        title="Number of Authorized Treatments/Units",
        description="Item #3418",
    )

    aut_19: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_19",
            "number_of_used_treatments_units",
            "AUT.19",
        ),
        serialization_alias="AUT.19",
        title="Number of Used Treatments/Units",
        description="Item #3419",
    )

    aut_20: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_20",
            "number_of_schedule_treatments_units",
            "AUT.20",
        ),
        serialization_alias="AUT.20",
        title="Number of Schedule Treatments/Units",
        description="Item #3420",
    )

    aut_21: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_21",
            "encounter_type",
            "AUT.21",
        ),
        serialization_alias="AUT.21",
        title="Encounter Type",
        description="Item #3421",
    )

    aut_22: Optional[MO] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_22",
            "remaining_benefit_amount",
            "AUT.22",
        ),
        serialization_alias="AUT.22",
        title="Remaining Benefit Amount",
        description="Item #3422",
    )

    aut_23: Optional[XON] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_23",
            "authorized_provider",
            "AUT.23",
        ),
        serialization_alias="AUT.23",
        title="Authorized Provider",
        description="Item #3423",
    )

    aut_24: Optional[XCN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_24",
            "authorized_health_professional",
            "AUT.24",
        ),
        serialization_alias="AUT.24",
        title="Authorized Health Professional",
        description="Item #3424",
    )

    aut_25: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_25",
            "source_text",
            "AUT.25",
        ),
        serialization_alias="AUT.25",
        title="Source Text",
        description="Item #3425",
    )

    aut_26: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_26",
            "source_date",
            "AUT.26",
        ),
        serialization_alias="AUT.26",
        title="Source Date",
        description="Item #3426",
    )

    aut_27: Optional[XTN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_27",
            "source_phone",
            "AUT.27",
        ),
        serialization_alias="AUT.27",
        title="Source Phone",
        description="Item #3427",
    )

    aut_28: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_28",
            "comment",
            "AUT.28",
        ),
        serialization_alias="AUT.28",
        title="Comment",
        description="Item #3428",
    )

    aut_29: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_29",
            "action_code",
            "AUT.29",
        ),
        serialization_alias="AUT.29",
        title="Action Code",
        description="Item #3429 | Table HL70206",
    )

    model_config = {"populate_by_name": True}
