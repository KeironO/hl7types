"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
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
    """Inventory Item Master (S17.4.1).

    Attributes
    ----------
    iim_1 : CWE
        IIM.1 - Primary Key Value - IIM (CWE) R S17.4.1.1

    iim_2 : CWE
        IIM.2 - Service Item Code (CWE) R S17.4.1.2

    iim_3 : str | None
        IIM.3 - Inventory Lot Number (ST) O S17.4.1.3

    iim_4 : str | None
        IIM.4 - Inventory Expiration Date (DTM) O S17.4.1.4

    iim_5 : CWE | None
        IIM.5 - Inventory Manufacturer Name (CWE) O S17.4.1.5

    iim_6 : CWE | None
        IIM.6 - Inventory Location (CWE) O S17.4.1.6

    iim_7 : str | None
        IIM.7 - Inventory Received Date (DTM) O S17.4.1.7

    iim_8 : str | None
        IIM.8 - Inventory Received Quantity (NM) O S17.4.1.8

    iim_9 : CWE | None
        IIM.9 - Inventory Received Quantity Unit (CWE) O S17.4.1.9

    iim_10 : MO | None
        IIM.10 - Inventory Received Item Cost (MO) O S17.4.1.10

    iim_11 : str | None
        IIM.11 - Inventory On Hand Date (DTM) O S17.4.1.11

    iim_12 : str | None
        IIM.12 - Inventory On Hand Quantity (NM) O S17.4.1.12

    iim_13 : CWE | None
        IIM.13 - Inventory On Hand Quantity Unit (CWE) O S17.4.1.13

    iim_14 : CNE | None
        IIM.14 - Procedure Code (CNE) O S17.4.1.14 | 0088 - Procedure Code

    iim_15 : list[CNE] | None
        IIM.15 - Procedure Code Modifier (CNE) O rep S17.4.1.15 | 0340 - Procedure Code Modifier
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

    iim_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "iim_4",
            "inventory_expiration_date",
            "IIM.4",
        ),
        serialization_alias="IIM.4",
        title="Inventory Expiration Date",
        description="O | Item #01801 | LEN:24",
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

    iim_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "iim_7",
            "inventory_received_date",
            "IIM.7",
        ),
        serialization_alias="IIM.7",
        title="Inventory Received Date",
        description="O | Item #01804 | LEN:24",
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

    iim_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "iim_11",
            "inventory_on_hand_date",
            "IIM.11",
        ),
        serialization_alias="IIM.11",
        title="Inventory On Hand Date",
        description="O | Item #01808 | LEN:24",
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

    iim_14: Optional[CNE] = Field(
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

    iim_15: Optional[List[CNE]] = Field(
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

    @field_validator("iim_4", "iim_7", "iim_11", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        import re
        if re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    @field_validator("iim_8", "iim_12", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
