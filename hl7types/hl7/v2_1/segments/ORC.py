"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: ORC
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model


class ORC(HL7Model):
    """COMMON ORDER.

    Attributes
    ----------
    orc_1 : str
        ORC.1 - ORDER CONTROL (ST) R S4-4 | 0119 - ORDER CONTROL

    orc_2 : str | None
        ORC.2 - PLACER ORDER # (CM) O

    orc_3 : str | None
        ORC.3 - FILLER ORDER # (CM) O

    orc_4 : str | None
        ORC.4 - PLACER GROUP # (CM) O

    orc_5 : str | None
        ORC.5 - ORDER STATUS (ST) O | 0038 - ORDER STATUS

    orc_6 : str | None
        ORC.6 - RESPONSE FLAG (ST) O | 0121 - RESPONSE FLAG

    orc_7 : str | None
        ORC.7 - TIMING/QUANTITY (CM) O

    orc_8 : str | None
        ORC.8 - PARENT (CM) O

    orc_9 : str | None
        ORC.9 - DATE/TIME OF TRANSACTION (TS) O

    orc_10 : str | None
        ORC.10 - ENTERED BY (CN) O

    orc_11 : str | None
        ORC.11 - VERIFIED BY (CN) O

    orc_12 : str | None
        ORC.12 - ORDERING PROVIDER (CN) O

    orc_13 : str | None
        ORC.13 - ENTERER'S LOCATION (CM) O

    orc_14 : list[str] | None
        ORC.14 - CALL BACK PHONE NUMBER (TN) O rep
    """

    orc_1: str = Field(
        validation_alias=AliasChoices(
            "orc_1",
            "order_control",
            "ORC.1",
        ),
        serialization_alias="ORC.1",
        title="ORDER CONTROL",
        description="R | Item #00714 | Table 0119 - ORDER CONTROL | LEN:2",
    )

    orc_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_2",
            "placer_order",
            "ORC.2",
        ),
        serialization_alias="ORC.2",
        title="PLACER ORDER #",
        description="O | Item #00715 | LEN:75",
    )

    orc_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_3",
            "filler_order",
            "ORC.3",
        ),
        serialization_alias="ORC.3",
        title="FILLER ORDER #",
        description="O | Item #00716 | LEN:75",
    )

    orc_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_4",
            "placer_group",
            "ORC.4",
        ),
        serialization_alias="ORC.4",
        title="PLACER GROUP #",
        description="O | Item #00717 | LEN:75",
    )

    orc_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_5",
            "order_status",
            "ORC.5",
        ),
        serialization_alias="ORC.5",
        title="ORDER STATUS",
        description="O | Item #00718 | Table 0038 - ORDER STATUS | LEN:2",
    )

    orc_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_6",
            "response_flag",
            "ORC.6",
        ),
        serialization_alias="ORC.6",
        title="RESPONSE FLAG",
        description="O | Item #00719 | Table 0121 - RESPONSE FLAG | LEN:1",
    )

    orc_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_7",
            "timing_quantity",
            "ORC.7",
        ),
        serialization_alias="ORC.7",
        title="TIMING/QUANTITY",
        description="O | Item #00720 | LEN:200",
    )

    orc_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_8",
            "parent",
            "ORC.8",
        ),
        serialization_alias="ORC.8",
        title="PARENT",
        description="O | Item #00721 | LEN:200",
    )

    orc_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_9",
            "date_time_of_transaction",
            "ORC.9",
        ),
        serialization_alias="ORC.9",
        title="DATE/TIME OF TRANSACTION",
        description="O | Item #00722 | LEN:19",
    )

    orc_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_10",
            "entered_by",
            "ORC.10",
        ),
        serialization_alias="ORC.10",
        title="ENTERED BY",
        description="O | Item #00723 | LEN:80",
    )

    orc_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_11",
            "verified_by",
            "ORC.11",
        ),
        serialization_alias="ORC.11",
        title="VERIFIED BY",
        description="O | Item #00724 | LEN:80",
    )

    orc_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_12",
            "ordering_provider",
            "ORC.12",
        ),
        serialization_alias="ORC.12",
        title="ORDERING PROVIDER",
        description="O | Item #00725 | LEN:80",
    )

    orc_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_13",
            "enterer_s_location",
            "ORC.13",
        ),
        serialization_alias="ORC.13",
        title="ENTERER'S LOCATION",
        description="O | Item #00726 | LEN:80",
    )

    orc_14: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_14",
            "call_back_phone_number",
            "ORC.14",
        ),
        serialization_alias="ORC.14",
        title="CALL BACK PHONE NUMBER",
        description="O | Item #00727 | LEN:40",
    )

    model_config = {"populate_by_name": True}
