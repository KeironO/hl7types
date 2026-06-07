"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: CM_PTA
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model


class CM_PTA(HL7Model):
    """HL7 v2 CM_PTA data type.

    Attributes
    ----------
    cm_pta_1 : str | None
        CM_PTA.1 (opt) - policy type (IS)

    cm_pta_2 : str | None
        CM_PTA.2 (opt) - amount class (IS)

    cm_pta_3 : str | None
        CM_PTA.3 (opt) - amount (NM)
    """

    cm_pta_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_pta_1",
            "policy_type",
            "CM_PTA.1",
        ),
        serialization_alias="CM_PTA.1",
        title="policy type",
    )

    cm_pta_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_pta_2",
            "amount_class",
            "CM_PTA.2",
        ),
        serialization_alias="CM_PTA.2",
        title="amount class",
    )

    cm_pta_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_pta_3",
            "amount",
            "CM_PTA.3",
        ),
        serialization_alias="CM_PTA.3",
        title="amount",
    )

    @field_validator("cm_pta_3", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
