"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: RQ1
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE


class RQ1(BaseModel):
    """HL7 v2 RQ1 segment."""

    rq1_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "rq1_1",
            "anticipated_price",
            "RQ1.1",
        ),
        serialization_alias="RQ1.1",
        title="Anticipated Price",
        description="Item #285",
    )

    rq1_2: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "rq1_2",
            "manufacturer_id",
            "RQ1.2",
        ),
        serialization_alias="RQ1.2",
        title="Manufacturer ID",
        description="Item #286",
    )

    rq1_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "rq1_3",
            "manufacturer_s_catalog",
            "RQ1.3",
        ),
        serialization_alias="RQ1.3",
        title="Manufacturer's Catalog",
        description="Item #287",
    )

    rq1_4: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "rq1_4",
            "vendor_id",
            "RQ1.4",
        ),
        serialization_alias="RQ1.4",
        title="Vendor ID",
        description="Item #288",
    )

    rq1_5: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "rq1_5",
            "vendor_catalog",
            "RQ1.5",
        ),
        serialization_alias="RQ1.5",
        title="Vendor Catalog",
        description="Item #289",
    )

    rq1_6: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "rq1_6",
            "taxable",
            "RQ1.6",
        ),
        serialization_alias="RQ1.6",
        title="Taxable",
        description="Item #290 | Table HL70136",
    )

    rq1_7: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "rq1_7",
            "substitute_allowed",
            "RQ1.7",
        ),
        serialization_alias="RQ1.7",
        title="Substitute Allowed",
        description="Item #291 | Table HL70136",
    )

    model_config = {"populate_by_name": True}
