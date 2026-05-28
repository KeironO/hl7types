"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: PES
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.EI import EI
from ..datatypes.FT import FT
from ..datatypes.XAD import XAD
from ..datatypes.XCN import XCN
from ..datatypes.XON import XON
from ..datatypes.XTN import XTN


class PES(BaseModel):
    """HL7 v2 PES segment."""

    pes_1: Optional[List[XON]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pes_1",
            "sender_organization_name",
            "PES.1",
        ),
        serialization_alias="PES.1",
        title="Sender Organization Name",
        description="Item #1059",
    )

    pes_2: Optional[List[XCN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pes_2",
            "sender_individual_name",
            "PES.2",
        ),
        serialization_alias="PES.2",
        title="Sender Individual Name",
        description="Item #1060",
    )

    pes_3: Optional[List[XAD]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pes_3",
            "sender_address",
            "PES.3",
        ),
        serialization_alias="PES.3",
        title="Sender Address",
        description="Item #1062",
    )

    pes_4: Optional[List[XTN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pes_4",
            "sender_telephone",
            "PES.4",
        ),
        serialization_alias="PES.4",
        title="Sender Telephone",
        description="Item #1063",
    )

    pes_5: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pes_5",
            "sender_event_identifier",
            "PES.5",
        ),
        serialization_alias="PES.5",
        title="Sender Event Identifier",
        description="Item #1064",
    )

    pes_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pes_6",
            "sender_sequence_number",
            "PES.6",
        ),
        serialization_alias="PES.6",
        title="Sender Sequence Number",
        description="Item #1065",
    )

    pes_7: Optional[List[FT]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pes_7",
            "sender_event_description",
            "PES.7",
        ),
        serialization_alias="PES.7",
        title="Sender Event Description",
        description="Item #1066",
    )

    pes_8: Optional[FT] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pes_8",
            "sender_comment",
            "PES.8",
        ),
        serialization_alias="PES.8",
        title="Sender Comment",
        description="Item #1067",
    )

    pes_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pes_9",
            "sender_aware_date_time",
            "PES.9",
        ),
        serialization_alias="PES.9",
        title="Sender Aware Date/Time",
        description="Item #1068",
    )

    pes_10: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "pes_10",
            "event_report_date",
            "PES.10",
        ),
        serialization_alias="PES.10",
        title="Event Report Date",
        description="Item #1069",
    )

    pes_11: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pes_11",
            "event_report_timing_type",
            "PES.11",
        ),
        serialization_alias="PES.11",
        title="Event Report Timing/Type",
        description="Item #1070 | Table HL70234",
    )

    pes_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pes_12",
            "event_report_source",
            "PES.12",
        ),
        serialization_alias="PES.12",
        title="Event Report Source",
        description="Item #1071 | Table HL70235",
    )

    pes_13: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pes_13",
            "event_reported_to",
            "PES.13",
        ),
        serialization_alias="PES.13",
        title="Event Reported To",
        description="Item #1072 | Table HL70236",
    )

    model_config = {"populate_by_name": True}
