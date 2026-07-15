"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: CTD
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE
from ..datatypes.PL import PL
from ..datatypes.PLN import PLN
from ..datatypes.XAD import XAD
from ..datatypes.XPN import XPN
from ..datatypes.XTN import XTN


class CTD(HL7Model):
    """Contact Data (S11.8.4).

    Attributes
    ----------
    ctd_1 : list[CWE]
        CTD.1 - Contact Role (CWE) R rep S11.8.4.1 | 0131 - Contact Role

    ctd_2 : list[XPN] | None
        CTD.2 - Contact Name (XPN) O rep S11.8.4.2

    ctd_3 : list[XAD] | None
        CTD.3 - Contact Address (XAD) O rep S11.8.4.3

    ctd_4 : PL | None
        CTD.4 - Contact Location (PL) O S11.8.4.4

    ctd_5 : list[XTN] | None
        CTD.5 - Contact Communication Information (XTN) O rep S11.8.4.5

    ctd_6 : CWE | None
        CTD.6 - Preferred Method of Contact (CWE) O S11.8.3.6 | 0185 - Preferred Method of Contact

    ctd_7 : list[PLN] | None
        CTD.7 - Contact Identifiers (PLN) O rep S11.8.4.7 | 0338 - Practitioner ID Number Type
    """

    ctd_1: List[CWE] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "ctd_1",
            "contact_role",
            "CTD.1",
        ),
        serialization_alias="CTD.1",
        title="Contact Role",
        description="R | Item #00196 | Table 0131 - Contact Role",
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
        description="O | Item #01166",
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

    ctd_6: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ctd_6",
            "preferred_method_of_contact",
            "CTD.6",
        ),
        serialization_alias="CTD.6",
        title="Preferred Method of Contact",
        description=(
            "O | Item #00684 | Table 0185 - Preferred Method of Contact"
        ),
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
        description=(
            "O | Item #01171 | Table 0338 - Practitioner ID Number Type"
        ),
    )

    model_config = {"populate_by_name": True}
