"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: NST
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.TS import TS


class NST(HL7Model):
    """Statistics.

    Attributes
    ----------
    nst_1 : str
        NST.1 - Statistics Available (ID) R SC-4 | 0136 - Y/N Indicator

    nst_2 : str | None
        NST.2 - Source Identifier (ST) NA

    nst_3 : str | None
        NST.3 - Source Type (ID) NA

    nst_4 : TS | None
        NST.4 - Statistics Start (TS) NA

    nst_5 : TS | None
        NST.5 - Statistics End (TS) NA

    nst_6 : str | None
        NST.6 - Receive Character Count (NM) NA

    nst_7 : str | None
        NST.7 - Send Character Count (NM) NA

    nst_8 : str | None
        NST.8 - Message Received (NM) NA

    nst_9 : str | None
        NST.9 - Message Sent (NM) NA

    nst_10 : str | None
        NST.10 - Checksum Errors Received (NM) NA

    nst_11 : str | None
        NST.11 - Length Errors Received (NM) NA

    nst_12 : str | None
        NST.12 - Other Errors Received (NM) NA

    nst_13 : str | None
        NST.13 - Connect Timeouts (NM) NA

    nst_14 : str | None
        NST.14 - Receive Timeouts (NM) NA

    nst_15 : str | None
        NST.15 - Network Errors (NM) NA
    """

    nst_1: str = Field(
        validation_alias=AliasChoices(
            "nst_1",
            "statistics_available",
            "NST.1",
        ),
        serialization_alias="NST.1",
        title="Statistics Available",
        description="R | Item #00743 | Table 0136 - Y/N Indicator | LEN:1",
    )

    nst_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nst_2",
            "source_identifier",
            "NST.2",
        ),
        serialization_alias="NST.2",
        title="Source Identifier",
        description="NA | Item #00744 | LEN:30",
    )

    nst_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nst_3",
            "source_type",
            "NST.3",
        ),
        serialization_alias="NST.3",
        title="Source Type",
        description="NA | Item #00745 | LEN:3",
    )

    nst_4: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nst_4",
            "statistics_start",
            "NST.4",
        ),
        serialization_alias="NST.4",
        title="Statistics Start",
        description="NA | Item #00746",
    )

    nst_5: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nst_5",
            "statistics_end",
            "NST.5",
        ),
        serialization_alias="NST.5",
        title="Statistics End",
        description="NA | Item #00747",
    )

    nst_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nst_6",
            "receive_character_count",
            "NST.6",
        ),
        serialization_alias="NST.6",
        title="Receive Character Count",
        description="NA | Item #00748 | LEN:10",
    )

    nst_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nst_7",
            "send_character_count",
            "NST.7",
        ),
        serialization_alias="NST.7",
        title="Send Character Count",
        description="NA | Item #00749 | LEN:10",
    )

    nst_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nst_8",
            "message_received",
            "NST.8",
        ),
        serialization_alias="NST.8",
        title="Message Received",
        description="NA | Item #00750 | LEN:10",
    )

    nst_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nst_9",
            "message_sent",
            "NST.9",
        ),
        serialization_alias="NST.9",
        title="Message Sent",
        description="NA | Item #00751 | LEN:10",
    )

    nst_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nst_10",
            "checksum_errors_received",
            "NST.10",
        ),
        serialization_alias="NST.10",
        title="Checksum Errors Received",
        description="NA | Item #00752 | LEN:10",
    )

    nst_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nst_11",
            "length_errors_received",
            "NST.11",
        ),
        serialization_alias="NST.11",
        title="Length Errors Received",
        description="NA | Item #00753 | LEN:10",
    )

    nst_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nst_12",
            "other_errors_received",
            "NST.12",
        ),
        serialization_alias="NST.12",
        title="Other Errors Received",
        description="NA | Item #00754 | LEN:10",
    )

    nst_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nst_13",
            "connect_timeouts",
            "NST.13",
        ),
        serialization_alias="NST.13",
        title="Connect Timeouts",
        description="NA | Item #00755 | LEN:10",
    )

    nst_14: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nst_14",
            "receive_timeouts",
            "NST.14",
        ),
        serialization_alias="NST.14",
        title="Receive Timeouts",
        description="NA | Item #00756 | LEN:10",
    )

    nst_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nst_15",
            "network_errors",
            "NST.15",
        ),
        serialization_alias="NST.15",
        title="Network Errors",
        description="NA | Item #00757 | LEN:10",
    )

    @field_validator("nst_6", "nst_7", "nst_8", "nst_9", "nst_10", "nst_11", "nst_12", "nst_13", "nst_14", "nst_15", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
