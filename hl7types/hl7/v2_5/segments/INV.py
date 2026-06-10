"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: INV
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.CQ import CQ
from ..datatypes.TQ import TQ
from ..datatypes.TS import TS


class INV(HL7Model):
    """HL7 v2 INV segment.

    Attributes
    ----------
    inv_1 : CE
        INV.1 (req) - Substance Identifier (CE)

    inv_2 : list[CE]
        INV.2 (req, rep) - Substance Status (CE)

    inv_3 : CE | None
        INV.3 (opt) - Substance Type (CE)

    inv_4 : CE | None
        INV.4 (opt) - Inventory Container Identifier (CE)

    inv_5 : CE | None
        INV.5 (opt) - Container Carrier Identifier (CE)

    inv_6 : CE | None
        INV.6 (opt) - Position on Carrier (CE)

    inv_7 : str | None
        INV.7 (opt) - Initial Quantity (NM)

    inv_8 : str | None
        INV.8 (opt) - Current Quantity (NM)

    inv_9 : str | None
        INV.9 (opt) - Available Quantity (NM)

    inv_10 : str | None
        INV.10 (opt) - Consumption Quantity (NM)

    inv_11 : CE | None
        INV.11 (opt) - Quantity Units (CE)

    inv_12 : TS | None
        INV.12 (opt) - Expiration Date/Time (TS)

    inv_13 : TS | None
        INV.13 (opt) - First Used Date/Time (TS)

    inv_14 : TQ | None
        INV.14 (opt) - On Board Stability Duration (TQ)

    inv_15 : list[CE] | None
        INV.15 (opt, rep) - Test/Fluid Identifier(s) (CE)

    inv_16 : str | None
        INV.16 (opt) - Manufacturer Lot Number (ST)

    inv_17 : CE | None
        INV.17 (opt) - Manufacturer Identifier (CE)

    inv_18 : CE | None
        INV.18 (opt) - Supplier Identifier (CE)

    inv_19 : CQ | None
        INV.19 (opt) - On Board Stability Time (CQ)

    inv_20 : CQ | None
        INV.20 (opt) - Target Value (CQ)
    """

    inv_1: CE = Field(
        validation_alias=AliasChoices(
            "inv_1",
            "substance_identifier",
            "INV.1",
        ),
        serialization_alias="INV.1",
        title="Substance Identifier",
        description="Item #1372 | Table HL70451",
    )

    inv_2: List[CE] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "inv_2",
            "substance_status",
            "INV.2",
        ),
        serialization_alias="INV.2",
        title="Substance Status",
        description="Item #1373 | Table HL70383",
    )

    inv_3: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "inv_3",
            "substance_type",
            "INV.3",
        ),
        serialization_alias="INV.3",
        title="Substance Type",
        description="Item #1374 | Table HL70384",
    )

    inv_4: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "inv_4",
            "inventory_container_identifier",
            "INV.4",
        ),
        serialization_alias="INV.4",
        title="Inventory Container Identifier",
        description="Item #1532",
    )

    inv_5: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "inv_5",
            "container_carrier_identifier",
            "INV.5",
        ),
        serialization_alias="INV.5",
        title="Container Carrier Identifier",
        description="Item #1376",
    )

    inv_6: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "inv_6",
            "position_on_carrier",
            "INV.6",
        ),
        serialization_alias="INV.6",
        title="Position on Carrier",
        description="Item #1377",
    )

    inv_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "inv_7",
            "initial_quantity",
            "INV.7",
        ),
        serialization_alias="INV.7",
        title="Initial Quantity",
        description="Item #1378",
    )

    inv_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "inv_8",
            "current_quantity",
            "INV.8",
        ),
        serialization_alias="INV.8",
        title="Current Quantity",
        description="Item #1379",
    )

    inv_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "inv_9",
            "available_quantity",
            "INV.9",
        ),
        serialization_alias="INV.9",
        title="Available Quantity",
        description="Item #1380",
    )

    inv_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "inv_10",
            "consumption_quantity",
            "INV.10",
        ),
        serialization_alias="INV.10",
        title="Consumption Quantity",
        description="Item #1381",
    )

    inv_11: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "inv_11",
            "quantity_units",
            "INV.11",
        ),
        serialization_alias="INV.11",
        title="Quantity Units",
        description="Item #1382",
    )

    inv_12: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "inv_12",
            "expiration_date_time",
            "INV.12",
        ),
        serialization_alias="INV.12",
        title="Expiration Date/Time",
        description="Item #1383",
    )

    inv_13: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "inv_13",
            "first_used_date_time",
            "INV.13",
        ),
        serialization_alias="INV.13",
        title="First Used Date/Time",
        description="Item #1384",
    )

    inv_14: Optional[TQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "inv_14",
            "on_board_stability_duration",
            "INV.14",
        ),
        serialization_alias="INV.14",
        title="On Board Stability Duration",
        description="Item #1385",
    )

    inv_15: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "inv_15",
            "test_fluid_identifier_s",
            "INV.15",
        ),
        serialization_alias="INV.15",
        title="Test/Fluid Identifier(s)",
        description="Item #1386",
    )

    inv_16: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "inv_16",
            "manufacturer_lot_number",
            "INV.16",
        ),
        serialization_alias="INV.16",
        title="Manufacturer Lot Number",
        description="Item #1387",
    )

    inv_17: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "inv_17",
            "manufacturer_identifier",
            "INV.17",
        ),
        serialization_alias="INV.17",
        title="Manufacturer Identifier",
        description="Item #286 | Table HL70385",
    )

    inv_18: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "inv_18",
            "supplier_identifier",
            "INV.18",
        ),
        serialization_alias="INV.18",
        title="Supplier Identifier",
        description="Item #1389 | Table HL70386",
    )

    inv_19: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "inv_19",
            "on_board_stability_time",
            "INV.19",
        ),
        serialization_alias="INV.19",
        title="On Board Stability Time",
        description="Item #1626",
    )

    inv_20: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "inv_20",
            "target_value",
            "INV.20",
        ),
        serialization_alias="INV.20",
        title="Target Value",
        description="Item #1896",
    )

    @field_validator("inv_7", "inv_8", "inv_9", "inv_10", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
