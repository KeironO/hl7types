"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: PCE
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CP import CP
from ..datatypes.CWE import CWE
from ..datatypes.CX import CX

_RE_SI = re.compile(r'\d*')


class PCE(HL7Model):
    """Patient Charge Cost Center Exceptions (S17.4.6).

    Attributes
    ----------
    pce_1 : str
        PCE.1 - Set ID - PCE (SI) R S17.4.6.1

    pce_2 : CX | None
        PCE.2 - Cost Center Account Number (CX) O S17.4.6.2 | 0319 - Department Cost Center

    pce_3 : CWE | None
        PCE.3 - Transaction Code (CWE) O S17.4.2.12 | 0132 - Transaction Code

    pce_4 : CP | None
        PCE.4 - Transaction amount - unit (CP) O S17.4.2.13
    """

    pce_1: str = Field(
        validation_alias=AliasChoices(
            "pce_1",
            "set_id_pce",
            "PCE.1",
        ),
        serialization_alias="PCE.1",
        title="Set ID - PCE",
        description="R | Item #02228 | LEN:4",
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
        description="O | Item #00281 | Table 0319 - Department Cost Center",
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
        description="O | Item #00361 | Table 0132 - Transaction Code",
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
        description="O | Item #00366",
    )

    @field_validator("pce_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        if not _RE_SI.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    model_config = ConfigDict(populate_by_name=True)
