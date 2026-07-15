"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: RXG
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.TQ import TQ


class RXG(HL7Model):
    """PHARMACY GIVE (S4.8.12).

    Attributes
    ----------
    rxg_1 : str
        RXG.1 - Give Sub-ID Counter (NM) R S4.8.14.1

    rxg_2 : str | None
        RXG.2 - Dispense Sub-ID Counter (NM) NA S4.8.12.2

    rxg_3 : list[TQ] | None
        RXG.3 - Quantity / timing (TQ) NA rep S4.8.12.3

    rxg_4 : CE
        RXG.4 - Give Code (CE) R S4.8.12.4

    rxg_5 : str
        RXG.5 - Give Amount - Minimum (NM) R S4.8.12.5

    rxg_6 : str | None
        RXG.6 - Give Amount - Maximum (NM) NA S4.8.12.6

    rxg_7 : CE
        RXG.7 - Give Units (CE) R S4.8.12.7

    rxg_8 : CE | None
        RXG.8 - Give Dosage Form (CE) NA S4.8.12.8

    rxg_9 : str | None
        RXG.9 - Administration Notes (ST) C S4.8.14.9

    rxg_10 : str | None
        RXG.10 - Substitution Status (ID) NA S4.8.12.10 | 0167 - SUBSTITUTION STATUS

    rxg_11 : str | None
        RXG.11 - Deliver-to location (CM) C S4.8.12.11

    rxg_12 : str | None
        RXG.12 - Needs Human Review (ID) NA S4.8.12.12

    rxg_13 : list[CE] | None
        RXG.13 - Pharmacy Special Administration Instructions (CE) NA rep S4.8.12.9

    rxg_14 : str | None
        RXG.14 - Give Per (Time Unit) (ST) C S4.8.12.14

    rxg_15 : CE | None
        RXG.15 - Give Rate Amount (CE) NA S4.8.12.15

    rxg_16 : CE | None
        RXG.16 - Give Rate Units (CE) NA S4.8.12.16
    """

    rxg_1: str = Field(
        validation_alias=AliasChoices(
            "rxg_1",
            "give_sub_id_counter",
            "RXG.1",
        ),
        serialization_alias="RXG.1",
        title="Give Sub-ID Counter",
        description="R | Item #00342 | LEN:4",
    )

    rxg_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxg_2",
            "dispense_sub_id_counter",
            "RXG.2",
        ),
        serialization_alias="RXG.2",
        title="Dispense Sub-ID Counter",
        description="NA | Item #00334 | LEN:4",
    )

    rxg_3: Optional[List[TQ]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxg_3",
            "quantity_timing",
            "RXG.3",
        ),
        serialization_alias="RXG.3",
        title="Quantity / timing",
        description="NA | Item #00221",
    )

    rxg_4: CE = Field(
        validation_alias=AliasChoices(
            "rxg_4",
            "give_code",
            "RXG.4",
        ),
        serialization_alias="RXG.4",
        title="Give Code",
        description="R | Item #00317",
    )

    rxg_5: str = Field(
        validation_alias=AliasChoices(
            "rxg_5",
            "give_amount_minimum",
            "RXG.5",
        ),
        serialization_alias="RXG.5",
        title="Give Amount - Minimum",
        description="R | Item #00318 | LEN:20",
    )

    rxg_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxg_6",
            "give_amount_maximum",
            "RXG.6",
        ),
        serialization_alias="RXG.6",
        title="Give Amount - Maximum",
        description="NA | Item #00319 | LEN:20",
    )

    rxg_7: CE = Field(
        validation_alias=AliasChoices(
            "rxg_7",
            "give_units",
            "RXG.7",
        ),
        serialization_alias="RXG.7",
        title="Give Units",
        description="R | Item #00320",
    )

    rxg_8: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxg_8",
            "give_dosage_form",
            "RXG.8",
        ),
        serialization_alias="RXG.8",
        title="Give Dosage Form",
        description="NA | Item #00321",
    )

    rxg_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxg_9",
            "administration_notes",
            "RXG.9",
        ),
        serialization_alias="RXG.9",
        title="Administration Notes",
        description="C | Item #00351 | LEN:200",
    )

    rxg_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxg_10",
            "substitution_status",
            "RXG.10",
        ),
        serialization_alias="RXG.10",
        title="Substitution Status",
        description=(
            "NA | Item #00322 | Table 0167 - SUBSTITUTION STATUS | LEN:1"
        ),
    )

    rxg_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxg_11",
            "deliver_to_location",
            "RXG.11",
        ),
        serialization_alias="RXG.11",
        title="Deliver-to location",
        description="C | Item #00299",
    )

    rxg_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxg_12",
            "needs_human_review",
            "RXG.12",
        ),
        serialization_alias="RXG.12",
        title="Needs Human Review",
        description="NA | Item #00307 | LEN:1",
    )

    rxg_13: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxg_13",
            "pharmacy_special_administration_instructions",
            "RXG.13",
        ),
        serialization_alias="RXG.13",
        title="Pharmacy Special Administration Instructions",
        description="NA | Item #00343",
    )

    rxg_14: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxg_14",
            "give_per_time_unit",
            "RXG.14",
        ),
        serialization_alias="RXG.14",
        title="Give Per (Time Unit)",
        description="C | Item #00331 | LEN:20",
    )

    rxg_15: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxg_15",
            "give_rate_amount",
            "RXG.15",
        ),
        serialization_alias="RXG.15",
        title="Give Rate Amount",
        description="NA | Item #00332",
    )

    rxg_16: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxg_16",
            "give_rate_units",
            "RXG.16",
        ),
        serialization_alias="RXG.16",
        title="Give Rate Units",
        description="NA | Item #00333",
    )

    @field_validator("rxg_1", "rxg_2", "rxg_5", "rxg_6", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
