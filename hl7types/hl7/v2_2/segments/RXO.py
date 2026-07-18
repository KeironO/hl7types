"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: RXO
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE

_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class RXO(HL7Model):
    """PHARMACY PRESCRIPTION ORDER (S4.8.2).

    Attributes
    ----------
    rxo_1 : CE
        RXO.1 - Requested Give Code (CE) R S4.8.2.1

    rxo_2 : str
        RXO.2 - Requested Give Amount - Minimum (NM) R S4.8.2.2

    rxo_3 : str | None
        RXO.3 - Requested Give Amount - Maximum (NM) NA S4.8.2.3

    rxo_4 : CE
        RXO.4 - Requested Give Units (CE) R S4.8.2.4

    rxo_5 : CE | None
        RXO.5 - Requested Dosage Form (CE) NA S4.8.2.5

    rxo_6 : list[CE] | None
        RXO.6 - Provider's Pharmacy Instructions (CE) NA rep S4.8.2.6

    rxo_7 : list[CE] | None
        RXO.7 - Provider's Administration Instructions (CE) NA rep S4.8.7.7

    rxo_8 : str | None
        RXO.8 - Deliver-to location (CM) C S4.8.12.11

    rxo_9 : str | None
        RXO.9 - Allow Substitutions (ID) NA S4.8.2.9 | 0161 - ALLOW SUBSTITUTION

    rxo_10 : CE | None
        RXO.10 - Requested Dispense Code (CE) C S4.8.2.10

    rxo_11 : str | None
        RXO.11 - Requested Dispense Amount (NM) C S4.8.2.11

    rxo_12 : CE | None
        RXO.12 - Requested Dispense Units (CE) C S4.8.2.12

    rxo_13 : str | None
        RXO.13 - Number of Refills (NM) NA S4.8.7.12

    rxo_14 : str | None
        RXO.14 - Ordering Provider's DEA Number (CN) C S4.8.7.13

    rxo_15 : str | None
        RXO.15 - Pharmacist Verifier ID (CN) C S4.8.7.14

    rxo_16 : str | None
        RXO.16 - Needs Human Review (ID) NA S4.8.12.12

    rxo_17 : str | None
        RXO.17 - Requested Give Per (Time Unit) (ST) C S4.8.2.17
    """

    rxo_1: CE = Field(
        validation_alias=AliasChoices(
            "rxo_1",
            "requested_give_code",
            "RXO.1",
        ),
        serialization_alias="RXO.1",
        title="Requested Give Code",
        description="R | Item #00292",
    )

    rxo_2: str = Field(
        validation_alias=AliasChoices(
            "rxo_2",
            "requested_give_amount_minimum",
            "RXO.2",
        ),
        serialization_alias="RXO.2",
        title="Requested Give Amount - Minimum",
        description="R | Item #00293 | LEN:20",
    )

    rxo_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_3",
            "requested_give_amount_maximum",
            "RXO.3",
        ),
        serialization_alias="RXO.3",
        title="Requested Give Amount - Maximum",
        description="NA | Item #00294 | LEN:20",
    )

    rxo_4: CE = Field(
        validation_alias=AliasChoices(
            "rxo_4",
            "requested_give_units",
            "RXO.4",
        ),
        serialization_alias="RXO.4",
        title="Requested Give Units",
        description="R | Item #00295",
    )

    rxo_5: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_5",
            "requested_dosage_form",
            "RXO.5",
        ),
        serialization_alias="RXO.5",
        title="Requested Dosage Form",
        description="NA | Item #00296",
    )

    rxo_6: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_6",
            "provider_s_pharmacy_instructions",
            "RXO.6",
        ),
        serialization_alias="RXO.6",
        title="Provider's Pharmacy Instructions",
        description="NA | Item #00297",
    )

    rxo_7: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_7",
            "provider_s_administration_instructions",
            "RXO.7",
        ),
        serialization_alias="RXO.7",
        title="Provider's Administration Instructions",
        description="NA | Item #00298",
    )

    rxo_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_8",
            "deliver_to_location",
            "RXO.8",
        ),
        serialization_alias="RXO.8",
        title="Deliver-to location",
        description="C | Item #00299",
    )

    rxo_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_9",
            "allow_substitutions",
            "RXO.9",
        ),
        serialization_alias="RXO.9",
        title="Allow Substitutions",
        description=(
            "NA | Item #00300 | Table 0161 - ALLOW SUBSTITUTION | LEN:1"
        ),
    )

    rxo_10: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_10",
            "requested_dispense_code",
            "RXO.10",
        ),
        serialization_alias="RXO.10",
        title="Requested Dispense Code",
        description="C | Item #00301",
    )

    rxo_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_11",
            "requested_dispense_amount",
            "RXO.11",
        ),
        serialization_alias="RXO.11",
        title="Requested Dispense Amount",
        description="C | Item #00302 | LEN:20",
    )

    rxo_12: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_12",
            "requested_dispense_units",
            "RXO.12",
        ),
        serialization_alias="RXO.12",
        title="Requested Dispense Units",
        description="C | Item #00303",
    )

    rxo_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_13",
            "number_of_refills",
            "RXO.13",
        ),
        serialization_alias="RXO.13",
        title="Number of Refills",
        description="NA | Item #00304 | LEN:3",
    )

    rxo_14: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_14",
            "ordering_provider_s_dea_number",
            "RXO.14",
        ),
        serialization_alias="RXO.14",
        title="Ordering Provider's DEA Number",
        description="C | Item #00305",
    )

    rxo_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_15",
            "pharmacist_verifier_id",
            "RXO.15",
        ),
        serialization_alias="RXO.15",
        title="Pharmacist Verifier ID",
        description="C | Item #00306",
    )

    rxo_16: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_16",
            "needs_human_review",
            "RXO.16",
        ),
        serialization_alias="RXO.16",
        title="Needs Human Review",
        description="NA | Item #00307 | LEN:1",
    )

    rxo_17: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_17",
            "requested_give_per_time_unit",
            "RXO.17",
        ),
        serialization_alias="RXO.17",
        title="Requested Give Per (Time Unit)",
        description="C | Item #00308 | LEN:20",
    )

    @field_validator("rxo_2", "rxo_3", "rxo_11", "rxo_13", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
