"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: ADJ
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CP import CP
from ..datatypes.CQ import CQ
from ..datatypes.CWE import CWE
from ..datatypes.EI import EI
from ..datatypes.XON import XON


class ADJ(HL7Model):
    """Adjustment (S16.4.7).

    Attributes
    ----------
    adj_1 : EI
        ADJ.1 - Provider Adjustment Number (EI) R S16.4.7.1

    adj_2 : EI
        ADJ.2 - Payer Adjustment Number (EI) R S16.4.7.2

    adj_3 : str
        ADJ.3 - Adjustment Sequence Number (SI) R S16.4.7.3

    adj_4 : CWE
        ADJ.4 - Adjustment Category (CWE) R S16.4.7.4 | 0564 - Adjustment Category Code

    adj_5 : list[CP] | None
        ADJ.5 - Adjustment Amount (CP) O rep S16.4.7.5

    adj_6 : CQ | None
        ADJ.6 - Adjustment Quantity (CQ) O S16.4.7.6 | 0560 - Quantity Units

    adj_7 : CWE | None
        ADJ.7 - Adjustment Reason PA (CWE) C S16.4.7.7 | 0565 - Provider Adjustment Reason Code

    adj_8 : str | None
        ADJ.8 - Adjustment Description (ST) O S16.4.7.8

    adj_9 : str | None
        ADJ.9 - Original Value (NM) O S16.4.7.9

    adj_10 : str | None
        ADJ.10 - Substitute Value (NM) O S16.4.7.10

    adj_11 : CWE | None
        ADJ.11 - Adjustment Action (CWE) O S16.4.7.11 | 0569 - Adjustment Action

    adj_12 : EI | None
        ADJ.12 - Provider Adjustment Number Cross Reference (EI) O S16.4.7.12

    adj_13 : EI | None
        ADJ.13 - Provider Product/Service Line Item Number Cross Reference (EI) O S16.4.7.13

    adj_14 : str
        ADJ.14 - Adjustment Date (DTM) R S16.4.7.14

    adj_15 : XON | None
        ADJ.15 - Responsible Organization (XON) O S16.4.7.15
    """

    adj_1: EI = Field(
        validation_alias=AliasChoices(
            "adj_1",
            "provider_adjustment_number",
            "ADJ.1",
        ),
        serialization_alias="ADJ.1",
        title="Provider Adjustment Number",
        description="R | Item #02003",
    )

    adj_2: EI = Field(
        validation_alias=AliasChoices(
            "adj_2",
            "payer_adjustment_number",
            "ADJ.2",
        ),
        serialization_alias="ADJ.2",
        title="Payer Adjustment Number",
        description="R | Item #02004",
    )

    adj_3: str = Field(
        validation_alias=AliasChoices(
            "adj_3",
            "adjustment_sequence_number",
            "ADJ.3",
        ),
        serialization_alias="ADJ.3",
        title="Adjustment Sequence Number",
        description="R | Item #02005 | LEN:4",
    )

    adj_4: CWE = Field(
        validation_alias=AliasChoices(
            "adj_4",
            "adjustment_category",
            "ADJ.4",
        ),
        serialization_alias="ADJ.4",
        title="Adjustment Category",
        description="R | Item #02006 | Table 0564 - Adjustment Category Code",
    )

    adj_5: Optional[List[CP]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "adj_5",
            "adjustment_amount",
            "ADJ.5",
        ),
        serialization_alias="ADJ.5",
        title="Adjustment Amount",
        description="O | Item #02007",
    )

    adj_6: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "adj_6",
            "adjustment_quantity",
            "ADJ.6",
        ),
        serialization_alias="ADJ.6",
        title="Adjustment Quantity",
        description="O | Item #02008 | Table 0560 - Quantity Units",
    )

    adj_7: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "adj_7",
            "adjustment_reason_pa",
            "ADJ.7",
        ),
        serialization_alias="ADJ.7",
        title="Adjustment Reason PA",
        description=(
            "C | Item #02009 | Table 0565 - Provider Adjustment Reason Code"
        ),
    )

    adj_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "adj_8",
            "adjustment_description",
            "ADJ.8",
        ),
        serialization_alias="ADJ.8",
        title="Adjustment Description",
        description="O | Item #02010",
    )

    adj_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "adj_9",
            "original_value",
            "ADJ.9",
        ),
        serialization_alias="ADJ.9",
        title="Original Value",
        description="O | Item #02011",
    )

    adj_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "adj_10",
            "substitute_value",
            "ADJ.10",
        ),
        serialization_alias="ADJ.10",
        title="Substitute Value",
        description="O | Item #02012",
    )

    adj_11: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "adj_11",
            "adjustment_action",
            "ADJ.11",
        ),
        serialization_alias="ADJ.11",
        title="Adjustment Action",
        description="O | Item #02013 | Table 0569 - Adjustment Action",
    )

    adj_12: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "adj_12",
            "provider_adjustment_number_cross_reference",
            "ADJ.12",
        ),
        serialization_alias="ADJ.12",
        title="Provider Adjustment Number Cross Reference",
        description="O | Item #02014",
    )

    adj_13: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "adj_13",
            "provider_product_service_line_item_number_cross_reference",
            "ADJ.13",
        ),
        serialization_alias="ADJ.13",
        title="Provider Product/Service Line Item Number Cross Reference",
        description="O | Item #02015",
    )

    adj_14: str = Field(
        validation_alias=AliasChoices(
            "adj_14",
            "adjustment_date",
            "ADJ.14",
        ),
        serialization_alias="ADJ.14",
        title="Adjustment Date",
        description="R | Item #02016",
    )

    adj_15: Optional[XON] = Field(
        default=None,
        validation_alias=AliasChoices(
            "adj_15",
            "responsible_organization",
            "ADJ.15",
        ),
        serialization_alias="ADJ.15",
        title="Responsible Organization",
        description="O | Item #02017",
    )

    @field_validator("adj_3", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("adj_9", "adj_10", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    @field_validator("adj_14", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        import re
        if re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = {"populate_by_name": True}
