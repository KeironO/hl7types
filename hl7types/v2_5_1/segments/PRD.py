"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: PRD
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE
from ..datatypes.PL import PL
from ..datatypes.PLN import PLN
from ..datatypes.TS import TS
from ..datatypes.XAD import XAD
from ..datatypes.XPN import XPN
from ..datatypes.XTN import XTN


class PRD(BaseModel):
    """HL7 v2 PRD segment."""

    prd_1: List[CE] = Field(
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

    prd_2: Optional[List[XPN]] = Field(
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

    prd_3: Optional[List[XAD]] = Field(
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

    prd_4: Optional[PL] = Field(
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

    prd_5: Optional[List[XTN]] = Field(
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

    prd_6: Optional[CE] = Field(
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

    prd_7: Optional[List[PLN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prd_7",
            "provider_identifiers",
            "PRD.7",
        ),
        serialization_alias="PRD.7",
        title="Provider Identifiers",
        description="Item #1162",
    )

    prd_8: Optional[TS] = Field(
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

    prd_9: Optional[TS] = Field(
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

    model_config = {"populate_by_name": True}
