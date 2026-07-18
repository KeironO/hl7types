"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: BTS
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field
from hl7types.hl7 import HL7Model


class BTS(HL7Model):
    """BATCH TRAILER (S2.10.14).

    Attributes
    ----------
    bts_1 : str | None
        BTS.1 - Batch Message Count (ST) NA S2.10.14.1

    bts_2 : str | None
        BTS.2 - Batch Comment (ST) NA S2.10.14.2

    bts_3 : list[str] | None
        BTS.3 - Batch Totals (CM) NA rep S2.10.14.3
    """

    bts_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bts_1",
            "batch_message_count",
            "BTS.1",
        ),
        serialization_alias="BTS.1",
        title="Batch Message Count",
        description="NA | Item #00093 | LEN:10",
    )

    bts_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bts_2",
            "batch_comment",
            "BTS.2",
        ),
        serialization_alias="BTS.2",
        title="Batch Comment",
        description="NA | Item #00094 | LEN:80",
    )

    bts_3: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bts_3",
            "batch_totals",
            "BTS.3",
        ),
        serialization_alias="BTS.3",
        title="Batch Totals",
        description="NA | Item #00095",
    )

    model_config = ConfigDict(populate_by_name=True)
