"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: IVT
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CNE import CNE
from ..datatypes.CP import CP
from ..datatypes.CWE import CWE
from ..datatypes.EI import EI

_RE_SI = re.compile(r'\d*')
_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class IVT(HL7Model):
    """Material Location (S17.4.7).

    Attributes
    ----------
    ivt_1 : str
        IVT.1 - Set Id - IVT (SI) R S17.4.7.1

    ivt_2 : EI
        IVT.2 - Inventory Location Identifier (EI) R S17.4.7.2

    ivt_3 : str | None
        IVT.3 - Inventory Location Name (ST) O S17.4.7.3

    ivt_4 : EI | None
        IVT.4 - Source Location Identifier (EI) O S17.4.7.4

    ivt_5 : str | None
        IVT.5 - Source Location Name (ST) O S17.4.7.5

    ivt_6 : CWE | None
        IVT.6 - Item Status (CWE) O S17.4.7.6 | 0625 - Item Status Codes

    ivt_7 : list[EI] | None
        IVT.7 - Bin Location Identifier (EI) O rep S17.4.7.7

    ivt_8 : CWE | None
        IVT.8 - Order Packaging (CWE) O S17.4.7.8 | 0818 - Package

    ivt_9 : CWE | None
        IVT.9 - Issue Packaging (CWE) O S17.4.7.9

    ivt_10 : EI | None
        IVT.10 - Default Inventory Asset Account (EI) O S17.4.7.10

    ivt_11 : CNE | None
        IVT.11 - Patient Chargeable Indicator (CNE) O S17.4.2.11 | 0532 - Expanded Yes/no Indicator

    ivt_12 : CWE | None
        IVT.12 - Transaction Code (CWE) O S17.4.2.12 | 0132 - Transaction Code

    ivt_13 : CP | None
        IVT.13 - Transaction amount - unit (CP) O S17.4.2.13

    ivt_14 : CWE | None
        IVT.14 - Item Importance Code (CWE) O S17.4.7.14 | 0634 - Item Importance Codes

    ivt_15 : CNE | None
        IVT.15 - Stocked Item Indicator (CNE) O S17.4.7.15 | 0532 - Expanded Yes/no Indicator

    ivt_16 : CNE | None
        IVT.16 - Consignment Item Indicator (CNE) O S17.4.7.16 | 0532 - Expanded Yes/no Indicator

    ivt_17 : CNE | None
        IVT.17 - Reusable Item Indicator (CNE) O S17.4.7.17 | 0532 - Expanded Yes/no Indicator

    ivt_18 : CP | None
        IVT.18 - Reusable Cost (CP) O S17.4.7.18

    ivt_19 : list[EI] | None
        IVT.19 - Substitute Item Identifier (EI) O rep S17.4.7.19

    ivt_20 : EI | None
        IVT.20 - Latex-Free Substitute Item Identifier (EI) O S17.4.7.20

    ivt_21 : CWE | None
        IVT.21 - Recommended Reorder Theory (CWE) O S17.4.7.21 | 0642 - Reorder Theory Codes

    ivt_22 : str | None
        IVT.22 - Recommended Safety Stock Days (NM) O S17.4.7.22

    ivt_23 : str | None
        IVT.23 - Recommended Maximum Days Inventory (NM) O S17.4.7.23

    ivt_24 : str | None
        IVT.24 - Recommended Order Point (NM) O S17.4.7.24

    ivt_25 : str | None
        IVT.25 - Recommended Order Amount (NM) O S17.4.7.25

    ivt_26 : CNE | None
        IVT.26 - Operating Room Par Level Indicator (CNE) O S17.4.7.26 | 0532 - Expanded Yes/no Indicator
    """

    ivt_1: str = Field(
        validation_alias=AliasChoices(
            "ivt_1",
            "set_id_ivt",
            "IVT.1",
        ),
        serialization_alias="IVT.1",
        title="Set Id - IVT",
        description="R | Item #02062 | LEN:4",
    )

    ivt_2: EI = Field(
        validation_alias=AliasChoices(
            "ivt_2",
            "inventory_location_identifier",
            "IVT.2",
        ),
        serialization_alias="IVT.2",
        title="Inventory Location Identifier",
        description="R | Item #02063",
    )

    ivt_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivt_3",
            "inventory_location_name",
            "IVT.3",
        ),
        serialization_alias="IVT.3",
        title="Inventory Location Name",
        description="O | Item #02277",
    )

    ivt_4: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivt_4",
            "source_location_identifier",
            "IVT.4",
        ),
        serialization_alias="IVT.4",
        title="Source Location Identifier",
        description="O | Item #02064",
    )

    ivt_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivt_5",
            "source_location_name",
            "IVT.5",
        ),
        serialization_alias="IVT.5",
        title="Source Location Name",
        description="O | Item #02278",
    )

    ivt_6: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivt_6",
            "item_status",
            "IVT.6",
        ),
        serialization_alias="IVT.6",
        title="Item Status",
        description="O | Item #02065 | Table 0625 - Item Status Codes",
    )

    ivt_7: Optional[List[EI]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivt_7",
            "bin_location_identifier",
            "IVT.7",
        ),
        serialization_alias="IVT.7",
        title="Bin Location Identifier",
        description="O | Item #02066",
    )

    ivt_8: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivt_8",
            "order_packaging",
            "IVT.8",
        ),
        serialization_alias="IVT.8",
        title="Order Packaging",
        description="O | Item #02067 | Table 0818 - Package",
    )

    ivt_9: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivt_9",
            "issue_packaging",
            "IVT.9",
        ),
        serialization_alias="IVT.9",
        title="Issue Packaging",
        description="O | Item #02068",
    )

    ivt_10: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivt_10",
            "default_inventory_asset_account",
            "IVT.10",
        ),
        serialization_alias="IVT.10",
        title="Default Inventory Asset Account",
        description="O | Item #02069",
    )

    ivt_11: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivt_11",
            "patient_chargeable_indicator",
            "IVT.11",
        ),
        serialization_alias="IVT.11",
        title="Patient Chargeable Indicator",
        description="O | Item #02070 | Table 0532 - Expanded Yes/no Indicator",
    )

    ivt_12: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivt_12",
            "transaction_code",
            "IVT.12",
        ),
        serialization_alias="IVT.12",
        title="Transaction Code",
        description="O | Item #00361 | Table 0132 - Transaction Code",
    )

    ivt_13: Optional[CP] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivt_13",
            "transaction_amount_unit",
            "IVT.13",
        ),
        serialization_alias="IVT.13",
        title="Transaction amount - unit",
        description="O | Item #00366",
    )

    ivt_14: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivt_14",
            "item_importance_code",
            "IVT.14",
        ),
        serialization_alias="IVT.14",
        title="Item Importance Code",
        description="O | Item #02073 | Table 0634 - Item Importance Codes",
    )

    ivt_15: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivt_15",
            "stocked_item_indicator",
            "IVT.15",
        ),
        serialization_alias="IVT.15",
        title="Stocked Item Indicator",
        description="O | Item #02074 | Table 0532 - Expanded Yes/no Indicator",
    )

    ivt_16: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivt_16",
            "consignment_item_indicator",
            "IVT.16",
        ),
        serialization_alias="IVT.16",
        title="Consignment Item Indicator",
        description="O | Item #02075 | Table 0532 - Expanded Yes/no Indicator",
    )

    ivt_17: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivt_17",
            "reusable_item_indicator",
            "IVT.17",
        ),
        serialization_alias="IVT.17",
        title="Reusable Item Indicator",
        description="O | Item #02076 | Table 0532 - Expanded Yes/no Indicator",
    )

    ivt_18: Optional[CP] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivt_18",
            "reusable_cost",
            "IVT.18",
        ),
        serialization_alias="IVT.18",
        title="Reusable Cost",
        description="O | Item #02077",
    )

    ivt_19: Optional[List[EI]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivt_19",
            "substitute_item_identifier",
            "IVT.19",
        ),
        serialization_alias="IVT.19",
        title="Substitute Item Identifier",
        description="O | Item #02078",
    )

    ivt_20: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivt_20",
            "latex_free_substitute_item_identifier",
            "IVT.20",
        ),
        serialization_alias="IVT.20",
        title="Latex-Free Substitute Item Identifier",
        description="O | Item #02079",
    )

    ivt_21: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivt_21",
            "recommended_reorder_theory",
            "IVT.21",
        ),
        serialization_alias="IVT.21",
        title="Recommended Reorder Theory",
        description="O | Item #02080 | Table 0642 - Reorder Theory Codes",
    )

    ivt_22: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivt_22",
            "recommended_safety_stock_days",
            "IVT.22",
        ),
        serialization_alias="IVT.22",
        title="Recommended Safety Stock Days",
        description="O | Item #02081",
    )

    ivt_23: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivt_23",
            "recommended_maximum_days_inventory",
            "IVT.23",
        ),
        serialization_alias="IVT.23",
        title="Recommended Maximum Days Inventory",
        description="O | Item #02082",
    )

    ivt_24: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivt_24",
            "recommended_order_point",
            "IVT.24",
        ),
        serialization_alias="IVT.24",
        title="Recommended Order Point",
        description="O | Item #02083",
    )

    ivt_25: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivt_25",
            "recommended_order_amount",
            "IVT.25",
        ),
        serialization_alias="IVT.25",
        title="Recommended Order Amount",
        description="O | Item #02084",
    )

    ivt_26: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ivt_26",
            "operating_room_par_level_indicator",
            "IVT.26",
        ),
        serialization_alias="IVT.26",
        title="Operating Room Par Level Indicator",
        description="O | Item #02085 | Table 0532 - Expanded Yes/no Indicator",
    )

    @field_validator("ivt_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        if not _RE_SI.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("ivt_22", "ivt_23", "ivt_24", "ivt_25", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
