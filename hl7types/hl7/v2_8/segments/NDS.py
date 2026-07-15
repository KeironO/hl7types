"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: NDS
Type: Segment
"""
from __future__ import annotations

from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE


class NDS(HL7Model):
    """Notification Detail (S13.4.7).

    Attributes
    ----------
    nds_1 : str
        NDS.1 - Notification Reference Number (NM) R S13.4.7.1

    nds_2 : str
        NDS.2 - Notification Date/Time (DTM) R S13.4.7.2

    nds_3 : CWE
        NDS.3 - Notification Alert Severity (CWE) R S13.4.7.3 | 0367 - Alert Level

    nds_4 : CWE
        NDS.4 - Notification Code (CWE) R S13.4.7.4 | 9999 - no table for CE
    """

    nds_1: str = Field(
        validation_alias=AliasChoices(
            "nds_1",
            "notification_reference_number",
            "NDS.1",
        ),
        serialization_alias="NDS.1",
        title="Notification Reference Number",
        description="R | Item #01398",
    )

    nds_2: str = Field(
        validation_alias=AliasChoices(
            "nds_2",
            "notification_date_time",
            "NDS.2",
        ),
        serialization_alias="NDS.2",
        title="Notification Date/Time",
        description="R | Item #01399",
    )

    nds_3: CWE = Field(
        validation_alias=AliasChoices(
            "nds_3",
            "notification_alert_severity",
            "NDS.3",
        ),
        serialization_alias="NDS.3",
        title="Notification Alert Severity",
        description="R | Item #01400 | Table 0367 - Alert Level",
    )

    nds_4: CWE = Field(
        validation_alias=AliasChoices(
            "nds_4",
            "notification_code",
            "NDS.4",
        ),
        serialization_alias="NDS.4",
        title="Notification Code",
        description="R | Item #01401 | Table 9999 - no table for CE",
    )

    @field_validator("nds_1", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    @field_validator("nds_2", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        import re
        if re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = {"populate_by_name": True}
