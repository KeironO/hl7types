"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: NSC
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.HD import HD


class NSC(BaseModel):
    """HL7 v2 NSC segment."""

    nsc_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "nsc_1",
            "application_change_type",
            "NSC.1",
        ),
        serialization_alias="NSC.1",
        title="Application Change Type",
        description="Item #1188 | Table HL70409",
    )

    nsc_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "nsc_2",
            "current_cpu",
            "NSC.2",
        ),
        serialization_alias="NSC.2",
        title="Current CPU",
        description="Item #1189",
    )

    nsc_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "nsc_3",
            "current_fileserver",
            "NSC.3",
        ),
        serialization_alias="NSC.3",
        title="Current Fileserver",
        description="Item #1190",
    )

    nsc_4: HD | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "nsc_4",
            "current_application",
            "NSC.4",
        ),
        serialization_alias="NSC.4",
        title="Current Application",
        description="Item #1191",
    )

    nsc_5: HD | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "nsc_5",
            "current_facility",
            "NSC.5",
        ),
        serialization_alias="NSC.5",
        title="Current Facility",
        description="Item #1192",
    )

    nsc_6: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "nsc_6",
            "new_cpu",
            "NSC.6",
        ),
        serialization_alias="NSC.6",
        title="New CPU",
        description="Item #1193",
    )

    nsc_7: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "nsc_7",
            "new_fileserver",
            "NSC.7",
        ),
        serialization_alias="NSC.7",
        title="New Fileserver",
        description="Item #1194",
    )

    nsc_8: HD | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "nsc_8",
            "new_application",
            "NSC.8",
        ),
        serialization_alias="NSC.8",
        title="New Application",
        description="Item #1195",
    )

    nsc_9: HD | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "nsc_9",
            "new_facility",
            "NSC.9",
        ),
        serialization_alias="NSC.9",
        title="New Facility",
        description="Item #1196",
    )

    model_config = {"populate_by_name": True}
