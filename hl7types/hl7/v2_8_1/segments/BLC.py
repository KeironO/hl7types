"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: BLC
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CQ import CQ
from ..datatypes.CWE import CWE


class BLC(BaseModel):
    """HL7 v2 BLC segment.

    Attributes
    ----------
    blc_1 : CWE | None
        BLC.1 (opt) - Blood Product Code (CWE)

    blc_2 : CQ | None
        BLC.2 (opt) - Blood Amount (CQ)
    """

    blc_1: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "blc_1",
            "blood_product_code",
            "BLC.1",
        ),
        serialization_alias="BLC.1",
        title="Blood Product Code",
        description="Item #1528 | Table HL70426",
    )

    blc_2: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "blc_2",
            "blood_amount",
            "BLC.2",
        ),
        serialization_alias="BLC.2",
        title="Blood Amount",
        description="Item #1529",
    )

    model_config = {"populate_by_name": True}
