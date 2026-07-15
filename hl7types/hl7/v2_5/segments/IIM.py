"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: IIM
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.CWE import CWE
from ..datatypes.MO import MO
from ..datatypes.TS import TS


class IIM(HL7Model):
    """Inventory Item Master (S8.12.2).

    Attributes
    ----------
    iim_1 : CWE
        IIM.1 - Primary Key Value - IIM (CWE) R S8.12.2.1

    iim_2 : CWE
        IIM.2 - Service Item Code (CWE) R S8.12.2.2

    iim_3 : str | None
        IIM.3 - Inventory Lot Number (ST) O S8.12.2.3

    iim_4 : TS | None
        IIM.4 - Inventory Expiration Date (TS) O S8.12.2.4

    iim_5 : CWE | None
        IIM.5 - Inventory Manufacturer Name (CWE) O S8.12.2.5

    iim_6 : CWE | None
        IIM.6 - Inventory Location (CWE) O S8.12.2.6

    iim_7 : TS | None
        IIM.7 - Inventory Received Date (TS) O S8.12.2.7

    iim_8 : str | None
        IIM.8 - Inventory Received Quantity (NM) O S8.12.2.8

    iim_9 : CWE | None
        IIM.9 - Inventory Received Quantity Unit (CWE) O S8.12.2.9

    iim_10 : MO | None
        IIM.10 - Inventory Received Item Cost (MO) O S8.12.2.10

    iim_11 : TS | None
        IIM.11 - Inventory On Hand Date (TS) O S8.12.2.11

    iim_12 : str | None
        IIM.12 - Inventory On Hand Quantity (NM) O S8.12.2.12

    iim_13 : CWE | None
        IIM.13 - Inventory On Hand Quantity Unit (CWE) O S8.12.2.13

    iim_14 : CE | None
        IIM.14 - Procedure Code (CE) O S4.5.3.44 | 0088 - Procedure Code

    iim_15 : list[CE] | None
        IIM.15 - Procedure Code Modifier (CE) O rep S4.5.3.45 | 0340 - Procedure Code Modifier
    """

    iim_1: CWE = Field(
        validation_alias=AliasChoices(
            "iim_1",
            "primary_key_value_iim",
            "IIM.1",
        ),
        serialization_alias="IIM.1",
        title="Primary Key Value - IIM",
        description="R | Item #01897",
    )

    iim_2: CWE = Field(
        validation_alias=AliasChoices(
            "iim_2",
            "service_item_code",
            "IIM.2",
        ),
        serialization_alias="IIM.2",
        title="Service Item Code",
        description="R | Item #01799",
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
        description="O | Item #01800 | LEN:250",
    )

    iim_4: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "iim_4",
            "inventory_expiration_date",
            "IIM.4",
        ),
        serialization_alias="IIM.4",
        title="Inventory Expiration Date",
        description="O | Item #01801",
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
        description="O | Item #01802",
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
        description="O | Item #01803",
    )

    iim_7: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "iim_7",
            "inventory_received_date",
            "IIM.7",
        ),
        serialization_alias="IIM.7",
        title="Inventory Received Date",
        description="O | Item #01804",
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
        description="O | Item #01805 | LEN:12",
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
        description="O | Item #01806",
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
        description="O | Item #01807",
    )

    iim_11: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "iim_11",
            "inventory_on_hand_date",
            "IIM.11",
        ),
        serialization_alias="IIM.11",
        title="Inventory On Hand Date",
        description="O | Item #01808",
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
        description="O | Item #01809 | LEN:12",
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
        description="O | Item #01810",
    )

    iim_14: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "iim_14",
            "procedure_code",
            "IIM.14",
        ),
        serialization_alias="IIM.14",
        title="Procedure Code",
        description="O | Item #00393 | Table 0088 - Procedure Code",
    )

    iim_15: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "iim_15",
            "procedure_code_modifier",
            "IIM.15",
        ),
        serialization_alias="IIM.15",
        title="Procedure Code Modifier",
        description="O | Item #01316 | Table 0340 - Procedure Code Modifier",
    )

    @field_validator("iim_8", "iim_12", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
