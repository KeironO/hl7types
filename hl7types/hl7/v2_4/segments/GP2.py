"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: GP2
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.CP import CP


class GP2(HL7Model):
    """Grouping/Reimbursement - Procedure Line Item (S6.5.16).

    Attributes
    ----------
    gp2_1 : str | None
        GP2.1 - Revenue Code (IS) O S6.5.16.1 | 0456 - Revenue code

    gp2_2 : str | None
        GP2.2 - Number of Service Units (NM) O S6.5.16.2

    gp2_3 : CP | None
        GP2.3 - Charge (CP) O S6.5.16.3

    gp2_4 : str | None
        GP2.4 - Reimbursement Action Code (IS) O S6.5.16.4 | 0459 - Reimbursement Action Code

    gp2_5 : str | None
        GP2.5 - Denial or Rejection Code (IS) O S6.5.16.5 | 0460 - Denial or rejection code

    gp2_6 : list[str] | None
        GP2.6 - OCE Edit Code (IS) O rep S6.5.16.6 | 0458 - OCE edit code

    gp2_7 : CE | None
        GP2.7 - Ambulatory Payment Classification Code (CE) O S6.5.16.7 | 0466 - Ambulatory payment classification code

    gp2_8 : list[str] | None
        GP2.8 - Modifier Edit Code (IS) O rep S6.5.16.8 | 0467 - Modifier edit code

    gp2_9 : str | None
        GP2.9 - Payment Adjustment Code (IS) O S6.5.16.9 | 0468 - Payment adjustment code

    gp2_10 : str | None
        GP2.10 - Packaging Status Code (IS) O S6.5.16.10 | 0469 - Packaging status code

    gp2_11 : CP | None
        GP2.11 - Expected HCFA Payment Amount (CP) O S6.5.16.11

    gp2_12 : str | None
        GP2.12 - Reimbursement Type Code (IS) O S6.5.16.12 | 0470 - Reimbursement type code

    gp2_13 : CP | None
        GP2.13 - Co-Pay Amount (CP) O S6.5.16.13

    gp2_14 : str | None
        GP2.14 - Pay Rate per Unit (NM) O S6.5.16.14
    """

    gp2_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gp2_1",
            "revenue_code",
            "GP2.1",
        ),
        serialization_alias="GP2.1",
        title="Revenue Code",
        description="O | Item #01600 | Table 0456 - Revenue code | LEN:3",
    )

    gp2_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gp2_2",
            "number_of_service_units",
            "GP2.2",
        ),
        serialization_alias="GP2.2",
        title="Number of Service Units",
        description="O | Item #01604 | LEN:7",
    )

    gp2_3: Optional[CP] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gp2_3",
            "charge",
            "GP2.3",
        ),
        serialization_alias="GP2.3",
        title="Charge",
        description="O | Item #01605",
    )

    gp2_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gp2_4",
            "reimbursement_action_code",
            "GP2.4",
        ),
        serialization_alias="GP2.4",
        title="Reimbursement Action Code",
        description=(
            "O | Item #01606 | Table 0459 - Reimbursement Action Code | LEN:1"
        ),
    )

    gp2_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gp2_5",
            "denial_or_rejection_code",
            "GP2.5",
        ),
        serialization_alias="GP2.5",
        title="Denial or Rejection Code",
        description=(
            "O | Item #01607 | Table 0460 - Denial or rejection code | LEN:1"
        ),
    )

    gp2_6: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gp2_6",
            "oce_edit_code",
            "GP2.6",
        ),
        serialization_alias="GP2.6",
        title="OCE Edit Code",
        description="O | Item #01608 | Table 0458 - OCE edit code | LEN:3",
    )

    gp2_7: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gp2_7",
            "ambulatory_payment_classification_code",
            "GP2.7",
        ),
        serialization_alias="GP2.7",
        title="Ambulatory Payment Classification Code",
        description=(
            "O | Item #01609 | Table 0466 - Ambulatory payment classification "
            "code"
        ),
    )

    gp2_8: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gp2_8",
            "modifier_edit_code",
            "GP2.8",
        ),
        serialization_alias="GP2.8",
        title="Modifier Edit Code",
        description="O | Item #01610 | Table 0467 - Modifier edit code | LEN:1",
    )

    gp2_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gp2_9",
            "payment_adjustment_code",
            "GP2.9",
        ),
        serialization_alias="GP2.9",
        title="Payment Adjustment Code",
        description=(
            "O | Item #01611 | Table 0468 - Payment adjustment code | LEN:1"
        ),
    )

    gp2_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gp2_10",
            "packaging_status_code",
            "GP2.10",
        ),
        serialization_alias="GP2.10",
        title="Packaging Status Code",
        description=(
            "O | Item #01617 | Table 0469 - Packaging status code | LEN:1"
        ),
    )

    gp2_11: Optional[CP] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gp2_11",
            "expected_hcfa_payment_amount",
            "GP2.11",
        ),
        serialization_alias="GP2.11",
        title="Expected HCFA Payment Amount",
        description="O | Item #01618",
    )

    gp2_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gp2_12",
            "reimbursement_type_code",
            "GP2.12",
        ),
        serialization_alias="GP2.12",
        title="Reimbursement Type Code",
        description=(
            "O | Item #01619 | Table 0470 - Reimbursement type code | LEN:2"
        ),
    )

    gp2_13: Optional[CP] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gp2_13",
            "co_pay_amount",
            "GP2.13",
        ),
        serialization_alias="GP2.13",
        title="Co-Pay Amount",
        description="O | Item #01620",
    )

    gp2_14: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gp2_14",
            "pay_rate_per_unit",
            "GP2.14",
        ),
        serialization_alias="GP2.14",
        title="Pay Rate per Unit",
        description="O | Item #01621 | LEN:4",
    )

    @field_validator("gp2_2", "gp2_14", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
