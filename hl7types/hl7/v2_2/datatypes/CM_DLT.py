"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: CM_DLT
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator


class CM_DLT(HL7Model):
    """HL7 v2 CM_DLT data type.

    Attributes
    ----------
    cm_dlt_1 : str | None
        CM_DLT.1 (opt) - Range (CM)

    cm_dlt_2 : str | None
        CM_DLT.2 (opt) - numeric threshold (NM)

    cm_dlt_3 : str | None
        CM_DLT.3 (opt) - change (ST)

    cm_dlt_4 : str | None
        CM_DLT.4 (opt) - length of time-days (NM)
    """

    cm_dlt_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_dlt_1",
            "range",
            "CM_DLT.1",
        ),
        serialization_alias="CM_DLT.1",
        title="Range",
    )

    cm_dlt_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_dlt_2",
            "numeric_threshold",
            "CM_DLT.2",
        ),
        serialization_alias="CM_DLT.2",
        title="numeric threshold",
    )

    cm_dlt_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_dlt_3",
            "change",
            "CM_DLT.3",
        ),
        serialization_alias="CM_DLT.3",
        title="change",
    )

    cm_dlt_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_dlt_4",
            "length_of_time_days",
            "CM_DLT.4",
        ),
        serialization_alias="CM_DLT.4",
        title="length of time-days",
    )

    @field_validator("cm_dlt_2", "cm_dlt_4", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
