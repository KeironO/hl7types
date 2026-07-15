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
    """ORDER OTHER.

    Attributes
    ----------
    oro_1 : CE | None
        ORO.1 - ORDER ITEM ID (CE) O S4-18

    oro_2 : str | None
        ORO.2 - SUBSTITUTE ALLOWED (ID) O

    oro_3 : list[str] | None
        ORO.3 - RESULTS COPIES TO (CN) O rep

    oro_4 : str | None
        ORO.4 - STOCK LOCATION (ID) O | 0012 - STOCK LOCATION
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
        description="O | Item #00731",
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
        description="O | Item #00120 | LEN:1",
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
        description="O | Item #00586 | LEN:80",
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
        description="O | Item #00068 | Table 0012 - STOCK LOCATION | LEN:2",
    )

    model_config = {"populate_by_name": True}
