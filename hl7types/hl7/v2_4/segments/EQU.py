"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: EQU
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.EI import EI
from ..datatypes.TS import TS


class EQU(HL7Model):
    """Equipment Detail (S13.4.1).

    Attributes
    ----------
    equ_1 : EI
        EQU.1 - Equipment Instance Identifier (EI) R S13.4.1.1

    equ_2 : TS
        EQU.2 - Event Date/Time (TS) R S13.4.1.2

    equ_3 : CE | None
        EQU.3 - Equipment State (CE) C S13.4.1.3 | 0365 - Equipment state

    equ_4 : CE | None
        EQU.4 - Local/Remote Control State (CE) O S13.4.1.4 | 0366 - Local/remote control state

    equ_5 : CE | None
        EQU.5 - Alert Level (CE) O S13.4.1.5 | 0367 - Alert level
    """

    equ_1: EI = Field(
        validation_alias=AliasChoices(
            "equ_1",
            "equipment_instance_identifier",
            "EQU.1",
        ),
        serialization_alias="EQU.1",
        title="Equipment Instance Identifier",
        description="R | Item #01479",
    )

    equ_2: TS = Field(
        validation_alias=AliasChoices(
            "equ_2",
            "event_date_time",
            "EQU.2",
        ),
        serialization_alias="EQU.2",
        title="Event Date/Time",
        description="R | Item #01322",
    )

    equ_3: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "equ_3",
            "equipment_state",
            "EQU.3",
        ),
        serialization_alias="EQU.3",
        title="Equipment State",
        description="C | Item #01323 | Table 0365 - Equipment state",
    )

    equ_4: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "equ_4",
            "local_remote_control_state",
            "EQU.4",
        ),
        serialization_alias="EQU.4",
        title="Local/Remote Control State",
        description="O | Item #01324 | Table 0366 - Local/remote control state",
    )

    equ_5: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "equ_5",
            "alert_level",
            "EQU.5",
        ),
        serialization_alias="EQU.5",
        title="Alert Level",
        description="O | Item #01325 | Table 0367 - Alert level",
    )

    model_config = {"populate_by_name": True}
