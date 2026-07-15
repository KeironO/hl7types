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
        RQ1.1 - Anticipated Price (ST) O S4.7.2.1

    rq1_2 : CE | None
        RQ1.2 - Manufactured ID (CE) O S4.7.2.2

    rq1_3 : str | None
        RQ1.3 - Manufacturer's Catalog (ST) O S4.7.2.3

    rq1_4 : CE | None
        RQ1.4 - Vendor ID (CE) O S4.7.2.4

    rq1_5 : str | None
        RQ1.5 - Vendor Catalog (ST) O S4.7.2.5

    rq1_6 : str | None
        RQ1.6 - Taxable (ID) O S4.7.2.6 | 0136 - Yes/No Indicator

    rq1_7 : str | None
        RQ1.7 - Substitute Allowed (ID) O S4.7.2.7 | 0136 - Yes/No Indicator
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
        description="O | Item #00285 | LEN:10",
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
        description="O | Item #00286",
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
        description="O | Item #00287 | LEN:16",
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
        description="O | Item #00288",
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
        description="O | Item #00289 | LEN:16",
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
        description="O | Item #00290 | Table 0136 - Yes/No Indicator | LEN:1",
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
        description="O | Item #00291 | Table 0136 - Yes/No Indicator | LEN:1",
    )

    model_config = {"populate_by_name": True}
