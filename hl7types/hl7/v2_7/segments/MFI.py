"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: MFI
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CWE import CWE
from ..datatypes.HD import HD


class MFI(BaseModel):
    """HL7 v2 MFI segment.

    Attributes
    ----------
    mfi_1 : CWE
        MFI.1 (req) - Master File Identifier (CWE)

    mfi_2 : list[HD] | None
        MFI.2 (opt, rep) - Master File Application Identifier (HD)

    mfi_3 : str
        MFI.3 (req) - File-Level Event Code (ID)

    mfi_4 : str | None
        MFI.4 (opt) - Entered Date/Time (DTM)

    mfi_5 : str | None
        MFI.5 (opt) - Effective Date/Time (DTM)

    mfi_6 : str
        MFI.6 (req) - Response Level Code (ID)
    """

    mfi_1: CWE = Field(
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

    mfi_2: Optional[List[HD]] = Field(
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

    mfi_4: Optional[str] = Field(
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

    mfi_5: Optional[str] = Field(
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
