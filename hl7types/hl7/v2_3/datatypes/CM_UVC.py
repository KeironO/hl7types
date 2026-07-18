"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: CM_UVC
Type: Datatype
"""
from __future__ import annotations

import re

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class CM_UVC(HL7Model):
    """Value code and amount.

    Attributes
    ----------
    cm_uvc_1 : str | None
        CM_UVC.1 (opt) - value code (IS)

    cm_uvc_2 : str | None
        CM_UVC.2 (opt) - value amount (NM)
    """

    cm_uvc_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_uvc_1",
            "value_code",
            "CM_UVC.1",
        ),
        serialization_alias="CM_UVC.1",
        title="value code",
    )

    cm_uvc_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_uvc_2",
            "value_amount",
            "CM_UVC.2",
        ),
        serialization_alias="CM_UVC.2",
        title="value amount",
    )

    @field_validator("cm_uvc_2", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
