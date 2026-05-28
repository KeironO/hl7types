"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: CTD
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE
from ..datatypes.PI import PI
from ..datatypes.PL import PL
from ..datatypes.XAD import XAD
from ..datatypes.XPN import XPN
from ..datatypes.XTN import XTN


class CTD(BaseModel):
    """HL7 v2 CTD segment."""

    ctd_1: list[CE] = Field(
        default=...,
        validation_alias=AliasChoices(
            "ctd_1",
            "contact_role",
            "CTD.1",
        ),
        serialization_alias="CTD.1",
        title="Contact Role",
        description="Item #196 | Table HL70131",
    )

    ctd_2: list[XPN] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ctd_2",
            "contact_name",
            "CTD.2",
        ),
        serialization_alias="CTD.2",
        title="Contact Name",
        description="Item #1165",
    )

    ctd_3: list[XAD] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ctd_3",
            "contact_address",
            "CTD.3",
        ),
        serialization_alias="CTD.3",
        title="Contact Address",
        description="Item #1166",
    )

    ctd_4: PL | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ctd_4",
            "contact_location",
            "CTD.4",
        ),
        serialization_alias="CTD.4",
        title="Contact Location",
        description="Item #1167",
    )

    ctd_5: list[XTN] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ctd_5",
            "contact_communication_information",
            "CTD.5",
        ),
        serialization_alias="CTD.5",
        title="Contact Communication Information",
        description="Item #1168",
    )

    ctd_6: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ctd_6",
            "preferred_method_of_contact",
            "CTD.6",
        ),
        serialization_alias="CTD.6",
        title="Preferred Method of Contact",
        description="Item #684 | Table HL70185",
    )

    ctd_7: list[PI] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ctd_7",
            "contact_identifiers",
            "CTD.7",
        ),
        serialization_alias="CTD.7",
        title="Contact Identifiers",
        description="Item #1171",
    )

    model_config = {"populate_by_name": True}
