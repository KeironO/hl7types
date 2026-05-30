"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: SPS
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from .CE import CE
from .TX import TX


class SPS(HL7Model):
    """HL7 v2 SPS data type.

    Attributes
    ----------
    sps_1 : CE | None
        SPS.1 (opt) - specimen source name or code (CE)

    sps_2 : TX | None
        SPS.2 (opt) - additives (TX)

    sps_3 : TX | None
        SPS.3 (opt) - freetext (TX)

    sps_4 : CE | None
        SPS.4 (opt) - body site (CE)

    sps_5 : CE | None
        SPS.5 (opt) - site modifier (CE)

    sps_6 : CE | None
        SPS.6 (opt) - collection modifier method code (CE)

    sps_7 : CE | None
        SPS.7 (opt) - specimen role (CE)
    """

    sps_1: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sps_1",
            "specimen_source_name_or_code",
            "SPS.1",
        ),
        serialization_alias="SPS.1",
        title="specimen source name or code",
    )

    sps_2: Optional[TX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sps_2",
            "additives",
            "SPS.2",
        ),
        serialization_alias="SPS.2",
        title="additives",
    )

    sps_3: Optional[TX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sps_3",
            "freetext",
            "SPS.3",
        ),
        serialization_alias="SPS.3",
        title="freetext",
    )

    sps_4: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sps_4",
            "body_site",
            "SPS.4",
        ),
        serialization_alias="SPS.4",
        title="body site",
    )

    sps_5: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sps_5",
            "site_modifier",
            "SPS.5",
        ),
        serialization_alias="SPS.5",
        title="site modifier",
    )

    sps_6: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sps_6",
            "collection_modifier_method_code",
            "SPS.6",
        ),
        serialization_alias="SPS.6",
        title="collection modifier method code",
    )

    sps_7: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sps_7",
            "specimen_role",
            "SPS.7",
        ),
        serialization_alias="SPS.7",
        title="specimen role",
    )

    model_config = {"populate_by_name": True}
