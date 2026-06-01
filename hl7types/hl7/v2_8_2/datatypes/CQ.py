"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: CQ
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator

from .CWE import CWE


class CQ(HL7Model):
    """HL7 v2 CQ data type.

    Attributes
    ----------
    cq_1 : str | None
        CQ.1 (opt) - Quantity (NM)

    cq_2 : CWE | None
        CQ.2 (opt) - Units (CWE)
    """

    cq_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cq_1",
            "quantity",
            "CQ.1",
        ),
        serialization_alias="CQ.1",
        title="Quantity",
    )

    cq_2: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cq_2",
            "units",
            "CQ.2",
        ),
        serialization_alias="CQ.2",
        title="Units",
    )

    @field_validator("cq_1", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
