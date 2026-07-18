"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: RQ1
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE


class RQ1(HL7Model):
    """Requisition Detail-1 (S4.11.2).

    Attributes
    ----------
    rq1_1 : str | None
        RQ1.1 - Anticipated Price (ST) O S4.11.2.1

    rq1_2 : CWE | None
        RQ1.2 - Manufacturer Identifier (CWE) C S13.4.4.17 | 0385 - Manufacturer Identifier

    rq1_3 : str | None
        RQ1.3 - Manufacturer's Catalog (ST) C S4.11.2.3

    rq1_4 : CWE | None
        RQ1.4 - Vendor ID (CWE) C S4.11.2.4 | 9999 - no table for CE

    rq1_5 : str | None
        RQ1.5 - Vendor Catalog (ST) C S4.11.2.5

    rq1_6 : str | None
        RQ1.6 - Taxable (ID) O S4.11.2.6 | 0136 - Yes/no Indicator

    rq1_7 : str | None
        RQ1.7 - Substitute Allowed (ID) O S4.11.2.7 | 0136 - Yes/no Indicator
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
        description="O | Item #00285",
    )

    rq1_2: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rq1_2",
            "manufacturer_identifier",
            "RQ1.2",
        ),
        serialization_alias="RQ1.2",
        title="Manufacturer Identifier",
        description="C | Item #00286 | Table 0385 - Manufacturer Identifier",
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
        description="C | Item #00287",
    )

    rq1_4: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rq1_4",
            "vendor_id",
            "RQ1.4",
        ),
        serialization_alias="RQ1.4",
        title="Vendor ID",
        description="C | Item #00288 | Table 9999 - no table for CE",
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
        description="C | Item #00289",
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
        description="O | Item #00290 | Table 0136 - Yes/no Indicator | LEN:1",
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
        description="O | Item #00291 | Table 0136 - Yes/no Indicator | LEN:1",
    )

    model_config = ConfigDict(populate_by_name=True)
