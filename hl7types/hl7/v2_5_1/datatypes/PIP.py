"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: PIP
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from .CE import CE
from .EI import EI


class PIP(HL7Model):
    """HL7 v2 PIP data type.

    Attributes
    ----------
    pip_1 : CE | None
        PIP.1 (opt) - Privilege (CE)

    pip_2 : CE | None
        PIP.2 (opt) - Privilege Class (CE)

    pip_3 : str | None
        PIP.3 (opt) - Expiration Date (DT)

    pip_4 : str | None
        PIP.4 (opt) - Activation Date (DT)

    pip_5 : EI | None
        PIP.5 (opt) - Facility (EI)
    """

    pip_1: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pip_1",
            "privilege",
            "PIP.1",
        ),
        serialization_alias="PIP.1",
        title="Privilege",
    )

    pip_2: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pip_2",
            "privilege_class",
            "PIP.2",
        ),
        serialization_alias="PIP.2",
        title="Privilege Class",
    )

    pip_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pip_3",
            "expiration_date",
            "PIP.3",
        ),
        serialization_alias="PIP.3",
        title="Expiration Date",
    )

    pip_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pip_4",
            "activation_date",
            "PIP.4",
        ),
        serialization_alias="PIP.4",
        title="Activation Date",
    )

    pip_5: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pip_5",
            "facility",
            "PIP.5",
        ),
        serialization_alias="PIP.5",
        title="Facility",
    )

    @field_validator("pip_3", "pip_4", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2})?)?)?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    model_config = {"populate_by_name": True}
