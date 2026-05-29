"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: MSG
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class MSG(BaseModel):
    """HL7 v2 MSG data type.

    Attributes
    ----------
    msg_1 : str
        MSG.1 (req) - Message Code (ID)

    msg_2 : str
        MSG.2 (req) - Trigger Event (ID)

    msg_3 : str
        MSG.3 (req) - Message Structure (ID)
    """

    msg_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "msg_1",
            "message_code",
            "MSG.1",
        ),
        serialization_alias="MSG.1",
        title="Message Code",
    )

    msg_2: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "msg_2",
            "trigger_event",
            "MSG.2",
        ),
        serialization_alias="MSG.2",
        title="Trigger Event",
    )

    msg_3: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "msg_3",
            "message_structure",
            "MSG.3",
        ),
        serialization_alias="MSG.3",
        title="Message Structure",
    )

    model_config = {"populate_by_name": True}
