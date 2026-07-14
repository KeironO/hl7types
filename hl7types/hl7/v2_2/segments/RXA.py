"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: RXA
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.TS import TS


class RXA(HL7Model):
    """PHARMACY AADMINISTRATION (S4.8.14).

    Attributes
    ----------
    rxa_1 : str
        RXA.1 (req) - Give Sub-ID Counter (NM) S4.8.14.1

    rxa_2 : str
        RXA.2 (req) - Administration Sub-ID Counter (NM) S4.8.14.2

    rxa_3 : TS
        RXA.3 (req) - Date / time start of administration (TS) S4.8.14.3

    rxa_4 : TS
        RXA.4 (req) - Date / time end of administration (TS) S4.8.14.4

    rxa_5 : CE
        RXA.5 (req) - Administered Code (CE) S4.8.14.5

    rxa_6 : str
        RXA.6 (req) - Administered Amount (NM) S4.8.14.6

    rxa_7 : CE | None
        RXA.7 (opt) - Administered Units (CE) S4.8.14.7

    rxa_8 : CE | None
        RXA.8 (opt) - Administered Dosage Form (CE) S4.8.14.8

    rxa_9 : str | None
        RXA.9 (opt) - Administration Notes (ST) S4.8.14.9

    rxa_10 : str | None
        RXA.10 (opt) - Administering Provider (CN) S4.8.14.10

    rxa_11 : str | None
        RXA.11 (opt) - Administered-at Location (CM) S4.8.14.11

    rxa_12 : str | None
        RXA.12 (opt) - Administered Per (Time Unit) (ST) S4.8.14.12
    """

    rxa_1: str = Field(
        validation_alias=AliasChoices(
            "rxa_1",
            "give_sub_id_counter",
            "RXA.1",
        ),
        serialization_alias="RXA.1",
        title="Give Sub-ID Counter",
        description="Item #342",
    )

    rxa_2: str = Field(
        validation_alias=AliasChoices(
            "rxa_2",
            "administration_sub_id_counter",
            "RXA.2",
        ),
        serialization_alias="RXA.2",
        title="Administration Sub-ID Counter",
        description="Item #344",
    )

    rxa_3: TS = Field(
        validation_alias=AliasChoices(
            "rxa_3",
            "date_time_start_of_administration",
            "RXA.3",
        ),
        serialization_alias="RXA.3",
        title="Date / time start of administration",
        description="Item #345",
    )

    rxa_4: TS = Field(
        validation_alias=AliasChoices(
            "rxa_4",
            "date_time_end_of_administration",
            "RXA.4",
        ),
        serialization_alias="RXA.4",
        title="Date / time end of administration",
        description="Item #346",
    )

    rxa_5: CE = Field(
        validation_alias=AliasChoices(
            "rxa_5",
            "administered_code",
            "RXA.5",
        ),
        serialization_alias="RXA.5",
        title="Administered Code",
        description="Item #347",
    )

    rxa_6: str = Field(
        validation_alias=AliasChoices(
            "rxa_6",
            "administered_amount",
            "RXA.6",
        ),
        serialization_alias="RXA.6",
        title="Administered Amount",
        description="Item #348",
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
        description="Item #349",
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
        description="Item #350",
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
        description="Item #351",
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
        description="Item #352",
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
        description="Item #353",
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
        description="Item #354",
    )

    @field_validator("rxa_1", "rxa_2", "rxa_6", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
