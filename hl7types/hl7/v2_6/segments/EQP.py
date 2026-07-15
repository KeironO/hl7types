"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: EQP
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE


class EQP(HL7Model):
    """Equipment/log Service (S13.4.12).

    Attributes
    ----------
    eqp_1 : CWE
        EQP.1 - Event type (CWE) R S13.4.12.1 | 0450 - Event type

    eqp_2 : str | None
        EQP.2 - File Name (ST) O S13.4.12.2

    eqp_3 : str
        EQP.3 - Start Date/Time (DTM) R S10.6.4.4

    eqp_4 : str | None
        EQP.4 - End Date/Time (DTM) O S13.4.12.4

    eqp_5 : str
        EQP.5 - Transaction Data (FT) R S13.4.12.5
    """

    eqp_1: CWE = Field(
        validation_alias=AliasChoices(
            "eqp_1",
            "event_type",
            "EQP.1",
        ),
        serialization_alias="EQP.1",
        title="Event type",
        description="R | Item #01430 | Table 0450 - Event type",
    )

    eqp_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "eqp_2",
            "file_name",
            "EQP.2",
        ),
        serialization_alias="EQP.2",
        title="File Name",
        description="O | Item #01431 | LEN:20",
    )

    eqp_3: str = Field(
        validation_alias=AliasChoices(
            "eqp_3",
            "start_date_time",
            "EQP.3",
        ),
        serialization_alias="EQP.3",
        title="Start Date/Time",
        description="R | Item #01202 | LEN:24",
    )

    eqp_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "eqp_4",
            "end_date_time",
            "EQP.4",
        ),
        serialization_alias="EQP.4",
        title="End Date/Time",
        description="O | Item #01432 | LEN:24",
    )

    eqp_5: str = Field(
        validation_alias=AliasChoices(
            "eqp_5",
            "transaction_data",
            "EQP.5",
        ),
        serialization_alias="EQP.5",
        title="Transaction Data",
        description="R | Item #01433",
    )

    @field_validator("eqp_3", "eqp_4", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        import re
        if re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = {"populate_by_name": True}
