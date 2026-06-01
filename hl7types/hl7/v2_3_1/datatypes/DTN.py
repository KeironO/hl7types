"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: DTN
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator


class DTN(HL7Model):
    """HL7 v2 DTN data type.

    Attributes
    ----------
    dtn_1 : str | None
        DTN.1 (opt) - day type (IS)

    dtn_2 : str | None
        DTN.2 (opt) - number of days (NM)
    """

    dtn_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dtn_1",
            "day_type",
            "DTN.1",
        ),
        serialization_alias="DTN.1",
        title="day type",
    )

    dtn_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dtn_2",
            "number_of_days",
            "DTN.2",
        ),
        serialization_alias="DTN.2",
        title="number of days",
    )

    @field_validator("dtn_2", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
