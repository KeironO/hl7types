"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: AUT
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.CP import CP
from ..datatypes.EI import EI
from ..datatypes.TS import TS


class AUT(HL7Model):
    """Authorization Information (S11.6.2).

    Attributes
    ----------
    aut_1 : CE | None
        AUT.1 - Authorizing Payor, Plan ID (CE) O S11.6.2.1 | 0072 - Insurance Plan ID

    aut_2 : CE
        AUT.2 - Authorizing Payor, Company ID (CE) R S11.6.2.2 | 0285 - Insurance company ID codes

    aut_3 : str | None
        AUT.3 - Authorizing Payor, Company Name (ST) O S11.6.2.3

    aut_4 : TS | None
        AUT.4 - Authorization Effective Date (TS) O S11.6.2.4

    aut_5 : TS | None
        AUT.5 - Authorization Expiration Date (TS) O S11.6.2.5

    aut_6 : EI | None
        AUT.6 - Authorization Identifier (EI) C S11.6.2.6

    aut_7 : CP | None
        AUT.7 - Reimbursement Limit (CP) O S11.6.2.7

    aut_8 : str | None
        AUT.8 - Requested Number of Treatments (NM) O S11.6.2.8

    aut_9 : str | None
        AUT.9 - Authorized Number of Treatments (NM) O S11.6.2.9

    aut_10 : TS | None
        AUT.10 - Process Date (TS) O S11.6.1.9
    """

    aut_1: Optional[CE] = Field(
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

    aut_2: CE = Field(
        validation_alias=AliasChoices(
            "aut_2",
            "authorizing_payor_company_id",
            "AUT.2",
        ),
        serialization_alias="AUT.2",
        title="Authorizing Payor, Company ID",
        description="R | Item #01147 | Table 0285 - Insurance company ID codes",
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
        description="O | Item #01148 | LEN:45",
    )

    aut_4: Optional[TS] = Field(
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

    aut_5: Optional[TS] = Field(
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

    aut_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_8",
            "requested_number_of_treatments",
            "AUT.8",
        ),
        serialization_alias="AUT.8",
        title="Requested Number of Treatments",
        description="O | Item #01153 | LEN:2",
    )

    aut_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_9",
            "authorized_number_of_treatments",
            "AUT.9",
        ),
        serialization_alias="AUT.9",
        title="Authorized Number of Treatments",
        description="O | Item #01154 | LEN:2",
    )

    aut_10: Optional[TS] = Field(
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

    @field_validator("aut_8", "aut_9", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
