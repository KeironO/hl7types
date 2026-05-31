"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: PLN
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model


class PLN(HL7Model):
    """HL7 v2 PLN data type.

    Attributes
    ----------
    pln_1 : str
        PLN.1 (req) - ID Number (ST)

    pln_2 : str
        PLN.2 (req) - Type of ID Number (IS)

    pln_3 : str | None
        PLN.3 (opt) - State/other Qualifying Information (ST)

    pln_4 : str | None
        PLN.4 (opt) - Expiration Date (DT)
    """

    pln_1: str = Field(
        default=...,
        max_length=20,
        validation_alias=AliasChoices(
            "pln_1",
            "id_number",
            "PLN.1",
        ),
        serialization_alias="PLN.1",
        title="ID Number",
    )

    pln_2: str = Field(
        default=...,
        max_length=8,
        validation_alias=AliasChoices(
            "pln_2",
            "type_of_id_number",
            "PLN.2",
        ),
        serialization_alias="PLN.2",
        title="Type of ID Number",
    )

    pln_3: Optional[str] = Field(
        default=None,
        max_length=62,
        validation_alias=AliasChoices(
            "pln_3",
            "state_other_qualifying_information",
            "PLN.3",
        ),
        serialization_alias="PLN.3",
        title="State/other Qualifying Information",
    )

    pln_4: Optional[str] = Field(
        default=None,
        max_length=8,
        validation_alias=AliasChoices(
            "pln_4",
            "expiration_date",
            "PLN.4",
        ),
        serialization_alias="PLN.4",
        title="Expiration Date",
    )

    model_config = {"populate_by_name": True}
