"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: ORO
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE


class ORO(HL7Model):
    """HL7 v2 ORO segment.

    Attributes
    ----------
    oro_1 : CE | None
        ORO.1 (opt) - ORDER ITEM ID (CE)

    oro_2 : str | None
        ORO.2 (opt) - SUBSTITUTE ALLOWED (ID)

    oro_3 : list[str] | None
        ORO.3 (opt, rep) - RESULTS COPIES TO (CN)

    oro_4 : str | None
        ORO.4 (opt) - STOCK LOCATION (ID)
    """

    oro_1: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "oro_1",
            "order_item_id",
            "ORO.1",
        ),
        serialization_alias="ORO.1",
        title="ORDER ITEM ID",
        description="Item #731",
    )

    oro_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "oro_2",
            "substitute_allowed",
            "ORO.2",
        ),
        serialization_alias="ORO.2",
        title="SUBSTITUTE ALLOWED",
        description="Item #120",
    )

    oro_3: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "oro_3",
            "results_copies_to",
            "ORO.3",
        ),
        serialization_alias="ORO.3",
        title="RESULTS COPIES TO",
        description="Item #586",
    )

    oro_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "oro_4",
            "stock_location",
            "ORO.4",
        ),
        serialization_alias="ORO.4",
        title="STOCK LOCATION",
        description="Item #68 | Table HL70012",
    )

    model_config = {"populate_by_name": True}
