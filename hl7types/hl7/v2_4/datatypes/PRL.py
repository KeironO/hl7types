"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: PRL
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from .CE import CE


class PRL(HL7Model):
    """HL7 v2 PRL data type.

    Attributes
    ----------
    prl_1 : CE | None
        PRL.1 (opt) - OBX-3 observation identifier of parent result (CE)

    prl_2 : str | None
        PRL.2 (opt) - OBX-4 sub-ID of parent result (ST)

    prl_3 : str | None
        PRL.3 (opt) - part of OBX-5 observation result from parent (TX)
    """

    prl_1: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prl_1",
            "obx_3_observation_identifier_of_parent_result",
            "PRL.1",
        ),
        serialization_alias="PRL.1",
        title="OBX-3 observation identifier of parent result",
    )

    prl_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "prl_2",
            "obx_4_sub_id_of_parent_result",
            "PRL.2",
        ),
        serialization_alias="PRL.2",
        title="OBX-4 sub-ID of parent result",
    )

    prl_3: Optional[str] = Field(
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
