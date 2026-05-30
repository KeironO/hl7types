"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: FHS
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.TS import TS


class FHS(HL7Model):
    """HL7 v2 FHS segment.

    Attributes
    ----------
    fhs_1 : str
        FHS.1 (req) - File Field Separator (ST)

    fhs_2 : str
        FHS.2 (req) - File Encoding Characters (ST)

    fhs_3 : str | None
        FHS.3 (opt) - File Sending Application (ST)

    fhs_4 : str | None
        FHS.4 (opt) - File Sending Facility (ST)

    fhs_5 : str | None
        FHS.5 (opt) - File Receiving Application (ST)

    fhs_6 : str | None
        FHS.6 (opt) - File Receiving Facility (ST)

    fhs_7 : TS | None
        FHS.7 (opt) - File creation date / time (TS)

    fhs_8 : str | None
        FHS.8 (opt) - File Security (ST)

    fhs_9 : str | None
        FHS.9 (opt) - File name / ID (ST)

    fhs_10 : str | None
        FHS.10 (opt) - File Header Comment (ST)

    fhs_11 : str | None
        FHS.11 (opt) - File Control ID (ST)

    fhs_12 : str | None
        FHS.12 (opt) - Reference File Control ID (ST)
    """

    fhs_1: str = Field(
        default="|",
        validation_alias=AliasChoices(
            "fhs_1",
            "file_field_separator",
            "FHS.1",
        ),
        serialization_alias="FHS.1",
        title="File Field Separator",
        description="Item #67",
    )

    fhs_2: str = Field(
        default="^~\\&",
        validation_alias=AliasChoices(
            "fhs_2",
            "file_encoding_characters",
            "FHS.2",
        ),
        serialization_alias="FHS.2",
        title="File Encoding Characters",
        description="Item #68",
    )

    fhs_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "fhs_3",
            "file_sending_application",
            "FHS.3",
        ),
        serialization_alias="FHS.3",
        title="File Sending Application",
        description="Item #69",
    )

    fhs_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "fhs_4",
            "file_sending_facility",
            "FHS.4",
        ),
        serialization_alias="FHS.4",
        title="File Sending Facility",
        description="Item #70",
    )

    fhs_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "fhs_5",
            "file_receiving_application",
            "FHS.5",
        ),
        serialization_alias="FHS.5",
        title="File Receiving Application",
        description="Item #71",
    )

    fhs_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "fhs_6",
            "file_receiving_facility",
            "FHS.6",
        ),
        serialization_alias="FHS.6",
        title="File Receiving Facility",
        description="Item #72",
    )

    fhs_7: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "fhs_7",
            "file_creation_date_time",
            "FHS.7",
        ),
        serialization_alias="FHS.7",
        title="File creation date / time",
        description="Item #73",
    )

    fhs_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "fhs_8",
            "file_security",
            "FHS.8",
        ),
        serialization_alias="FHS.8",
        title="File Security",
        description="Item #74",
    )

    fhs_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "fhs_9",
            "file_name_id",
            "FHS.9",
        ),
        serialization_alias="FHS.9",
        title="File name / ID",
        description="Item #75",
    )

    fhs_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "fhs_10",
            "file_header_comment",
            "FHS.10",
        ),
        serialization_alias="FHS.10",
        title="File Header Comment",
        description="Item #76",
    )

    fhs_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "fhs_11",
            "file_control_id",
            "FHS.11",
        ),
        serialization_alias="FHS.11",
        title="File Control ID",
        description="Item #77",
    )

    fhs_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "fhs_12",
            "reference_file_control_id",
            "FHS.12",
        ),
        serialization_alias="FHS.12",
        title="Reference File Control ID",
        description="Item #78",
    )

    model_config = {"populate_by_name": True}
