"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: CM_MSG
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class CM_MSG(BaseModel):
    """HL7 v2 CM_MSG data type.

    Attributes
    ----------
    cm_msg_1 : str | None
        CM_MSG.1 (opt) - message type (ID)

    cm_msg_2 : str | None
        CM_MSG.2 (opt) - Trigger Event (ID)
    """

    cm_msg_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_msg_1",
            "message_type",
            "CM_MSG.1",
        ),
        serialization_alias="CM_MSG.1",
        title="message type",
    )

    cm_msg_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_msg_2",
            "trigger_event",
            "CM_MSG.2",
        ),
        serialization_alias="CM_MSG.2",
        title="Trigger Event",
    )

    model_config = {"populate_by_name": True}
