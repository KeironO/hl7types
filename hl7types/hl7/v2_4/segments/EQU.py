"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: EQU
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE
from ..datatypes.EI import EI
from ..datatypes.TS import TS


class EQU(BaseModel):
    """HL7 v2 EQU segment."""

    equ_1: EI = Field(
        default=...,
        validation_alias=AliasChoices(
            "equ_1",
            "equipment_instance_identifier",
            "EQU.1",
        ),
        serialization_alias="EQU.1",
        title="Equipment Instance Identifier",
        description="Item #1479",
    )

    equ_2: TS = Field(
        default=...,
        validation_alias=AliasChoices(
            "equ_2",
            "event_date_time",
            "EQU.2",
        ),
        serialization_alias="EQU.2",
        title="Event Date/Time",
        description="Item #1322",
    )

    equ_3: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "equ_3",
            "equipment_state",
            "EQU.3",
        ),
        serialization_alias="EQU.3",
        title="Equipment State",
        description="Item #1323 | Table HL70365",
    )

    equ_4: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "equ_4",
            "local_remote_control_state",
            "EQU.4",
        ),
        serialization_alias="EQU.4",
        title="Local/Remote Control State",
        description="Item #1324 | Table HL70366",
    )

    equ_5: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "equ_5",
            "alert_level",
            "EQU.5",
        ),
        serialization_alias="EQU.5",
        title="Alert Level",
        description="Item #1325 | Table HL70367",
    )

    model_config = {"populate_by_name": True}
