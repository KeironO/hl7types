"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: CM_FINANCE
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from .TS import TS


class CM_FINANCE(BaseModel):
    """HL7 v2 CM_FINANCE data type.

    Attributes
    ----------
    cm_finance_1 : str | None
        CM_FINANCE.1 (opt) - financial class ID (ID)

    cm_finance_2 : TS | None
        CM_FINANCE.2 (opt) - effective date (TS)
    """

    cm_finance_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_finance_1",
            "financial_class_id",
            "CM_FINANCE.1",
        ),
        serialization_alias="CM_FINANCE.1",
        title="financial class ID",
    )

    cm_finance_2: Optional[TS] = Field(
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
