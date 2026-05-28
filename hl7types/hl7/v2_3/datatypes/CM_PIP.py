"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: CM_PIP
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from .CE import CE


class CM_PIP(BaseModel):
    """HL7 v2 CM_PIP data type."""

    cm_pip_1: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_pip_1",
            "privilege",
            "CM_PIP.1",
        ),
        serialization_alias="CM_PIP.1",
        title="privilege",
    )

    cm_pip_2: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_pip_2",
            "privilege_class",
            "CM_PIP.2",
        ),
        serialization_alias="CM_PIP.2",
        title="privilege class",
    )

    cm_pip_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_pip_3",
            "expiration_date",
            "CM_PIP.3",
        ),
        serialization_alias="CM_PIP.3",
        title="expiration date",
    )

    cm_pip_4: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_pip_4",
            "activation_date",
            "CM_PIP.4",
        ),
        serialization_alias="CM_PIP.4",
        title="activation date",
    )

    model_config = {"populate_by_name": True}
