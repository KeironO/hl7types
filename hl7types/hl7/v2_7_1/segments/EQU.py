"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: EQU
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field, ValidationInfo, field_validator
from hl7types.hl7 import HL7Model
from hl7types.hl7._validators import _apply_dt_fallback

from ..datatypes.CWE import CWE
from ..datatypes.EI import EI

_RE_DTM = re.compile(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?')


class EQU(HL7Model):
    """Equipment Detail (S13.4.1).

    Attributes
    ----------
    equ_1 : EI
        EQU.1 - Equipment Instance Identifier (EI) R S13.4.1.1

    equ_2 : str
        EQU.2 - Event Date/Time (DTM) R S13.4.1.2

    equ_3 : CWE | None
        EQU.3 - Equipment State (CWE) C S13.4.1.3 | 0365 - Equipment State

    equ_4 : CWE | None
        EQU.4 - Local/Remote Control State (CWE) O S13.4.1.4 | 0366 - Local/Remote Control State

    equ_5 : CWE | None
        EQU.5 - Alert Level (CWE) O S13.4.1.5 | 0367 - Alert Level
    """

    equ_1: EI = Field(
        validation_alias=AliasChoices(
            "equ_1",
            "equipment_instance_identifier",
            "EQU.1",
        ),
        serialization_alias="EQU.1",
        title="Equipment Instance Identifier",
        description="R | Item #01479",
    )

    equ_2: str = Field(
        validation_alias=AliasChoices(
            "equ_2",
            "event_date_time",
            "EQU.2",
        ),
        serialization_alias="EQU.2",
        title="Event Date/Time",
        description="R | Item #01322",
    )

    equ_3: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "equ_3",
            "equipment_state",
            "EQU.3",
        ),
        serialization_alias="EQU.3",
        title="Equipment State",
        description="C | Item #01323 | Table 0365 - Equipment State",
    )

    equ_4: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "equ_4",
            "local_remote_control_state",
            "EQU.4",
        ),
        serialization_alias="EQU.4",
        title="Local/Remote Control State",
        description="O | Item #01324 | Table 0366 - Local/Remote Control State",
    )

    equ_5: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "equ_5",
            "alert_level",
            "EQU.5",
        ),
        serialization_alias="EQU.5",
        title="Alert Level",
        description="O | Item #01325 | Table 0367 - Alert Level",
    )

    @field_validator("equ_2", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        if _RE_DTM.fullmatch(v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = ConfigDict(populate_by_name=True)
