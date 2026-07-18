"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: NST
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class NST(HL7Model):
    """STATISTICS.

    Attributes
    ----------
    nst_1 : str
        NST.1 - STATISTICS AVAILABLE (ID) R

    nst_2 : str | None
        NST.2 - SOURCE IDENTIFIER (ST) O

    nst_3 : str | None
        NST.3 - SOURCE TYPE (ID) O

    nst_4 : str | None
        NST.4 - STATISTICS START (TS) O

    nst_5 : str | None
        NST.5 - STATISTICS END (TS) O

    nst_6 : str | None
        NST.6 - RECEIVE CHARACTER COUNT (NM) O

    nst_7 : str | None
        NST.7 - SEND CHARACTER COUNT (NM) O

    nst_8 : str | None
        NST.8 - MESSAGES RECEIVED (NM) O

    nst_9 : str | None
        NST.9 - MESSAGES SENT (NM) O

    nst_10 : str | None
        NST.10 - CHECKSUM ERRORS RECEIVED (NM) O

    nst_11 : str | None
        NST.11 - LENGTH ERRORS RECEIVED (NM) O

    nst_12 : str | None
        NST.12 - OTHER ERRORS RECEIVED (NM) O

    nst_13 : str | None
        NST.13 - CONNECT TIMEOUTS (NM) O

    nst_14 : str | None
        NST.14 - RECEIVE TIMEOUTS (NM) O

    nst_15 : str | None
        NST.15 - NETWORK ERRORS (NM) O
    """

    nst_1: str = Field(
        validation_alias=AliasChoices(
            "nst_1",
            "statistics_available",
            "NST.1",
        ),
        serialization_alias="NST.1",
        title="STATISTICS AVAILABLE",
        description="R | Item #00743 | LEN:1",
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
        description="O | Item #00744 | LEN:30",
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
        description="O | Item #00745 | LEN:3",
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
        description="O | Item #00746 | LEN:19",
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
        description="O | Item #00747 | LEN:19",
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
        description="O | Item #00748 | LEN:10",
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
        description="O | Item #00749 | LEN:10",
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
        description="O | Item #00750 | LEN:10",
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
        description="O | Item #00751 | LEN:10",
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
        description="O | Item #00752 | LEN:10",
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
        description="O | Item #00753 | LEN:10",
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
        description="O | Item #00754 | LEN:10",
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
        description="O | Item #00755 | LEN:10",
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
        description="O | Item #00756 | LEN:10",
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
        description="O | Item #00757 | LEN:10",
    )

    @field_validator("nst_6", "nst_7", "nst_8", "nst_9", "nst_10", "nst_11", "nst_12", "nst_13", "nst_14", "nst_15", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
