"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: CM_GROUP_ID
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model


class CM_GROUP_ID(HL7Model):
    """HL7 v2 CM_GROUP_ID data type.

    Attributes
    ----------
    cm_group_id_1 : str | None
        CM_GROUP_ID.1 (opt) - unique group id (ID)

    cm_group_id_2 : str | None
        CM_GROUP_ID.2 (opt) - placer application id (ID)
    """

    cm_group_id_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_group_id_1",
            "unique_group_id",
            "CM_GROUP_ID.1",
        ),
        serialization_alias="CM_GROUP_ID.1",
        title="unique group id",
    )

    cm_group_id_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_group_id_2",
            "placer_application_id",
            "CM_GROUP_ID.2",
        ),
        serialization_alias="CM_GROUP_ID.2",
        title="placer application id",
    )

    model_config = {"populate_by_name": True}
