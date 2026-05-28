"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: GP2
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE
from ..datatypes.CP import CP


class GP2(BaseModel):
    """HL7 v2 GP2 segment."""

    gp2_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gp2_1",
            "revenue_code",
            "GP2.1",
        ),
        serialization_alias="GP2.1",
        title="Revenue Code",
        description="Item #1600 | Table HL70456",
    )

    gp2_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gp2_2",
            "number_of_service_units",
            "GP2.2",
        ),
        serialization_alias="GP2.2",
        title="Number of Service Units",
        description="Item #1604",
    )

    gp2_3: CP | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gp2_3",
            "charge",
            "GP2.3",
        ),
        serialization_alias="GP2.3",
        title="Charge",
        description="Item #1605",
    )

    gp2_4: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gp2_4",
            "reimbursement_action_code",
            "GP2.4",
        ),
        serialization_alias="GP2.4",
        title="Reimbursement Action Code",
        description="Item #1606 | Table HL70459",
    )

    gp2_5: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gp2_5",
            "denial_or_rejection_code",
            "GP2.5",
        ),
        serialization_alias="GP2.5",
        title="Denial or Rejection Code",
        description="Item #1607 | Table HL70460",
    )

    gp2_6: list[str] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gp2_6",
            "oce_edit_code",
            "GP2.6",
        ),
        serialization_alias="GP2.6",
        title="OCE Edit Code",
        description="Item #1608 | Table HL70458",
    )

    gp2_7: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gp2_7",
            "ambulatory_payment_classification_code",
            "GP2.7",
        ),
        serialization_alias="GP2.7",
        title="Ambulatory Payment Classification Code",
        description="Item #1609 | Table HL70466",
    )

    gp2_8: list[str] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gp2_8",
            "modifier_edit_code",
            "GP2.8",
        ),
        serialization_alias="GP2.8",
        title="Modifier Edit Code",
        description="Item #1610 | Table HL70467",
    )

    gp2_9: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gp2_9",
            "payment_adjustment_code",
            "GP2.9",
        ),
        serialization_alias="GP2.9",
        title="Payment Adjustment Code",
        description="Item #1611 | Table HL70468",
    )

    gp2_10: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gp2_10",
            "packaging_status_code",
            "GP2.10",
        ),
        serialization_alias="GP2.10",
        title="Packaging Status Code",
        description="Item #1617 | Table HL70469",
    )

    gp2_11: CP | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gp2_11",
            "expected_hcfa_payment_amount",
            "GP2.11",
        ),
        serialization_alias="GP2.11",
        title="Expected HCFA Payment Amount",
        description="Item #1618",
    )

    gp2_12: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gp2_12",
            "reimbursement_type_code",
            "GP2.12",
        ),
        serialization_alias="GP2.12",
        title="Reimbursement Type Code",
        description="Item #1619 | Table HL70470",
    )

    gp2_13: CP | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gp2_13",
            "co_pay_amount",
            "GP2.13",
        ),
        serialization_alias="GP2.13",
        title="Co-Pay Amount",
        description="Item #1620",
    )

    gp2_14: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gp2_14",
            "pay_rate_per_unit",
            "GP2.14",
        ),
        serialization_alias="GP2.14",
        title="Pay Rate per Unit",
        description="Item #1621",
    )

    model_config = {"populate_by_name": True}
