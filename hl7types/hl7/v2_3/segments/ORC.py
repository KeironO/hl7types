"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: ORC
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.EI import EI
from ..datatypes.PL import PL
from ..datatypes.TQ import TQ
from ..datatypes.TS import TS
from ..datatypes.XCN import XCN


class ORC(HL7Model):
    """HL7 v2 ORC segment.

    Attributes
    ----------
    orc_1 : str
        ORC.1 (req) - Order Control (ID)

    orc_2 : list[EI] | None
        ORC.2 (opt, rep) - Placer Order Number (EI)

    orc_3 : EI | None
        ORC.3 (opt) - Filler Order Number (EI)

    orc_4 : EI | None
        ORC.4 (opt) - Placer Group Number (EI)

    orc_5 : str | None
        ORC.5 (opt) - Order Status (ID)

    orc_6 : str | None
        ORC.6 (opt) - Response Flag (ID)

    orc_7 : TQ
        ORC.7 (req) - Quantity/Timing (TQ)

    orc_8 : str | None
        ORC.8 (opt) - Parent (CM)

    orc_9 : TS | None
        ORC.9 (opt) - Date/Time of Transaction (TS)

    orc_10 : XCN | None
        ORC.10 (opt) - Entered By (XCN)

    orc_11 : XCN | None
        ORC.11 (opt) - Verified By (XCN)

    orc_12 : list[XCN] | None
        ORC.12 (opt, rep) - Ordering Provider (XCN)

    orc_13 : PL | None
        ORC.13 (opt) - Enterer's Location (PL)

    orc_14 : list[str] | None
        ORC.14 (opt, rep) - Call Back Phone Number (TN)

    orc_15 : TS | None
        ORC.15 (opt) - Order Effective Date/Time (TS)

    orc_16 : CE | None
        ORC.16 (opt) - Order Control Code Reason (CE)

    orc_17 : CE | None
        ORC.17 (opt) - Entering Organization (CE)

    orc_18 : CE | None
        ORC.18 (opt) - Entering Device (CE)

    orc_19 : XCN | None
        ORC.19 (opt) - Action By (XCN)
    """

    orc_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "orc_1",
            "order_control",
            "ORC.1",
        ),
        serialization_alias="ORC.1",
        title="Order Control",
        description="Item #215 | Table HL70119",
    )

    orc_2: Optional[List[EI]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_2",
            "placer_order_number",
            "ORC.2",
        ),
        serialization_alias="ORC.2",
        title="Placer Order Number",
        description="Item #216",
    )

    orc_3: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_3",
            "filler_order_number",
            "ORC.3",
        ),
        serialization_alias="ORC.3",
        title="Filler Order Number",
        description="Item #217",
    )

    orc_4: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_4",
            "placer_group_number",
            "ORC.4",
        ),
        serialization_alias="ORC.4",
        title="Placer Group Number",
        description="Item #218",
    )

    orc_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_5",
            "order_status",
            "ORC.5",
        ),
        serialization_alias="ORC.5",
        title="Order Status",
        description="Item #219 | Table HL70038",
    )

    orc_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_6",
            "response_flag",
            "ORC.6",
        ),
        serialization_alias="ORC.6",
        title="Response Flag",
        description="Item #220 | Table HL70121",
    )

    orc_7: TQ = Field(
        default=...,
        validation_alias=AliasChoices(
            "orc_7",
            "quantity_timing",
            "ORC.7",
        ),
        serialization_alias="ORC.7",
        title="Quantity/Timing",
        description="Item #221",
    )

    orc_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_8",
            "parent",
            "ORC.8",
        ),
        serialization_alias="ORC.8",
        title="Parent",
        description="Item #222",
    )

    orc_9: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_9",
            "date_time_of_transaction",
            "ORC.9",
        ),
        serialization_alias="ORC.9",
        title="Date/Time of Transaction",
        description="Item #223",
    )

    orc_10: Optional[XCN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_10",
            "entered_by",
            "ORC.10",
        ),
        serialization_alias="ORC.10",
        title="Entered By",
        description="Item #224",
    )

    orc_11: Optional[XCN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_11",
            "verified_by",
            "ORC.11",
        ),
        serialization_alias="ORC.11",
        title="Verified By",
        description="Item #225",
    )

    orc_12: Optional[List[XCN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_12",
            "ordering_provider",
            "ORC.12",
        ),
        serialization_alias="ORC.12",
        title="Ordering Provider",
        description="Item #226",
    )

    orc_13: Optional[PL] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_13",
            "enterer_s_location",
            "ORC.13",
        ),
        serialization_alias="ORC.13",
        title="Enterer's Location",
        description="Item #227",
    )

    orc_14: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_14",
            "call_back_phone_number",
            "ORC.14",
        ),
        serialization_alias="ORC.14",
        title="Call Back Phone Number",
        description="Item #228",
    )

    orc_15: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_15",
            "order_effective_date_time",
            "ORC.15",
        ),
        serialization_alias="ORC.15",
        title="Order Effective Date/Time",
        description="Item #229",
    )

    orc_16: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_16",
            "order_control_code_reason",
            "ORC.16",
        ),
        serialization_alias="ORC.16",
        title="Order Control Code Reason",
        description="Item #230",
    )

    orc_17: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_17",
            "entering_organization",
            "ORC.17",
        ),
        serialization_alias="ORC.17",
        title="Entering Organization",
        description="Item #231",
    )

    orc_18: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_18",
            "entering_device",
            "ORC.18",
        ),
        serialization_alias="ORC.18",
        title="Entering Device",
        description="Item #232",
    )

    orc_19: Optional[XCN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_19",
            "action_by",
            "ORC.19",
        ),
        serialization_alias="ORC.19",
        title="Action By",
        description="Item #233",
    )

    model_config = {"populate_by_name": True}
