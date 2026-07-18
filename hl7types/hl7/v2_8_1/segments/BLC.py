"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: BLC
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CQ import CQ
from ..datatypes.CWE import CWE


class BLC(HL7Model):
    """Blood Code (S6.5.13).

    Attributes
    ----------
    blc_1 : CWE | None
        BLC.1 - Blood Product Code (CWE) O S6.5.13.1 | 0426 - Blood Product Code

    blc_2 : CQ | None
        BLC.2 - Blood Amount (CQ) O S6.5.13.2
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

    model_config = ConfigDict(populate_by_name=True)
