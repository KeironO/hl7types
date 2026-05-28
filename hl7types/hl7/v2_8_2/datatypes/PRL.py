"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: PRL
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from .CWE import CWE
from .OG import OG
from .TX import TX


class PRL(BaseModel):
    """HL7 v2 PRL data type."""

    prl_1: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "prl_1",
            "parent_observation_identifier",
            "PRL.1",
        ),
        serialization_alias="PRL.1",
        title="Parent Observation Identifier",
    )

    prl_2: Optional[OG] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prl_2",
            "parent_observation_sub_identifier",
            "PRL.2",
        ),
        serialization_alias="PRL.2",
        title="Parent Observation Sub-identifier",
    )

    prl_3: Optional[TX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prl_3",
            "parent_observation_value_descriptor",
            "PRL.3",
        ),
        serialization_alias="PRL.3",
        title="Parent Observation Value Descriptor",
    )

    model_config = {"populate_by_name": True}
