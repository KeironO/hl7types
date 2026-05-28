"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: CSU
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class CSU(BaseModel):
    """HL7 v2 CSU data type."""

    csu_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "csu_1",
            "channel_sensitivity",
            "CSU.1",
        ),
        serialization_alias="CSU.1",
        title="channel sensitivity",
    )

    csu_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "csu_2",
            "unit_of_measure_identifier",
            "CSU.2",
        ),
        serialization_alias="CSU.2",
        title="unit of measure identifier",
    )

    csu_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "csu_3",
            "unit_of_measure_description",
            "CSU.3",
        ),
        serialization_alias="CSU.3",
        title="unit of measure description",
    )

    csu_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "csu_4",
            "unit_of_measure_coding_system",
            "CSU.4",
        ),
        serialization_alias="CSU.4",
        title="unit of measure coding system",
    )

    csu_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "csu_5",
            "alternate_unit_of_measure_identifier",
            "CSU.5",
        ),
        serialization_alias="CSU.5",
        title="alternate unit of measure identifier",
    )

    csu_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "csu_6",
            "alternate_unit_of_measure_description",
            "CSU.6",
        ),
        serialization_alias="CSU.6",
        title="alternate unit of measure description",
    )

    csu_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "csu_7",
            "alternate_unit_of_measure_coding_system",
            "CSU.7",
        ),
        serialization_alias="CSU.7",
        title="alternate unit of measure coding system",
    )

    model_config = {"populate_by_name": True}
