"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
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
        PIP.1 (opt) - privilege (CE)

    pip_2 : CE | None
        PIP.2 (opt) - privilege class (CE)

    pip_3 : str | None
        PIP.3 (opt) - expiration date (DT)

    pip_4 : str | None
        PIP.4 (opt) - activation date (DT)

    pip_5 : EI | None
        PIP.5 (opt) - facility (EI) (EI)
    """

    pip_1: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pip_1",
            "privilege",
            "PIP.1",
        ),
        serialization_alias="PIP.1",
        title="privilege",
    )

    pip_2: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pip_2",
            "privilege_class",
            "PIP.2",
        ),
        serialization_alias="PIP.2",
        title="privilege class",
    )

    pip_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pip_3",
            "expiration_date",
            "PIP.3",
        ),
        serialization_alias="PIP.3",
        title="expiration date",
    )

    pip_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pip_4",
            "activation_date",
            "PIP.4",
        ),
        serialization_alias="PIP.4",
        title="activation date",
    )

    pip_5: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pip_5",
            "facility_ei",
            "PIP.5",
        ),
        serialization_alias="PIP.5",
        title="facility (EI)",
    )

    @field_validator("pip_3", "pip_4", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2})?)?)?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    model_config = {"populate_by_name": True}
