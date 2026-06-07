"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: IIM
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CNE import CNE
from ..datatypes.CWE import CWE
from ..datatypes.MO import MO


class IIM(HL7Model):
    """HL7 v2 IIM segment.

    Attributes
    ----------
    iim_1 : CWE
        IIM.1 (req) - Primary Key Value - IIM (CWE)

    iim_2 : CWE
        IIM.2 (req) - Service Item Code (CWE)

    iim_3 : str | None
        IIM.3 (opt) - Inventory Lot Number (ST)

    iim_4 : str | None
        IIM.4 (opt) - Inventory Expiration Date (DTM)

    iim_5 : CWE | None
        IIM.5 (opt) - Inventory Manufacturer Name (CWE)

    iim_6 : CWE | None
        IIM.6 (opt) - Inventory Location (CWE)

    iim_7 : str | None
        IIM.7 (opt) - Inventory Received Date (DTM)

    iim_8 : str | None
        IIM.8 (opt) - Inventory Received Quantity (NM)

    iim_9 : CWE | None
        IIM.9 (opt) - Inventory Received Quantity Unit (CWE)

    iim_10 : MO | None
        IIM.10 (opt) - Inventory Received Item Cost (MO)

    iim_11 : str | None
        IIM.11 (opt) - Inventory On Hand Date (DTM)

    iim_12 : str | None
        IIM.12 (opt) - Inventory On Hand Quantity (NM)

    iim_13 : CWE | None
        IIM.13 (opt) - Inventory On Hand Quantity Unit (CWE)

    iim_14 : CNE | None
        IIM.14 (opt) - Procedure Code (CNE)

    iim_15 : list[CNE] | None
        IIM.15 (opt, rep) - Procedure Code Modifier (CNE)
    """

    iim_1: CWE = Field(
        validation_alias=AliasChoices(
            "iim_1",
            "primary_key_value_iim",
            "IIM.1",
        ),
        serialization_alias="IIM.1",
        title="Primary Key Value - IIM",
        description="Item #1897",
    )

    iim_2: CWE = Field(
        validation_alias=AliasChoices(
            "iim_2",
            "service_item_code",
            "IIM.2",
        ),
        serialization_alias="IIM.2",
        title="Service Item Code",
        description="Item #1799",
    )

    iim_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "iim_3",
            "inventory_lot_number",
            "IIM.3",
        ),
        serialization_alias="IIM.3",
        title="Inventory Lot Number",
        description="Item #1800",
    )

    iim_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "iim_4",
            "inventory_expiration_date",
            "IIM.4",
        ),
        serialization_alias="IIM.4",
        title="Inventory Expiration Date",
        description="Item #1801",
    )

    iim_5: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "iim_5",
            "inventory_manufacturer_name",
            "IIM.5",
        ),
        serialization_alias="IIM.5",
        title="Inventory Manufacturer Name",
        description="Item #1802",
    )

    iim_6: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "iim_6",
            "inventory_location",
            "IIM.6",
        ),
        serialization_alias="IIM.6",
        title="Inventory Location",
        description="Item #1803",
    )

    iim_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "iim_7",
            "inventory_received_date",
            "IIM.7",
        ),
        serialization_alias="IIM.7",
        title="Inventory Received Date",
        description="Item #1804",
    )

    iim_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "iim_8",
            "inventory_received_quantity",
            "IIM.8",
        ),
        serialization_alias="IIM.8",
        title="Inventory Received Quantity",
        description="Item #1805",
    )

    iim_9: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "iim_9",
            "inventory_received_quantity_unit",
            "IIM.9",
        ),
        serialization_alias="IIM.9",
        title="Inventory Received Quantity Unit",
        description="Item #1806",
    )

    iim_10: Optional[MO] = Field(
        default=None,
        validation_alias=AliasChoices(
            "iim_10",
            "inventory_received_item_cost",
            "IIM.10",
        ),
        serialization_alias="IIM.10",
        title="Inventory Received Item Cost",
        description="Item #1807",
    )

    iim_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "iim_11",
            "inventory_on_hand_date",
            "IIM.11",
        ),
        serialization_alias="IIM.11",
        title="Inventory On Hand Date",
        description="Item #1808",
    )

    iim_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "iim_12",
            "inventory_on_hand_quantity",
            "IIM.12",
        ),
        serialization_alias="IIM.12",
        title="Inventory On Hand Quantity",
        description="Item #1809",
    )

    iim_13: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "iim_13",
            "inventory_on_hand_quantity_unit",
            "IIM.13",
        ),
        serialization_alias="IIM.13",
        title="Inventory On Hand Quantity Unit",
        description="Item #1810",
    )

    iim_14: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "iim_14",
            "procedure_code",
            "IIM.14",
        ),
        serialization_alias="IIM.14",
        title="Procedure Code",
        description="Item #393 | Table HL70088",
    )

    iim_15: Optional[List[CNE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "iim_15",
            "procedure_code_modifier",
            "IIM.15",
        ),
        serialization_alias="IIM.15",
        title="Procedure Code Modifier",
        description="Item #1316 | Table HL70340",
    )

    @field_validator("iim_4", "iim_7", "iim_11", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 datetime")
        return v

    @field_validator("iim_8", "iim_12", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
