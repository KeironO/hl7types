"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
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
        BLG.1 (opt) - When to Charge (CCD) S4.5.2.1 | 0100 - Invocation event

    blg_2 : str | None
        BLG.2 (opt) - Charge Type (ID) S4.5.2.2 | 0122 - Charge type

    blg_3 : CX | None
        BLG.3 (opt) - Account ID (CX) S4.5.2.3

    blg_4 : CWE | None
        BLG.4 (opt) - Charge Type Reason (CWE) S4.5.2.4 | 0475 - Charge Type Reason
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
        description="Item #234 | Table HL70100",
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
        description="Item #235 | Table HL70122",
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
        description="Item #236",
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
        description="Item #1645 | Table HL70475",
    )

    model_config = {"populate_by_name": True}
