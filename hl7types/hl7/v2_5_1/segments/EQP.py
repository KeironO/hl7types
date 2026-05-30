"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: EQP
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.FT import FT
from ..datatypes.TS import TS


class EQP(HL7Model):
    """HL7 v2 EQP segment.

    Attributes
    ----------
    eqp_1 : CE
        EQP.1 (req) - Event type (CE)

    eqp_2 : str | None
        EQP.2 (opt) - File Name (ST)

    eqp_3 : TS
        EQP.3 (req) - Start Date/Time (TS)

    eqp_4 : TS | None
        EQP.4 (opt) - End Date/Time (TS)

    eqp_5 : FT
        EQP.5 (req) - Transaction Data (FT)
    """

    eqp_1: CE = Field(
        default=...,
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
        default=...,
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

    eqp_5: FT = Field(
        default=...,
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
