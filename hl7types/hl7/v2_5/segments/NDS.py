"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: NDS
Type: Segment
"""
from __future__ import annotations

from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.TS import TS


class NDS(HL7Model):
    """Notification Detail (S13.4.7).

    Attributes
    ----------
    nds_1 : str
        NDS.1 - Notification Reference Number (NM) R S13.4.7.1

    nds_2 : TS
        NDS.2 - Notification Date/Time (TS) R S13.4.7.2

    nds_3 : CE
        NDS.3 - Notification Alert Severity (CE) R S13.4.7.3 | 0367 - Alert level

    nds_4 : CE
        NDS.4 - Notification Code (CE) R S13.4.7.4
    """

    nds_1: str = Field(
        validation_alias=AliasChoices(
            "nds_1",
            "notification_reference_number",
            "NDS.1",
        ),
        serialization_alias="NDS.1",
        title="Notification Reference Number",
        description="R | Item #01398 | LEN:20",
    )

    nds_2: TS = Field(
        validation_alias=AliasChoices(
            "nds_2",
            "notification_date_time",
            "NDS.2",
        ),
        serialization_alias="NDS.2",
        title="Notification Date/Time",
        description="R | Item #01399",
    )

    nds_3: CE = Field(
        validation_alias=AliasChoices(
            "nds_3",
            "notification_alert_severity",
            "NDS.3",
        ),
        serialization_alias="NDS.3",
        title="Notification Alert Severity",
        description="R | Item #01400 | Table 0367 - Alert level",
    )

    nds_4: CE = Field(
        validation_alias=AliasChoices(
            "nds_4",
            "notification_code",
            "NDS.4",
        ),
        serialization_alias="NDS.4",
        title="Notification Code",
        description="R | Item #01401",
    )

    @field_validator("nds_1", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
