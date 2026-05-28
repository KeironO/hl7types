"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: ISD
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE


class ISD(BaseModel):
    """HL7 v2 ISD segment."""

    isd_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "isd_1",
            "reference_interaction_number_unique_identifier",
            "ISD.1",
        ),
        serialization_alias="ISD.1",
        title="Reference Interaction Number (unique identifier)",
        description="Item #1326",
    )

    isd_2: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "isd_2",
            "interaction_type_identifier",
            "ISD.2",
        ),
        serialization_alias="ISD.2",
        title="Interaction Type Identifier",
        description="Item #1327 | Table HL70368",
    )

    isd_3: CE = Field(
        default=...,
        validation_alias=AliasChoices(
            "isd_3",
            "interaction_active_state",
            "ISD.3",
        ),
        serialization_alias="ISD.3",
        title="Interaction Active State",
        description="Item #1328 | Table HL70387",
    )

    model_config = {"populate_by_name": True}
