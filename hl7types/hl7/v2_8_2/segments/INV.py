"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: INV
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator

from ..datatypes.CQ import CQ
from ..datatypes.CWE import CWE


class INV(HL7Model):
    """HL7 v2 INV segment.

    Attributes
    ----------
    inv_1 : CWE
        INV.1 (req) - Substance Identifier (CWE)

    inv_2 : list[CWE] | None
        INV.2 (req, rep) - Substance Status (CWE) [optional: CWE has no required components]

    inv_3 : CWE | None
        INV.3 (opt) - Substance Type (CWE)

    inv_4 : CWE | None
        INV.4 (opt) - Inventory Container Identifier (CWE)

    inv_5 : CWE | None
        INV.5 (opt) - Container Carrier Identifier (CWE)

    inv_6 : CWE | None
        INV.6 (opt) - Position on Carrier (CWE)

    inv_7 : str | None
        INV.7 (opt) - Initial Quantity (NM)

    inv_8 : str | None
        INV.8 (opt) - Current Quantity (NM)

    inv_9 : str | None
        INV.9 (opt) - Available Quantity (NM)

    inv_10 : str | None
        INV.10 (opt) - Consumption Quantity (NM)

    inv_11 : CWE | None
        INV.11 (opt) - Quantity Units (CWE)

    inv_12 : str | None
        INV.12 (opt) - Expiration Date/Time (DTM)

    inv_13 : str | None
        INV.13 (opt) - First Used Date/Time (DTM)

    inv_15 : list[CWE] | None
        INV.15 (opt, rep) - Test/Fluid Identifier(s) (CWE)

    inv_16 : str | None
        INV.16 (opt) - Manufacturer Lot Number (ST)

    inv_17 : CWE | None
        INV.17 (opt) - Manufacturer Identifier (CWE)

    inv_18 : CWE | None
        INV.18 (opt) - Supplier Identifier (CWE)

    inv_19 : CQ | None
        INV.19 (opt) - On Board Stability Time (CQ)

    inv_20 : CQ | None
        INV.20 (opt) - Target Value (CQ)
    """

    inv_1: CWE = Field(
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

    inv_2: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "inv_2",
            "substance_status",
            "INV.2",
        ),
        serialization_alias="INV.2",
        title="Substance Status",
        description="Item #1373 | Table HL70383",
    )

    inv_3: Optional[CWE] = Field(
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

    inv_4: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "inv_4",
            "inventory_container_identifier",
            "INV.4",
        ),
        serialization_alias="INV.4",
        title="Inventory Container Identifier",
        description="Item #1532 | Table HL79999",
    )

    inv_5: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "inv_5",
            "container_carrier_identifier",
            "INV.5",
        ),
        serialization_alias="INV.5",
        title="Container Carrier Identifier",
        description="Item #1376 | Table HL79999",
    )

    inv_6: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "inv_6",
            "position_on_carrier",
            "INV.6",
        ),
        serialization_alias="INV.6",
        title="Position on Carrier",
        description="Item #1377 | Table HL79999",
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

    inv_11: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "inv_11",
            "quantity_units",
            "INV.11",
        ),
        serialization_alias="INV.11",
        title="Quantity Units",
        description="Item #1382 | Table HL79999",
    )

    inv_12: Optional[str] = Field(
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

    inv_13: Optional[str] = Field(
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

    inv_15: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "inv_15",
            "test_fluid_identifier_s",
            "INV.15",
        ),
        serialization_alias="INV.15",
        title="Test/Fluid Identifier(s)",
        description="Item #1386 | Table HL79999",
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

    inv_17: Optional[CWE] = Field(
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

    inv_18: Optional[CWE] = Field(
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

    @field_validator("inv_12", "inv_13", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 datetime")
        return v

    model_config = {"populate_by_name": True}
