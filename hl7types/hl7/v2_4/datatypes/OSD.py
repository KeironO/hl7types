"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: OSD
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model


class OSD(HL7Model):
    """HL7 v2 OSD data type.

    Attributes
    ----------
    osd_1 : str | None
        OSD.1 (opt) - sequence/results flag (ID)

    osd_2 : str | None
        OSD.2 (opt) - placer order number: entity identifier (ST)

    osd_3 : str | None
        OSD.3 (opt) - placer order number: namespace ID (IS)

    osd_4 : str | None
        OSD.4 (opt) - filler order number: entity identifier (ST)

    osd_5 : str | None
        OSD.5 (opt) - filler order number: namespace ID (IS)

    osd_6 : str | None
        OSD.6 (opt) - sequence condition value (ST)

    osd_7 : str | None
        OSD.7 (opt) - maximum number of repeats (NM)

    osd_8 : str | None
        OSD.8 (opt) - placer order number: universal ID (ST)

    osd_9 : str | None
        OSD.9 (opt) - placer order number; universal ID type (ID)

    osd_10 : str | None
        OSD.10 (opt) - filler order number: universal ID (ST)

    osd_11 : str | None
        OSD.11 (opt) - filler order number: universal ID type (ID)
    """

    osd_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "osd_1",
            "sequence_results_flag",
            "OSD.1",
        ),
        serialization_alias="OSD.1",
        title="sequence/results flag",
    )

    osd_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "osd_2",
            "placer_order_number_entity_identifier",
            "OSD.2",
        ),
        serialization_alias="OSD.2",
        title="placer order number: entity identifier",
    )

    osd_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "osd_3",
            "placer_order_number_namespace_id",
            "OSD.3",
        ),
        serialization_alias="OSD.3",
        title="placer order number: namespace ID",
    )

    osd_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "osd_4",
            "filler_order_number_entity_identifier",
            "OSD.4",
        ),
        serialization_alias="OSD.4",
        title="filler order number: entity identifier",
    )

    osd_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "osd_5",
            "filler_order_number_namespace_id",
            "OSD.5",
        ),
        serialization_alias="OSD.5",
        title="filler order number: namespace ID",
    )

    osd_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "osd_6",
            "sequence_condition_value",
            "OSD.6",
        ),
        serialization_alias="OSD.6",
        title="sequence condition value",
    )

    osd_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "osd_7",
            "maximum_number_of_repeats",
            "OSD.7",
        ),
        serialization_alias="OSD.7",
        title="maximum number of repeats",
    )

    osd_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "osd_8",
            "placer_order_number_universal_id",
            "OSD.8",
        ),
        serialization_alias="OSD.8",
        title="placer order number: universal ID",
    )

    osd_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "osd_9",
            "placer_order_number_universal_id_type",
            "OSD.9",
        ),
        serialization_alias="OSD.9",
        title="placer order number; universal ID type",
    )

    osd_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "osd_10",
            "filler_order_number_universal_id",
            "OSD.10",
        ),
        serialization_alias="OSD.10",
        title="filler order number: universal ID",
    )

    osd_11: Optional[str] = Field(
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
