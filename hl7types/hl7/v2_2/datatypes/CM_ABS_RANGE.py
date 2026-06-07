"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: CM_ABS_RANGE
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model


class CM_ABS_RANGE(HL7Model):
    """HL7 v2 CM_ABS_RANGE data type.

    Attributes
    ----------
    cm_abs_range_1 : str | None
        CM_ABS_RANGE.1 (opt) - Range (CM)

    cm_abs_range_2 : str | None
        CM_ABS_RANGE.2 (opt) - Numeric Change (NM)

    cm_abs_range_3 : str | None
        CM_ABS_RANGE.3 (opt) - Percent per Change (NM)

    cm_abs_range_4 : str | None
        CM_ABS_RANGE.4 (opt) - Days (NM)
    """

    cm_abs_range_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_abs_range_1",
            "range",
            "CM_ABS_RANGE.1",
        ),
        serialization_alias="CM_ABS_RANGE.1",
        title="Range",
    )

    cm_abs_range_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_abs_range_2",
            "numeric_change",
            "CM_ABS_RANGE.2",
        ),
        serialization_alias="CM_ABS_RANGE.2",
        title="Numeric Change",
    )

    cm_abs_range_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_abs_range_3",
            "percent_per_change",
            "CM_ABS_RANGE.3",
        ),
        serialization_alias="CM_ABS_RANGE.3",
        title="Percent per Change",
    )

    cm_abs_range_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_abs_range_4",
            "days",
            "CM_ABS_RANGE.4",
        ),
        serialization_alias="CM_ABS_RANGE.4",
        title="Days",
    )

    @field_validator("cm_abs_range_2", "cm_abs_range_3", "cm_abs_range_4", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
