"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: UVC
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from .CWE import CWE
from .MO import MO


class UVC(BaseModel):
    """HL7 v2 UVC data type."""

    uvc_1: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "uvc_1",
            "value_code",
            "UVC.1",
        ),
        serialization_alias="UVC.1",
        title="Value Code",
    )

    uvc_2: MO | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "uvc_2",
            "value_amount",
            "UVC.2",
        ),
        serialization_alias="UVC.2",
        title="Value Amount",
    )

    uvc_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "uvc_3",
            "non_monetary_value_amount_quantity",
            "UVC.3",
        ),
        serialization_alias="UVC.3",
        title="Non-Monetary Value Amount / Quantity",
    )

    uvc_4: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "uvc_4",
            "non_monetary_value_amount_units",
            "UVC.4",
        ),
        serialization_alias="UVC.4",
        title="Non-Monetary Value Amount / Units",
    )

    model_config = {"populate_by_name": True}
