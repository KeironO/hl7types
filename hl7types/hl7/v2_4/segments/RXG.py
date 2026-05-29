"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RXG
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE
from ..datatypes.LA2 import LA2
from ..datatypes.TQ import TQ
from ..datatypes.TS import TS


class RXG(BaseModel):
    """HL7 v2 RXG segment.

    Attributes
    ----------
    rxg_1 : str
        RXG.1 (req) - Give Sub-ID Counter (NM)

    rxg_2 : str | None
        RXG.2 (opt) - Dispense Sub-ID Counter (NM)

    rxg_3 : TQ
        RXG.3 (req) - Quantity/Timing (TQ)

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

    rxg_9 : list[CE] | None
        RXG.9 (opt, rep) - Administration Notes (CE)

    rxg_10 : str | None
        RXG.10 (opt) - Substitution Status (ID)

    rxg_11 : LA2 | None
        RXG.11 (opt) - Dispense-To Location (LA2)

    rxg_12 : str | None
        RXG.12 (opt) - Needs Human Review (ID)

    rxg_13 : list[CE] | None
        RXG.13 (opt, rep) - Pharmacy/Treatment Supplier's Special Administration Instructions (CE)

    rxg_14 : str | None
        RXG.14 (opt) - Give Per (Time Unit) (ST)

    rxg_15 : str | None
        RXG.15 (opt) - Give Rate Amount (ST)

    rxg_16 : CE | None
        RXG.16 (opt) - Give Rate Units (CE)

    rxg_17 : str | None
        RXG.17 (opt) - Give Strength (NM)

    rxg_18 : CE | None
        RXG.18 (opt) - Give Strength Units (CE)

    rxg_19 : list[str] | None
        RXG.19 (opt, rep) - Substance Lot Number (ST)

    rxg_20 : list[TS] | None
        RXG.20 (opt, rep) - Substance Expiration Date (TS)

    rxg_21 : list[CE] | None
        RXG.21 (opt, rep) - Substance Manufacturer Name (CE)

    rxg_22 : list[CE] | None
        RXG.22 (opt, rep) - Indication (CE)
    """

    rxg_1: str = Field(
        default=...,
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

    rxg_3: TQ = Field(
        default=...,
        validation_alias=AliasChoices(
            "rxg_3",
            "quantity_timing",
            "RXG.3",
        ),
        serialization_alias="RXG.3",
        title="Quantity/Timing",
        description="Item #221",
    )

    rxg_4: CE = Field(
        default=...,
        validation_alias=AliasChoices(
            "rxg_4",
            "give_code",
            "RXG.4",
        ),
        serialization_alias="RXG.4",
        title="Give Code",
        description="Item #317 | Table HL70292",
    )

    rxg_5: str = Field(
        default=...,
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
        default=...,
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

    rxg_9: Optional[List[CE]] = Field(
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

    rxg_11: Optional[LA2] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxg_11",
            "dispense_to_location",
            "RXG.11",
        ),
        serialization_alias="RXG.11",
        title="Dispense-To Location",
        description="Item #1303",
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
        description="Item #307 | Table HL70136",
    )

    rxg_13: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxg_13",
            "pharmacy_treatment_supplier_s_special_administration_instructions",
            "RXG.13",
        ),
        serialization_alias="RXG.13",
        title=(
            "Pharmacy/Treatment Supplier's Special Administration Instructions"
        ),
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

    rxg_15: Optional[str] = Field(
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

    rxg_17: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxg_17",
            "give_strength",
            "RXG.17",
        ),
        serialization_alias="RXG.17",
        title="Give Strength",
        description="Item #1126",
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
        description="Item #1127",
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
        description="Item #1129",
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
        description="Item #1130",
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
        description="Item #1131 | Table HL70227",
    )

    rxg_22: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxg_22",
            "indication",
            "RXG.22",
        ),
        serialization_alias="RXG.22",
        title="Indication",
        description="Item #1123",
    )

    model_config = {"populate_by_name": True}
