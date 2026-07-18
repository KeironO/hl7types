"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: NST
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.TS import TS

_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class NST(HL7Model):
    """Application control level statistics (S14.4.3).

    Attributes
    ----------
    nst_1 : str
        NST.1 - Statistics Available (ID) R S14.4.3.1 | 0136 - Yes/no indicator

    nst_2 : str | None
        NST.2 - Source Identifier (ST) O S14.4.3.2

    nst_3 : str | None
        NST.3 - Source Type (ID) O S14.4.3.3 | 0332 - Source type

    nst_4 : TS | None
        NST.4 - Statistics Start (TS) O S14.4.3.4

    nst_5 : TS | None
        NST.5 - Statistics End (TS) O S14.4.3.5

    nst_6 : str | None
        NST.6 - Receive Character Count (NM) O S14.4.3.6

    nst_7 : str | None
        NST.7 - Send Character Count (NM) O S14.4.3.7

    nst_8 : str | None
        NST.8 - Messages Received (NM) O S14.4.3.8

    nst_9 : str | None
        NST.9 - Messages Sent (NM) O S14.4.3.9

    nst_10 : str | None
        NST.10 - Checksum Errors Received (NM) O S14.4.3.10

    nst_11 : str | None
        NST.11 - Length Errors Received (NM) O S14.4.3.11

    nst_12 : str | None
        NST.12 - Other Errors Received (NM) O S14.4.3.12

    nst_13 : str | None
        NST.13 - Connect Timeouts (NM) O S14.4.3.13

    nst_14 : str | None
        NST.14 - Receive Timeouts (NM) O S14.4.3.14

    nst_15 : str | None
        NST.15 - Application control-level Errors (NM) O S14.4.3.15
    """

    nst_1: str = Field(
        validation_alias=AliasChoices(
            "nst_1",
            "statistics_available",
            "NST.1",
        ),
        serialization_alias="NST.1",
        title="Statistics Available",
        description="R | Item #01173 | Table 0136 - Yes/no indicator | LEN:1",
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
        description="O | Item #01174 | LEN:30",
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
        description="O | Item #01175 | Table 0332 - Source type | LEN:3",
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
        description="O | Item #01176",
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
        description="O | Item #01177",
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
        description="O | Item #01178 | LEN:10",
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
        description="O | Item #01179 | LEN:10",
    )

    nst_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nst_8",
            "messages_received",
            "NST.8",
        ),
        serialization_alias="NST.8",
        title="Messages Received",
        description="O | Item #01180 | LEN:10",
    )

    nst_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nst_9",
            "messages_sent",
            "NST.9",
        ),
        serialization_alias="NST.9",
        title="Messages Sent",
        description="O | Item #01181 | LEN:10",
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
        description="O | Item #01182 | LEN:10",
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
        description="O | Item #01183 | LEN:10",
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
        description="O | Item #01184 | LEN:10",
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
        description="O | Item #01185 | LEN:10",
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
        description="O | Item #01186 | LEN:10",
    )

    nst_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nst_15",
            "application_control_level_errors",
            "NST.15",
        ),
        serialization_alias="NST.15",
        title="Application control-level Errors",
        description="O | Item #01187 | LEN:10",
    )

    @field_validator("nst_6", "nst_7", "nst_8", "nst_9", "nst_10", "nst_11", "nst_12", "nst_13", "nst_14", "nst_15", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
