"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: IVT
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CNE import CNE
from ..datatypes.CP import CP
from ..datatypes.CWE import CWE
from ..datatypes.EI import EI


class IVT(BaseModel):
    """HL7 v2 IVT segment."""

    ivt_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "ivt_1",
            "set_id_ivt",
            "IVT.1",
        ),
        serialization_alias="IVT.1",
        title="Set Id - IVT",
        description="Item #2062",
    )

    ivt_2: EI = Field(
        default=...,
        validation_alias=AliasChoices(
            "ivt_2",
            "inventory_location_identifier",
            "IVT.2",
        ),
        serialization_alias="IVT.2",
        title="Inventory Location Identifier",
        description="Item #2063",
    )

    ivt_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivt_3",
            "inventory_location_name",
            "IVT.3",
        ),
        serialization_alias="IVT.3",
        title="Inventory Location Name",
        description="Item #2277",
    )

    ivt_4: EI | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivt_4",
            "source_location_identifier",
            "IVT.4",
        ),
        serialization_alias="IVT.4",
        title="Source Location Identifier",
        description="Item #2064",
    )

    ivt_5: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivt_5",
            "source_location_name",
            "IVT.5",
        ),
        serialization_alias="IVT.5",
        title="Source Location Name",
        description="Item #2278",
    )

    ivt_6: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivt_6",
            "item_status",
            "IVT.6",
        ),
        serialization_alias="IVT.6",
        title="Item Status",
        description="Item #2065 | Table HL70625",
    )

    ivt_7: list[EI] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivt_7",
            "bin_location_identifier",
            "IVT.7",
        ),
        serialization_alias="IVT.7",
        title="Bin Location Identifier",
        description="Item #2066",
    )

    ivt_8: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivt_8",
            "order_packaging",
            "IVT.8",
        ),
        serialization_alias="IVT.8",
        title="Order Packaging",
        description="Item #2067 | Table HL70818",
    )

    ivt_9: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivt_9",
            "issue_packaging",
            "IVT.9",
        ),
        serialization_alias="IVT.9",
        title="Issue Packaging",
        description="Item #2068",
    )

    ivt_10: EI | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivt_10",
            "default_inventory_asset_account",
            "IVT.10",
        ),
        serialization_alias="IVT.10",
        title="Default Inventory Asset Account",
        description="Item #2069",
    )

    ivt_11: CNE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivt_11",
            "patient_chargeable_indicator",
            "IVT.11",
        ),
        serialization_alias="IVT.11",
        title="Patient Chargeable Indicator",
        description="Item #2070 | Table HL70532",
    )

    ivt_12: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivt_12",
            "transaction_code",
            "IVT.12",
        ),
        serialization_alias="IVT.12",
        title="Transaction Code",
        description="Item #361 | Table HL70132",
    )

    ivt_13: CP | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivt_13",
            "transaction_amount_unit",
            "IVT.13",
        ),
        serialization_alias="IVT.13",
        title="Transaction amount - unit",
        description="Item #366",
    )

    ivt_14: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivt_14",
            "item_importance_code",
            "IVT.14",
        ),
        serialization_alias="IVT.14",
        title="Item Importance Code",
        description="Item #2073 | Table HL70634",
    )

    ivt_15: CNE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivt_15",
            "stocked_item_indicator",
            "IVT.15",
        ),
        serialization_alias="IVT.15",
        title="Stocked Item Indicator",
        description="Item #2074 | Table HL70532",
    )

    ivt_16: CNE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivt_16",
            "consignment_item_indicator",
            "IVT.16",
        ),
        serialization_alias="IVT.16",
        title="Consignment Item Indicator",
        description="Item #2075 | Table HL70532",
    )

    ivt_17: CNE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivt_17",
            "reusable_item_indicator",
            "IVT.17",
        ),
        serialization_alias="IVT.17",
        title="Reusable Item Indicator",
        description="Item #2076 | Table HL70532",
    )

    ivt_18: CP | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivt_18",
            "reusable_cost",
            "IVT.18",
        ),
        serialization_alias="IVT.18",
        title="Reusable Cost",
        description="Item #2077",
    )

    ivt_19: list[EI] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivt_19",
            "substitute_item_identifier",
            "IVT.19",
        ),
        serialization_alias="IVT.19",
        title="Substitute Item Identifier",
        description="Item #2078",
    )

    ivt_20: EI | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivt_20",
            "latex_free_substitute_item_identifier",
            "IVT.20",
        ),
        serialization_alias="IVT.20",
        title="Latex-Free Substitute Item Identifier",
        description="Item #2079",
    )

    ivt_21: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivt_21",
            "recommended_reorder_theory",
            "IVT.21",
        ),
        serialization_alias="IVT.21",
        title="Recommended Reorder Theory",
        description="Item #2080 | Table HL70642",
    )

    ivt_22: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivt_22",
            "recommended_safety_stock_days",
            "IVT.22",
        ),
        serialization_alias="IVT.22",
        title="Recommended Safety Stock Days",
        description="Item #2081",
    )

    ivt_23: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivt_23",
            "recommended_maximum_days_inventory",
            "IVT.23",
        ),
        serialization_alias="IVT.23",
        title="Recommended Maximum Days Inventory",
        description="Item #2082",
    )

    ivt_24: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivt_24",
            "recommended_order_point",
            "IVT.24",
        ),
        serialization_alias="IVT.24",
        title="Recommended Order Point",
        description="Item #2083",
    )

    ivt_25: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivt_25",
            "recommended_order_amount",
            "IVT.25",
        ),
        serialization_alias="IVT.25",
        title="Recommended Order Amount",
        description="Item #2084",
    )

    ivt_26: CNE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivt_26",
            "operating_room_par_level_indicator",
            "IVT.26",
        ),
        serialization_alias="IVT.26",
        title="Operating Room Par Level Indicator",
        description="Item #2085 | Table HL70532",
    )

    model_config = {"populate_by_name": True}
