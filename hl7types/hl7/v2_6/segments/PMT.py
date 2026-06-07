"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: PMT
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CP import CP
from ..datatypes.CWE import CWE
from ..datatypes.CX import CX
from ..datatypes.EI import EI
from ..datatypes.XON import XON


class PMT(HL7Model):
    """HL7 v2 PMT segment.

    Attributes
    ----------
    pmt_1 : EI
        PMT.1 (req) - Payment/Remittance Advice Number (EI)

    pmt_2 : str
        PMT.2 (req) - Payment/Remittance Effective Date/Time (DTM)

    pmt_3 : str
        PMT.3 (req) - Payment/Remittance Expiration Date/Time (DTM)

    pmt_4 : CWE
        PMT.4 (req) - Payment Method (CWE)

    pmt_5 : str
        PMT.5 (req) - Payment/Remittance Date/Time (DTM)

    pmt_6 : CP
        PMT.6 (req) - Payment/Remittance Amount (CP)

    pmt_7 : EI | None
        PMT.7 (opt) - Check Number (EI)

    pmt_8 : XON | None
        PMT.8 (opt) - Payee Bank Identification (XON)

    pmt_9 : str | None
        PMT.9 (opt) - Payee Transit Number (ST)

    pmt_10 : CX | None
        PMT.10 (opt) - Payee Bank Account ID (CX)

    pmt_11 : XON
        PMT.11 (req) - Payment Organization (XON)

    pmt_12 : str | None
        PMT.12 (opt) - ESR-Code-Line (ST)
    """

    pmt_1: EI = Field(
        validation_alias=AliasChoices(
            "pmt_1",
            "payment_remittance_advice_number",
            "PMT.1",
        ),
        serialization_alias="PMT.1",
        title="Payment/Remittance Advice Number",
        description="Item #2018",
    )

    pmt_2: str = Field(
        validation_alias=AliasChoices(
            "pmt_2",
            "payment_remittance_effective_date_time",
            "PMT.2",
        ),
        serialization_alias="PMT.2",
        title="Payment/Remittance Effective Date/Time",
        description="Item #2019",
    )

    pmt_3: str = Field(
        validation_alias=AliasChoices(
            "pmt_3",
            "payment_remittance_expiration_date_time",
            "PMT.3",
        ),
        serialization_alias="PMT.3",
        title="Payment/Remittance Expiration Date/Time",
        description="Item #2020",
    )

    pmt_4: CWE = Field(
        validation_alias=AliasChoices(
            "pmt_4",
            "payment_method",
            "PMT.4",
        ),
        serialization_alias="PMT.4",
        title="Payment Method",
        description="Item #2021 | Table HL70570",
    )

    pmt_5: str = Field(
        validation_alias=AliasChoices(
            "pmt_5",
            "payment_remittance_date_time",
            "PMT.5",
        ),
        serialization_alias="PMT.5",
        title="Payment/Remittance Date/Time",
        description="Item #2022",
    )

    pmt_6: CP = Field(
        validation_alias=AliasChoices(
            "pmt_6",
            "payment_remittance_amount",
            "PMT.6",
        ),
        serialization_alias="PMT.6",
        title="Payment/Remittance Amount",
        description="Item #2023",
    )

    pmt_7: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pmt_7",
            "check_number",
            "PMT.7",
        ),
        serialization_alias="PMT.7",
        title="Check Number",
        description="Item #2024",
    )

    pmt_8: Optional[XON] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pmt_8",
            "payee_bank_identification",
            "PMT.8",
        ),
        serialization_alias="PMT.8",
        title="Payee Bank Identification",
        description="Item #2025",
    )

    pmt_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pmt_9",
            "payee_transit_number",
            "PMT.9",
        ),
        serialization_alias="PMT.9",
        title="Payee Transit Number",
        description="Item #2026",
    )

    pmt_10: Optional[CX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pmt_10",
            "payee_bank_account_id",
            "PMT.10",
        ),
        serialization_alias="PMT.10",
        title="Payee Bank Account ID",
        description="Item #2027",
    )

    pmt_11: XON = Field(
        validation_alias=AliasChoices(
            "pmt_11",
            "payment_organization",
            "PMT.11",
        ),
        serialization_alias="PMT.11",
        title="Payment Organization",
        description="Item #2028",
    )

    pmt_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pmt_12",
            "esr_code_line",
            "PMT.12",
        ),
        serialization_alias="PMT.12",
        title="ESR-Code-Line",
        description="Item #2029",
    )

    @field_validator("pmt_2", "pmt_3", "pmt_5", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 datetime")
        return v

    model_config = {"populate_by_name": True}
