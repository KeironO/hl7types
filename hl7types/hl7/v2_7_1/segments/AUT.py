"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: AUT
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CP import CP
from ..datatypes.CQ import CQ
from ..datatypes.CWE import CWE
from ..datatypes.EI import EI


class AUT(BaseModel):
    """HL7 v2 AUT segment."""

    aut_1: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_1",
            "authorizing_payor_plan_id",
            "AUT.1",
        ),
        serialization_alias="AUT.1",
        title="Authorizing Payor, Plan ID",
        description="Item #1146 | Table HL70072",
    )

    aut_2: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "aut_2",
            "authorizing_payor_company_id",
            "AUT.2",
        ),
        serialization_alias="AUT.2",
        title="Authorizing Payor, Company ID",
        description="Item #1147 | Table HL70285",
    )

    aut_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_3",
            "authorizing_payor_company_name",
            "AUT.3",
        ),
        serialization_alias="AUT.3",
        title="Authorizing Payor, Company Name",
        description="Item #1148",
    )

    aut_4: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_4",
            "authorization_effective_date",
            "AUT.4",
        ),
        serialization_alias="AUT.4",
        title="Authorization Effective Date",
        description="Item #1149",
    )

    aut_5: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_5",
            "authorization_expiration_date",
            "AUT.5",
        ),
        serialization_alias="AUT.5",
        title="Authorization Expiration Date",
        description="Item #1150",
    )

    aut_6: EI | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_6",
            "authorization_identifier",
            "AUT.6",
        ),
        serialization_alias="AUT.6",
        title="Authorization Identifier",
        description="Item #1151",
    )

    aut_7: CP | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_7",
            "reimbursement_limit",
            "AUT.7",
        ),
        serialization_alias="AUT.7",
        title="Reimbursement Limit",
        description="Item #1152",
    )

    aut_8: CQ | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_8",
            "requested_number_of_treatments",
            "AUT.8",
        ),
        serialization_alias="AUT.8",
        title="Requested Number of Treatments",
        description="Item #1153",
    )

    aut_9: CQ | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_9",
            "authorized_number_of_treatments",
            "AUT.9",
        ),
        serialization_alias="AUT.9",
        title="Authorized Number of Treatments",
        description="Item #1154",
    )

    aut_10: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_10",
            "process_date",
            "AUT.10",
        ),
        serialization_alias="AUT.10",
        title="Process Date",
        description="Item #1145",
    )

    aut_11: list[CWE] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_11",
            "requested_discipline_s",
            "AUT.11",
        ),
        serialization_alias="AUT.11",
        title="Requested Discipline(s)",
        description="Item #2375",
    )

    aut_12: list[CWE] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_12",
            "authorized_discipline_s",
            "AUT.12",
        ),
        serialization_alias="AUT.12",
        title="Authorized Discipline(s)",
        description="Item #2376",
    )

    model_config = {"populate_by_name": True}
