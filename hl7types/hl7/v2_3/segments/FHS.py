"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: FHS
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.TS import TS


class FHS(HL7Model):
    """File header segment (S2.24.11).

    Attributes
    ----------
    fhs_1 : str
        FHS.1 - File Field Separator (ST) R S2.24.11.1

    fhs_2 : str
        FHS.2 - File Encoding Characters (ST) R S2.24.11.2

    fhs_3 : str | None
        FHS.3 - File Sending Application (ST) O S2.24.11.3

    fhs_4 : str | None
        FHS.4 - File Sending Facility (ST) O S2.24.11.4

    fhs_5 : str | None
        FHS.5 - File Receiving Application (ST) O S2.24.11.5

    fhs_6 : str | None
        FHS.6 - File Receiving Facility (ST) O S2.24.11.6

    fhs_7 : TS | None
        FHS.7 - File Creation Date/Time (TS) NA S2.24.11.7

    fhs_8 : str | None
        FHS.8 - File Security (ST) O S2.24.11.8

    fhs_9 : str | None
        FHS.9 - File Name/ID (ST) O S2.24.11.9

    fhs_10 : str | None
        FHS.10 - File Header Comment (ST) O S2.24.11.10

    fhs_11 : str | None
        FHS.11 - File Control ID (ST) O S2.24.11.11

    fhs_12 : str | None
        FHS.12 - Reference File Control ID (ST) O S2.24.11.12
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
        description="R | Item #00067 | LEN:1",
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
        description="R | Item #00068 | LEN:4",
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
        description="O | Item #00069 | LEN:15",
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
        description="O | Item #00070 | LEN:20",
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
        description="O | Item #00071 | LEN:15",
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
        description="O | Item #00072 | LEN:20",
    )

    fhs_7: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "fhs_7",
            "file_creation_date_time",
            "FHS.7",
        ),
        serialization_alias="FHS.7",
        title="File Creation Date/Time",
        description="NA | Item #00073",
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
        description="O | Item #00074 | LEN:40",
    )

    fhs_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "fhs_9",
            "file_name_id",
            "FHS.9",
        ),
        serialization_alias="FHS.9",
        title="File Name/ID",
        description="O | Item #00075 | LEN:20",
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
        description="O | Item #00076 | LEN:80",
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
        description="O | Item #00077 | LEN:20",
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
        description="O | Item #00078 | LEN:20",
    )

    model_config = {"populate_by_name": True}
