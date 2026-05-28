"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: UVC
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from .CNE import CNE
from .MO import MO


class UVC(BaseModel):
    """HL7 v2 UVC data type."""

    uvc_1: Optional[CNE] = Field(
        default=None,
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

    model_config = {"populate_by_name": True}
