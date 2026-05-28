"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: CM_FINANCE
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from .TS import TS


class CM_FINANCE(BaseModel):
    """HL7 v2 CM_FINANCE data type."""

    cm_finance_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_finance_1",
            "financial_class_id",
            "CM_FINANCE.1",
        ),
        serialization_alias="CM_FINANCE.1",
        title="financial class ID",
    )

    cm_finance_2: TS | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_finance_2",
            "effective_date",
            "CM_FINANCE.2",
        ),
        serialization_alias="CM_FINANCE.2",
        title="effective date",
    )

    model_config = {"populate_by_name": True}
