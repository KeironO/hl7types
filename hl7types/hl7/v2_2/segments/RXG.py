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
    """HL7 v2 RXG segment.

    Attributes
    ----------
    rxg_1 : str
        RXG.1 (req) - Give Sub-ID Counter (NM)

    rxg_2 : str | None
        RXG.2 (opt) - Dispense Sub-ID Counter (NM)

    rxg_3 : list[TQ] | None
        RXG.3 (opt, rep) - Quantity / timing (TQ)

    rxg_4 : CE
        RXG.4 (req) - Give Code (CE)

    rxg_5 : str
        RXG.5 (req) - Give Amount - Minimum (NM)

    rxg_6 : str | None
        RXG.6 (opt) - Give Amount - Maximum (NM)

    rxg_7 : CE
        RXG.7 (req) - Give Units (CE)

    rxg_8 : CE | None
        RXG.8 (opt) - Give Dosage Form (CE)

    rxg_9 : str | None
        RXG.9 (opt) - Administration Notes (ST)

    rxg_10 : str | None
        RXG.10 (opt) - Substitution Status (ID)

    rxg_11 : str | None
        RXG.11 (opt) - Deliver-to location (CM)

    rxg_12 : str | None
        RXG.12 (opt) - Needs Human Review (ID)

    rxg_13 : list[CE] | None
        RXG.13 (opt, rep) - Pharmacy Special Administration Instructions (CE)

    rxg_14 : str | None
        RXG.14 (opt) - Give Per (Time Unit) (ST)

    rxg_15 : CE | None
        RXG.15 (opt) - Give Rate Amount (CE)

    rxg_16 : CE | None
        RXG.16 (opt) - Give Rate Units (CE)
    """

    rxg_1: str = Field(
        validation_alias=AliasChoices(
            "rxg_1",
            "give_sub_id_counter",
            "RXG.1",
        ),
        serialization_alias="RXG.1",
        title="Give Sub-ID Counter",
        description="Item #342",
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
        description="Item #334",
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
        description="Item #221",
    )

    rxg_4: CE = Field(
        validation_alias=AliasChoices(
            "rxg_4",
            "give_code",
            "RXG.4",
        ),
        serialization_alias="RXG.4",
        title="Give Code",
        description="Item #317",
    )

    rxg_5: str = Field(
        validation_alias=AliasChoices(
            "rxg_5",
            "give_amount_minimum",
            "RXG.5",
        ),
        serialization_alias="RXG.5",
        title="Give Amount - Minimum",
        description="Item #318",
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
        description="Item #319",
    )

    rxg_7: CE = Field(
        validation_alias=AliasChoices(
            "rxg_7",
            "give_units",
            "RXG.7",
        ),
        serialization_alias="RXG.7",
        title="Give Units",
        description="Item #320",
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
        description="Item #321",
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
        description="Item #351",
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
        description="Item #322 | Table HL70167",
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
        description="Item #299",
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
        description="Item #307",
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
        description="Item #343",
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
        description="Item #331",
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
        description="Item #332",
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
        description="Item #333",
    )

    @field_validator("rxg_1", "rxg_2", "rxg_5", "rxg_6", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
