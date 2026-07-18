"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: BLG
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CK import CK


class BLG(HL7Model):
    """Billing Segment (S4.3.2).

    Attributes
    ----------
    blg_1 : str | None
        BLG.1 - When to Charge (CM) O S4.3.2.1 | 0100 - When to Charge

    blg_2 : str | None
        BLG.2 - Charge Type (ID) O S4.3.2.2 | 0122 - Charge Type

    blg_3 : CK | None
        BLG.3 - Account ID (CK) O S4.3.2.3
    """

    blg_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "blg_1",
            "when_to_charge",
            "BLG.1",
        ),
        serialization_alias="BLG.1",
        title="When to Charge",
        description="O | Item #00234 | Table 0100 - When to Charge",
    )

    blg_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "blg_2",
            "charge_type",
            "BLG.2",
        ),
        serialization_alias="BLG.2",
        title="Charge Type",
        description="O | Item #00235 | Table 0122 - Charge Type | LEN:50",
    )

    blg_3: Optional[CK] = Field(
        default=None,
        validation_alias=AliasChoices(
            "blg_3",
            "account_id",
            "BLG.3",
        ),
        serialization_alias="BLG.3",
        title="Account ID",
        description="O | Item #00236",
    )

    model_config = ConfigDict(populate_by_name=True)
