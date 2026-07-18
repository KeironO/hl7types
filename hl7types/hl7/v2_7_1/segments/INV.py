"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: INV
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, ValidationInfo, field_validator
from hl7types.hl7 import HL7Model
from hl7types.hl7._validators import _apply_dt_fallback

from ..datatypes.CQ import CQ
from ..datatypes.CWE import CWE

_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')
_RE_DTM = re.compile(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?')


class INV(HL7Model):
    """Inventory Detail (S13.4.4).

    Attributes
    ----------
    inv_1 : CWE
        INV.1 - Substance Identifier (CWE) R S13.4.4.1 | 0451 - Substance Identifier

    inv_2 : list[CWE]
        INV.2 - Substance Status (CWE) R rep S13.4.4.2 | 0383 - Substance Status

    inv_3 : CWE | None
        INV.3 - Substance Type (CWE) O S13.4.4.3 | 0384 - Substance Type

    inv_4 : CWE | None
        INV.4 - Inventory Container Identifier (CWE) O S13.4.4.4 | 9999 - no table for CE

    inv_5 : CWE | None
        INV.5 - Container Carrier Identifier (CWE) O S13.4.4.5 | 9999 - no table for CE

    inv_6 : CWE | None
        INV.6 - Position on Carrier (CWE) O S13.4.4.6 | 9999 - no table for CE

    inv_7 : str | None
        INV.7 - Initial Quantity (NM) O S13.4.4.7

    inv_8 : str | None
        INV.8 - Current Quantity (NM) O S13.4.4.8

    inv_9 : str | None
        INV.9 - Available Quantity (NM) O S13.4.4.9

    inv_10 : str | None
        INV.10 - Consumption Quantity (NM) O S13.4.4.10

    inv_11 : CWE | None
        INV.11 - Quantity Units (CWE) O S13.4.4.11 | 9999 - no table for CE

    inv_12 : str | None
        INV.12 - Expiration Date/Time (DTM) O S13.4.4.12

    inv_13 : str | None
        INV.13 - First Used Date/Time (DTM) O S13.4.4.13

    inv_15 : list[CWE] | None
        INV.15 - Test/Fluid Identifier(s) (CWE) O rep S13.4.4.15 | 9999 - no table for CE

    inv_16 : str | None
        INV.16 - Manufacturer Lot Number (ST) O S13.4.4.16

    inv_17 : CWE | None
        INV.17 - Manufacturer Identifier (CWE) O S13.4.4.17 | 0385 - Manufacturer Identifier

    inv_18 : CWE | None
        INV.18 - Supplier Identifier (CWE) O S13.4.4.18 | 0386 - Supplier Identifier

    inv_19 : CQ | None
        INV.19 - On Board Stability Time (CQ) O S13.4.4.19

    inv_20 : CQ | None
        INV.20 - Target Value (CQ) O S13.4.4.20
    """

    inv_1: CWE = Field(
        validation_alias=AliasChoices(
            "inv_1",
            "substance_identifier",
            "INV.1",
        ),
        serialization_alias="INV.1",
        title="Substance Identifier",
        description="R | Item #01372 | Table 0451 - Substance Identifier",
    )

    inv_2: List[CWE] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "inv_2",
            "substance_status",
            "INV.2",
        ),
        serialization_alias="INV.2",
        title="Substance Status",
        description="R | Item #01373 | Table 0383 - Substance Status",
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
        description="O | Item #01374 | Table 0384 - Substance Type",
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
        description="O | Item #01532 | Table 9999 - no table for CE",
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
        description="O | Item #01376 | Table 9999 - no table for CE",
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
        description="O | Item #01377 | Table 9999 - no table for CE",
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
        description="O | Item #01378",
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
        description="O | Item #01379",
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
        description="O | Item #01380",
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
        description="O | Item #01381",
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
        description="O | Item #01382 | Table 9999 - no table for CE",
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
        description="O | Item #01383",
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
        description="O | Item #01384",
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
        description="O | Item #01386 | Table 9999 - no table for CE",
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
        description="O | Item #01387",
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
        description="O | Item #00286 | Table 0385 - Manufacturer Identifier",
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
        description="O | Item #01389 | Table 0386 - Supplier Identifier",
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
        description="O | Item #01626",
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
        description="O | Item #01896",
    )

    @field_validator("inv_7", "inv_8", "inv_9", "inv_10", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    @field_validator("inv_12", "inv_13", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        if _RE_DTM.fullmatch(v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = ConfigDict(populate_by_name=True)
