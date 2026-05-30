"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: FHS
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model


class FHS(HL7Model):
    """HL7 v2 FHS segment.

    Attributes
    ----------
    fhs_1 : str
        FHS.1 (req) - FILE FIELD SEPARATOR (ST)

    fhs_2 : str
        FHS.2 (req) - FILE ENCODING CHARACTERS (ST)

    fhs_3 : str | None
        FHS.3 (opt) - FILE SENDING APPLICATION (ST)

    fhs_4 : str | None
        FHS.4 (opt) - FILE SENDING FACILITY (ST)

    fhs_5 : str | None
        FHS.5 (opt) - FILE RECEIVING APPLICATION (ST)

    fhs_6 : str | None
        FHS.6 (opt) - FILE RECEIVING FACILITY (ST)

    fhs_7 : str | None
        FHS.7 (opt) - DATE/TIME OF FILE CREATION (TS)

    fhs_8 : str | None
        FHS.8 (opt) - FILE SECURITY (ST)

    fhs_9 : str | None
        FHS.9 (opt) - FILE NAME/ID (ST)

    fhs_10 : str | None
        FHS.10 (opt) - FILE HEADER COMMENT (ST)

    fhs_11 : str | None
        FHS.11 (opt) - FILE CONTROL ID (ST)

    fhs_12 : str | None
        FHS.12 (opt) - REFERENCE FILE CONTROL ID (ST)
    """

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

    fhs_3: Optional[str] = Field(
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

    fhs_4: Optional[str] = Field(
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

    fhs_5: Optional[str] = Field(
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

    fhs_6: Optional[str] = Field(
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

    fhs_7: Optional[str] = Field(
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

    fhs_8: Optional[str] = Field(
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

    fhs_9: Optional[str] = Field(
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

    fhs_10: Optional[str] = Field(
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

    fhs_11: Optional[str] = Field(
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

    fhs_12: Optional[str] = Field(
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
