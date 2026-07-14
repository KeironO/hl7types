"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: EQP
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.TS import TS


class EQP(HL7Model):
    """Equipment/log Service (S13.4.12).

    Attributes
    ----------
    eqp_1 : CE
        EQP.1 (req) - Event type (CE) S13.4.12.1 | 0450 - Event type

    eqp_2 : str | None
        EQP.2 (opt) - File Name (ST) S13.4.12.2

    eqp_3 : TS
        EQP.3 (req) - Start Date/Time (TS) S13.4.12.3

    eqp_4 : TS | None
        EQP.4 (opt) - End Date/Time (TS) S13.4.12.4

    eqp_5 : str
        EQP.5 (req) - Transaction Data (FT) S13.4.12.5
    """

    eqp_1: CE = Field(
        validation_alias=AliasChoices(
            "eqp_1",
            "event_type",
            "EQP.1",
        ),
        serialization_alias="EQP.1",
        title="Event type",
        description="Item #1430 | Table HL70450",
    )

    eqp_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "eqp_2",
            "file_name",
            "EQP.2",
        ),
        serialization_alias="EQP.2",
        title="File Name",
        description="Item #1431",
    )

    eqp_3: TS = Field(
        validation_alias=AliasChoices(
            "eqp_3",
            "start_date_time",
            "EQP.3",
        ),
        serialization_alias="EQP.3",
        title="Start Date/Time",
        description="Item #1202",
    )

    eqp_4: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "eqp_4",
            "end_date_time",
            "EQP.4",
        ),
        serialization_alias="EQP.4",
        title="End Date/Time",
        description="Item #1432",
    )

    eqp_5: str = Field(
        validation_alias=AliasChoices(
            "eqp_5",
            "transaction_data",
            "EQP.5",
        ),
        serialization_alias="EQP.5",
        title="Transaction Data",
        description="Item #1433",
    )

    model_config = {"populate_by_name": True}
