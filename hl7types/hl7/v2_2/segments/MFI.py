"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: MFI
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.TS import TS


class MFI(HL7Model):
    """MASTER FILE IDENTIFICATION (S8.4.1).

    Attributes
    ----------
    mfi_1 : CE
        MFI.1 - Master file identifier (CE) R S8.4.1.1 | 0175 - MASTER FILE IDENTIFIER CODE

    mfi_2 : str | None
        MFI.2 - Master file application identifier (ID) NA S8.4.1.2 | 0176 - MASTER FILE APPLICATION IDENTIFIER

    mfi_3 : str
        MFI.3 - File-level event code (ID) R S8.4.1.3 | 0178 - FILE-LEVEL EVENT CODE

    mfi_4 : TS | None
        MFI.4 - Entered date / time (TS) NA S8.4.1.4

    mfi_5 : TS | None
        MFI.5 - Effective date / time (TS) NA S8.4.2.3

    mfi_6 : str
        MFI.6 - Response level code (ID) R S8.4.1.6 | 0179 - Response Level
    """

    mfi_1: CE = Field(
        validation_alias=AliasChoices(
            "mfi_1",
            "master_file_identifier",
            "MFI.1",
        ),
        serialization_alias="MFI.1",
        title="Master file identifier",
        description=(
            "R | Item #00658 | Table 0175 - MASTER FILE IDENTIFIER CODE"
        ),
    )

    mfi_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "mfi_2",
            "master_file_application_identifier",
            "MFI.2",
        ),
        serialization_alias="MFI.2",
        title="Master file application identifier",
        description=(
            "NA | Item #00659 | Table 0176 - MASTER FILE APPLICATION IDENTIFIER | "
            "LEN:6"
        ),
    )

    mfi_3: str = Field(
        validation_alias=AliasChoices(
            "mfi_3",
            "file_level_event_code",
            "MFI.3",
        ),
        serialization_alias="MFI.3",
        title="File-level event code",
        description=(
            "R | Item #00660 | Table 0178 - FILE-LEVEL EVENT CODE | LEN:3"
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
        title="Entered date / time",
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
        title="Effective date / time",
        description="NA | Item #00662",
    )

    mfi_6: str = Field(
        validation_alias=AliasChoices(
            "mfi_6",
            "response_level_code",
            "MFI.6",
        ),
        serialization_alias="MFI.6",
        title="Response level code",
        description="R | Item #00663 | Table 0179 - Response Level | LEN:2",
    )

    model_config = {"populate_by_name": True}
