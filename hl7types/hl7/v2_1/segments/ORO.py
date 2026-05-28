"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: ORO
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE


class ORO(BaseModel):
    """HL7 v2 ORO segment."""

    oro_1: CE | None = Field(
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

    oro_2: str | None = Field(
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

    oro_3: list[str] | None = Field(
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

    oro_4: str | None = Field(
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
