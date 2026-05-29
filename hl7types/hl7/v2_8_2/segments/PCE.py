"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: PCE
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CP import CP
from ..datatypes.CWE import CWE
from ..datatypes.CX import CX


class PCE(BaseModel):
    """HL7 v2 PCE segment.

    Attributes
    ----------
    pce_1 : str
        PCE.1 (req) - Set ID - PCE (SI)

    pce_2 : CX | None
        PCE.2 (opt) - Cost Center Account Number (CX)

    pce_3 : CWE | None
        PCE.3 (opt) - Transaction Code (CWE)

    pce_4 : CP | None
        PCE.4 (opt) - Transaction amount - unit (CP)
    """

    pce_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "pce_1",
            "set_id_pce",
            "PCE.1",
        ),
        serialization_alias="PCE.1",
        title="Set ID - PCE",
        description="Item #2228",
    )

    pce_2: Optional[CX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pce_2",
            "cost_center_account_number",
            "PCE.2",
        ),
        serialization_alias="PCE.2",
        title="Cost Center Account Number",
        description="Item #281 | Table HL70319",
    )

    pce_3: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pce_3",
            "transaction_code",
            "PCE.3",
        ),
        serialization_alias="PCE.3",
        title="Transaction Code",
        description="Item #361 | Table HL70132",
    )

    pce_4: Optional[CP] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pce_4",
            "transaction_amount_unit",
            "PCE.4",
        ),
        serialization_alias="PCE.4",
        title="Transaction amount - unit",
        description="Item #366",
    )

    model_config = {"populate_by_name": True}
