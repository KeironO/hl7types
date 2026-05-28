"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: OSD
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field


class OSD(BaseModel):
    """HL7 v2 OSD data type."""

    osd_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "osd_1",
            "sequence_results_flag",
            "OSD.1",
        ),
        serialization_alias="OSD.1",
        title="sequence/results flag",
    )

    osd_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "osd_2",
            "placer_order_number_entity_identifier",
            "OSD.2",
        ),
        serialization_alias="OSD.2",
        title="placer order number: entity identifier",
    )

    osd_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "osd_3",
            "placer_order_number_namespace_id",
            "OSD.3",
        ),
        serialization_alias="OSD.3",
        title="placer order number: namespace ID",
    )

    osd_4: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "osd_4",
            "filler_order_number_entity_identifier",
            "OSD.4",
        ),
        serialization_alias="OSD.4",
        title="filler order number: entity identifier",
    )

    osd_5: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "osd_5",
            "filler_order_number_namespace_id",
            "OSD.5",
        ),
        serialization_alias="OSD.5",
        title="filler order number: namespace ID",
    )

    osd_6: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "osd_6",
            "sequence_condition_value",
            "OSD.6",
        ),
        serialization_alias="OSD.6",
        title="sequence condition value",
    )

    osd_7: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "osd_7",
            "maximum_number_of_repeats",
            "OSD.7",
        ),
        serialization_alias="OSD.7",
        title="maximum number of repeats",
    )

    osd_8: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "osd_8",
            "placer_order_number_universal_id",
            "OSD.8",
        ),
        serialization_alias="OSD.8",
        title="placer order number: universal ID",
    )

    osd_9: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "osd_9",
            "placer_order_number_universal_id_type",
            "OSD.9",
        ),
        serialization_alias="OSD.9",
        title="placer order number; universal ID type",
    )

    osd_10: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "osd_10",
            "filler_order_number_universal_id",
            "OSD.10",
        ),
        serialization_alias="OSD.10",
        title="filler order number: universal ID",
    )

    osd_11: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "osd_11",
            "filler_order_number_universal_id_type",
            "OSD.11",
        ),
        serialization_alias="OSD.11",
        title="filler order number: universal ID type",
    )

    model_config = {"populate_by_name": True}
