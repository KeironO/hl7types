"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: PRL
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from .CE import CE
from .TX import TX


class PRL(BaseModel):
    """HL7 v2 PRL data type."""

    prl_1: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "prl_1",
            "obx_3_observation_identifier_of_parent_result",
            "PRL.1",
        ),
        serialization_alias="PRL.1",
        title="OBX-3 observation identifier of parent result",
    )

    prl_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "prl_2",
            "obx_4_sub_id_of_parent_result",
            "PRL.2",
        ),
        serialization_alias="PRL.2",
        title="OBX-4 sub-ID of parent result",
    )

    prl_3: TX | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "prl_3",
            "part_of_obx_5_observation_result_from_parent",
            "PRL.3",
        ),
        serialization_alias="PRL.3",
        title="part of OBX-5 observation result from parent",
    )

    model_config = {"populate_by_name": True}
