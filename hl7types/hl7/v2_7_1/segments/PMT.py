"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
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
    """Payment Information (S16.4.8).

    Attributes
    ----------
    pmt_1 : EI
        PMT.1 - Payment/Remittance Advice Number (EI) R S16.4.8.1

    pmt_2 : str
        PMT.2 - Payment/Remittance Effective Date/Time (DTM) R S16.4.8.2

    pmt_3 : str
        PMT.3 - Payment/Remittance Expiration Date/Time (DTM) R S16.4.8.3

    pmt_4 : CWE
        PMT.4 - Payment Method (CWE) R S16.4.8.4 | 0570 - Payment Method Code

    pmt_5 : str
        PMT.5 - Payment/Remittance Date/Time (DTM) R S16.4.8.5

    pmt_6 : CP
        PMT.6 - Payment/Remittance Amount (CP) R S16.4.8.6

    pmt_7 : EI | None
        PMT.7 - Check Number (EI) O S16.4.8.7

    pmt_8 : XON | None
        PMT.8 - Payee Bank Identification (XON) O S16.4.8.8

    pmt_9 : str | None
        PMT.9 - Payee Transit Number (ST) O S16.4.8.9

    pmt_10 : CX | None
        PMT.10 - Payee Bank Account ID (CX) O S16.4.8.10

    pmt_11 : XON
        PMT.11 - Payment Organization (XON) R S16.4.8.11

    pmt_12 : str | None
        PMT.12 - ESR-Code-Line (ST) O S16.4.8.12
    """

    pmt_1: EI = Field(
        validation_alias=AliasChoices(
            "pmt_1",
            "payment_remittance_advice_number",
            "PMT.1",
        ),
        serialization_alias="PMT.1",
        title="Payment/Remittance Advice Number",
        description="R | Item #02018",
    )

    pmt_2: str = Field(
        validation_alias=AliasChoices(
            "pmt_2",
            "payment_remittance_effective_date_time",
            "PMT.2",
        ),
        serialization_alias="PMT.2",
        title="Payment/Remittance Effective Date/Time",
        description="R | Item #02019",
    )

    pmt_3: str = Field(
        validation_alias=AliasChoices(
            "pmt_3",
            "payment_remittance_expiration_date_time",
            "PMT.3",
        ),
        serialization_alias="PMT.3",
        title="Payment/Remittance Expiration Date/Time",
        description="R | Item #02020",
    )

    pmt_4: CWE = Field(
        validation_alias=AliasChoices(
            "pmt_4",
            "payment_method",
            "PMT.4",
        ),
        serialization_alias="PMT.4",
        title="Payment Method",
        description="R | Item #02021 | Table 0570 - Payment Method Code",
    )

    pmt_5: str = Field(
        validation_alias=AliasChoices(
            "pmt_5",
            "payment_remittance_date_time",
            "PMT.5",
        ),
        serialization_alias="PMT.5",
        title="Payment/Remittance Date/Time",
        description="R | Item #02022",
    )

    pmt_6: CP = Field(
        validation_alias=AliasChoices(
            "pmt_6",
            "payment_remittance_amount",
            "PMT.6",
        ),
        serialization_alias="PMT.6",
        title="Payment/Remittance Amount",
        description="R | Item #02023",
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
        description="O | Item #02024",
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
        description="O | Item #02025",
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
        description="O | Item #02026",
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
        description="O | Item #02027",
    )

    pmt_11: XON = Field(
        validation_alias=AliasChoices(
            "pmt_11",
            "payment_organization",
            "PMT.11",
        ),
        serialization_alias="PMT.11",
        title="Payment Organization",
        description="R | Item #02028",
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
        description="O | Item #02029",
    )

    @field_validator("pmt_2", "pmt_3", "pmt_5", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        import re
        if re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = {"populate_by_name": True}
