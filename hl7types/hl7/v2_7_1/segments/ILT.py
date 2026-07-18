"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: ILT
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field, ValidationInfo, field_validator
from hl7types.hl7 import HL7Model
from hl7types.hl7._validators import _apply_dt_fallback

from ..datatypes.CWE import CWE
from ..datatypes.MO import MO

_RE_SI = re.compile(r'\d*')
_RE_DTM = re.compile(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?')
_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class ILT(HL7Model):
    """Material Lot (S17.4.8).

    Attributes
    ----------
    ilt_1 : str
        ILT.1 - Set Id - ILT (SI) R S17.4.8.1

    ilt_2 : str
        ILT.2 - Inventory Lot Number (ST) R S17.4.1.3

    ilt_3 : str | None
        ILT.3 - Inventory Expiration Date (DTM) O S17.4.1.4

    ilt_4 : str | None
        ILT.4 - Inventory Received Date (DTM) O S17.4.1.7

    ilt_5 : str | None
        ILT.5 - Inventory Received Quantity (NM) O S17.4.1.8

    ilt_6 : CWE | None
        ILT.6 - Inventory Received Quantity Unit (CWE) O S17.4.1.9

    ilt_7 : MO | None
        ILT.7 - Inventory Received Item Cost (MO) O S17.4.1.10

    ilt_8 : str | None
        ILT.8 - Inventory On Hand Date (DTM) O S17.4.1.11

    ilt_9 : str | None
        ILT.9 - Inventory On Hand Quantity (NM) O S17.4.1.12

    ilt_10 : CWE | None
        ILT.10 - Inventory On Hand Quantity Unit (CWE) O S17.4.1.13
    """

    ilt_1: str = Field(
        validation_alias=AliasChoices(
            "ilt_1",
            "set_id_ilt",
            "ILT.1",
        ),
        serialization_alias="ILT.1",
        title="Set Id - ILT",
        description="R | Item #02086 | LEN:4",
    )

    ilt_2: str = Field(
        validation_alias=AliasChoices(
            "ilt_2",
            "inventory_lot_number",
            "ILT.2",
        ),
        serialization_alias="ILT.2",
        title="Inventory Lot Number",
        description="R | Item #01800",
    )

    ilt_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ilt_3",
            "inventory_expiration_date",
            "ILT.3",
        ),
        serialization_alias="ILT.3",
        title="Inventory Expiration Date",
        description="O | Item #01801",
    )

    ilt_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ilt_4",
            "inventory_received_date",
            "ILT.4",
        ),
        serialization_alias="ILT.4",
        title="Inventory Received Date",
        description="O | Item #01804",
    )

    ilt_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ilt_5",
            "inventory_received_quantity",
            "ILT.5",
        ),
        serialization_alias="ILT.5",
        title="Inventory Received Quantity",
        description="O | Item #01805",
    )

    ilt_6: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ilt_6",
            "inventory_received_quantity_unit",
            "ILT.6",
        ),
        serialization_alias="ILT.6",
        title="Inventory Received Quantity Unit",
        description="O | Item #01806",
    )

    ilt_7: Optional[MO] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ilt_7",
            "inventory_received_item_cost",
            "ILT.7",
        ),
        serialization_alias="ILT.7",
        title="Inventory Received Item Cost",
        description="O | Item #01807",
    )

    ilt_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ilt_8",
            "inventory_on_hand_date",
            "ILT.8",
        ),
        serialization_alias="ILT.8",
        title="Inventory On Hand Date",
        description="O | Item #01808",
    )

    ilt_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ilt_9",
            "inventory_on_hand_quantity",
            "ILT.9",
        ),
        serialization_alias="ILT.9",
        title="Inventory On Hand Quantity",
        description="O | Item #01809",
    )

    ilt_10: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ilt_10",
            "inventory_on_hand_quantity_unit",
            "ILT.10",
        ),
        serialization_alias="ILT.10",
        title="Inventory On Hand Quantity Unit",
        description="O | Item #01810",
    )

    @field_validator("ilt_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        if not _RE_SI.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("ilt_3", "ilt_4", "ilt_8", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        if _RE_DTM.fullmatch(v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    @field_validator("ilt_5", "ilt_9", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
