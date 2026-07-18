"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: RMI
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field, ValidationInfo, field_validator
from hl7types.hl7 import HL7Model
from hl7types.hl7._validators import _apply_dt_fallback

from ..datatypes.CWE import CWE

_RE_DTM = re.compile(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?')


class RMI(HL7Model):
    """Risk Management Incident (S6.5.14).

    Attributes
    ----------
    rmi_1 : CWE | None
        RMI.1 - Risk Management Incident Code (CWE) O S6.5.14.1 | 0427 - Risk Management Incident Code

    rmi_2 : str | None
        RMI.2 - Date/Time Incident (DTM) O S6.5.14.2

    rmi_3 : CWE | None
        RMI.3 - Incident Type Code (CWE) O S6.5.14.3 | 0428 - Incident Type Code
    """

    rmi_1: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rmi_1",
            "risk_management_incident_code",
            "RMI.1",
        ),
        serialization_alias="RMI.1",
        title="Risk Management Incident Code",
        description=(
            "O | Item #01530 | Table 0427 - Risk Management Incident Code"
        ),
    )

    rmi_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rmi_2",
            "date_time_incident",
            "RMI.2",
        ),
        serialization_alias="RMI.2",
        title="Date/Time Incident",
        description="O | Item #01531",
    )

    rmi_3: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rmi_3",
            "incident_type_code",
            "RMI.3",
        ),
        serialization_alias="RMI.3",
        title="Incident Type Code",
        description="O | Item #01533 | Table 0428 - Incident Type Code",
    )

    @field_validator("rmi_2", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        if _RE_DTM.fullmatch(v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = ConfigDict(populate_by_name=True)
