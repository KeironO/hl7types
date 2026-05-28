"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: BTX
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE
from ..datatypes.CNE import CNE
from ..datatypes.CWE import CWE
from ..datatypes.EI import EI
from ..datatypes.TS import TS
from ..datatypes.XCN import XCN
from ..datatypes.XON import XON


class BTX(BaseModel):
    """HL7 v2 BTX segment."""

    btx_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "btx_1",
            "set_id_btx",
            "BTX.1",
        ),
        serialization_alias="BTX.1",
        title="Set ID - BTX",
        description="Item #1735",
    )

    btx_2: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "btx_2",
            "bc_donation_id",
            "BTX.2",
        ),
        serialization_alias="BTX.2",
        title="BC Donation ID",
        description="Item #1736",
    )

    btx_3: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "btx_3",
            "bc_component",
            "BTX.3",
        ),
        serialization_alias="BTX.3",
        title="BC Component",
        description="Item #1737",
    )

    btx_4: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "btx_4",
            "bc_blood_group",
            "BTX.4",
        ),
        serialization_alias="BTX.4",
        title="BC Blood Group",
        description="Item #1738",
    )

    btx_5: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "btx_5",
            "cp_commercial_product",
            "BTX.5",
        ),
        serialization_alias="BTX.5",
        title="CP Commercial Product",
        description="Item #1739 | Table HL70512",
    )

    btx_6: Optional[XON] = Field(
        default=None,
        validation_alias=AliasChoices(
            "btx_6",
            "cp_manufacturer",
            "BTX.6",
        ),
        serialization_alias="BTX.6",
        title="CP Manufacturer",
        description="Item #1740",
    )

    btx_7: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "btx_7",
            "cp_lot_number",
            "BTX.7",
        ),
        serialization_alias="BTX.7",
        title="CP Lot Number",
        description="Item #1741",
    )

    btx_8: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "btx_8",
            "bp_quantity",
            "BTX.8",
        ),
        serialization_alias="BTX.8",
        title="BP Quantity",
        description="Item #1742",
    )

    btx_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "btx_9",
            "bp_amount",
            "BTX.9",
        ),
        serialization_alias="BTX.9",
        title="BP Amount",
        description="Item #1743",
    )

    btx_10: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "btx_10",
            "bp_units",
            "BTX.10",
        ),
        serialization_alias="BTX.10",
        title="BP Units",
        description="Item #1744",
    )

    btx_11: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "btx_11",
            "bp_transfusion_disposition_status",
            "BTX.11",
        ),
        serialization_alias="BTX.11",
        title="BP Transfusion/Disposition Status",
        description="Item #1745 | Table HL70513",
    )

    btx_12: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "btx_12",
            "bp_message_status",
            "BTX.12",
        ),
        serialization_alias="BTX.12",
        title="BP Message Status",
        description="Item #1746 | Table HL70511",
    )

    btx_13: TS = Field(
        default=...,
        validation_alias=AliasChoices(
            "btx_13",
            "bp_date_time_of_status",
            "BTX.13",
        ),
        serialization_alias="BTX.13",
        title="BP Date/Time of Status",
        description="Item #1747",
    )

    btx_14: Optional[XCN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "btx_14",
            "bp_administrator",
            "BTX.14",
        ),
        serialization_alias="BTX.14",
        title="BP Administrator",
        description="Item #1748",
    )

    btx_15: Optional[XCN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "btx_15",
            "bp_verifier",
            "BTX.15",
        ),
        serialization_alias="BTX.15",
        title="BP Verifier",
        description="Item #1749",
    )

    btx_16: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "btx_16",
            "bp_transfusion_start_date_time_of_status",
            "BTX.16",
        ),
        serialization_alias="BTX.16",
        title="BP Transfusion Start Date/Time of Status",
        description="Item #1750",
    )

    btx_17: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "btx_17",
            "bp_transfusion_end_date_time_of_status",
            "BTX.17",
        ),
        serialization_alias="BTX.17",
        title="BP Transfusion End Date/Time of Status",
        description="Item #1751",
    )

    btx_18: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "btx_18",
            "bp_adverse_reaction_type",
            "BTX.18",
        ),
        serialization_alias="BTX.18",
        title="BP Adverse Reaction Type",
        description="Item #1752 | Table HL70514",
    )

    btx_19: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "btx_19",
            "bp_transfusion_interrupted_reason",
            "BTX.19",
        ),
        serialization_alias="BTX.19",
        title="BP Transfusion Interrupted Reason",
        description="Item #1753 | Table HL70515",
    )

    model_config = {"populate_by_name": True}
