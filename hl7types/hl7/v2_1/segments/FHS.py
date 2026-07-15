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
    """FILE HEADER (S2.5.5).

    Attributes
    ----------
    fhs_1 : str
        FHS.1 - FILE FIELD SEPARATOR (ST) R S2-43

    fhs_2 : str
        FHS.2 - FILE ENCODING CHARACTERS (ST) R

    fhs_3 : str | None
        FHS.3 - FILE SENDING APPLICATION (ST) O

    fhs_4 : str | None
        FHS.4 - FILE SENDING FACILITY (ST) O

    fhs_5 : str | None
        FHS.5 - FILE RECEIVING APPLICATION (ST) O

    fhs_6 : str | None
        FHS.6 - FILE RECEIVING FACILITY (ST) O

    fhs_7 : str | None
        FHS.7 - DATE/TIME OF FILE CREATION (TS) O

    fhs_8 : str | None
        FHS.8 - FILE SECURITY (ST) O

    fhs_9 : str | None
        FHS.9 - FILE NAME/ID (ST) O

    fhs_10 : str | None
        FHS.10 - FILE HEADER COMMENT (ST) O

    fhs_11 : str | None
        FHS.11 - FILE CONTROL ID (ST) O

    fhs_12 : str | None
        FHS.12 - REFERENCE FILE CONTROL ID (ST) O
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
        description="R | Item #00692 | LEN:1",
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
        description="R | Item #00693 | LEN:4",
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
        description="O | Item #00694 | LEN:15",
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
        description="O | Item #00695 | LEN:20",
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
        description="O | Item #00696 | LEN:15",
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
        description="O | Item #00697 | LEN:20",
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
        description="O | Item #00660 | LEN:19",
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
        description="O | Item #00698 | LEN:40",
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
        description="O | Item #00661 | LEN:20",
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
        description="O | Item #00662 | LEN:80",
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
        description="O | Item #00663 | LEN:20",
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
        description="O | Item #00768 | LEN:20",
    )

    model_config = {"populate_by_name": True}
