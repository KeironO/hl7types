"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: CNS
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field, ValidationInfo, field_validator
from hl7types.hl7 import HL7Model
from hl7types.hl7._validators import _apply_dt_fallback

from ..datatypes.CWE import CWE

_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')
_RE_DTM = re.compile(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?')


class CNS(HL7Model):
    """Clear Notification (S13.4.8).

    Attributes
    ----------
    cns_1 : str | None
        CNS.1 - Starting Notification Reference Number (NM) O S13.4.8.1

    cns_2 : str | None
        CNS.2 - Ending Notification Reference Number (NM) O S13.4.8.2

    cns_3 : str | None
        CNS.3 - Starting Notification Date/Time (DTM) O S13.4.8.3

    cns_4 : str | None
        CNS.4 - Ending Notification Date/Time (DTM) O S13.4.8.4

    cns_5 : CWE | None
        CNS.5 - Starting Notification Code (CWE) O S13.4.8.5 | 9999 - no table for CE

    cns_6 : CWE | None
        CNS.6 - Ending Notification Code (CWE) O S13.4.8.6 | 9999 - no table for CE
    """

    cns_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cns_1",
            "starting_notification_reference_number",
            "CNS.1",
        ),
        serialization_alias="CNS.1",
        title="Starting Notification Reference Number",
        description="O | Item #01402",
    )

    cns_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cns_2",
            "ending_notification_reference_number",
            "CNS.2",
        ),
        serialization_alias="CNS.2",
        title="Ending Notification Reference Number",
        description="O | Item #01403",
    )

    cns_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cns_3",
            "starting_notification_date_time",
            "CNS.3",
        ),
        serialization_alias="CNS.3",
        title="Starting Notification Date/Time",
        description="O | Item #01404",
    )

    cns_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cns_4",
            "ending_notification_date_time",
            "CNS.4",
        ),
        serialization_alias="CNS.4",
        title="Ending Notification Date/Time",
        description="O | Item #01405",
    )

    cns_5: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cns_5",
            "starting_notification_code",
            "CNS.5",
        ),
        serialization_alias="CNS.5",
        title="Starting Notification Code",
        description="O | Item #01406 | Table 9999 - no table for CE",
    )

    cns_6: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cns_6",
            "ending_notification_code",
            "CNS.6",
        ),
        serialization_alias="CNS.6",
        title="Ending Notification Code",
        description="O | Item #01407 | Table 9999 - no table for CE",
    )

    @field_validator("cns_1", "cns_2", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    @field_validator("cns_3", "cns_4", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        if _RE_DTM.fullmatch(v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = ConfigDict(populate_by_name=True)
