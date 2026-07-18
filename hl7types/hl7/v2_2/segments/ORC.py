"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: ORC
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.TQ import TQ
from ..datatypes.TS import TS


class ORC(HL7Model):
    """COMMOM ORDER (S4.3.1).

    Attributes
    ----------
    orc_1 : str
        ORC.1 - Order Control (ID) R S4.3.1.1 | 0119 - ORDER CONTROL

    orc_2 : str | None
        ORC.2 - Placer Order Number (CM) C S4.5.1.2

    orc_3 : str | None
        ORC.3 - Filler Order Number (CM) C S6.4.1.23

    orc_4 : str | None
        ORC.4 - Placer Group Number (CM) NA S4.3.1.4

    orc_5 : str | None
        ORC.5 - Order Status (ID) NA S4.3.1.5 | 0038 - ORDER STATUS

    orc_6 : str | None
        ORC.6 - Response Flag (ID) NA S4.3.1.6 | 0121 - RESPONSE FLAG

    orc_7 : list[TQ] | None
        ORC.7 - Quantity / timing (TQ) NA rep S4.8.12.3

    orc_8 : str | None
        ORC.8 - Parent (CM) NA S4.3.1.8

    orc_9 : TS | None
        ORC.9 - Date / time of transaction (TS) NA S4.3.1.9

    orc_10 : str | None
        ORC.10 - Entered By (CN) NA S4.3.1.10

    orc_11 : str | None
        ORC.11 - Verified By (CN) NA S4.3.1.11

    orc_12 : str | None
        ORC.12 - Ordering Provider (CN) NA S4.5.1.16

    orc_13 : str | None
        ORC.13 - Enterer's Location (CM) NA S4.3.1.13

    orc_14 : list[str] | None
        ORC.14 - Call Back Phone Number (TN) NA rep S4.3.1.14

    orc_15 : TS | None
        ORC.15 - Order effective date / time (TS) NA S4.3.1.15

    orc_16 : CE | None
        ORC.16 - Order Control Code Reason (CE) NA S4.3.1.16

    orc_17 : CE | None
        ORC.17 - Entering Organization (CE) NA S4.3.1.17

    orc_18 : CE | None
        ORC.18 - Entering Device (CE) NA S4.3.1.18

    orc_19 : str | None
        ORC.19 - Action by (CN) NA S4.3.1.19
    """

    orc_1: str = Field(
        validation_alias=AliasChoices(
            "orc_1",
            "order_control",
            "ORC.1",
        ),
        serialization_alias="ORC.1",
        title="Order Control",
        description="R | Item #00215 | Table 0119 - ORDER CONTROL | LEN:2",
    )

    orc_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_2",
            "placer_order_number",
            "ORC.2",
        ),
        serialization_alias="ORC.2",
        title="Placer Order Number",
        description="C | Item #00216",
    )

    orc_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_3",
            "filler_order_number",
            "ORC.3",
        ),
        serialization_alias="ORC.3",
        title="Filler Order Number",
        description="C | Item #00217",
    )

    orc_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_4",
            "placer_group_number",
            "ORC.4",
        ),
        serialization_alias="ORC.4",
        title="Placer Group Number",
        description="NA | Item #00218",
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
        description="NA | Item #00219 | Table 0038 - ORDER STATUS | LEN:2",
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
        description="NA | Item #00220 | Table 0121 - RESPONSE FLAG | LEN:1",
    )

    orc_7: Optional[List[TQ]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_7",
            "quantity_timing",
            "ORC.7",
        ),
        serialization_alias="ORC.7",
        title="Quantity / timing",
        description="NA | Item #00221",
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
        description="NA | Item #00222",
    )

    orc_9: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_9",
            "date_time_of_transaction",
            "ORC.9",
        ),
        serialization_alias="ORC.9",
        title="Date / time of transaction",
        description="NA | Item #00223",
    )

    orc_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_10",
            "entered_by",
            "ORC.10",
        ),
        serialization_alias="ORC.10",
        title="Entered By",
        description="NA | Item #00224",
    )

    orc_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_11",
            "verified_by",
            "ORC.11",
        ),
        serialization_alias="ORC.11",
        title="Verified By",
        description="NA | Item #00225",
    )

    orc_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_12",
            "ordering_provider",
            "ORC.12",
        ),
        serialization_alias="ORC.12",
        title="Ordering Provider",
        description="NA | Item #00226",
    )

    orc_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_13",
            "enterer_s_location",
            "ORC.13",
        ),
        serialization_alias="ORC.13",
        title="Enterer's Location",
        description="NA | Item #00227",
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
        description="NA | Item #00228 | LEN:40",
    )

    orc_15: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_15",
            "order_effective_date_time",
            "ORC.15",
        ),
        serialization_alias="ORC.15",
        title="Order effective date / time",
        description="NA | Item #00229",
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
        description="NA | Item #00230",
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
        description="NA | Item #00231",
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
        description="NA | Item #00232",
    )

    orc_19: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_19",
            "action_by",
            "ORC.19",
        ),
        serialization_alias="ORC.19",
        title="Action by",
        description="NA | Item #00233",
    )

    model_config = ConfigDict(populate_by_name=True)
