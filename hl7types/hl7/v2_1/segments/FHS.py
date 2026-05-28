"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: FHS
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field


class FHS(BaseModel):
    """HL7 v2 FHS segment."""

    fhs_1: str = Field(
        default="|",
        validation_alias=AliasChoices(
            "fhs_1",
            "file_field_separator",
            "FHS.1",
        ),
        serialization_alias="FHS.1",
        title="FILE FIELD SEPARATOR",
        description="Item #692",
    )

    fhs_2: str = Field(
        default="^~\\&",
        validation_alias=AliasChoices(
            "fhs_2",
            "file_encoding_characters",
            "FHS.2",
        ),
        serialization_alias="FHS.2",
        title="FILE ENCODING CHARACTERS",
        description="Item #693",
    )

    fhs_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "fhs_3",
            "file_sending_application",
            "FHS.3",
        ),
        serialization_alias="FHS.3",
        title="FILE SENDING APPLICATION",
        description="Item #694",
    )

    fhs_4: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "fhs_4",
            "file_sending_facility",
            "FHS.4",
        ),
        serialization_alias="FHS.4",
        title="FILE SENDING FACILITY",
        description="Item #695",
    )

    fhs_5: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "fhs_5",
            "file_receiving_application",
            "FHS.5",
        ),
        serialization_alias="FHS.5",
        title="FILE RECEIVING APPLICATION",
        description="Item #696",
    )

    fhs_6: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "fhs_6",
            "file_receiving_facility",
            "FHS.6",
        ),
        serialization_alias="FHS.6",
        title="FILE RECEIVING FACILITY",
        description="Item #697",
    )

    fhs_7: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "fhs_7",
            "date_time_of_file_creation",
            "FHS.7",
        ),
        serialization_alias="FHS.7",
        title="DATE/TIME OF FILE CREATION",
        description="Item #660",
    )

    fhs_8: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "fhs_8",
            "file_security",
            "FHS.8",
        ),
        serialization_alias="FHS.8",
        title="FILE SECURITY",
        description="Item #698",
    )

    fhs_9: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "fhs_9",
            "file_name_id",
            "FHS.9",
        ),
        serialization_alias="FHS.9",
        title="FILE NAME/ID",
        description="Item #661",
    )

    fhs_10: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "fhs_10",
            "file_header_comment",
            "FHS.10",
        ),
        serialization_alias="FHS.10",
        title="FILE HEADER COMMENT",
        description="Item #662",
    )

    fhs_11: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "fhs_11",
            "file_control_id",
            "FHS.11",
        ),
        serialization_alias="FHS.11",
        title="FILE CONTROL ID",
        description="Item #663",
    )

    fhs_12: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "fhs_12",
            "reference_file_control_id",
            "FHS.12",
        ),
        serialization_alias="FHS.12",
        title="REFERENCE FILE CONTROL ID",
        description="Item #768",
    )

    model_config = {"populate_by_name": True}
