"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: PRD
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE
from ..datatypes.PL import PL
from ..datatypes.PLN import PLN
from ..datatypes.XAD import XAD
from ..datatypes.XON import XON
from ..datatypes.XPN import XPN
from ..datatypes.XTN import XTN


class PRD(HL7Model):
    """HL7 v2 PRD segment.

    Attributes
    ----------
    prd_1 : list[CWE] | None
        PRD.1 (req, rep) - Provider Role (CWE) [optional: CWE has no required components]

    prd_2 : list[XPN] | None
        PRD.2 (opt, rep) - Provider Name (XPN)

    prd_3 : list[XAD] | None
        PRD.3 (opt, rep) - Provider Address (XAD)

    prd_4 : PL | None
        PRD.4 (opt) - Provider Location (PL)

    prd_5 : list[XTN] | None
        PRD.5 (opt, rep) - Provider Communication Information (XTN)

    prd_6 : CWE | None
        PRD.6 (opt) - Preferred Method of Contact (CWE)

    prd_7 : list[PLN] | None
        PRD.7 (opt, rep) - Provider Identifiers (PLN)

    prd_8 : str | None
        PRD.8 (opt) - Effective Start Date of Provider Role (DTM)

    prd_9 : list[str] | None
        PRD.9 (opt, rep) - Effective End Date of Provider Role (DTM)

    prd_10 : XON | None
        PRD.10 (opt) - Provider Organization Name and Identifier (XON)

    prd_11 : list[XAD] | None
        PRD.11 (opt, rep) - Provider Organization Address (XAD)

    prd_12 : list[PL] | None
        PRD.12 (opt, rep) - Provider Organization Location Information (PL)

    prd_13 : list[XTN] | None
        PRD.13 (opt, rep) - Provider Organization Communication Information (XTN)

    prd_14 : CWE | None
        PRD.14 (opt) - Provider Organization Method of Contact (CWE)
    """

    prd_1: Optional[List[CWE]] = Field(
        default=None,
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

    prd_6: Optional[CWE] = Field(
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
        description="Item #1162 | Table HL70338",
    )

    prd_8: Optional[str] = Field(
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

    prd_9: Optional[List[str]] = Field(
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

    prd_10: Optional[XON] = Field(
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

    prd_11: Optional[List[XAD]] = Field(
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

    prd_12: Optional[List[PL]] = Field(
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

    prd_13: Optional[List[XTN]] = Field(
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

    prd_14: Optional[CWE] = Field(
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

    @field_validator("prd_8", "prd_9", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 datetime")
        return v

    model_config = {"populate_by_name": True}
