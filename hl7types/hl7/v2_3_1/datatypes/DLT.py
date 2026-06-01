"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: DLT
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator

from .NR import NR


class DLT(HL7Model):
    """HL7 v2 DLT data type.

    Attributes
    ----------
    dlt_1 : NR | None
        DLT.1 (opt) - Range (NR)

    dlt_2 : str | None
        DLT.2 (opt) - numeric threshold (NM)

    dlt_3 : str | None
        DLT.3 (opt) - change computation (ST)

    dlt_4 : str | None
        DLT.4 (opt) - length of time-days (NM)
    """

    dlt_1: Optional[NR] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dlt_1",
            "range",
            "DLT.1",
        ),
        serialization_alias="DLT.1",
        title="Range",
    )

    dlt_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dlt_2",
            "numeric_threshold",
            "DLT.2",
        ),
        serialization_alias="DLT.2",
        title="numeric threshold",
    )

    dlt_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dlt_3",
            "change_computation",
            "DLT.3",
        ),
        serialization_alias="DLT.3",
        title="change computation",
    )

    dlt_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dlt_4",
            "length_of_time_days",
            "DLT.4",
        ),
        serialization_alias="DLT.4",
        title="length of time-days",
    )

    @field_validator("dlt_2", "dlt_4", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
