"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: ORC
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field


class ORC(BaseModel):
    """HL7 v2 ORC segment.

    Attributes
    ----------
    orc_1 : str
        ORC.1 (req) - ORDER CONTROL (ST)

    orc_2 : str | None
        ORC.2 (opt) - PLACER ORDER # (CM)

    orc_3 : str | None
        ORC.3 (opt) - FILLER ORDER # (CM)

    orc_4 : str | None
        ORC.4 (opt) - PLACER GROUP # (CM)

    orc_5 : str | None
        ORC.5 (opt) - ORDER STATUS (ST)

    orc_6 : str | None
        ORC.6 (opt) - RESPONSE FLAG (ST)

    orc_7 : str | None
        ORC.7 (opt) - TIMING/QUANTITY (CM)

    orc_8 : str | None
        ORC.8 (opt) - PARENT (CM)

    orc_9 : str | None
        ORC.9 (opt) - DATE/TIME OF TRANSACTION (TS)

    orc_10 : str | None
        ORC.10 (opt) - ENTERED BY (CN)

    orc_11 : str | None
        ORC.11 (opt) - VERIFIED BY (CN)

    orc_12 : str | None
        ORC.12 (opt) - ORDERING PROVIDER (CN)

    orc_13 : str | None
        ORC.13 (opt) - ENTERER'S LOCATION (CM)

    orc_14 : list[str] | None
        ORC.14 (opt, rep) - CALL BACK PHONE NUMBER (TN)
    """

    orc_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "orc_1",
            "order_control",
            "ORC.1",
        ),
        serialization_alias="ORC.1",
        title="ORDER CONTROL",
        description="Item #714 | Table HL70119",
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
        description="Item #715",
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
        description="Item #716",
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
        description="Item #717",
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
        description="Item #718 | Table HL70038",
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
        description="Item #719 | Table HL70121",
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
        description="Item #720",
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
        description="Item #721",
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
        description="Item #722",
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
        description="Item #723",
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
        description="Item #724",
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
        description="Item #725",
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
        description="Item #726",
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
        description="Item #727",
    )

    model_config = {"populate_by_name": True}
