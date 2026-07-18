"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: AIP
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.TS import TS
from ..datatypes.XCN import XCN

_RE_SI = re.compile(r'\d*')
_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class AIP(HL7Model):
    """AIP - appointment information - personnel resource segment (S10.5.7).

    Attributes
    ----------
    aip_1 : str
        AIP.1 - Set ID - AIP (SI) R S10.5.7.1

    aip_2 : str | None
        AIP.2 - Segment Action Code (ID) C S10.5.7.2 | 0206 - Segment action code

    aip_3 : list[XCN] | None
        AIP.3 - Personnel Resource ID (XCN) C rep S10.5.7.3

    aip_4 : CE
        AIP.4 - Resource Role (CE) R S10.5.7.4

    aip_5 : CE | None
        AIP.5 - Resource Group (CE) O S10.5.7.5

    aip_6 : TS | None
        AIP.6 - Start Date/Time (TS) C S10.5.7.6

    aip_7 : str | None
        AIP.7 - Start Date/Time Offset (NM) C S10.5.7.7

    aip_8 : CE | None
        AIP.8 - Start Date/Time Offset Units (CE) C S10.5.7.8

    aip_9 : str | None
        AIP.9 - Duration (NM) O S10.5.7.9

    aip_10 : CE | None
        AIP.10 - Duration Units (CE) O S10.5.7.10

    aip_11 : str | None
        AIP.11 - Allow Substitution Code (IS) C S10.5.7.11 | 0279 - Allow substitution codes

    aip_12 : CE | None
        AIP.12 - Filler Status Code (CE) C S10.5.7.12 | 0278 - Filler status codes
    """

    aip_1: str = Field(
        validation_alias=AliasChoices(
            "aip_1",
            "set_id_aip",
            "AIP.1",
        ),
        serialization_alias="AIP.1",
        title="Set ID - AIP",
        description="R | Item #00906 | LEN:4",
    )

    aip_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aip_2",
            "segment_action_code",
            "AIP.2",
        ),
        serialization_alias="AIP.2",
        title="Segment Action Code",
        description=(
            "C | Item #00763 | Table 0206 - Segment action code | LEN:3"
        ),
    )

    aip_3: Optional[List[XCN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aip_3",
            "personnel_resource_id",
            "AIP.3",
        ),
        serialization_alias="AIP.3",
        title="Personnel Resource ID",
        description="C | Item #00913",
    )

    aip_4: CE = Field(
        validation_alias=AliasChoices(
            "aip_4",
            "resource_role",
            "AIP.4",
        ),
        serialization_alias="AIP.4",
        title="Resource Role",
        description="R | Item #00907",
    )

    aip_5: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aip_5",
            "resource_group",
            "AIP.5",
        ),
        serialization_alias="AIP.5",
        title="Resource Group",
        description="O | Item #00899",
    )

    aip_6: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aip_6",
            "start_date_time",
            "AIP.6",
        ),
        serialization_alias="AIP.6",
        title="Start Date/Time",
        description="C | Item #01202",
    )

    aip_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aip_7",
            "start_date_time_offset",
            "AIP.7",
        ),
        serialization_alias="AIP.7",
        title="Start Date/Time Offset",
        description="C | Item #00891 | LEN:20",
    )

    aip_8: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aip_8",
            "start_date_time_offset_units",
            "AIP.8",
        ),
        serialization_alias="AIP.8",
        title="Start Date/Time Offset Units",
        description="C | Item #00892",
    )

    aip_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aip_9",
            "duration",
            "AIP.9",
        ),
        serialization_alias="AIP.9",
        title="Duration",
        description="O | Item #00893 | LEN:20",
    )

    aip_10: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aip_10",
            "duration_units",
            "AIP.10",
        ),
        serialization_alias="AIP.10",
        title="Duration Units",
        description="O | Item #00894",
    )

    aip_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aip_11",
            "allow_substitution_code",
            "AIP.11",
        ),
        serialization_alias="AIP.11",
        title="Allow Substitution Code",
        description=(
            "C | Item #00895 | Table 0279 - Allow substitution codes | LEN:10"
        ),
    )

    aip_12: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aip_12",
            "filler_status_code",
            "AIP.12",
        ),
        serialization_alias="AIP.12",
        title="Filler Status Code",
        description="C | Item #00889 | Table 0278 - Filler status codes",
    )

    @field_validator("aip_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        if not _RE_SI.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("aip_7", "aip_9", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
