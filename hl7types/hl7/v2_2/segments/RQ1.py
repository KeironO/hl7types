"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: RQ1
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator

from ..datatypes.CE import CE


class RQ1(HL7Model):
    """HL7 v2 RQ1 segment.

    Attributes
    ----------
    rq1_1 : str | None
        RQ1.1 (opt) - Anticipated Price (SI)

    rq1_2 : CE | None
        RQ1.2 (opt) - Manufacturer ID (CE)

    rq1_3 : str | None
        RQ1.3 (opt) - Manufacturer's Catalog (ST)

    rq1_4 : CE | None
        RQ1.4 (opt) - Vendor ID (CE)

    rq1_5 : str | None
        RQ1.5 (opt) - Vendor Catalog (ST)

    rq1_6 : str | None
        RQ1.6 (opt) - Taxable (ID)

    rq1_7 : str | None
        RQ1.7 (opt) - Substitute Allowed (ID)
    """

    rq1_1: Optional[str] = Field(
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

    rq1_2: Optional[CE] = Field(
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

    rq1_3: Optional[str] = Field(
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

    rq1_4: Optional[CE] = Field(
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

    rq1_5: Optional[str] = Field(
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

    rq1_6: Optional[str] = Field(
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

    rq1_7: Optional[str] = Field(
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

    @field_validator("rq1_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    model_config = {"populate_by_name": True}
