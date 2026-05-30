"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: CM_PRL
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from .CE import CE
from .TX import TX


class CM_PRL(HL7Model):
    """HL7 v2 CM_PRL data type.

    Attributes
    ----------
    cm_prl_1 : CE | None
        CM_PRL.1 (opt) - OBX-3 observation identifier of parent result (CE)

    cm_prl_2 : str | None
        CM_PRL.2 (opt) - OBX-4 sub-ID of parent result (ST)

    cm_prl_3 : TX | None
        CM_PRL.3 (opt) - part of OBX-5 observation result from parent (TX)
    """

    cm_prl_1: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_prl_1",
            "obx_3_observation_identifier_of_parent_result",
            "CM_PRL.1",
        ),
        serialization_alias="CM_PRL.1",
        title="OBX-3 observation identifier of parent result",
    )

    cm_prl_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_prl_2",
            "obx_4_sub_id_of_parent_result",
            "CM_PRL.2",
        ),
        serialization_alias="CM_PRL.2",
        title="OBX-4 sub-ID of parent result",
    )

    cm_prl_3: Optional[TX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_prl_3",
            "part_of_obx_5_observation_result_from_parent",
            "CM_PRL.3",
        ),
        serialization_alias="CM_PRL.3",
        title="part of OBX-5 observation result from parent",
    )

    model_config = {"populate_by_name": True}
