"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: UVC
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model


class UVC(HL7Model):
    """HL7 v2 UVC data type.

    Attributes
    ----------
    uvc_1 : str | None
        UVC.1 (opt) - value code (IS)

    uvc_2 : str | None
        UVC.2 (opt) - value amount (NM)
    """

    uvc_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "uvc_1",
            "value_code",
            "UVC.1",
        ),
        serialization_alias="UVC.1",
        title="value code",
    )

    uvc_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "uvc_2",
            "value_amount",
            "UVC.2",
        ),
        serialization_alias="UVC.2",
        title="value amount",
    )

    @field_validator("uvc_2", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
