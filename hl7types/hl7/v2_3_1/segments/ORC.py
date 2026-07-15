"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: ORC
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.EI import EI
from ..datatypes.EIP import EIP
from ..datatypes.PL import PL
from ..datatypes.TQ import TQ
from ..datatypes.TS import TS
from ..datatypes.XAD import XAD
from ..datatypes.XCN import XCN
from ..datatypes.XON import XON
from ..datatypes.XTN import XTN


class ORC(HL7Model):
    """ORC - common order segment (S4.3.1).

    Attributes
    ----------
    orc_1 : str | None
        ORC.1 - Order Control (ID) NA S4.3.1.1 | 0119 - Order control codes

    orc_2 : EI | None
        ORC.2 - Placer Order Number (EI) NA S9.5.1.14

    orc_3 : EI | None
        ORC.3 - Filler Order Number (EI) NA S9.5.1.15

    orc_4 : EI | None
        ORC.4 - Placer Group Number (EI) NA S10.5.2.4

    orc_5 : str | None
        ORC.5 - Order Status (ID) NA S4.3.1.5 | 0038 - Order status

    orc_6 : str | None
        ORC.6 - Response Flag (ID) NA S4.3.1.6 | 0121 - Response flag

    orc_7 : TQ | None
        ORC.7 - Quantity/Timing (TQ) NA S7.3.1.27

    orc_8 : EIP | None
        ORC.8 - Parent (EIP) NA S4.3.1.8

    orc_9 : TS | None
        ORC.9 - Date/Time of Transaction (TS) NA S4.3.1.9

    orc_10 : list[XCN] | None
        ORC.10 - Entered By (XCN) NA rep S4.3.1.10

    orc_11 : list[XCN] | None
        ORC.11 - Verified By (XCN) NA rep S4.3.1.11

    orc_12 : list[XCN] | None
        ORC.12 - Ordering Provider (XCN) NA rep S7.3.1.16

    orc_13 : PL | None
        ORC.13 - Enterer’s Location (PL) NA S4.3.1.13

    orc_14 : list[XTN] | None
        ORC.14 - Call Back Phone Number (XTN) NA rep S4.3.1.14

    orc_15 : TS | None
        ORC.15 - Order Effective Date/Time (TS) NA S4.3.1.15

    orc_16 : CE | None
        ORC.16 - Order Control Code Reason (CE) NA S4.3.1.16

    orc_17 : CE | None
        ORC.17 - Entering Organization (CE) NA S4.3.1.17

    orc_18 : CE | None
        ORC.18 - Entering Device (CE) NA S4.3.1.18

    orc_19 : list[XCN] | None
        ORC.19 - Action By (XCN) NA rep S4.3.1.19

    orc_20 : CE | None
        ORC.20 - Advanced Beneficiary Notice Code (CE) O S4.3.1.20 | 0339 - Advanced Beneficiary Notice Code

    orc_21 : list[XON] | None
        ORC.21 - Ordering Facility Name (XON) O rep S4.3.1.21

    orc_22 : list[XAD] | None
        ORC.22 - Ordering Facility Address (XAD) O rep S4.3.1.22

    orc_23 : list[XTN] | None
        ORC.23 - Ordering Facility Phone Number (XTN) O rep S4.3.1.23

    orc_24 : list[XAD] | None
        ORC.24 - Ordering Provider Address (XAD) O rep S4.3.1.24
    """

    orc_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_1",
            "order_control",
            "ORC.1",
        ),
        serialization_alias="ORC.1",
        title="Order Control",
        description=(
            "NA | Item #00215 | Table 0119 - Order control codes | LEN:2"
        ),
    )

    orc_2: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_2",
            "placer_order_number",
            "ORC.2",
        ),
        serialization_alias="ORC.2",
        title="Placer Order Number",
        description="NA | Item #00216",
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
        description="NA | Item #00217",
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
        description="NA | Item #00219 | Table 0038 - Order status | LEN:2",
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
        description="NA | Item #00220 | Table 0121 - Response flag | LEN:1",
    )

    orc_7: Optional[TQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_7",
            "quantity_timing",
            "ORC.7",
        ),
        serialization_alias="ORC.7",
        title="Quantity/Timing",
        description="NA | Item #00221",
    )

    orc_8: Optional[EIP] = Field(
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
        title="Date/Time of Transaction",
        description="NA | Item #00223",
    )

    orc_10: Optional[List[XCN]] = Field(
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

    orc_11: Optional[List[XCN]] = Field(
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

    orc_12: Optional[List[XCN]] = Field(
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

    orc_13: Optional[PL] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_13",
            "enterer_s_location",
            "ORC.13",
        ),
        serialization_alias="ORC.13",
        title="Enterer’s Location",
        description="NA | Item #00227",
    )

    orc_14: Optional[List[XTN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_14",
            "call_back_phone_number",
            "ORC.14",
        ),
        serialization_alias="ORC.14",
        title="Call Back Phone Number",
        description="NA | Item #00228",
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

    orc_19: Optional[List[XCN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_19",
            "action_by",
            "ORC.19",
        ),
        serialization_alias="ORC.19",
        title="Action By",
        description="NA | Item #00233",
    )

    orc_20: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_20",
            "advanced_beneficiary_notice_code",
            "ORC.20",
        ),
        serialization_alias="ORC.20",
        title="Advanced Beneficiary Notice Code",
        description=(
            "O | Item #01310 | Table 0339 - Advanced Beneficiary Notice Code"
        ),
    )

    orc_21: Optional[List[XON]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_21",
            "ordering_facility_name",
            "ORC.21",
        ),
        serialization_alias="ORC.21",
        title="Ordering Facility Name",
        description="O | Item #01311",
    )

    orc_22: Optional[List[XAD]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_22",
            "ordering_facility_address",
            "ORC.22",
        ),
        serialization_alias="ORC.22",
        title="Ordering Facility Address",
        description="O | Item #01312",
    )

    orc_23: Optional[List[XTN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_23",
            "ordering_facility_phone_number",
            "ORC.23",
        ),
        serialization_alias="ORC.23",
        title="Ordering Facility Phone Number",
        description="O | Item #01313",
    )

    orc_24: Optional[List[XAD]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_24",
            "ordering_provider_address",
            "ORC.24",
        ),
        serialization_alias="ORC.24",
        title="Ordering Provider Address",
        description="O | Item #01314",
    )

    model_config = {"populate_by_name": True}
