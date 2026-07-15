"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: BLG
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model


class BLG(HL7Model):
    """BILLING.

    Attributes
    ----------
    blg_1 : str | None
        BLG.1 - WHEN TO CHARGE (CM) O S4-12 | 0100 - WHEN TO CHARGE

    blg_2 : str | None
        BLG.2 - CHARGE TYPE (ID) O | 0122 - CHARGE TYPE

    blg_3 : str | None
        BLG.3 - ACCOUNT ID (CM) O
    """

    blg_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "blg_1",
            "when_to_charge",
            "BLG.1",
        ),
        serialization_alias="BLG.1",
        title="WHEN TO CHARGE",
        description="O | Item #00066 | Table 0100 - WHEN TO CHARGE | LEN:15",
    )

    blg_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "blg_2",
            "charge_type",
            "BLG.2",
        ),
        serialization_alias="BLG.2",
        title="CHARGE TYPE",
        description="O | Item #00729 | Table 0122 - CHARGE TYPE | LEN:50",
    )

    blg_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "blg_3",
            "account_id",
            "BLG.3",
        ),
        serialization_alias="BLG.3",
        title="ACCOUNT ID",
        description="O | Item #00730 | LEN:100",
    )

    model_config = {"populate_by_name": True}
