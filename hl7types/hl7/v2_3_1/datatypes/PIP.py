"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: PIP
Type: Datatype
"""
from __future__ import annotations

import re

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from .CE import CE
from .EI import EI

_RE_DT = re.compile(r'(\d{4}([01]\d(\d{2})?)?)?')


class PIP(HL7Model):
    """Privileges (S8).

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
        if not _RE_DT.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    model_config = ConfigDict(populate_by_name=True)
