"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: CTD
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.PI import PI
from ..datatypes.PL import PL
from ..datatypes.XAD import XAD
from ..datatypes.XPN import XPN
from ..datatypes.XTN import XTN


class CTD(HL7Model):
    """Contact Data (S11.5.4).

    Attributes
    ----------
    ctd_1 : list[CE] | None
        CTD.1 - Contact Role (CE) NA rep S11.5.4.1 | 0131 - Contact Role

    ctd_2 : list[XPN] | None
        CTD.2 - Contact Name (XPN) O rep S11.5.4.2

    ctd_3 : list[XAD] | None
        CTD.3 - Contact Address (XAD) NA rep S11.5.4.3

    ctd_4 : PL | None
        CTD.4 - Contact Location (PL) O S11.5.4.4

    ctd_5 : list[XTN] | None
        CTD.5 - Contact Communication Information (XTN) O rep S11.5.4.5

    ctd_6 : CE | None
        CTD.6 - Preferred Method Of Contact (CE) NA S11.5.4.6 | 0185 - Preferred method of contact

    ctd_7 : list[PI] | None
        CTD.7 - Contact Identifiers (PI) O rep S11.5.4.7
    """

    ctd_1: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ctd_1",
            "contact_role",
            "CTD.1",
        ),
        serialization_alias="CTD.1",
        title="Contact Role",
        description="NA | Item #00196 | Table 0131 - Contact Role",
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
        description="O | Item #01165",
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
        description="NA | Item #01166",
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
        description="O | Item #01167",
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
        description="O | Item #01168",
    )

    ctd_6: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ctd_6",
            "preferred_method_of_contact",
            "CTD.6",
        ),
        serialization_alias="CTD.6",
        title="Preferred Method Of Contact",
        description=(
            "NA | Item #00684 | Table 0185 - Preferred method of contact"
        ),
    )

    ctd_7: Optional[List[PI]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ctd_7",
            "contact_identifiers",
            "CTD.7",
        ),
        serialization_alias="CTD.7",
        title="Contact Identifiers",
        description="O | Item #01171",
    )

    model_config = ConfigDict(populate_by_name=True)
