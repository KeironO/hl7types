"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: FC
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model


class FC(HL7Model):
    """HL7 v2 FC data type.

    Attributes
    ----------
    fc_1 : str
        FC.1 (req) - Financial Class Code (IS)

    fc_2 : str | None
        FC.2 (opt) - Effective Date (DTM)
    """

    fc_1: str = Field(
        default=...,
        max_length=20,
        validation_alias=AliasChoices(
            "fc_1",
            "financial_class_code",
            "FC.1",
        ),
        serialization_alias="FC.1",
        title="Financial Class Code",
    )

    fc_2: Optional[str] = Field(
        default=None,
        max_length=24,
        validation_alias=AliasChoices(
            "fc_2",
            "effective_date",
            "FC.2",
        ),
        serialization_alias="FC.2",
        title="Effective Date",
    )

    model_config = {"populate_by_name": True}
