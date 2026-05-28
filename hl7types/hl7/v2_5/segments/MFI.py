"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: MFI
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE
from ..datatypes.HD import HD
from ..datatypes.TS import TS


class MFI(BaseModel):
    """HL7 v2 MFI segment."""

    mfi_1: CE = Field(
        default=...,
        validation_alias=AliasChoices(
            "mfi_1",
            "master_file_identifier",
            "MFI.1",
        ),
        serialization_alias="MFI.1",
        title="Master File Identifier",
        description="Item #658 | Table HL70175",
    )

    mfi_2: HD | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "mfi_2",
            "master_file_application_identifier",
            "MFI.2",
        ),
        serialization_alias="MFI.2",
        title="Master File Application Identifier",
        description="Item #659 | Table HL70361",
    )

    mfi_3: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "mfi_3",
            "file_level_event_code",
            "MFI.3",
        ),
        serialization_alias="MFI.3",
        title="File-Level Event Code",
        description="Item #660 | Table HL70178",
    )

    mfi_4: TS | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "mfi_4",
            "entered_date_time",
            "MFI.4",
        ),
        serialization_alias="MFI.4",
        title="Entered Date/Time",
        description="Item #661",
    )

    mfi_5: TS | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "mfi_5",
            "effective_date_time",
            "MFI.5",
        ),
        serialization_alias="MFI.5",
        title="Effective Date/Time",
        description="Item #662",
    )

    mfi_6: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "mfi_6",
            "response_level_code",
            "MFI.6",
        ),
        serialization_alias="MFI.6",
        title="Response Level Code",
        description="Item #663 | Table HL70179",
    )

    model_config = {"populate_by_name": True}
