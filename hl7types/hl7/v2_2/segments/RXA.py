"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: RXA
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.TS import TS

_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class RXA(HL7Model):
    """PHARMACY AADMINISTRATION (S4.8.14).

    Attributes
    ----------
    rxa_1 : str
        RXA.1 - Give Sub-ID Counter (NM) R S4.8.14.1

    rxa_2 : str
        RXA.2 - Administration Sub-ID Counter (NM) R S4.8.14.2

    rxa_3 : TS
        RXA.3 - Date / time start of administration (TS) R S4.8.14.3

    rxa_4 : TS
        RXA.4 - Date / time end of administration (TS) R S4.8.14.4

    rxa_5 : CE
        RXA.5 - Administered Code (CE) R S4.8.14.5

    rxa_6 : str
        RXA.6 - Administered Amount (NM) R S4.8.14.6

    rxa_7 : CE | None
        RXA.7 - Administered Units (CE) C S4.8.14.7

    rxa_8 : CE | None
        RXA.8 - Administered Dosage Form (CE) NA S4.8.14.8

    rxa_9 : str | None
        RXA.9 - Administration Notes (ST) C S4.8.14.9

    rxa_10 : str | None
        RXA.10 - Administering Provider (CN) NA S4.8.14.10

    rxa_11 : str | None
        RXA.11 - Administered-at Location (CM) C S4.8.14.11

    rxa_12 : str | None
        RXA.12 - Administered Per (Time Unit) (ST) C S4.8.14.12
    """

    rxa_1: str = Field(
        validation_alias=AliasChoices(
            "rxa_1",
            "give_sub_id_counter",
            "RXA.1",
        ),
        serialization_alias="RXA.1",
        title="Give Sub-ID Counter",
        description="R | Item #00342 | LEN:4",
    )

    rxa_2: str = Field(
        validation_alias=AliasChoices(
            "rxa_2",
            "administration_sub_id_counter",
            "RXA.2",
        ),
        serialization_alias="RXA.2",
        title="Administration Sub-ID Counter",
        description="R | Item #00344 | LEN:4",
    )

    rxa_3: TS = Field(
        validation_alias=AliasChoices(
            "rxa_3",
            "date_time_start_of_administration",
            "RXA.3",
        ),
        serialization_alias="RXA.3",
        title="Date / time start of administration",
        description="R | Item #00345",
    )

    rxa_4: TS = Field(
        validation_alias=AliasChoices(
            "rxa_4",
            "date_time_end_of_administration",
            "RXA.4",
        ),
        serialization_alias="RXA.4",
        title="Date / time end of administration",
        description="R | Item #00346",
    )

    rxa_5: CE = Field(
        validation_alias=AliasChoices(
            "rxa_5",
            "administered_code",
            "RXA.5",
        ),
        serialization_alias="RXA.5",
        title="Administered Code",
        description="R | Item #00347",
    )

    rxa_6: str = Field(
        validation_alias=AliasChoices(
            "rxa_6",
            "administered_amount",
            "RXA.6",
        ),
        serialization_alias="RXA.6",
        title="Administered Amount",
        description="R | Item #00348 | LEN:20",
    )

    rxa_7: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_7",
            "administered_units",
            "RXA.7",
        ),
        serialization_alias="RXA.7",
        title="Administered Units",
        description="C | Item #00349",
    )

    rxa_8: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_8",
            "administered_dosage_form",
            "RXA.8",
        ),
        serialization_alias="RXA.8",
        title="Administered Dosage Form",
        description="NA | Item #00350",
    )

    rxa_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_9",
            "administration_notes",
            "RXA.9",
        ),
        serialization_alias="RXA.9",
        title="Administration Notes",
        description="C | Item #00351 | LEN:200",
    )

    rxa_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_10",
            "administering_provider",
            "RXA.10",
        ),
        serialization_alias="RXA.10",
        title="Administering Provider",
        description="NA | Item #00352",
    )

    rxa_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_11",
            "administered_at_location",
            "RXA.11",
        ),
        serialization_alias="RXA.11",
        title="Administered-at Location",
        description="C | Item #00353",
    )

    rxa_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_12",
            "administered_per_time_unit",
            "RXA.12",
        ),
        serialization_alias="RXA.12",
        title="Administered Per (Time Unit)",
        description="C | Item #00354 | LEN:20",
    )

    @field_validator("rxa_1", "rxa_2", "rxa_6", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
