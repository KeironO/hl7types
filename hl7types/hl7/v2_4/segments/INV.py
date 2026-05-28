"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: INV
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE
from ..datatypes.TQ import TQ
from ..datatypes.TS import TS


class INV(BaseModel):
    """HL7 v2 INV segment."""

    inv_1: CE = Field(
        default=...,
        validation_alias=AliasChoices(
            "inv_1",
            "substance_identifier",
            "INV.1",
        ),
        serialization_alias="INV.1",
        title="Substance Identifier",
        description="Item #1372 | Table HL70451",
    )

    inv_2: list[CE] = Field(
        default=...,
        validation_alias=AliasChoices(
            "inv_2",
            "substance_status",
            "INV.2",
        ),
        serialization_alias="INV.2",
        title="Substance Status",
        description="Item #1373 | Table HL70383",
    )

    inv_3: CE | None = Field(
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

    inv_4: CE | None = Field(
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

    inv_5: CE | None = Field(
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

    inv_6: CE | None = Field(
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

    inv_7: str | None = Field(
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

    inv_8: str | None = Field(
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

    inv_9: str | None = Field(
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

    inv_10: str | None = Field(
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

    inv_11: CE | None = Field(
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

    inv_12: TS | None = Field(
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

    inv_13: TS | None = Field(
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

    inv_14: TQ | None = Field(
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

    inv_15: list[CE] | None = Field(
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

    inv_16: str | None = Field(
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

    inv_17: CE | None = Field(
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

    inv_18: CE | None = Field(
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

    model_config = {"populate_by_name": True}
