"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: IPR
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CP import CP
from ..datatypes.CWE import CWE
from ..datatypes.EI import EI


class IPR(HL7Model):
    """HL7 v2 IPR segment.

    Attributes
    ----------
    ipr_1 : EI
        IPR.1 (req) - IPR Identifier (EI)

    ipr_2 : EI
        IPR.2 (req) - Provider Cross Reference Identifier (EI)

    ipr_3 : EI
        IPR.3 (req) - Payer Cross Reference Identifier (EI)

    ipr_4 : CWE
        IPR.4 (req) - IPR Status (CWE)

    ipr_5 : str
        IPR.5 (req) - IPR Date/Time (DTM)

    ipr_6 : CP | None
        IPR.6 (opt) - Adjudicated/Paid Amount (CP)

    ipr_7 : str | None
        IPR.7 (opt) - Expected Payment Date/Time (DTM)

    ipr_8 : str
        IPR.8 (req) - IPR Checksum (ST)
    """

    ipr_1: EI = Field(
        validation_alias=AliasChoices(
            "ipr_1",
            "ipr_identifier",
            "IPR.1",
        ),
        serialization_alias="IPR.1",
        title="IPR Identifier",
        description="Item #2030",
    )

    ipr_2: EI = Field(
        validation_alias=AliasChoices(
            "ipr_2",
            "provider_cross_reference_identifier",
            "IPR.2",
        ),
        serialization_alias="IPR.2",
        title="Provider Cross Reference Identifier",
        description="Item #2031",
    )

    ipr_3: EI = Field(
        validation_alias=AliasChoices(
            "ipr_3",
            "payer_cross_reference_identifier",
            "IPR.3",
        ),
        serialization_alias="IPR.3",
        title="Payer Cross Reference Identifier",
        description="Item #2032",
    )

    ipr_4: CWE = Field(
        validation_alias=AliasChoices(
            "ipr_4",
            "ipr_status",
            "IPR.4",
        ),
        serialization_alias="IPR.4",
        title="IPR Status",
        description="Item #2033 | Table HL70571",
    )

    ipr_5: str = Field(
        validation_alias=AliasChoices(
            "ipr_5",
            "ipr_date_time",
            "IPR.5",
        ),
        serialization_alias="IPR.5",
        title="IPR Date/Time",
        description="Item #2034",
    )

    ipr_6: Optional[CP] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ipr_6",
            "adjudicated_paid_amount",
            "IPR.6",
        ),
        serialization_alias="IPR.6",
        title="Adjudicated/Paid Amount",
        description="Item #2035",
    )

    ipr_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ipr_7",
            "expected_payment_date_time",
            "IPR.7",
        ),
        serialization_alias="IPR.7",
        title="Expected Payment Date/Time",
        description="Item #2036",
    )

    ipr_8: str = Field(
        validation_alias=AliasChoices(
            "ipr_8",
            "ipr_checksum",
            "IPR.8",
        ),
        serialization_alias="IPR.8",
        title="IPR Checksum",
        description="Item #2037",
    )

    @field_validator("ipr_5", "ipr_7", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        import re
        if re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = {"populate_by_name": True}
