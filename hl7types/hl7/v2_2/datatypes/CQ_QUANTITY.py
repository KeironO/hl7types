"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: CQ_QUANTITY
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model


class CQ_QUANTITY(HL7Model):
    """HL7 v2 CQ_QUANTITY data type.

    Attributes
    ----------
    cq_quantity_1 : str | None
        CQ_QUANTITY.1 (opt) - quantity (ST)

    cq_quantity_2 : str | None
        CQ_QUANTITY.2 (opt) - units (ST)
    """

    cq_quantity_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cq_quantity_1",
            "quantity",
            "CQ_QUANTITY.1",
        ),
        serialization_alias="CQ_QUANTITY.1",
        title="quantity",
    )

    cq_quantity_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cq_quantity_2",
            "units",
            "CQ_QUANTITY.2",
        ),
        serialization_alias="CQ_QUANTITY.2",
        title="units",
    )

    model_config = {"populate_by_name": True}
