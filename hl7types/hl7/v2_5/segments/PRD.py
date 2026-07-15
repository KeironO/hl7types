"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: PRD
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.PL import PL
from ..datatypes.PLN import PLN
from ..datatypes.TS import TS
from ..datatypes.XAD import XAD
from ..datatypes.XPN import XPN
from ..datatypes.XTN import XTN


class PRD(HL7Model):
    """Provider Data (S11.6.3).

    Attributes
    ----------
    prd_1 : list[CE]
        PRD.1 - Provider Role (CE) R rep S11.6.3.1 | 0286 - Provider role

    prd_2 : list[XPN] | None
        PRD.2 - Provider Name (XPN) O rep S11.6.3.2

    prd_3 : list[XAD] | None
        PRD.3 - Provider Address (XAD) O rep S11.6.3.3

    prd_4 : PL | None
        PRD.4 - Provider Location (PL) O S11.6.3.4

    prd_5 : list[XTN] | None
        PRD.5 - Provider Communication Information (XTN) O rep S11.6.3.5

    prd_6 : CE | None
        PRD.6 - Preferred Method of Contact (CE) O S11.6.3.6 | 0185 - Preferred method of contact

    prd_7 : list[PLN] | None
        PRD.7 - Provider Identifiers (PLN) O rep S11.6.3.7

    prd_8 : TS | None
        PRD.8 - Effective Start Date of Provider Role (TS) O S11.6.3.8

    prd_9 : TS | None
        PRD.9 - Effective End Date of Provider Role (TS) O S11.6.3.9
    """

    prd_1: List[CE] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "prd_1",
            "provider_role",
            "PRD.1",
        ),
        serialization_alias="PRD.1",
        title="Provider Role",
        description="R | Item #01155 | Table 0286 - Provider role",
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
        description="O | Item #01156",
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
        description="O | Item #01157",
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
        description="O | Item #01158",
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
        description="O | Item #01159",
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
        description=(
            "O | Item #00684 | Table 0185 - Preferred method of contact"
        ),
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
        description="O | Item #01162",
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
        description="O | Item #01163",
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
        description="O | Item #01164",
    )

    model_config = {"populate_by_name": True}
