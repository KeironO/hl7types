"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: CM_BATCH_TOTAL
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator


class CM_BATCH_TOTAL(HL7Model):
    """HL7 v2 CM_BATCH_TOTAL data type.

    Attributes
    ----------
    cm_batch_total_1 : str | None
        CM_BATCH_TOTAL.1 (opt) - Batch total 1 (NM)

    cm_batch_total_2 : str | None
        CM_BATCH_TOTAL.2 (opt) - Batch total 2 (NM)
    """

    cm_batch_total_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_batch_total_1",
            "batch_total_1",
            "CM_BATCH_TOTAL.1",
        ),
        serialization_alias="CM_BATCH_TOTAL.1",
        title="Batch total 1",
    )

    cm_batch_total_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_batch_total_2",
            "batch_total_2",
            "CM_BATCH_TOTAL.2",
        ),
        serialization_alias="CM_BATCH_TOTAL.2",
        title="Batch total 2",
    )

    @field_validator("cm_batch_total_1", "cm_batch_total_2", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
