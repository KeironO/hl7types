"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: ILT
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE
from ..datatypes.MO import MO


class ILT(HL7Model):
    """HL7 v2 ILT segment.

    Attributes
    ----------
    ilt_1 : str
        ILT.1 (req) - Set Id - ILT (SI)

    ilt_2 : str
        ILT.2 (req) - Inventory Lot Number (ST)

    ilt_3 : str | None
        ILT.3 (opt) - Inventory Expiration Date (DTM)

    ilt_4 : str | None
        ILT.4 (opt) - Inventory Received Date (DTM)

    ilt_5 : str | None
        ILT.5 (opt) - Inventory Received Quantity (NM)

    ilt_6 : CWE | None
        ILT.6 (opt) - Inventory Received Quantity Unit (CWE)

    ilt_7 : MO | None
        ILT.7 (opt) - Inventory Received Item Cost (MO)

    ilt_8 : str | None
        ILT.8 (opt) - Inventory On Hand Date (DTM)

    ilt_9 : str | None
        ILT.9 (opt) - Inventory On Hand Quantity (NM)

    ilt_10 : CWE | None
        ILT.10 (opt) - Inventory On Hand Quantity Unit (CWE)
    """

    ilt_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "ilt_1",
            "set_id_ilt",
            "ILT.1",
        ),
        serialization_alias="ILT.1",
        title="Set Id - ILT",
        description="Item #2086",
    )

    ilt_2: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "ilt_2",
            "inventory_lot_number",
            "ILT.2",
        ),
        serialization_alias="ILT.2",
        title="Inventory Lot Number",
        description="Item #1800",
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
        description="Item #1801",
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
        description="Item #1804",
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
        description="Item #1805",
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
        description="Item #1806",
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
        description="Item #1807",
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
        description="Item #1808",
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
        description="Item #1809",
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
        description="Item #1810",
    )

    model_config = {"populate_by_name": True}
