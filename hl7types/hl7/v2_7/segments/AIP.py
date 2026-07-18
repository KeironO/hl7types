"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: AIP
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, ValidationInfo, field_validator
from hl7types.hl7 import HL7Model
from hl7types.hl7._validators import _apply_dt_fallback

from ..datatypes.CNE import CNE
from ..datatypes.CWE import CWE
from ..datatypes.XCN import XCN

_RE_SI = re.compile(r'\d*')
_RE_DTM = re.compile(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?')
_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class AIP(HL7Model):
    """Appointment Information - Personnel Resource (S10.6.7).

    Attributes
    ----------
    aip_1 : str
        AIP.1 - Set ID - AIP (SI) R S10.6.7.1

    aip_2 : str | None
        AIP.2 - Segment Action Code (ID) C S10.6.3.2 | 0206 - Segment action code

    aip_3 : list[XCN] | None
        AIP.3 - Personnel Resource ID (XCN) C rep S10.6.7.3

    aip_4 : CWE | None
        AIP.4 - Resource Type (CWE) C S10.6.7.4 | 0182 - Staff type

    aip_5 : CWE | None
        AIP.5 - Resource Group (CWE) O S10.6.5.5

    aip_6 : str | None
        AIP.6 - Start Date/Time (DTM) C S10.6.4.4

    aip_7 : str | None
        AIP.7 - Start Date/Time Offset (NM) C S10.6.4.5

    aip_8 : CNE | None
        AIP.8 - Start Date/Time Offset Units (CNE) C S10.6.4.6

    aip_9 : str | None
        AIP.9 - Duration (NM) O S10.6.4.7

    aip_10 : CNE | None
        AIP.10 - Duration Units (CNE) O S10.6.4.8

    aip_11 : CWE | None
        AIP.11 - Allow Substitution Code (CWE) C S10.6.4.9 | 0279 - Allow Substitution Codes

    aip_12 : CWE | None
        AIP.12 - Filler Status Code (CWE) C S10.6.2.25 | 0278 - Filler status codes
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
            "C | Item #00763 | Table 0206 - Segment action code | LEN:1"
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

    aip_4: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aip_4",
            "resource_type",
            "AIP.4",
        ),
        serialization_alias="AIP.4",
        title="Resource Type",
        description="C | Item #00907 | Table 0182 - Staff type",
    )

    aip_5: Optional[CWE] = Field(
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

    aip_6: Optional[str] = Field(
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
        description="C | Item #00891",
    )

    aip_8: Optional[CNE] = Field(
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
        description="O | Item #00893",
    )

    aip_10: Optional[CNE] = Field(
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

    aip_11: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aip_11",
            "allow_substitution_code",
            "AIP.11",
        ),
        serialization_alias="AIP.11",
        title="Allow Substitution Code",
        description="C | Item #00895 | Table 0279 - Allow Substitution Codes",
    )

    aip_12: Optional[CWE] = Field(
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

    @field_validator("aip_6", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        if _RE_DTM.fullmatch(v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    @field_validator("aip_7", "aip_9", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
