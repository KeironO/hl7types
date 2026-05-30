"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: CTD
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.PL import PL
from ..datatypes.PLN import PLN
from ..datatypes.XAD import XAD
from ..datatypes.XPN import XPN
from ..datatypes.XTN import XTN


class CTD(HL7Model):
    """HL7 v2 CTD segment.

    Attributes
    ----------
    ctd_1 : list[CE]
        CTD.1 (req, rep) - Contact Role (CE)

    ctd_2 : list[XPN] | None
        CTD.2 (opt, rep) - Contact Name (XPN)

    ctd_3 : list[XAD] | None
        CTD.3 (opt, rep) - Contact Address (XAD)

    ctd_4 : PL | None
        CTD.4 (opt) - Contact Location (PL)

    ctd_5 : list[XTN] | None
        CTD.5 (opt, rep) - Contact Communication Information (XTN)

    ctd_6 : CE | None
        CTD.6 (opt) - Preferred Method of Contact (CE)

    ctd_7 : list[PLN] | None
        CTD.7 (opt, rep) - Contact Identifiers (PLN)
    """

    ctd_1: List[CE] = Field(
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

    ctd_2: Optional[List[XPN]] = Field(
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

    ctd_3: Optional[List[XAD]] = Field(
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

    ctd_4: Optional[PL] = Field(
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

    ctd_5: Optional[List[XTN]] = Field(
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

    ctd_6: Optional[CE] = Field(
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

    ctd_7: Optional[List[PLN]] = Field(
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
