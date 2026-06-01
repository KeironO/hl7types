"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: PRA
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator

from ..datatypes.CE import CE
from ..datatypes.PIP import PIP
from ..datatypes.PLN import PLN
from ..datatypes.SPD import SPD


class PRA(HL7Model):
    """HL7 v2 PRA segment.

    Attributes
    ----------
    pra_1 : CE | None
        PRA.1 (opt) - Primary Key Value - PRA (CE)

    pra_2 : list[CE] | None
        PRA.2 (opt, rep) - Practitioner Group (CE)

    pra_3 : list[str] | None
        PRA.3 (opt, rep) - Practitioner Category (IS)

    pra_4 : str | None
        PRA.4 (opt) - Provider Billing (ID)

    pra_5 : list[SPD] | None
        PRA.5 (opt, rep) - Specialty (SPD)

    pra_6 : list[PLN] | None
        PRA.6 (opt, rep) - Practitioner ID Numbers (PLN)

    pra_7 : list[PIP] | None
        PRA.7 (opt, rep) - Privileges (PIP)

    pra_8 : str | None
        PRA.8 (opt) - Date Entered Practice (DT)

    pra_9 : CE | None
        PRA.9 (opt) - Institution (CE)

    pra_10 : str | None
        PRA.10 (opt) - Date Left Practice (DT)

    pra_11 : list[CE] | None
        PRA.11 (opt, rep) - Government Reimbursement Billing Eligibility (CE)

    pra_12 : str | None
        PRA.12 (opt) - Set ID - PRA (SI)
    """

    pra_1: Optional[CE] = Field(
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

    pra_2: Optional[List[CE]] = Field(
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

    pra_9: Optional[CE] = Field(
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

    pra_11: Optional[List[CE]] = Field(
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
