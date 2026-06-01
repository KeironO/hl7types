"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: OSD
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator


class OSD(HL7Model):
    """HL7 v2 OSD data type.

    Attributes
    ----------
    osd_1 : str | None
        OSD.1 (opt) - Sequence/Results Flag (ID)

    osd_2 : str | None
        OSD.2 (opt) - Placer Order Number: Entity Identifier (ST)

    osd_3 : str | None
        OSD.3 (opt) - Placer Order Number: Namespace ID (IS)

    osd_4 : str | None
        OSD.4 (opt) - Filler Order Number: Entity Identifier (ST)

    osd_5 : str | None
        OSD.5 (opt) - Filler Order Number: Namespace ID (IS)

    osd_6 : str | None
        OSD.6 (opt) - Sequence Condition Value (ST)

    osd_7 : str | None
        OSD.7 (opt) - Maximum Number of Repeats (NM)

    osd_8 : str | None
        OSD.8 (opt) - Placer Order Number: Universal ID (ST)

    osd_9 : str | None
        OSD.9 (opt) - Placer Order Number: Universal ID Type (ID)

    osd_10 : str | None
        OSD.10 (opt) - Filler Order Number: Universal ID (ST)

    osd_11 : str | None
        OSD.11 (opt) - Filler Order Number: Universal ID Type (ID)
    """

    osd_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "osd_1",
            "sequence_results_flag",
            "OSD.1",
        ),
        serialization_alias="OSD.1",
        title="Sequence/Results Flag",
    )

    osd_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "osd_2",
            "placer_order_number_entity_identifier",
            "OSD.2",
        ),
        serialization_alias="OSD.2",
        title="Placer Order Number: Entity Identifier",
    )

    osd_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "osd_3",
            "placer_order_number_namespace_id",
            "OSD.3",
        ),
        serialization_alias="OSD.3",
        title="Placer Order Number: Namespace ID",
    )

    osd_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "osd_4",
            "filler_order_number_entity_identifier",
            "OSD.4",
        ),
        serialization_alias="OSD.4",
        title="Filler Order Number: Entity Identifier",
    )

    osd_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "osd_5",
            "filler_order_number_namespace_id",
            "OSD.5",
        ),
        serialization_alias="OSD.5",
        title="Filler Order Number: Namespace ID",
    )

    osd_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "osd_6",
            "sequence_condition_value",
            "OSD.6",
        ),
        serialization_alias="OSD.6",
        title="Sequence Condition Value",
    )

    osd_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "osd_7",
            "maximum_number_of_repeats",
            "OSD.7",
        ),
        serialization_alias="OSD.7",
        title="Maximum Number of Repeats",
    )

    osd_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "osd_8",
            "placer_order_number_universal_id",
            "OSD.8",
        ),
        serialization_alias="OSD.8",
        title="Placer Order Number: Universal ID",
    )

    osd_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "osd_9",
            "placer_order_number_universal_id_type",
            "OSD.9",
        ),
        serialization_alias="OSD.9",
        title="Placer Order Number: Universal ID Type",
    )

    osd_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "osd_10",
            "filler_order_number_universal_id",
            "OSD.10",
        ),
        serialization_alias="OSD.10",
        title="Filler Order Number: Universal ID",
    )

    osd_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "osd_11",
            "filler_order_number_universal_id_type",
            "OSD.11",
        ),
        serialization_alias="OSD.11",
        title="Filler Order Number: Universal ID Type",
    )

    @field_validator("osd_7", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
