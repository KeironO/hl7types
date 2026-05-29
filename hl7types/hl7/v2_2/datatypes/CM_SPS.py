"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: CM_SPS
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from .CE import CE
from .TX import TX


class CM_SPS(BaseModel):
    """HL7 v2 CM_SPS data type.

    Attributes
    ----------
    cm_sps_1 : CE | None
        CM_SPS.1 (opt) - Specimen source name or code (CE)

    cm_sps_2 : TX | None
        CM_SPS.2 (opt) - additives (TX)

    cm_sps_3 : TX | None
        CM_SPS.3 (opt) - freetext (TX)

    cm_sps_4 : CE | None
        CM_SPS.4 (opt) - body site (CE)

    cm_sps_5 : CE | None
        CM_SPS.5 (opt) - site modifier (CE)
    """

    cm_sps_1: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_sps_1",
            "specimen_source_name_or_code",
            "CM_SPS.1",
        ),
        serialization_alias="CM_SPS.1",
        title="Specimen source name or code",
    )

    cm_sps_2: Optional[TX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_sps_2",
            "additives",
            "CM_SPS.2",
        ),
        serialization_alias="CM_SPS.2",
        title="additives",
    )

    cm_sps_3: Optional[TX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_sps_3",
            "freetext",
            "CM_SPS.3",
        ),
        serialization_alias="CM_SPS.3",
        title="freetext",
    )

    cm_sps_4: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_sps_4",
            "body_site",
            "CM_SPS.4",
        ),
        serialization_alias="CM_SPS.4",
        title="body site",
    )

    cm_sps_5: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_sps_5",
            "site_modifier",
            "CM_SPS.5",
        ),
        serialization_alias="CM_SPS.5",
        title="site modifier",
    )

    model_config = {"populate_by_name": True}
