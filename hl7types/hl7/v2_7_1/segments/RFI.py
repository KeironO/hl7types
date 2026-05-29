"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: RFI
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class RFI(BaseModel):
    """HL7 v2 RFI segment.

    Attributes
    ----------
    rfi_1 : str
        RFI.1 (req) - Request Date (DTM)

    rfi_2 : str
        RFI.2 (req) - Response Due Date (DTM)

    rfi_3 : str | None
        RFI.3 (opt) - Patient Consent (ID)

    rfi_4 : str | None
        RFI.4 (opt) - Date Additional Information Was Submitted (DTM)
    """

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
