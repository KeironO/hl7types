"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: PLN
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field


class PLN(BaseModel):
    """HL7 v2 PLN data type."""

    pln_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pln_1",
            "id_number",
            "PLN.1",
        ),
        serialization_alias="PLN.1",
        title="ID Number",
    )

    pln_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pln_2",
            "type_of_id_number",
            "PLN.2",
        ),
        serialization_alias="PLN.2",
        title="Type of ID Number",
    )

    pln_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pln_3",
            "state_other_qualifying_information",
            "PLN.3",
        ),
        serialization_alias="PLN.3",
        title="State/other Qualifying Information",
    )

    pln_4: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pln_4",
            "expiration_date",
            "PLN.4",
        ),
        serialization_alias="PLN.4",
        title="Expiration Date",
    )

    model_config = {"populate_by_name": True}
