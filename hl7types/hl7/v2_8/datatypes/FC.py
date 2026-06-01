"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: FC
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator

from .CWE import CWE


class FC(HL7Model):
    """HL7 v2 FC data type.

    Attributes
    ----------
    fc_1 : CWE
        FC.1 (req) - Financial Class Code (CWE)

    fc_2 : str | None
        FC.2 (opt) - Effective Date (DTM)
    """

    fc_1: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "fc_1",
            "financial_class_code",
            "FC.1",
        ),
        serialization_alias="FC.1",
        title="Financial Class Code",
    )

    fc_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "fc_2",
            "effective_date",
            "FC.2",
        ),
        serialization_alias="FC.2",
        title="Effective Date",
    )

    @field_validator("fc_2", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 datetime")
        return v

    model_config = {"populate_by_name": True}
