"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: PRD
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, ValidationInfo, field_validator
from hl7types.hl7 import HL7Model
from hl7types.hl7._validators import _apply_dt_fallback

from ..datatypes.CWE import CWE
from ..datatypes.PL import PL
from ..datatypes.PLN import PLN
from ..datatypes.XAD import XAD
from ..datatypes.XON import XON
from ..datatypes.XPN import XPN
from ..datatypes.XTN import XTN

_RE_DTM = re.compile(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?')


class PRD(HL7Model):
    """Provider Data (S11.6.3).

    Attributes
    ----------
    prd_1 : list[CWE]
        PRD.1 - Provider Role (CWE) R rep S11.6.3.1 | 0286 - Provider role

    prd_2 : list[XPN] | None
        PRD.2 - Provider Name (XPN) O rep S11.6.3.2

    prd_3 : list[XAD] | None
        PRD.3 - Provider Address (XAD) O rep S11.6.3.3

    prd_4 : PL | None
        PRD.4 - Provider Location (PL) O S11.6.3.4

    prd_5 : list[XTN] | None
        PRD.5 - Provider Communication Information (XTN) O rep S11.6.3.5

    prd_6 : CWE | None
        PRD.6 - Preferred Method of Contact (CWE) O S11.6.3.6 | 0185 - Preferred method of contact

    prd_7 : list[PLN] | None
        PRD.7 - Provider Identifiers (PLN) O rep S11.6.3.7 | 0338 - Practitioner ID number type

    prd_8 : str | None
        PRD.8 - Effective Start Date of Provider Role (DTM) O S11.6.3.8

    prd_9 : list[str] | None
        PRD.9 - Effective End Date of Provider Role (DTM) O rep S11.6.3.9

    prd_10 : XON | None
        PRD.10 - Provider Organization Name and Identifier (XON) O S11.6.3.10

    prd_11 : list[XAD] | None
        PRD.11 - Provider Organization Address (XAD) O rep S11.6.3.11

    prd_12 : list[PL] | None
        PRD.12 - Provider Organization Location Information (PL) O rep S11.6.3.12

    prd_13 : list[XTN] | None
        PRD.13 - Provider Organization Communication Information (XTN) O rep S11.6.3.13

    prd_14 : CWE | None
        PRD.14 - Provider Organization Method of Contact (CWE) O S11.6.3.14 | 0185 - Preferred method of contact
    """

    prd_1: List[CWE] = Field(
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

    prd_6: Optional[CWE] = Field(
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
        description=(
            "O | Item #01162 | Table 0338 - Practitioner ID number type"
        ),
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
        description="O | Item #01163 | LEN:24",
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
        description="O | Item #01164 | LEN:24",
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
        description="O | Item #02256",
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
        description="O | Item #02257",
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
        description="O | Item #02258",
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
        description="O | Item #02259",
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
        description=(
            "O | Item #02260 | Table 0185 - Preferred method of contact"
        ),
    )

    @field_validator("prd_8", "prd_9", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        if _RE_DTM.fullmatch(v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = ConfigDict(populate_by_name=True)
