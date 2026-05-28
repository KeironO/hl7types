"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: PRA
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE


class PRA(BaseModel):
    """HL7 v2 PRA segment."""

    pra_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "pra_1",
            "pra_primary_key_value",
            "PRA.1",
        ),
        serialization_alias="PRA.1",
        title="PRA - primary key value",
        description="Item #685",
    )

    pra_2: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pra_2",
            "practitioner_group",
            "PRA.2",
        ),
        serialization_alias="PRA.2",
        title="Practitioner group",
        description="Item #686",
    )

    pra_3: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pra_3",
            "practitioner_category",
            "PRA.3",
        ),
        serialization_alias="PRA.3",
        title="Practitioner Category",
        description="Item #687 | Table HL70186",
    )

    pra_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pra_4",
            "provider_billing",
            "PRA.4",
        ),
        serialization_alias="PRA.4",
        title="Provider Billing",
        description="Item #688 | Table HL70187",
    )

    pra_5: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pra_5",
            "specialty",
            "PRA.5",
        ),
        serialization_alias="PRA.5",
        title="Specialty",
        description="Item #689",
    )

    pra_6: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pra_6",
            "practitioner_id_numbers",
            "PRA.6",
        ),
        serialization_alias="PRA.6",
        title="Practitioner ID Numbers",
        description="Item #690",
    )

    pra_7: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pra_7",
            "privileges",
            "PRA.7",
        ),
        serialization_alias="PRA.7",
        title="Privileges",
        description="Item #691",
    )

    model_config = {"populate_by_name": True}
