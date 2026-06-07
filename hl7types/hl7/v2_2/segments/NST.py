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
    """HL7 v2 NST segment.

    Attributes
    ----------
    nst_1 : str
        NST.1 (req) - Statistics Available (ID)

    nst_2 : str | None
        NST.2 (opt) - Source Identifier (ST)

    nst_3 : str | None
        NST.3 (opt) - Source Type (ID)

    nst_4 : TS | None
        NST.4 (opt) - Statistics Start (TS)

    nst_5 : TS | None
        NST.5 (opt) - Statistics End (TS)

    nst_6 : str | None
        NST.6 (opt) - Receive Character Count (NM)

    nst_7 : str | None
        NST.7 (opt) - Send Character Count (NM)

    nst_8 : str | None
        NST.8 (opt) - Message Received (NM)

    nst_9 : str | None
        NST.9 (opt) - Message Sent (NM)

    nst_10 : str | None
        NST.10 (opt) - Checksum Errors Received (NM)

    nst_11 : str | None
        NST.11 (opt) - Length Errors Received (NM)

    nst_12 : str | None
        NST.12 (opt) - Other Errors Received (NM)

    nst_13 : str | None
        NST.13 (opt) - Connect Timeouts (NM)

    nst_14 : str | None
        NST.14 (opt) - Receive Timeouts (NM)

    nst_15 : str | None
        NST.15 (opt) - Network Errors (NM)
    """

    nst_1: str = Field(
        validation_alias=AliasChoices(
            "nst_1",
            "statistics_available",
            "NST.1",
        ),
        serialization_alias="NST.1",
        title="Statistics Available",
        description="Item #743 | Table HL70136",
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
        description="Item #744",
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
        description="Item #745",
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
        description="Item #746",
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
        description="Item #747",
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
        description="Item #748",
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
        description="Item #749",
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
        description="Item #750",
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
        description="Item #751",
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
        description="Item #752",
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
        description="Item #753",
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
        description="Item #754",
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
        description="Item #755",
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
        description="Item #756",
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
        description="Item #757",
    )

    @field_validator("nst_6", "nst_7", "nst_8", "nst_9", "nst_10", "nst_11", "nst_12", "nst_13", "nst_14", "nst_15", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
