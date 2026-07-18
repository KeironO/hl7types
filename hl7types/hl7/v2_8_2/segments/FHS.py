"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: FHS
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field, ValidationInfo, field_validator
from hl7types.hl7 import HL7Model
from hl7types.hl7._validators import _apply_dt_fallback

from ..datatypes.HD import HD

_RE_DTM = re.compile(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?')


class FHS(HL7Model):
    """File Header (S2.14.6).

    Attributes
    ----------
    fhs_1 : str
        FHS.1 - File Field Separator (ST) R S2.14.6.1

    fhs_2 : str
        FHS.2 - File Encoding Characters (ST) R S2.14.6.2

    fhs_3 : HD | None
        FHS.3 - File Sending Application (HD) O S2.14.6.3

    fhs_4 : HD | None
        FHS.4 - File Sending Facility (HD) O S2.14.6.4

    fhs_5 : HD | None
        FHS.5 - File Receiving Application (HD) O S2.14.6.5

    fhs_6 : HD | None
        FHS.6 - File Receiving Facility (HD) O S2.14.6.6

    fhs_7 : str | None
        FHS.7 - File Creation Date/Time (DTM) O S2.14.6.7

    fhs_8 : str | None
        FHS.8 - File Security (ST) O S2.14.6.8

    fhs_9 : str | None
        FHS.9 - File Name/ID (ST) O S2.14.6.9

    fhs_10 : str | None
        FHS.10 - File Header Comment (ST) O S2.14.6.10

    fhs_11 : str | None
        FHS.11 - File Control ID (ST) O S2.14.6.11

    fhs_12 : str | None
        FHS.12 - Reference File Control ID (ST) O S2.14.6.12

    fhs_13 : HD | None
        FHS.13 - File Sending Network Address (HD) O S2.14.6.13

    fhs_14 : HD | None
        FHS.14 - File Receiving Network Address (HD) O S2.14.6.14
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
        description="R | Item #00068 | LEN:5",
    )

    fhs_3: Optional[HD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "fhs_3",
            "file_sending_application",
            "FHS.3",
        ),
        serialization_alias="FHS.3",
        title="File Sending Application",
        description="O | Item #00069",
    )

    fhs_4: Optional[HD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "fhs_4",
            "file_sending_facility",
            "FHS.4",
        ),
        serialization_alias="FHS.4",
        title="File Sending Facility",
        description="O | Item #00070",
    )

    fhs_5: Optional[HD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "fhs_5",
            "file_receiving_application",
            "FHS.5",
        ),
        serialization_alias="FHS.5",
        title="File Receiving Application",
        description="O | Item #00071",
    )

    fhs_6: Optional[HD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "fhs_6",
            "file_receiving_facility",
            "FHS.6",
        ),
        serialization_alias="FHS.6",
        title="File Receiving Facility",
        description="O | Item #00072",
    )

    fhs_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "fhs_7",
            "file_creation_date_time",
            "FHS.7",
        ),
        serialization_alias="FHS.7",
        title="File Creation Date/Time",
        description="O | Item #00073",
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
        description="O | Item #00074",
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
        description="O | Item #00075",
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
        description="O | Item #00076",
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
        description="O | Item #00077",
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
        description="O | Item #00078",
    )

    fhs_13: Optional[HD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "fhs_13",
            "file_sending_network_address",
            "FHS.13",
        ),
        serialization_alias="FHS.13",
        title="File Sending Network Address",
        description="O | Item #02269",
    )

    fhs_14: Optional[HD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "fhs_14",
            "file_receiving_network_address",
            "FHS.14",
        ),
        serialization_alias="FHS.14",
        title="File Receiving Network Address",
        description="O | Item #02270",
    )

    @field_validator("fhs_7", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        if _RE_DTM.fullmatch(v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = ConfigDict(populate_by_name=True)
