"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: OM4
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CQ import CQ
from ..datatypes.CWE import CWE


class OM4(HL7Model):
    """Observations that Require Specimens (S8.8.12).

    Attributes
    ----------
    om4_1 : str | None
        OM4.1 - Sequence Number - Test/Observation Master File (NM) O S8.8.10.1

    om4_2 : str | None
        OM4.2 - Derived Specimen (ID) O S8.8.12.2 | 0170 - Derived Specimen

    om4_3 : list[str] | None
        OM4.3 - Container Description (TX) O rep S8.8.12.3

    om4_4 : list[str] | None
        OM4.4 - Container Volume (NM) O rep S8.8.12.4

    om4_5 : list[CWE] | None
        OM4.5 - Container Units (CWE) O rep S8.8.12.5 | 9999 - no table for CE

    om4_6 : CWE | None
        OM4.6 - Specimen (CWE) O S8.8.12.6 | 9999 - no table for CE

    om4_7 : CWE | None
        OM4.7 - Additive (CWE) O S13.4.3.27 | 0371 - Additive/Preservative

    om4_8 : str | None
        OM4.8 - Preparation (TX) O S8.8.12.8

    om4_9 : str | None
        OM4.9 - Special Handling Requirements (TX) O S8.8.12.9

    om4_10 : CQ | None
        OM4.10 - Normal Collection Volume (CQ) O S8.8.12.10

    om4_11 : CQ | None
        OM4.11 - Minimum Collection Volume (CQ) O S8.8.12.11

    om4_12 : str | None
        OM4.12 - Specimen Requirements (TX) O S8.8.12.12

    om4_13 : list[str] | None
        OM4.13 - Specimen Priorities (ID) O rep S8.8.12.13 | 0027 - Priority

    om4_14 : CQ | None
        OM4.14 - Specimen Retention Time (CQ) O S8.8.12.14

    om4_15 : list[CWE] | None
        OM4.15 - Specimen Handling Code (CWE) O rep S7.4.3.15 | 0376 - Special Handling Code

    om4_16 : str | None
        OM4.16 - Specimen Preference (ID) O S8.8.12.16 | 0920 - Preferred Specimen/Attribute Status

    om4_17 : str | None
        OM4.17 - Preferred Specimen/Attribture Sequence ID (NM) O S8.8.12.17

    om4_18 : list[CWE] | None
        OM4.18 - Taxonomic Classification Code (CWE) O rep S3.4.2.35
    """

    om4_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_1",
            "sequence_number_test_observation_master_file",
            "OM4.1",
        ),
        serialization_alias="OM4.1",
        title="Sequence Number - Test/Observation Master File",
        description="O | Item #00586",
    )

    om4_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_2",
            "derived_specimen",
            "OM4.2",
        ),
        serialization_alias="OM4.2",
        title="Derived Specimen",
        description="O | Item #00642 | Table 0170 - Derived Specimen | LEN:1",
    )

    om4_3: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_3",
            "container_description",
            "OM4.3",
        ),
        serialization_alias="OM4.3",
        title="Container Description",
        description="O | Item #00643",
    )

    om4_4: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_4",
            "container_volume",
            "OM4.4",
        ),
        serialization_alias="OM4.4",
        title="Container Volume",
        description="O | Item #00644",
    )

    om4_5: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_5",
            "container_units",
            "OM4.5",
        ),
        serialization_alias="OM4.5",
        title="Container Units",
        description="O | Item #00645 | Table 9999 - no table for CE",
    )

    om4_6: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_6",
            "specimen",
            "OM4.6",
        ),
        serialization_alias="OM4.6",
        title="Specimen",
        description="O | Item #00646 | Table 9999 - no table for CE",
    )

    om4_7: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_7",
            "additive",
            "OM4.7",
        ),
        serialization_alias="OM4.7",
        title="Additive",
        description="O | Item #00647 | Table 0371 - Additive/Preservative",
    )

    om4_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_8",
            "preparation",
            "OM4.8",
        ),
        serialization_alias="OM4.8",
        title="Preparation",
        description="O | Item #00648",
    )

    om4_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_9",
            "special_handling_requirements",
            "OM4.9",
        ),
        serialization_alias="OM4.9",
        title="Special Handling Requirements",
        description="O | Item #00649",
    )

    om4_10: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_10",
            "normal_collection_volume",
            "OM4.10",
        ),
        serialization_alias="OM4.10",
        title="Normal Collection Volume",
        description="O | Item #00650",
    )

    om4_11: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_11",
            "minimum_collection_volume",
            "OM4.11",
        ),
        serialization_alias="OM4.11",
        title="Minimum Collection Volume",
        description="O | Item #00651",
    )

    om4_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_12",
            "specimen_requirements",
            "OM4.12",
        ),
        serialization_alias="OM4.12",
        title="Specimen Requirements",
        description="O | Item #00652",
    )

    om4_13: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_13",
            "specimen_priorities",
            "OM4.13",
        ),
        serialization_alias="OM4.13",
        title="Specimen Priorities",
        description="O | Item #00653 | Table 0027 - Priority | LEN:1",
    )

    om4_14: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_14",
            "specimen_retention_time",
            "OM4.14",
        ),
        serialization_alias="OM4.14",
        title="Specimen Retention Time",
        description="O | Item #00654",
    )

    om4_15: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_15",
            "specimen_handling_code",
            "OM4.15",
        ),
        serialization_alias="OM4.15",
        title="Specimen Handling Code",
        description="O | Item #01908 | Table 0376 - Special Handling Code",
    )

    om4_16: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_16",
            "specimen_preference",
            "OM4.16",
        ),
        serialization_alias="OM4.16",
        title="Specimen Preference",
        description=(
            "O | Item #03311 | Table 0920 - Preferred Specimen/Attribute Status"
        ),
    )

    om4_17: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_17",
            "preferred_specimen_attribture_sequence_id",
            "OM4.17",
        ),
        serialization_alias="OM4.17",
        title="Preferred Specimen/Attribture Sequence ID",
        description="O | Item #03312",
    )

    om4_18: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om4_18",
            "taxonomic_classification_code",
            "OM4.18",
        ),
        serialization_alias="OM4.18",
        title="Taxonomic Classification Code",
        description="O | Item #01539",
    )

    @field_validator("om4_1", "om4_4", "om4_17", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
