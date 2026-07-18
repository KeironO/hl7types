"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: AUT
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, ValidationInfo, field_validator
from hl7types.hl7 import HL7Model
from hl7types.hl7._validators import _apply_dt_fallback

from ..datatypes.CP import CP
from ..datatypes.CQ import CQ
from ..datatypes.CWE import CWE
from ..datatypes.EI import EI

_RE_DTM = re.compile(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?')


class AUT(HL7Model):
    """Authorization Information (S11.7.2).

    Attributes
    ----------
    aut_1 : CWE | None
        AUT.1 - Authorizing Payor, Plan ID (CWE) O S11.7.2.1 | 0072 - Insurance Plan ID

    aut_2 : CWE
        AUT.2 - Authorizing Payor, Company ID (CWE) R S11.7.2.2 | 0285 - Insurance Company ID Codes

    aut_3 : str | None
        AUT.3 - Authorizing Payor, Company Name (ST) O S11.7.2.3

    aut_4 : str | None
        AUT.4 - Authorization Effective Date (DTM) O S11.7.2.4

    aut_5 : str | None
        AUT.5 - Authorization Expiration Date (DTM) O S11.7.2.5

    aut_6 : EI | None
        AUT.6 - Authorization Identifier (EI) C S11.7.2.6

    aut_7 : CP | None
        AUT.7 - Reimbursement Limit (CP) O S11.7.2.7

    aut_8 : CQ | None
        AUT.8 - Requested Number of Treatments (CQ) O S11.7.2.8

    aut_9 : CQ | None
        AUT.9 - Authorized Number of Treatments (CQ) O S11.7.2.9

    aut_10 : str | None
        AUT.10 - Process Date (DTM) O S11.7.1.9

    aut_11 : list[CWE] | None
        AUT.11 - Requested Discipline(s) (CWE) O rep S11.7.2.11

    aut_12 : list[CWE] | None
        AUT.12 - Authorized Discipline(s) (CWE) O rep S11.7.2.12
    """

    aut_1: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_1",
            "authorizing_payor_plan_id",
            "AUT.1",
        ),
        serialization_alias="AUT.1",
        title="Authorizing Payor, Plan ID",
        description="O | Item #01146 | Table 0072 - Insurance Plan ID",
    )

    aut_2: CWE = Field(
        validation_alias=AliasChoices(
            "aut_2",
            "authorizing_payor_company_id",
            "AUT.2",
        ),
        serialization_alias="AUT.2",
        title="Authorizing Payor, Company ID",
        description="R | Item #01147 | Table 0285 - Insurance Company ID Codes",
    )

    aut_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_3",
            "authorizing_payor_company_name",
            "AUT.3",
        ),
        serialization_alias="AUT.3",
        title="Authorizing Payor, Company Name",
        description="O | Item #01148",
    )

    aut_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_4",
            "authorization_effective_date",
            "AUT.4",
        ),
        serialization_alias="AUT.4",
        title="Authorization Effective Date",
        description="O | Item #01149",
    )

    aut_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_5",
            "authorization_expiration_date",
            "AUT.5",
        ),
        serialization_alias="AUT.5",
        title="Authorization Expiration Date",
        description="O | Item #01150",
    )

    aut_6: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_6",
            "authorization_identifier",
            "AUT.6",
        ),
        serialization_alias="AUT.6",
        title="Authorization Identifier",
        description="C | Item #01151",
    )

    aut_7: Optional[CP] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_7",
            "reimbursement_limit",
            "AUT.7",
        ),
        serialization_alias="AUT.7",
        title="Reimbursement Limit",
        description="O | Item #01152",
    )

    aut_8: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_8",
            "requested_number_of_treatments",
            "AUT.8",
        ),
        serialization_alias="AUT.8",
        title="Requested Number of Treatments",
        description="O | Item #01153",
    )

    aut_9: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_9",
            "authorized_number_of_treatments",
            "AUT.9",
        ),
        serialization_alias="AUT.9",
        title="Authorized Number of Treatments",
        description="O | Item #01154",
    )

    aut_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_10",
            "process_date",
            "AUT.10",
        ),
        serialization_alias="AUT.10",
        title="Process Date",
        description="O | Item #01145",
    )

    aut_11: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_11",
            "requested_discipline_s",
            "AUT.11",
        ),
        serialization_alias="AUT.11",
        title="Requested Discipline(s)",
        description="O | Item #02375",
    )

    aut_12: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_12",
            "authorized_discipline_s",
            "AUT.12",
        ),
        serialization_alias="AUT.12",
        title="Authorized Discipline(s)",
        description="O | Item #02376",
    )

    @field_validator("aut_4", "aut_5", "aut_10", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        if _RE_DTM.fullmatch(v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = ConfigDict(populate_by_name=True)
