"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: INV
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.TQ import TQ
from ..datatypes.TS import TS

_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class INV(HL7Model):
    """Inventory Detail (S13.4.4).

    Attributes
    ----------
    inv_1 : CE
        INV.1 - Substance Identifier (CE) R S13.4.4.1 | 0451 - Substance identifier

    inv_2 : list[CE]
        INV.2 - Substance Status (CE) R rep S13.4.4.2 | 0383 - Substance status

    inv_3 : CE | None
        INV.3 - Substance Type (CE) O S13.4.4.3 | 0384 - Substance type

    inv_4 : CE | None
        INV.4 - Inventory Container Identifier (CE) O S13.4.4.4

    inv_5 : CE | None
        INV.5 - Container Carrier Identifier (CE) O S13.4.4.5

    inv_6 : CE | None
        INV.6 - Position on Carrier (CE) O S13.4.4.6

    inv_7 : str | None
        INV.7 - Initial Quantity (NM) O S13.4.4.7

    inv_8 : str | None
        INV.8 - Current Quantity (NM) O S13.4.4.8

    inv_9 : str | None
        INV.9 - Available Quantity (NM) O S13.4.4.9

    inv_10 : str | None
        INV.10 - Consumption Quantity (NM) O S13.4.4.10

    inv_11 : CE | None
        INV.11 - Quantity Units (CE) O S13.4.4.11

    inv_12 : TS | None
        INV.12 - Expiration Date/Time (TS) O S13.4.4.12

    inv_13 : TS | None
        INV.13 - First Used Date/Time (TS) O S13.4.4.13

    inv_14 : TQ | None
        INV.14 - On Board Stability Duration (TQ) O S13.4.4.14

    inv_15 : list[CE] | None
        INV.15 - Test/Fluid Identifier(s) (CE) O rep S13.4.4.15

    inv_16 : str | None
        INV.16 - Manufacturer Lot Number (ST) O S13.4.4.16

    inv_17 : CE | None
        INV.17 - Manufacturer Identifier (CE) O S13.4.4.17 | 0385 - Manufacturer identifier

    inv_18 : CE | None
        INV.18 - Supplier Identifier (CE) O S13.4.4.18 | 0386 - Supplier identifier
    """

    inv_1: CE = Field(
        validation_alias=AliasChoices(
            "inv_1",
            "substance_identifier",
            "INV.1",
        ),
        serialization_alias="INV.1",
        title="Substance Identifier",
        description="R | Item #01372 | Table 0451 - Substance identifier",
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
        description="R | Item #01373 | Table 0383 - Substance status",
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
        description="O | Item #01374 | Table 0384 - Substance type",
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
        description="O | Item #01532",
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
        description="O | Item #01376",
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
        description="O | Item #01377",
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
        description="O | Item #01378 | LEN:20",
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
        description="O | Item #01379 | LEN:20",
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
        description="O | Item #01380 | LEN:20",
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
        description="O | Item #01381 | LEN:20",
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
        description="O | Item #01382",
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
        description="O | Item #01383",
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
        description="O | Item #01384",
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
        description="O | Item #01385",
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
        description="O | Item #01386",
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
        description="O | Item #01387 | LEN:200",
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
        description="O | Item #00286 | Table 0385 - Manufacturer identifier",
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
        description="O | Item #01389 | Table 0386 - Supplier identifier",
    )

    @field_validator("inv_7", "inv_8", "inv_9", "inv_10", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
