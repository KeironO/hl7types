"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: PRA
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE
from ..datatypes.PIP import PIP
from ..datatypes.PLN import PLN
from ..datatypes.SPD import SPD


class PRA(HL7Model):
    """Practitioner Detail (S15.4.6).

    Attributes
    ----------
    pra_1 : CWE | None
        PRA.1 - Primary Key Value - PRA (CWE) C S15.4.6.1 | 9999 - no table for CE

    pra_2 : list[CWE] | None
        PRA.2 - Practitioner Group (CWE) O rep S15.4.6.2 | 0358 - Practitioner Group

    pra_3 : list[CWE] | None
        PRA.3 - Practitioner Category (CWE) O rep S15.4.6.3 | 0186 - Practitioner Category

    pra_4 : str | None
        PRA.4 - Provider Billing (ID) O S15.4.6.4 | 0187 - Provider Billing

    pra_5 : list[SPD] | None
        PRA.5 - Specialty (SPD) O rep S15.4.6.5 | 0337 - Certification Status

    pra_6 : list[PLN] | None
        PRA.6 - Practitioner ID Numbers (PLN) O rep S15.4.6.6 | 0338 - Practitioner ID Number Type

    pra_7 : list[PIP] | None
        PRA.7 - Privileges (PIP) O rep S15.4.6.7

    pra_8 : str | None
        PRA.8 - Date Entered Practice (DT) O S15.4.6.8

    pra_9 : CWE | None
        PRA.9 - Institution (CWE) O S15.4.6.9 | 0537 - Institution

    pra_10 : str | None
        PRA.10 - Date Left Practice (DT) O S15.4.6.10

    pra_11 : list[CWE] | None
        PRA.11 - Government Reimbursement Billing Eligibility (CWE) O rep S15.4.6.11 | 0401 - Government Reimbursement Program

    pra_12 : str | None
        PRA.12 - Set ID - PRA (SI) C S15.4.6.12
    """

    pra_1: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pra_1",
            "primary_key_value_pra",
            "PRA.1",
        ),
        serialization_alias="PRA.1",
        title="Primary Key Value - PRA",
        description="C | Item #00685 | Table 9999 - no table for CE",
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
        description="O | Item #00686 | Table 0358 - Practitioner Group",
    )

    pra_3: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pra_3",
            "practitioner_category",
            "PRA.3",
        ),
        serialization_alias="PRA.3",
        title="Practitioner Category",
        description="O | Item #00687 | Table 0186 - Practitioner Category",
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
        description="O | Item #00688 | Table 0187 - Provider Billing | LEN:1",
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
        description="O | Item #00689 | Table 0337 - Certification Status",
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
        description=(
            "O | Item #00690 | Table 0338 - Practitioner ID Number Type"
        ),
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
        description="O | Item #00691",
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
        description="O | Item #01296",
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
        description="O | Item #01613 | Table 0537 - Institution",
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
        description="O | Item #01348",
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
        description=(
            "O | Item #01388 | Table 0401 - Government Reimbursement Program"
        ),
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
        description="C | Item #01616 | LEN:4",
    )

    @field_validator("pra_8", "pra_10", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2})?)?)?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    @field_validator("pra_12", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    model_config = {"populate_by_name": True}
