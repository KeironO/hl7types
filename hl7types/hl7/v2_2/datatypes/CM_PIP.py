"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: CM_PIP
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator

from .CE import CE


class CM_PIP(HL7Model):
    """HL7 v2 CM_PIP data type.

    Attributes
    ----------
    cm_pip_1 : CE | None
        CM_PIP.1 (opt) - Privilege (CE)

    cm_pip_2 : CE | None
        CM_PIP.2 (opt) - privilege class (CE)

    cm_pip_3 : str | None
        CM_PIP.3 (opt) - expiration date (DT)

    cm_pip_4 : str | None
        CM_PIP.4 (opt) - activation date (DT)
    """

    cm_pip_1: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_pip_1",
            "privilege",
            "CM_PIP.1",
        ),
        serialization_alias="CM_PIP.1",
        title="Privilege",
    )

    cm_pip_2: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_pip_2",
            "privilege_class",
            "CM_PIP.2",
        ),
        serialization_alias="CM_PIP.2",
        title="privilege class",
    )

    cm_pip_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_pip_3",
            "expiration_date",
            "CM_PIP.3",
        ),
        serialization_alias="CM_PIP.3",
        title="expiration date",
    )

    cm_pip_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_pip_4",
            "activation_date",
            "CM_PIP.4",
        ),
        serialization_alias="CM_PIP.4",
        title="activation date",
    )

    @field_validator("cm_pip_3", "cm_pip_4", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2})?)?)?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    model_config = {"populate_by_name": True}
