"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: PIP
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from .CE import CE
from .EI import EI


class PIP(BaseModel):
    """HL7 v2 PIP data type."""

    pip_1: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pip_1",
            "privilege",
            "PIP.1",
        ),
        serialization_alias="PIP.1",
        title="privilege",
    )

    pip_2: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pip_2",
            "privilege_class",
            "PIP.2",
        ),
        serialization_alias="PIP.2",
        title="privilege class",
    )

    pip_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pip_3",
            "expiration_date",
            "PIP.3",
        ),
        serialization_alias="PIP.3",
        title="expiration date",
    )

    pip_4: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pip_4",
            "activation_date",
            "PIP.4",
        ),
        serialization_alias="PIP.4",
        title="activation date",
    )

    pip_5: EI | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pip_5",
            "facility_ei",
            "PIP.5",
        ),
        serialization_alias="PIP.5",
        title="facility (EI)",
    )

    model_config = {"populate_by_name": True}
