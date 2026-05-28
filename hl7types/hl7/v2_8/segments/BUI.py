"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: BUI
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CNE import CNE
from ..datatypes.CWE import CWE
from ..datatypes.EI import EI
from ..datatypes.NR import NR
from ..datatypes.XON import XON


class BUI(BaseModel):
    """HL7 v2 BUI segment."""

    bui_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bui_1",
            "set_id_bui",
            "BUI.1",
        ),
        serialization_alias="BUI.1",
        title="Set ID - BUI",
        description="Item #3373",
    )

    bui_2: EI = Field(
        default=...,
        validation_alias=AliasChoices(
            "bui_2",
            "blood_unit_identifier",
            "BUI.2",
        ),
        serialization_alias="BUI.2",
        title="Blood Unit Identifier",
        description="Item #3374",
    )

    bui_3: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "bui_3",
            "blood_unit_type",
            "BUI.3",
        ),
        serialization_alias="BUI.3",
        title="Blood Unit Type",
        description="Item #3375 | Table HL70566",
    )

    bui_4: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "bui_4",
            "blood_unit_weight",
            "BUI.4",
        ),
        serialization_alias="BUI.4",
        title="Blood Unit Weight",
        description="Item #3376",
    )

    bui_5: CNE = Field(
        default=...,
        validation_alias=AliasChoices(
            "bui_5",
            "weight_units",
            "BUI.5",
        ),
        serialization_alias="BUI.5",
        title="Weight Units",
        description="Item #3377 | Table HL70929",
    )

    bui_6: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "bui_6",
            "blood_unit_volume",
            "BUI.6",
        ),
        serialization_alias="BUI.6",
        title="Blood Unit Volume",
        description="Item #3378",
    )

    bui_7: CNE = Field(
        default=...,
        validation_alias=AliasChoices(
            "bui_7",
            "volume_units",
            "BUI.7",
        ),
        serialization_alias="BUI.7",
        title="Volume Units",
        description="Item #3379 | Table HL70930",
    )

    bui_8: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "bui_8",
            "container_catalog_number",
            "BUI.8",
        ),
        serialization_alias="BUI.8",
        title="Container Catalog Number",
        description="Item #3380",
    )

    bui_9: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "bui_9",
            "container_lot_number",
            "BUI.9",
        ),
        serialization_alias="BUI.9",
        title="Container Lot Number",
        description="Item #3381",
    )

    bui_10: XON = Field(
        default=...,
        validation_alias=AliasChoices(
            "bui_10",
            "container_manufacturer",
            "BUI.10",
        ),
        serialization_alias="BUI.10",
        title="Container Manufacturer",
        description="Item #3382",
    )

    bui_11: NR = Field(
        default=...,
        validation_alias=AliasChoices(
            "bui_11",
            "transport_temperature",
            "BUI.11",
        ),
        serialization_alias="BUI.11",
        title="Transport Temperature",
        description="Item #3383",
    )

    bui_12: CNE = Field(
        default=...,
        validation_alias=AliasChoices(
            "bui_12",
            "transport_temperature_units",
            "BUI.12",
        ),
        serialization_alias="BUI.12",
        title="Transport Temperature Units",
        description="Item #3384 | Table HL70931",
    )

    model_config = {"populate_by_name": True}
