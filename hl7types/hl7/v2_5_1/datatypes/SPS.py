"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: SPS
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from .CWE import CWE
from .TX import TX


class SPS(BaseModel):
    """HL7 v2 SPS data type."""

    sps_1: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sps_1",
            "specimen_source_name_or_code",
            "SPS.1",
        ),
        serialization_alias="SPS.1",
        title="Specimen Source Name or Code",
    )

    sps_2: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sps_2",
            "additives",
            "SPS.2",
        ),
        serialization_alias="SPS.2",
        title="Additives",
    )

    sps_3: Optional[TX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sps_3",
            "specimen_collection_method",
            "SPS.3",
        ),
        serialization_alias="SPS.3",
        title="Specimen Collection Method",
    )

    sps_4: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sps_4",
            "body_site",
            "SPS.4",
        ),
        serialization_alias="SPS.4",
        title="Body Site",
    )

    sps_5: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sps_5",
            "site_modifier",
            "SPS.5",
        ),
        serialization_alias="SPS.5",
        title="Site Modifier",
    )

    sps_6: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sps_6",
            "collection_method_modifier_code",
            "SPS.6",
        ),
        serialization_alias="SPS.6",
        title="Collection Method Modifier Code",
    )

    sps_7: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sps_7",
            "specimen_role",
            "SPS.7",
        ),
        serialization_alias="SPS.7",
        title="Specimen Role",
    )

    model_config = {"populate_by_name": True}
