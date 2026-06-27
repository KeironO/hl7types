"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: EQP
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE


class EQP(HL7Model):
    """HL7 v2 EQP segment.

    Attributes
    ----------
    eqp_1 : CWE
        EQP.1 (req) - Event type (CWE)

    eqp_2 : str | None
        EQP.2 (opt) - File Name (ST)

    eqp_3 : str
        EQP.3 (req) - Start Date/Time (DTM)

    eqp_4 : str | None
        EQP.4 (opt) - End Date/Time (DTM)

    eqp_5 : str
        EQP.5 (req) - Transaction Data (FT)
    """

    eqp_1: CWE = Field(
        validation_alias=AliasChoices(
            "eqp_1",
            "event_type",
            "EQP.1",
        ),
        serialization_alias="EQP.1",
        title="Event type",
        description="Item #1430 | Table HL70450",
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
        description="Item #1431",
    )

    eqp_3: str = Field(
        validation_alias=AliasChoices(
            "eqp_3",
            "start_date_time",
            "EQP.3",
        ),
        serialization_alias="EQP.3",
        title="Start Date/Time",
        description="Item #1202",
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
        description="Item #1432",
    )

    eqp_5: str = Field(
        validation_alias=AliasChoices(
            "eqp_5",
            "transaction_data",
            "EQP.5",
        ),
        serialization_alias="EQP.5",
        title="Transaction Data",
        description="Item #1433",
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
