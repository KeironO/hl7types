"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: PRA
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE


class PRA(HL7Model):
    """practitioner detail (S9.1.2).

    Attributes
    ----------
    pra_1 : str
        PRA.1 - PRA - primary key value (ST) R S9.1.2.1

    pra_2 : list[CE] | None
        PRA.2 - Practitioner group (CE) NA rep S9.1.2.2

    pra_3 : list[str] | None
        PRA.3 - Practitioner Category (ID) NA rep S9.1.2.3 | 0186 - Practioner Category

    pra_4 : str | None
        PRA.4 - Provider Billing (ID) NA S9.1.2.4 | 0187 - Provider billing

    pra_5 : list[str] | None
        PRA.5 - Specialty (CM) NA rep S9.1.2.5

    pra_6 : list[str] | None
        PRA.6 - Practitioner ID Numbers (CM) NA rep S9.1.2.6

    pra_7 : list[str] | None
        PRA.7 - Privileges (CM) NA rep S9.1.2.7
    """

    pra_1: str = Field(
        validation_alias=AliasChoices(
            "pra_1",
            "pra_primary_key_value",
            "PRA.1",
        ),
        serialization_alias="PRA.1",
        title="PRA - primary key value",
        description="R | Item #00685 | LEN:20",
    )

    pra_2: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pra_2",
            "practitioner_group",
            "PRA.2",
        ),
        serialization_alias="PRA.2",
        title="Practitioner group",
        description="NA | Item #00686",
    )

    pra_3: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pra_3",
            "practitioner_category",
            "PRA.3",
        ),
        serialization_alias="PRA.3",
        title="Practitioner Category",
        description=(
            "NA | Item #00687 | Table 0186 - Practioner Category | LEN:3"
        ),
    )

    pra_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pra_4",
            "provider_billing",
            "PRA.4",
        ),
        serialization_alias="PRA.4",
        title="Provider Billing",
        description="NA | Item #00688 | Table 0187 - Provider billing | LEN:1",
    )

    pra_5: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pra_5",
            "specialty",
            "PRA.5",
        ),
        serialization_alias="PRA.5",
        title="Specialty",
        description="NA | Item #00689",
    )

    pra_6: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pra_6",
            "practitioner_id_numbers",
            "PRA.6",
        ),
        serialization_alias="PRA.6",
        title="Practitioner ID Numbers",
        description="NA | Item #00690",
    )

    pra_7: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pra_7",
            "privileges",
            "PRA.7",
        ),
        serialization_alias="PRA.7",
        title="Privileges",
        description="NA | Item #00691",
    )

    model_config = {"populate_by_name": True}
