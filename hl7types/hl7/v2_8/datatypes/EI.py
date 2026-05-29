"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: EI
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class EI(BaseModel):
    """HL7 v2 EI data type.

    Attributes
    ----------
    ei_1 : str | None
        EI.1 (opt) - Entity Identifier (ST)

    ei_2 : str | None
        EI.2 (opt) - Namespace ID (IS)

    ei_3 : str | None
        EI.3 (opt) - Universal ID (ST)

    ei_4 : str | None
        EI.4 (opt) - Universal ID Type (ID)
    """

    ei_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ei_1",
            "entity_identifier",
            "EI.1",
        ),
        serialization_alias="EI.1",
        title="Entity Identifier",
    )

    ei_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ei_2",
            "namespace_id",
            "EI.2",
        ),
        serialization_alias="EI.2",
        title="Namespace ID",
    )

    ei_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ei_3",
            "universal_id",
            "EI.3",
        ),
        serialization_alias="EI.3",
        title="Universal ID",
    )

    ei_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ei_4",
            "universal_id_type",
            "EI.4",
        ),
        serialization_alias="EI.4",
        title="Universal ID Type",
    )

    model_config = {"populate_by_name": True}
