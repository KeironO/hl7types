"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: BLG
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CCD import CCD
from ..datatypes.CWE import CWE
from ..datatypes.CX import CX


class BLG(HL7Model):
    """Billing (S4.5.2).

    Attributes
    ----------
    blg_1 : CCD | None
        BLG.1 - When to Charge (CCD) O S4.5.2.1 | 0100 - Invocation event

    blg_2 : str | None
        BLG.2 - Charge Type (ID) O S4.5.2.2 | 0122 - Charge Type

    blg_3 : CX | None
        BLG.3 - Account ID (CX) O S4.5.2.3

    blg_4 : CWE | None
        BLG.4 - Charge Type Reason (CWE) O S4.5.2.4 | 0475 - Charge Type Reason
    """

    blg_1: Optional[CCD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "blg_1",
            "when_to_charge",
            "BLG.1",
        ),
        serialization_alias="BLG.1",
        title="When to Charge",
        description="O | Item #00234 | Table 0100 - Invocation event",
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
        description="O | Item #00235 | Table 0122 - Charge Type | LEN:2",
    )

    blg_3: Optional[CX] = Field(
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

    blg_4: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "blg_4",
            "charge_type_reason",
            "BLG.4",
        ),
        serialization_alias="BLG.4",
        title="Charge Type Reason",
        description="O | Item #01645 | Table 0475 - Charge Type Reason",
    )

    model_config = {"populate_by_name": True}
