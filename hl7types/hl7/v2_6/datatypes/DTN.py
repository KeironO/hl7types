"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: DTN
Type: Datatype
"""
from __future__ import annotations

from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model


class DTN(HL7Model):
    """HL7 v2 DTN data type.

    Attributes
    ----------
    dtn_1 : str
        DTN.1 (req) - Day Type (IS)

    dtn_2 : str
        DTN.2 (req) - Number of Days (NM)
    """

    dtn_1: str = Field(
        max_length=2,
        validation_alias=AliasChoices(
            "dtn_1",
            "day_type",
            "DTN.1",
        ),
        serialization_alias="DTN.1",
        title="Day Type",
    )

    dtn_2: str = Field(
        max_length=3,
        validation_alias=AliasChoices(
            "dtn_2",
            "number_of_days",
            "DTN.2",
        ),
        serialization_alias="DTN.2",
        title="Number of Days",
    )

    @field_validator("dtn_2", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
