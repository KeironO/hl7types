"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: CM_PLN
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class CM_PLN(BaseModel):
    """HL7 v2 CM_PLN data type.

    Attributes
    ----------
    cm_pln_1 : str | None
        CM_PLN.1 (opt) - ID number (ST)

    cm_pln_2 : str | None
        CM_PLN.2 (opt) - type of ID number (ID) (ID)

    cm_pln_3 : str | None
        CM_PLN.3 (opt) - state/other qualifiying info (ST)
    """

    cm_pln_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_pln_1",
            "id_number",
            "CM_PLN.1",
        ),
        serialization_alias="CM_PLN.1",
        title="ID number",
    )

    cm_pln_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_pln_2",
            "type_of_id_number_id",
            "CM_PLN.2",
        ),
        serialization_alias="CM_PLN.2",
        title="type of ID number (ID)",
    )

    cm_pln_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_pln_3",
            "state_other_qualifiying_info",
            "CM_PLN.3",
        ),
        serialization_alias="CM_PLN.3",
        title="state/other qualifiying info",
    )

    model_config = {"populate_by_name": True}
