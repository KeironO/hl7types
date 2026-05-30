"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: MSG
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model


class MSG(HL7Model):
    """HL7 v2 MSG data type.

    Attributes
    ----------
    msg_1 : str | None
        MSG.1 (opt) - Message Code (ID)

    msg_2 : str | None
        MSG.2 (opt) - Trigger Event (ID)

    msg_3 : str | None
        MSG.3 (opt) - Message Structure (ID)
    """

    msg_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "msg_1",
            "message_code",
            "MSG.1",
        ),
        serialization_alias="MSG.1",
        title="Message Code",
    )

    msg_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "msg_2",
            "trigger_event",
            "MSG.2",
        ),
        serialization_alias="MSG.2",
        title="Trigger Event",
    )

    msg_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "msg_3",
            "message_structure",
            "MSG.3",
        ),
        serialization_alias="MSG.3",
        title="Message Structure",
    )

    model_config = {"populate_by_name": True}
