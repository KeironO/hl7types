"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: CM_PLN
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field


class CM_PLN(BaseModel):
    """HL7 v2 CM_PLN data type."""

    cm_pln_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_pln_1",
            "id_number",
            "CM_PLN.1",
        ),
        serialization_alias="CM_PLN.1",
        title="ID number",
    )

    cm_pln_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_pln_2",
            "type_of_id_number_is",
            "CM_PLN.2",
        ),
        serialization_alias="CM_PLN.2",
        title="type of ID number (IS)",
    )

    cm_pln_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_pln_3",
            "state_other_qualifying_info",
            "CM_PLN.3",
        ),
        serialization_alias="CM_PLN.3",
        title="state/other qualifying info",
    )

    cm_pln_4: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_pln_4",
            "expiration_date",
            "CM_PLN.4",
        ),
        serialization_alias="CM_PLN.4",
        title="expiration date",
    )

    model_config = {"populate_by_name": True}
