"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: PIP
Type: Datatype
"""
from __future__ import annotations

import re

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from .CWE import CWE
from .EI import EI

_RE_DT = re.compile(r'(\d{4}([01]\d(\d{2})?)?)?')


class PIP(HL7Model):
    """Practitioner institutional privileges (S2.A.52).

    Attributes
    ----------
    pip_1 : CWE
        PIP.1 (req) - Privilege (CWE)

    pip_2 : CWE | None
        PIP.2 (opt) - Privilege Class (CWE)

    pip_3 : str | None
        PIP.3 (opt) - Expiration Date (DT)

    pip_4 : str | None
        PIP.4 (opt) - Activation Date (DT)

    pip_5 : EI | None
        PIP.5 (opt) - Facility (EI)
    """

    pip_1: CWE = Field(
        validation_alias=AliasChoices(
            "pip_1",
            "privilege",
            "PIP.1",
        ),
        serialization_alias="PIP.1",
        title="Privilege",
    )

    pip_2: Optional[CWE] = Field(
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
        if not _RE_DT.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    model_config = ConfigDict(populate_by_name=True)
