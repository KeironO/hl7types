"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: RXG
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.TQ import TQ
from ..datatypes.TS import TS


class RXG(HL7Model):
    """Pharmacy give segment (S4.8.12).

    Attributes
    ----------
    rxg_1 : str | None
        RXG.1 - Give Sub-ID Counter (ID) O S4.8.12

    rxg_2 : str
        RXG.2 - Dispense Sub-ID Counter (NM) R S4.8.10

    rxg_3 : TQ
        RXG.3 - Quantity/Timing (TQ) R S4.3.1

    rxg_4 : CE
        RXG.4 - Give Code (CE) R S4.8.7

    rxg_5 : str
        RXG.5 - Give Amount - Minimum (NM) R S4.8.7

    rxg_6 : str | None
        RXG.6 - Give Amount - Maximum (NM) O S4.8.7

    rxg_7 : CE
        RXG.7 - Give Units (CE) R S4.8.7

    rxg_8 : CE | None
        RXG.8 - Give Dosage Form (CE) O S4.8.7

    rxg_9 : list[CE] | None
        RXG.9 - Administration Notes (CE) C rep S4.8.12

    rxg_10 : str | None
        RXG.10 - Substitution Status (ID) O S4.8.7 | 0167 - Substitution Status

    rxg_11 : str | None
        RXG.11 - Dispense-To Location (CM) O S4.8.10

    rxg_12 : str | None
        RXG.12 - Needs Human Review (ID) O S4.8.2 | 0136 - Yes/No Indicator

    rxg_13 : CE | None
        RXG.13 - Pharmacy Special Administration Instructions (CE) NA S4.8.12.13

    rxg_14 : str | None
        RXG.14 - Give Per (Time Unit) (ST) C S4.8.12.14

    rxg_15 : str | None
        RXG.15 - Give Rate Amount (ST) O S4.8.7

    rxg_16 : CE | None
        RXG.16 - Give Rate Units (CE) O S4.8.7

    rxg_17 : str | None
        RXG.17 - Give Strength (NM) O S4.8.7

    rxg_18 : CE | None
        RXG.18 - Give Strength Units (CE) O S4.8.7

    rxg_19 : list[str] | None
        RXG.19 - Substance Lot Number (ST) O rep S4.8.10

    rxg_20 : list[TS] | None
        RXG.20 - Substance Expiration Date (TS) O rep S4.8.10

    rxg_21 : list[CE] | None
        RXG.21 - Substance Manufacturer Name (CE) O rep S4.8.10 | 0227 - Manufacturers of Vaccines

    rxg_22 : CE | None
        RXG.22 - Indication (CE) O S4.8.2
    """

    rxg_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxg_1",
            "give_sub_id_counter",
            "RXG.1",
        ),
        serialization_alias="RXG.1",
        title="Give Sub-ID Counter",
        description="O | Item #00342 | LEN:4",
    )

    rxg_2: str = Field(
        validation_alias=AliasChoices(
            "rxg_2",
            "dispense_sub_id_counter",
            "RXG.2",
        ),
        serialization_alias="RXG.2",
        title="Dispense Sub-ID Counter",
        description="R | Item #00334 | LEN:4",
    )

    rxg_3: TQ = Field(
        validation_alias=AliasChoices(
            "rxg_3",
            "quantity_timing",
            "RXG.3",
        ),
        serialization_alias="RXG.3",
        title="Quantity/Timing",
        description="R | Item #00221",
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
        description="O | Item #00319 | LEN:20",
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
        description="O | Item #00321",
    )

    rxg_9: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxg_9",
            "administration_notes",
            "RXG.9",
        ),
        serialization_alias="RXG.9",
        title="Administration Notes",
        description="C | Item #00351",
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
            "O | Item #00322 | Table 0167 - Substitution Status | LEN:1"
        ),
    )

    rxg_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxg_11",
            "dispense_to_location",
            "RXG.11",
        ),
        serialization_alias="RXG.11",
        title="Dispense-To Location",
        description="O | Item #01303",
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
        description="O | Item #00307 | Table 0136 - Yes/No Indicator | LEN:1",
    )

    rxg_13: Optional[CE] = Field(
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

    rxg_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxg_15",
            "give_rate_amount",
            "RXG.15",
        ),
        serialization_alias="RXG.15",
        title="Give Rate Amount",
        description="O | Item #00332 | LEN:6",
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
        description="O | Item #00333",
    )

    rxg_17: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxg_17",
            "give_strength",
            "RXG.17",
        ),
        serialization_alias="RXG.17",
        title="Give Strength",
        description="O | Item #01126 | LEN:20",
    )

    rxg_18: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxg_18",
            "give_strength_units",
            "RXG.18",
        ),
        serialization_alias="RXG.18",
        title="Give Strength Units",
        description="O | Item #01127",
    )

    rxg_19: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxg_19",
            "substance_lot_number",
            "RXG.19",
        ),
        serialization_alias="RXG.19",
        title="Substance Lot Number",
        description="O | Item #01129 | LEN:20",
    )

    rxg_20: Optional[List[TS]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxg_20",
            "substance_expiration_date",
            "RXG.20",
        ),
        serialization_alias="RXG.20",
        title="Substance Expiration Date",
        description="O | Item #01130",
    )

    rxg_21: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxg_21",
            "substance_manufacturer_name",
            "RXG.21",
        ),
        serialization_alias="RXG.21",
        title="Substance Manufacturer Name",
        description="O | Item #01131 | Table 0227 - Manufacturers of Vaccines",
    )

    rxg_22: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxg_22",
            "indication",
            "RXG.22",
        ),
        serialization_alias="RXG.22",
        title="Indication",
        description="O | Item #01123",
    )

    @field_validator("rxg_2", "rxg_5", "rxg_6", "rxg_17", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
