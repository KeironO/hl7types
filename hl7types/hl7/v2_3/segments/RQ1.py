"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: RQ1
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE


class RQ1(HL7Model):
    """Requisition detail-1 segment (S4.7.2).

    Attributes
    ----------
    rq1_1 : str | None
        RQ1.1 (opt) - Anticipated Price (ST) S4.7.2.1

    rq1_2 : CE | None
        RQ1.2 (opt) - Manufactured ID (CE) S4.7.2.2

    rq1_3 : str | None
        RQ1.3 (opt) - Manufacturer's Catalog (ST) S4.7.2.3

    rq1_4 : CE | None
        RQ1.4 (opt) - Vendor ID (CE) S4.7.2.4

    rq1_5 : str | None
        RQ1.5 (opt) - Vendor Catalog (ST) S4.7.2.5

    rq1_6 : str | None
        RQ1.6 (opt) - Taxable (ID) S4.7.2.6 | 0136 - Yes/No Indicator

    rq1_7 : str | None
        RQ1.7 (opt) - Substitute Allowed (ID) S4.7.2.7 | 0136 - Yes/No Indicator
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
            "manufactured_id",
            "RQ1.2",
        ),
        serialization_alias="RQ1.2",
        title="Manufactured ID",
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

    model_config = {"populate_by_name": True}
