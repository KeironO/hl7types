"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: IVC
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CP import CP
from ..datatypes.CWE import CWE
from ..datatypes.CX import CX
from ..datatypes.EI import EI
from ..datatypes.XCN import XCN
from ..datatypes.XON import XON


class IVC(BaseModel):
    """HL7 v2 IVC segment."""

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

    ivc_2: EI | None = Field(
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

    ivc_3: EI | None = Field(
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

    ivc_4: CWE = Field(
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

    ivc_5: CWE = Field(
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

    ivc_6: CWE = Field(
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

    ivc_9: str | None = Field(
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

    ivc_12: XCN | None = Field(
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

    ivc_13: str | None = Field(
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

    ivc_14: str | None = Field(
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

    ivc_15: str | None = Field(
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

    ivc_16: CP | None = Field(
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

    ivc_17: CP | None = Field(
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

    ivc_18: CP | None = Field(
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

    ivc_19: XCN | None = Field(
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

    ivc_20: CX | None = Field(
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

    ivc_21: CP | None = Field(
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

    ivc_22: CP | None = Field(
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

    ivc_23: CP | None = Field(
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

    ivc_24: list[str] | None = Field(
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

    ivc_25: CWE = Field(
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

    ivc_26: str | None = Field(
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

    ivc_27: str | None = Field(
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

    ivc_28: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivc_28",
            "provider_tax_status",
            "IVC.28",
        ),
        serialization_alias="IVC.28",
        title="Provider Tax Status",
        description="Item #2040 | Table HL70572",
    )

    ivc_29: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivc_29",
            "payer_tax_status",
            "IVC.29",
        ),
        serialization_alias="IVC.29",
        title="Payer Tax Status",
        description="Item #2041 | Table HL70572",
    )

    ivc_30: str | None = Field(
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

    model_config = {"populate_by_name": True}
