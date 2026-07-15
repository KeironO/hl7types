"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: BTS
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model


class BTS(HL7Model):
    """BATCH TRAILER (S2.5.3).

    Attributes
    ----------
    bts_1 : str | None
        BTS.1 - BATCH MESSAGE COUNT (ST) O S2-41

    bts_2 : str | None
        BTS.2 - BATCH COMMENT (ST) O

    bts_3 : str | None
        BTS.3 - BATCH TOTALS (CM) O
    """

    bts_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bts_1",
            "batch_message_count",
            "BTS.1",
        ),
        serialization_alias="BTS.1",
        title="BATCH MESSAGE COUNT",
        description="O | Item #00664 | LEN:10",
    )

    bts_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bts_2",
            "batch_comment",
            "BTS.2",
        ),
        serialization_alias="BTS.2",
        title="BATCH COMMENT",
        description="O | Item #00665 | LEN:80",
    )

    bts_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "bts_3",
            "batch_totals",
            "BTS.3",
        ),
        serialization_alias="BTS.3",
        title="BATCH TOTALS",
        description="O | Item #00666 | LEN:100",
    )

    model_config = {"populate_by_name": True}
