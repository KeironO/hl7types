"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: OG
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model


class OG(HL7Model):
    """HL7 v2 OG data type.

    Attributes
    ----------
    og_1 : str | None
        OG.1 (opt) - Original Sub-Identifier (ST)

    og_2 : str | None
        OG.2 (opt) - Group (NM)

    og_3 : str | None
        OG.3 (opt) - Sequence (NM)

    og_4 : str | None
        OG.4 (opt) - Identifier (ST)
    """

    og_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "og_1",
            "original_sub_identifier",
            "OG.1",
        ),
        serialization_alias="OG.1",
        title="Original Sub-Identifier",
    )

    og_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "og_2",
            "group",
            "OG.2",
        ),
        serialization_alias="OG.2",
        title="Group",
    )

    og_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "og_3",
            "sequence",
            "OG.3",
        ),
        serialization_alias="OG.3",
        title="Sequence",
    )

    og_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "og_4",
            "identifier",
            "OG.4",
        ),
        serialization_alias="OG.4",
        title="Identifier",
    )

    @field_validator("og_2", "og_3", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
