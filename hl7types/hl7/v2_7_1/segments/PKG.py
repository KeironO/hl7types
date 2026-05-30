"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: PKG
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CNE import CNE
from ..datatypes.CP import CP
from ..datatypes.CWE import CWE


class PKG(HL7Model):
    """HL7 v2 PKG segment.

    Attributes
    ----------
    pkg_1 : str
        PKG.1 (req) - Set Id - PKG (SI)

    pkg_2 : CWE | None
        PKG.2 (opt) - Packaging Units (CWE)

    pkg_3 : CNE | None
        PKG.3 (opt) - Default Order Unit Of Measure Indicator (CNE)

    pkg_4 : str | None
        PKG.4 (opt) - Package Quantity (NM)

    pkg_5 : CP | None
        PKG.5 (opt) - Price (CP)

    pkg_6 : CP | None
        PKG.6 (opt) - Future Item Price (CP)

    pkg_7 : str | None
        PKG.7 (opt) - Future Item Price Effective Date (DTM)
    """

    pkg_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "pkg_1",
            "set_id_pkg",
            "PKG.1",
        ),
        serialization_alias="PKG.1",
        title="Set Id - PKG",
        description="Item #2221",
    )

    pkg_2: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pkg_2",
            "packaging_units",
            "PKG.2",
        ),
        serialization_alias="PKG.2",
        title="Packaging Units",
        description="Item #2222 | Table HL70818",
    )

    pkg_3: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pkg_3",
            "default_order_unit_of_measure_indicator",
            "PKG.3",
        ),
        serialization_alias="PKG.3",
        title="Default Order Unit Of Measure Indicator",
        description="Item #2223 | Table HL70532",
    )

    pkg_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pkg_4",
            "package_quantity",
            "PKG.4",
        ),
        serialization_alias="PKG.4",
        title="Package Quantity",
        description="Item #2224",
    )

    pkg_5: Optional[CP] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pkg_5",
            "price",
            "PKG.5",
        ),
        serialization_alias="PKG.5",
        title="Price",
        description="Item #2225",
    )

    pkg_6: Optional[CP] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pkg_6",
            "future_item_price",
            "PKG.6",
        ),
        serialization_alias="PKG.6",
        title="Future Item Price",
        description="Item #2226",
    )

    pkg_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pkg_7",
            "future_item_price_effective_date",
            "PKG.7",
        ),
        serialization_alias="PKG.7",
        title="Future Item Price Effective Date",
        description="Item #2227",
    )

    model_config = {"populate_by_name": True}
