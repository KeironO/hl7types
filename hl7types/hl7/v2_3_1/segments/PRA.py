"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: PRA
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.PIP import PIP
from ..datatypes.PLN import PLN
from ..datatypes.SPD import SPD


class PRA(HL7Model):
    """HL7 v2 PRA segment.

    Attributes
    ----------
    pra_1 : CE
        PRA.1 (req) - Primary Key Value - PRA (CE)

    pra_2 : list[CE] | None
        PRA.2 (opt, rep) - Practitioner Group (CE)

    pra_3 : list[str] | None
        PRA.3 (opt, rep) - Practitioner Category (IS)

    pra_4 : str | None
        PRA.4 (opt) - Provider Billing (ID)

    pra_5 : list[SPD] | None
        PRA.5 (opt, rep) - Specialty (SPD)

    pra_6 : list[PLN] | None
        PRA.6 (opt, rep) - Practitioner ID Numbers (PLN)

    pra_7 : list[PIP] | None
        PRA.7 (opt, rep) - Privileges (PIP)

    pra_8 : str | None
        PRA.8 (opt) - Date Entered Practice (DT)
    """

    pra_1: CE = Field(
        default=...,
        validation_alias=AliasChoices(
            "pra_1",
            "primary_key_value_pra",
            "PRA.1",
        ),
        serialization_alias="PRA.1",
        title="Primary Key Value - PRA",
        description="Item #685",
    )

    pra_2: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pra_2",
            "practitioner_group",
            "PRA.2",
        ),
        serialization_alias="PRA.2",
        title="Practitioner Group",
        description="Item #686 | Table HL70358",
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
        description="Item #687 | Table HL70186",
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
        description="Item #688 | Table HL70187",
    )

    pra_5: Optional[List[SPD]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pra_5",
            "specialty",
            "PRA.5",
        ),
        serialization_alias="PRA.5",
        title="Specialty",
        description="Item #689 | Table HL70337",
    )

    pra_6: Optional[List[PLN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pra_6",
            "practitioner_id_numbers",
            "PRA.6",
        ),
        serialization_alias="PRA.6",
        title="Practitioner ID Numbers",
        description="Item #690 | Table HL70338",
    )

    pra_7: Optional[List[PIP]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pra_7",
            "privileges",
            "PRA.7",
        ),
        serialization_alias="PRA.7",
        title="Privileges",
        description="Item #691",
    )

    pra_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pra_8",
            "date_entered_practice",
            "PRA.8",
        ),
        serialization_alias="PRA.8",
        title="Date Entered Practice",
        description="Item #1296",
    )

    model_config = {"populate_by_name": True}
