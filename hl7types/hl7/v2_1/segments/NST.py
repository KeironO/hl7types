"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: NST
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model


class NST(HL7Model):
    """HL7 v2 NST segment.

    Attributes
    ----------
    nst_1 : str
        NST.1 (req) - STATISTICS AVAILABLE (ID)

    nst_2 : str | None
        NST.2 (opt) - SOURCE IDENTIFIER (ST)

    nst_3 : str | None
        NST.3 (opt) - SOURCE TYPE (ID)

    nst_4 : str | None
        NST.4 (opt) - STATISTICS START (TS)

    nst_5 : str | None
        NST.5 (opt) - STATISTICS END (TS)

    nst_6 : str | None
        NST.6 (opt) - RECEIVE CHARACTER COUNT (NM)

    nst_7 : str | None
        NST.7 (opt) - SEND CHARACTER COUNT (NM)

    nst_8 : str | None
        NST.8 (opt) - MESSAGES RECEIVED (NM)

    nst_9 : str | None
        NST.9 (opt) - MESSAGES SENT (NM)

    nst_10 : str | None
        NST.10 (opt) - CHECKSUM ERRORS RECEIVED (NM)

    nst_11 : str | None
        NST.11 (opt) - LENGTH ERRORS RECEIVED (NM)

    nst_12 : str | None
        NST.12 (opt) - OTHER ERRORS RECEIVED (NM)

    nst_13 : str | None
        NST.13 (opt) - CONNECT TIMEOUTS (NM)

    nst_14 : str | None
        NST.14 (opt) - RECEIVE TIMEOUTS (NM)

    nst_15 : str | None
        NST.15 (opt) - NETWORK ERRORS (NM)
    """

    nst_1: str = Field(
        validation_alias=AliasChoices(
            "nst_1",
            "statistics_available",
            "NST.1",
        ),
        serialization_alias="NST.1",
        title="STATISTICS AVAILABLE",
        description="Item #743",
    )

    nst_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nst_2",
            "source_identifier",
            "NST.2",
        ),
        serialization_alias="NST.2",
        title="SOURCE IDENTIFIER",
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
        title="SOURCE TYPE",
        description="Item #745",
    )

    nst_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nst_4",
            "statistics_start",
            "NST.4",
        ),
        serialization_alias="NST.4",
        title="STATISTICS START",
        description="Item #746",
    )

    nst_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nst_5",
            "statistics_end",
            "NST.5",
        ),
        serialization_alias="NST.5",
        title="STATISTICS END",
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
        title="RECEIVE CHARACTER COUNT",
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
        title="SEND CHARACTER COUNT",
        description="Item #749",
    )

    nst_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nst_8",
            "messages_received",
            "NST.8",
        ),
        serialization_alias="NST.8",
        title="MESSAGES RECEIVED",
        description="Item #750",
    )

    nst_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nst_9",
            "messages_sent",
            "NST.9",
        ),
        serialization_alias="NST.9",
        title="MESSAGES SENT",
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
        title="CHECKSUM ERRORS RECEIVED",
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
        title="LENGTH ERRORS RECEIVED",
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
        title="OTHER ERRORS RECEIVED",
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
        title="CONNECT TIMEOUTS",
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
        title="RECEIVE TIMEOUTS",
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
        title="NETWORK ERRORS",
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
