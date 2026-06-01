"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: CM_ELD
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator

from .CE import CE


class CM_ELD(HL7Model):
    """HL7 v2 CM_ELD data type.

    Attributes
    ----------
    cm_eld_1 : str | None
        CM_ELD.1 (opt) - Segment-ID (ST)

    cm_eld_2 : str | None
        CM_ELD.2 (opt) - Sequence (NM)

    cm_eld_3 : str | None
        CM_ELD.3 (opt) - Field-Position (NM)

    cm_eld_4 : CE | None
        CM_ELD.4 (opt) - Code Identifying Error (CE)
    """

    cm_eld_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_eld_1",
            "segment_id",
            "CM_ELD.1",
        ),
        serialization_alias="CM_ELD.1",
        title="Segment-ID",
    )

    cm_eld_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_eld_2",
            "sequence",
            "CM_ELD.2",
        ),
        serialization_alias="CM_ELD.2",
        title="Sequence",
    )

    cm_eld_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_eld_3",
            "field_position",
            "CM_ELD.3",
        ),
        serialization_alias="CM_ELD.3",
        title="Field-Position",
    )

    cm_eld_4: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_eld_4",
            "code_identifying_error",
            "CM_ELD.4",
        ),
        serialization_alias="CM_ELD.4",
        title="Code Identifying Error",
    )

    @field_validator("cm_eld_2", "cm_eld_3", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
