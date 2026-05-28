"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: PIP
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from .CE import CE
from .EI import EI


class PIP(BaseModel):
    """HL7 v2 PIP data type."""

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

    model_config = {"populate_by_name": True}
