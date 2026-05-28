"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: RFI
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class RFI(BaseModel):
    """HL7 v2 RFI segment."""

    rfi_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "rfi_1",
            "request_date",
            "RFI.1",
        ),
        serialization_alias="RFI.1",
        title="Request Date",
        description="Item #1910",
    )

    rfi_2: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "rfi_2",
            "response_due_date",
            "RFI.2",
        ),
        serialization_alias="RFI.2",
        title="Response Due Date",
        description="Item #1911",
    )

    rfi_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rfi_3",
            "patient_consent",
            "RFI.3",
        ),
        serialization_alias="RFI.3",
        title="Patient Consent",
        description="Item #1912 | Table HL70136",
    )

    rfi_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rfi_4",
            "date_additional_information_was_submitted",
            "RFI.4",
        ),
        serialization_alias="RFI.4",
        title="Date Additional Information Was Submitted",
        description="Item #1913",
    )

    model_config = {"populate_by_name": True}
