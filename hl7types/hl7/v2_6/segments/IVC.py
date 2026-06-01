"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: IVC
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator

from ..datatypes.CP import CP
from ..datatypes.CX import CX
from ..datatypes.EI import EI
from ..datatypes.XCN import XCN
from ..datatypes.XON import XON


class IVC(HL7Model):
    """HL7 v2 IVC segment.

    Attributes
    ----------
    ivc_1 : EI
        IVC.1 (req) - Provider Invoice Number (EI)

    ivc_2 : EI | None
        IVC.2 (opt) - Payer Invoice Number (EI)

    ivc_3 : EI | None
        IVC.3 (opt) - Contract/Agreement Number (EI)

    ivc_4 : str
        IVC.4 (req) - Invoice Control (IS)

    ivc_5 : str
        IVC.5 (req) - Invoice Reason (IS)

    ivc_6 : str
        IVC.6 (req) - Invoice Type (IS)

    ivc_7 : str
        IVC.7 (req) - Invoice Date/Time (DTM)

    ivc_8 : CP
        IVC.8 (req) - Invoice Amount (CP)

    ivc_9 : str | None
        IVC.9 (opt) - Payment Terms (ST)

    ivc_10 : XON
        IVC.10 (req) - Provider Organization (XON)

    ivc_11 : XON
        IVC.11 (req) - Payer Organization (XON)

    ivc_12 : XCN | None
        IVC.12 (opt) - Attention (XCN)

    ivc_13 : str | None
        IVC.13 (opt) - Last Invoice Indicator (ID)

    ivc_14 : str | None
        IVC.14 (opt) - Invoice Booking Period (DTM)

    ivc_15 : str | None
        IVC.15 (opt) - Origin (ST)

    ivc_16 : CP | None
        IVC.16 (opt) - Invoice Fixed Amount (CP)

    ivc_17 : CP | None
        IVC.17 (opt) - Special Costs (CP)

    ivc_18 : CP | None
        IVC.18 (opt) - Amount for Doctors Treatment (CP)

    ivc_19 : XCN | None
        IVC.19 (opt) - Responsible Physician (XCN)

    ivc_20 : CX | None
        IVC.20 (opt) - Cost Center (CX)

    ivc_21 : CP | None
        IVC.21 (opt) - Invoice Prepaid Amount (CP)

    ivc_22 : CP | None
        IVC.22 (opt) - Total Invoice Amount without Prepaid Amount (CP)

    ivc_23 : CP | None
        IVC.23 (opt) - Total-Amount of VAT (CP)

    ivc_24 : list[str] | None
        IVC.24 (opt, rep) - VAT-Rates applied (NM)

    ivc_25 : str
        IVC.25 (req) - Benefit Group (IS)

    ivc_26 : str | None
        IVC.26 (opt) - Provider Tax ID (ST)

    ivc_27 : str | None
        IVC.27 (opt) - Payer Tax ID (ST)

    ivc_28 : str | None
        IVC.28 (opt) - Provider Tax status (IS)

    ivc_29 : str | None
        IVC.29 (opt) - Payer Tax status (IS)

    ivc_30 : str | None
        IVC.30 (opt) - Sales Tax ID (ST)
    """

    ivc_1: EI = Field(
        default=...,
        validation_alias=AliasChoices(
            "ivc_1",
            "provider_invoice_number",
            "IVC.1",
        ),
        serialization_alias="IVC.1",
        title="Provider Invoice Number",
        description="Item #1914",
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
        description="Item #1915",
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
        description="Item #1916",
    )

    ivc_4: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "ivc_4",
            "invoice_control",
            "IVC.4",
        ),
        serialization_alias="IVC.4",
        title="Invoice Control",
        description="Item #1917 | Table HL70553",
    )

    ivc_5: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "ivc_5",
            "invoice_reason",
            "IVC.5",
        ),
        serialization_alias="IVC.5",
        title="Invoice Reason",
        description="Item #1918 | Table HL70554",
    )

    ivc_6: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "ivc_6",
            "invoice_type",
            "IVC.6",
        ),
        serialization_alias="IVC.6",
        title="Invoice Type",
        description="Item #1919 | Table HL70555",
    )

    ivc_7: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "ivc_7",
            "invoice_date_time",
            "IVC.7",
        ),
        serialization_alias="IVC.7",
        title="Invoice Date/Time",
        description="Item #1920",
    )

    ivc_8: CP = Field(
        default=...,
        validation_alias=AliasChoices(
            "ivc_8",
            "invoice_amount",
            "IVC.8",
        ),
        serialization_alias="IVC.8",
        title="Invoice Amount",
        description="Item #1921",
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
        description="Item #1922",
    )

    ivc_10: XON = Field(
        default=...,
        validation_alias=AliasChoices(
            "ivc_10",
            "provider_organization",
            "IVC.10",
        ),
        serialization_alias="IVC.10",
        title="Provider Organization",
        description="Item #1923",
    )

    ivc_11: XON = Field(
        default=...,
        validation_alias=AliasChoices(
            "ivc_11",
            "payer_organization",
            "IVC.11",
        ),
        serialization_alias="IVC.11",
        title="Payer Organization",
        description="Item #1924",
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
        description="Item #1925",
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
        description="Item #1926 | Table HL70136",
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
        description="Item #1927",
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
        description="Item #1928",
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
        description="Item #1929",
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
        description="Item #1930",
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
        description="Item #1931",
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
        description="Item #1932",
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
        description="Item #1933",
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
        description="Item #1934",
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
        description="Item #1935",
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
        description="Item #1936",
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
        description="Item #1937",
    )

    ivc_25: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "ivc_25",
            "benefit_group",
            "IVC.25",
        ),
        serialization_alias="IVC.25",
        title="Benefit Group",
        description="Item #1938 | Table HL70556",
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
        description="Item #2038",
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
        description="Item #2039",
    )

    ivc_28: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivc_28",
            "provider_tax_status",
            "IVC.28",
        ),
        serialization_alias="IVC.28",
        title="Provider Tax status",
        description="Item #2040 | Table HL70572",
    )

    ivc_29: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivc_29",
            "payer_tax_status",
            "IVC.29",
        ),
        serialization_alias="IVC.29",
        title="Payer Tax status",
        description="Item #2041 | Table HL70572",
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
        description="Item #2042",
    )

    @field_validator("ivc_7", "ivc_14", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 datetime")
        return v

    @field_validator("ivc_24", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
