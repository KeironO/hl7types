"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: MFI
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.HD import HD
from ..datatypes.TS import TS


class MFI(HL7Model):
    """Master file identification segment (S8.4.1).

    Attributes
    ----------
    mfi_1 : CE
        MFI.1 - Master File Identifier (CE) R S8.4.1.1 | 0175 - Master File Identifier Code

    mfi_2 : HD | None
        MFI.2 - Master File Application Identifier (HD) O S8.4.1.2 | 0176 - Master File Application Identifier

    mfi_3 : str
        MFI.3 - File-Level Event Code (ID) R S8.4.1.3 | 0178 - File Level Event Code

    mfi_4 : TS | None
        MFI.4 - Entered Date/Time (TS) NA S8.4.1.4

    mfi_5 : TS | None
        MFI.5 - Effective Date/Time (TS) NA S8.4.1

    mfi_6 : str
        MFI.6 - Response Level Code (ID) R S8.4.1.6 | 0179 - Response Level
    """

    mfi_1: CE = Field(
        validation_alias=AliasChoices(
            "mfi_1",
            "master_file_identifier",
            "MFI.1",
        ),
        serialization_alias="MFI.1",
        title="Master File Identifier",
        description=(
            "R | Item #00658 | Table 0175 - Master File Identifier Code"
        ),
    )

    mfi_2: Optional[HD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "mfi_2",
            "master_file_application_identifier",
            "MFI.2",
        ),
        serialization_alias="MFI.2",
        title="Master File Application Identifier",
        description=(
            "O | Item #00659 | Table 0176 - Master File Application Identifier"
        ),
    )

    mfi_3: str = Field(
        validation_alias=AliasChoices(
            "mfi_3",
            "file_level_event_code",
            "MFI.3",
        ),
        serialization_alias="MFI.3",
        title="File-Level Event Code",
        description=(
            "R | Item #00660 | Table 0178 - File Level Event Code | LEN:3"
        ),
    )

    mfi_4: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "mfi_4",
            "entered_date_time",
            "MFI.4",
        ),
        serialization_alias="MFI.4",
        title="Entered Date/Time",
        description="NA | Item #00661",
    )

    mfi_5: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "mfi_5",
            "effective_date_time",
            "MFI.5",
        ),
        serialization_alias="MFI.5",
        title="Effective Date/Time",
        description="NA | Item #00662",
    )

    mfi_6: str = Field(
        validation_alias=AliasChoices(
            "mfi_6",
            "response_level_code",
            "MFI.6",
        ),
        serialization_alias="MFI.6",
        title="Response Level Code",
        description="R | Item #00663 | Table 0179 - Response Level | LEN:2",
    )

    model_config = {"populate_by_name": True}
