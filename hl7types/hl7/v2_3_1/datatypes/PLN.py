"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
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
            "id_number_st",
            "PLN.1",
        ),
        serialization_alias="PLN.1",
        title="ID number (ST)",
    )

    pln_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pln_2",
            "type_of_id_number_is",
            "PLN.2",
        ),
        serialization_alias="PLN.2",
        title="type of ID number (IS)",
    )

    pln_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pln_3",
            "state_other_qualifying_info",
            "PLN.3",
        ),
        serialization_alias="PLN.3",
        title="state/other qualifying info",
    )

    pln_4: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pln_4",
            "expiration_date",
            "PLN.4",
        ),
        serialization_alias="PLN.4",
        title="expiration date",
    )

    model_config = {"populate_by_name": True}
