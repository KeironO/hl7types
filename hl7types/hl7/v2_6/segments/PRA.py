"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: PRA
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CWE import CWE
from ..datatypes.PIP import PIP
from ..datatypes.PLN import PLN
from ..datatypes.SPD import SPD


class PRA(BaseModel):
    """HL7 v2 PRA segment."""

    pra_1: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pra_1",
            "primary_key_value_pra",
            "PRA.1",
        ),
        serialization_alias="PRA.1",
        title="Primary Key Value - PRA",
        description="Item #685 | Table HL79999",
    )

    pra_2: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pra_2",
            "practitioner_group",
            "PRA.2",
        ),
        serialization_alias="PRA.2",
        title="Practitioner Group",
        description="Item #686 | Table HL70358",
    )

    pra_3: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pra_3",
            "practitioner_category",
            "PRA.3",
        ),
        serialization_alias="PRA.3",
        title="Practitioner Category",
        description="Item #687 | Table HL70186",
    )

    pra_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pra_4",
            "provider_billing",
            "PRA.4",
        ),
        serialization_alias="PRA.4",
        title="Provider Billing",
        description="Item #688 | Table HL70187",
    )

    pra_5: Optional[List[SPD]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pra_5",
            "specialty",
            "PRA.5",
        ),
        serialization_alias="PRA.5",
        title="Specialty",
        description="Item #689 | Table HL70337",
    )

    pra_6: Optional[List[PLN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pra_6",
            "practitioner_id_numbers",
            "PRA.6",
        ),
        serialization_alias="PRA.6",
        title="Practitioner ID Numbers",
        description="Item #690 | Table HL70338",
    )

    pra_7: Optional[List[PIP]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pra_7",
            "privileges",
            "PRA.7",
        ),
        serialization_alias="PRA.7",
        title="Privileges",
        description="Item #691",
    )

    pra_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pra_8",
            "date_entered_practice",
            "PRA.8",
        ),
        serialization_alias="PRA.8",
        title="Date Entered Practice",
        description="Item #1296",
    )

    pra_9: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pra_9",
            "institution",
            "PRA.9",
        ),
        serialization_alias="PRA.9",
        title="Institution",
        description="Item #1613 | Table HL70537",
    )

    pra_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pra_10",
            "date_left_practice",
            "PRA.10",
        ),
        serialization_alias="PRA.10",
        title="Date Left Practice",
        description="Item #1348",
    )

    pra_11: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pra_11",
            "government_reimbursement_billing_eligibility",
            "PRA.11",
        ),
        serialization_alias="PRA.11",
        title="Government Reimbursement Billing Eligibility",
        description="Item #1388 | Table HL70401",
    )

    pra_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pra_12",
            "set_id_pra",
            "PRA.12",
        ),
        serialization_alias="PRA.12",
        title="Set ID - PRA",
        description="Item #1616",
    )

    model_config = {"populate_by_name": True}
