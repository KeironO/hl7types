"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: AIS
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

_RE_SI = re.compile(r'\d*')
_RE_DTM = re.compile(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?')
_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class AIS(HL7Model):
    """Appointment Information (S10.6.4).

    Attributes
    ----------
    ais_1 : str
        AIS.1 - Set ID - AIS (SI) R S10.6.4.1

    ais_2 : str | None
        AIS.2 - Segment Action Code (ID) C S10.6.3.2 | 0206 - Segment Action Code

    ais_3 : CWE
        AIS.3 - Universal Service Identifier (CWE) R S10.6.4.3

    ais_4 : str | None
        AIS.4 - Start Date/Time (DTM) C S10.6.4.4

    ais_5 : str | None
        AIS.5 - Start Date/Time Offset (NM) C S10.6.4.5

    ais_6 : CNE | None
        AIS.6 - Start Date/Time Offset Units (CNE) C S10.6.4.6

    ais_7 : str | None
        AIS.7 - Duration (NM) O S10.6.4.7

    ais_8 : CNE | None
        AIS.8 - Duration Units (CNE) O S10.6.4.8

    ais_9 : CWE | None
        AIS.9 - Allow Substitution Code (CWE) C S10.6.4.9 | 0279 - Allow Substitution Codes

    ais_10 : CWE | None
        AIS.10 - Filler Status Code (CWE) C S10.6.2.25 | 0278 - Filler status codes

    ais_11 : list[CWE] | None
        AIS.11 - Placer Supplemental Service Information (CWE) O rep S10.6.4.11 | 0411 - Supplemental Service Information Values

    ais_12 : list[CWE] | None
        AIS.12 - Filler Supplemental Service Information (CWE) O rep S10.6.4.12 | 0411 - Supplemental Service Information Values
    """

    ais_1: str = Field(
        validation_alias=AliasChoices(
            "ais_1",
            "set_id_ais",
            "AIS.1",
        ),
        serialization_alias="AIS.1",
        title="Set ID - AIS",
        description="R | Item #00890 | LEN:4",
    )

    ais_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ais_2",
            "segment_action_code",
            "AIS.2",
        ),
        serialization_alias="AIS.2",
        title="Segment Action Code",
        description=(
            "C | Item #00763 | Table 0206 - Segment Action Code | LEN:1"
        ),
    )

    ais_3: CWE = Field(
        validation_alias=AliasChoices(
            "ais_3",
            "universal_service_identifier",
            "AIS.3",
        ),
        serialization_alias="AIS.3",
        title="Universal Service Identifier",
        description="R | Item #00238",
    )

    ais_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ais_4",
            "start_date_time",
            "AIS.4",
        ),
        serialization_alias="AIS.4",
        title="Start Date/Time",
        description="C | Item #01202",
    )

    ais_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ais_5",
            "start_date_time_offset",
            "AIS.5",
        ),
        serialization_alias="AIS.5",
        title="Start Date/Time Offset",
        description="C | Item #00891",
    )

    ais_6: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ais_6",
            "start_date_time_offset_units",
            "AIS.6",
        ),
        serialization_alias="AIS.6",
        title="Start Date/Time Offset Units",
        description="C | Item #00892",
    )

    ais_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ais_7",
            "duration",
            "AIS.7",
        ),
        serialization_alias="AIS.7",
        title="Duration",
        description="O | Item #00893",
    )

    ais_8: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ais_8",
            "duration_units",
            "AIS.8",
        ),
        serialization_alias="AIS.8",
        title="Duration Units",
        description="O | Item #00894",
    )

    ais_9: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ais_9",
            "allow_substitution_code",
            "AIS.9",
        ),
        serialization_alias="AIS.9",
        title="Allow Substitution Code",
        description="C | Item #00895 | Table 0279 - Allow Substitution Codes",
    )

    ais_10: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ais_10",
            "filler_status_code",
            "AIS.10",
        ),
        serialization_alias="AIS.10",
        title="Filler Status Code",
        description="C | Item #00889 | Table 0278 - Filler status codes",
    )

    ais_11: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ais_11",
            "placer_supplemental_service_information",
            "AIS.11",
        ),
        serialization_alias="AIS.11",
        title="Placer Supplemental Service Information",
        description=(
            "O | Item #01474 | Table 0411 - Supplemental Service Information "
            "Values"
        ),
    )

    ais_12: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ais_12",
            "filler_supplemental_service_information",
            "AIS.12",
        ),
        serialization_alias="AIS.12",
        title="Filler Supplemental Service Information",
        description=(
            "O | Item #01475 | Table 0411 - Supplemental Service Information "
            "Values"
        ),
    )

    @field_validator("ais_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        if not _RE_SI.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("ais_4", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        if _RE_DTM.fullmatch(v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    @field_validator("ais_5", "ais_7", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
