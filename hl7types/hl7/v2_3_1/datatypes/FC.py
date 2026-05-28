"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: FC
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from .TS import TS


class FC(BaseModel):
    """HL7 v2 FC data type."""

    fc_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "fc_1",
            "financial_class",
            "FC.1",
        ),
        serialization_alias="FC.1",
        title="Financial Class",
    )

    fc_2: TS | None = Field(
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
