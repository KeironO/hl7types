"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: PRD
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CWE import CWE
from ..datatypes.PL import PL
from ..datatypes.PLN import PLN
from ..datatypes.XAD import XAD
from ..datatypes.XON import XON
from ..datatypes.XPN import XPN
from ..datatypes.XTN import XTN


class PRD(BaseModel):
    """HL7 v2 PRD segment."""

    prd_1: list[CWE] = Field(
        default=...,
        validation_alias=AliasChoices(
            "prd_1",
            "provider_role",
            "PRD.1",
        ),
        serialization_alias="PRD.1",
        title="Provider Role",
        description="Item #1155 | Table HL70286",
    )

    prd_2: list[XPN] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "prd_2",
            "provider_name",
            "PRD.2",
        ),
        serialization_alias="PRD.2",
        title="Provider Name",
        description="Item #1156",
    )

    prd_3: list[XAD] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "prd_3",
            "provider_address",
            "PRD.3",
        ),
        serialization_alias="PRD.3",
        title="Provider Address",
        description="Item #1157",
    )

    prd_4: PL | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "prd_4",
            "provider_location",
            "PRD.4",
        ),
        serialization_alias="PRD.4",
        title="Provider Location",
        description="Item #1158",
    )

    prd_5: list[XTN] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "prd_5",
            "provider_communication_information",
            "PRD.5",
        ),
        serialization_alias="PRD.5",
        title="Provider Communication Information",
        description="Item #1159",
    )

    prd_6: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "prd_6",
            "preferred_method_of_contact",
            "PRD.6",
        ),
        serialization_alias="PRD.6",
        title="Preferred Method of Contact",
        description="Item #684 | Table HL70185",
    )

    prd_7: list[PLN] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "prd_7",
            "provider_identifiers",
            "PRD.7",
        ),
        serialization_alias="PRD.7",
        title="Provider Identifiers",
        description="Item #1162 | Table HL70338",
    )

    prd_8: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "prd_8",
            "effective_start_date_of_provider_role",
            "PRD.8",
        ),
        serialization_alias="PRD.8",
        title="Effective Start Date of Provider Role",
        description="Item #1163",
    )

    prd_9: list[str] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "prd_9",
            "effective_end_date_of_provider_role",
            "PRD.9",
        ),
        serialization_alias="PRD.9",
        title="Effective End Date of Provider Role",
        description="Item #1164",
    )

    prd_10: XON | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "prd_10",
            "provider_organization_name_and_identifier",
            "PRD.10",
        ),
        serialization_alias="PRD.10",
        title="Provider Organization Name and Identifier",
        description="Item #2256",
    )

    prd_11: list[XAD] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "prd_11",
            "provider_organization_address",
            "PRD.11",
        ),
        serialization_alias="PRD.11",
        title="Provider Organization Address",
        description="Item #2257",
    )

    prd_12: list[PL] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "prd_12",
            "provider_organization_location_information",
            "PRD.12",
        ),
        serialization_alias="PRD.12",
        title="Provider Organization Location Information",
        description="Item #2258",
    )

    prd_13: list[XTN] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "prd_13",
            "provider_organization_communication_information",
            "PRD.13",
        ),
        serialization_alias="PRD.13",
        title="Provider Organization Communication Information",
        description="Item #2259",
    )

    prd_14: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "prd_14",
            "provider_organization_method_of_contact",
            "PRD.14",
        ),
        serialization_alias="PRD.14",
        title="Provider Organization Method of Contact",
        description="Item #2260 | Table HL70185",
    )

    model_config = {"populate_by_name": True}
