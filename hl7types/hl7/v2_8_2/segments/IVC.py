"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: IVC
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CP import CP
from ..datatypes.CWE import CWE
from ..datatypes.CX import CX
from ..datatypes.EI import EI
from ..datatypes.XCN import XCN
from ..datatypes.XON import XON


class IVC(HL7Model):
    """Invoice Segment (S16.4.2).

    Attributes
    ----------
    ivc_1 : EI
        IVC.1 - Provider Invoice Number (EI) R S16.4.2.1

    ivc_2 : EI | None
        IVC.2 - Payer Invoice Number (EI) O S16.4.2.2

    ivc_3 : EI | None
        IVC.3 - Contract/Agreement Number (EI) O S16.4.2.3

    ivc_4 : CWE
        IVC.4 - Invoice Control (CWE) R S16.4.2.4 | 0553 - Invoice Control Code

    ivc_5 : CWE
        IVC.5 - Invoice Reason (CWE) R S16.4.2.5 | 0554 - Invoice Reason Codes

    ivc_6 : CWE
        IVC.6 - Invoice Type (CWE) R S16.4.2.6 | 0555 - Invoice Type

    ivc_7 : str
        IVC.7 - Invoice Date/Time (DTM) R S16.4.2.7

    ivc_8 : CP
        IVC.8 - Invoice Amount (CP) R S16.4.2.8

    ivc_9 : str | None
        IVC.9 - Payment Terms (ST) O S16.4.2.9

    ivc_10 : XON
        IVC.10 - Provider Organization (XON) R S16.4.2.10

    ivc_11 : XON
        IVC.11 - Payer Organization (XON) R S16.4.2.11

    ivc_12 : XCN | None
        IVC.12 - Attention (XCN) O S16.4.2.12

    ivc_13 : str | None
        IVC.13 - Last Invoice Indicator (ID) O S16.4.2.13 | 0136 - Yes/no Indicator

    ivc_14 : str | None
        IVC.14 - Invoice Booking Period (DTM) O S16.4.2.14

    ivc_15 : str | None
        IVC.15 - Origin (ST) O S16.4.2.15

    ivc_16 : CP | None
        IVC.16 - Invoice Fixed Amount (CP) O S16.4.2.16

    ivc_17 : CP | None
        IVC.17 - Special Costs (CP) O S16.4.2.17

    ivc_18 : CP | None
        IVC.18 - Amount for Doctors Treatment (CP) O S16.4.2.18

    ivc_19 : XCN | None
        IVC.19 - Responsible Physician (XCN) O S16.4.2.19

    ivc_20 : CX | None
        IVC.20 - Cost Center (CX) O S16.4.2.20

    ivc_21 : CP | None
        IVC.21 - Invoice Prepaid Amount (CP) O S16.4.2.21

    ivc_22 : CP | None
        IVC.22 - Total Invoice Amount without Prepaid Amount (CP) O S16.4.2.22

    ivc_23 : CP | None
        IVC.23 - Total-Amount of VAT (CP) C S16.4.2.23

    ivc_24 : list[str] | None
        IVC.24 - VAT-Rates applied (NM) O rep S16.4.2.24

    ivc_25 : CWE
        IVC.25 - Benefit Group (CWE) R S16.4.2.25 | 0556 - Benefit Group

    ivc_26 : str | None
        IVC.26 - Provider Tax ID (ST) O S16.4.2.26

    ivc_27 : str | None
        IVC.27 - Payer Tax ID (ST) O S16.4.2.27

    ivc_28 : CWE | None
        IVC.28 - Provider Tax Status (CWE) O S16.4.2.28 | 0572 - Tax status

    ivc_29 : CWE | None
        IVC.29 - Payer Tax Status (CWE) O S16.4.2.29 | 0572 - Tax status

    ivc_30 : str | None
        IVC.30 - Sales Tax ID (ST) O S16.4.2.30
    """

    ivc_1: EI = Field(
        validation_alias=AliasChoices(
            "ivc_1",
            "provider_invoice_number",
            "IVC.1",
        ),
        serialization_alias="IVC.1",
        title="Provider Invoice Number",
        description="R | Item #01914",
    )

    ivc_2: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivc_2",
            "payer_invoice_number",
            "IVC.2",
        ),
        serialization_alias="IVC.2",
        title="Payer Invoice Number",
        description="O | Item #01915",
    )

    ivc_3: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivc_3",
            "contract_agreement_number",
            "IVC.3",
        ),
        serialization_alias="IVC.3",
        title="Contract/Agreement Number",
        description="O | Item #01916",
    )

    ivc_4: CWE = Field(
        validation_alias=AliasChoices(
            "ivc_4",
            "invoice_control",
            "IVC.4",
        ),
        serialization_alias="IVC.4",
        title="Invoice Control",
        description="R | Item #01917 | Table 0553 - Invoice Control Code",
    )

    ivc_5: CWE = Field(
        validation_alias=AliasChoices(
            "ivc_5",
            "invoice_reason",
            "IVC.5",
        ),
        serialization_alias="IVC.5",
        title="Invoice Reason",
        description="R | Item #01918 | Table 0554 - Invoice Reason Codes",
    )

    ivc_6: CWE = Field(
        validation_alias=AliasChoices(
            "ivc_6",
            "invoice_type",
            "IVC.6",
        ),
        serialization_alias="IVC.6",
        title="Invoice Type",
        description="R | Item #01919 | Table 0555 - Invoice Type",
    )

    ivc_7: str = Field(
        validation_alias=AliasChoices(
            "ivc_7",
            "invoice_date_time",
            "IVC.7",
        ),
        serialization_alias="IVC.7",
        title="Invoice Date/Time",
        description="R | Item #01920",
    )

    ivc_8: CP = Field(
        validation_alias=AliasChoices(
            "ivc_8",
            "invoice_amount",
            "IVC.8",
        ),
        serialization_alias="IVC.8",
        title="Invoice Amount",
        description="R | Item #01921",
    )

    ivc_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivc_9",
            "payment_terms",
            "IVC.9",
        ),
        serialization_alias="IVC.9",
        title="Payment Terms",
        description="O | Item #01922",
    )

    ivc_10: XON = Field(
        validation_alias=AliasChoices(
            "ivc_10",
            "provider_organization",
            "IVC.10",
        ),
        serialization_alias="IVC.10",
        title="Provider Organization",
        description="R | Item #01923",
    )

    ivc_11: XON = Field(
        validation_alias=AliasChoices(
            "ivc_11",
            "payer_organization",
            "IVC.11",
        ),
        serialization_alias="IVC.11",
        title="Payer Organization",
        description="R | Item #01924",
    )

    ivc_12: Optional[XCN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivc_12",
            "attention",
            "IVC.12",
        ),
        serialization_alias="IVC.12",
        title="Attention",
        description="O | Item #01925",
    )

    ivc_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivc_13",
            "last_invoice_indicator",
            "IVC.13",
        ),
        serialization_alias="IVC.13",
        title="Last Invoice Indicator",
        description="O | Item #01926 | Table 0136 - Yes/no Indicator | LEN:1",
    )

    ivc_14: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivc_14",
            "invoice_booking_period",
            "IVC.14",
        ),
        serialization_alias="IVC.14",
        title="Invoice Booking Period",
        description="O | Item #01927",
    )

    ivc_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivc_15",
            "origin",
            "IVC.15",
        ),
        serialization_alias="IVC.15",
        title="Origin",
        description="O | Item #01928",
    )

    ivc_16: Optional[CP] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivc_16",
            "invoice_fixed_amount",
            "IVC.16",
        ),
        serialization_alias="IVC.16",
        title="Invoice Fixed Amount",
        description="O | Item #01929",
    )

    ivc_17: Optional[CP] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivc_17",
            "special_costs",
            "IVC.17",
        ),
        serialization_alias="IVC.17",
        title="Special Costs",
        description="O | Item #01930",
    )

    ivc_18: Optional[CP] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivc_18",
            "amount_for_doctors_treatment",
            "IVC.18",
        ),
        serialization_alias="IVC.18",
        title="Amount for Doctors Treatment",
        description="O | Item #01931",
    )

    ivc_19: Optional[XCN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivc_19",
            "responsible_physician",
            "IVC.19",
        ),
        serialization_alias="IVC.19",
        title="Responsible Physician",
        description="O | Item #01932",
    )

    ivc_20: Optional[CX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivc_20",
            "cost_center",
            "IVC.20",
        ),
        serialization_alias="IVC.20",
        title="Cost Center",
        description="O | Item #01933",
    )

    ivc_21: Optional[CP] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivc_21",
            "invoice_prepaid_amount",
            "IVC.21",
        ),
        serialization_alias="IVC.21",
        title="Invoice Prepaid Amount",
        description="O | Item #01934",
    )

    ivc_22: Optional[CP] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivc_22",
            "total_invoice_amount_without_prepaid_amount",
            "IVC.22",
        ),
        serialization_alias="IVC.22",
        title="Total Invoice Amount without Prepaid Amount",
        description="O | Item #01935",
    )

    ivc_23: Optional[CP] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivc_23",
            "total_amount_of_vat",
            "IVC.23",
        ),
        serialization_alias="IVC.23",
        title="Total-Amount of VAT",
        description="C | Item #01936",
    )

    ivc_24: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivc_24",
            "vat_rates_applied",
            "IVC.24",
        ),
        serialization_alias="IVC.24",
        title="VAT-Rates applied",
        description="O | Item #01937",
    )

    ivc_25: CWE = Field(
        validation_alias=AliasChoices(
            "ivc_25",
            "benefit_group",
            "IVC.25",
        ),
        serialization_alias="IVC.25",
        title="Benefit Group",
        description="R | Item #01938 | Table 0556 - Benefit Group",
    )

    ivc_26: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivc_26",
            "provider_tax_id",
            "IVC.26",
        ),
        serialization_alias="IVC.26",
        title="Provider Tax ID",
        description="O | Item #02038",
    )

    ivc_27: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivc_27",
            "payer_tax_id",
            "IVC.27",
        ),
        serialization_alias="IVC.27",
        title="Payer Tax ID",
        description="O | Item #02039",
    )

    ivc_28: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivc_28",
            "provider_tax_status",
            "IVC.28",
        ),
        serialization_alias="IVC.28",
        title="Provider Tax Status",
        description="O | Item #02040 | Table 0572 - Tax status",
    )

    ivc_29: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivc_29",
            "payer_tax_status",
            "IVC.29",
        ),
        serialization_alias="IVC.29",
        title="Payer Tax Status",
        description="O | Item #02041 | Table 0572 - Tax status",
    )

    ivc_30: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivc_30",
            "sales_tax_id",
            "IVC.30",
        ),
        serialization_alias="IVC.30",
        title="Sales Tax ID",
        description="O | Item #02042",
    )

    @field_validator("ivc_7", "ivc_14", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        import re
        if re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    @field_validator("ivc_24", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
