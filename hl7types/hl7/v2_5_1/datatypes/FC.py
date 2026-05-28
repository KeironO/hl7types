"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: FC
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from .TS import TS


class FC(BaseModel):
    """HL7 v2 FC data type."""

    fc_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "fc_1",
            "financial_class_code",
            "FC.1",
        ),
        serialization_alias="FC.1",
        title="Financial Class Code",
    )

    fc_2: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "fc_2",
            "effective_date",
            "FC.2",
        ),
        serialization_alias="FC.2",
        title="Effective Date",
    )

    model_config = {"populate_by_name": True}
