"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: BLC
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.CQ import CQ


class BLC(HL7Model):
    """Blood Code (S6.5.13).

    Attributes
    ----------
    blc_1 : CE | None
        BLC.1 - Blood Product Code (CE) O S6.5.13.1 | 0426 - Blood Product Code

    blc_2 : CQ | None
        BLC.2 - Blood Amount (CQ) O S6.5.13.2
    """

    blc_1: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "blc_1",
            "blood_product_code",
            "BLC.1",
        ),
        serialization_alias="BLC.1",
        title="Blood Product Code",
        description="O | Item #01528 | Table 0426 - Blood Product Code",
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
        description="O | Item #01529",
    )

    model_config = {"populate_by_name": True}
