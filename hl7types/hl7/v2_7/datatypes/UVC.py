"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: UVC
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from .CWE import CWE
from .MO import MO


class UVC(HL7Model):
    """HL7 v2 UVC data type.

    Attributes
    ----------
    uvc_1 : CWE
        UVC.1 (req) - Value Code (CWE)

    uvc_2 : MO | None
        UVC.2 (opt) - Value Amount (MO)

    uvc_3 : str | None
        UVC.3 (opt) - Non-Monetary Value Amount / Quantity (NM)

    uvc_4 : CWE | None
        UVC.4 (opt) - Non-Monetary Value Amount / Units (CWE)
    """

    uvc_1: CWE = Field(
        validation_alias=AliasChoices(
            "uvc_1",
            "value_code",
            "UVC.1",
        ),
        serialization_alias="UVC.1",
        title="Value Code",
    )

    uvc_2: Optional[MO] = Field(
        default=None,
        validation_alias=AliasChoices(
            "uvc_2",
            "value_amount",
            "UVC.2",
        ),
        serialization_alias="UVC.2",
        title="Value Amount",
    )

    uvc_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "uvc_3",
            "non_monetary_value_amount_quantity",
            "UVC.3",
        ),
        serialization_alias="UVC.3",
        title="Non-Monetary Value Amount / Quantity",
    )

    uvc_4: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "uvc_4",
            "non_monetary_value_amount_units",
            "UVC.4",
        ),
        serialization_alias="UVC.4",
        title="Non-Monetary Value Amount / Units",
    )

    @field_validator("uvc_3", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
