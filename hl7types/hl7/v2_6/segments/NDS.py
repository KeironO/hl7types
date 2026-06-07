"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: NDS
Type: Segment
"""
from __future__ import annotations

from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE


class NDS(HL7Model):
    """HL7 v2 NDS segment.

    Attributes
    ----------
    nds_1 : str
        NDS.1 (req) - Notification Reference Number (NM)

    nds_2 : str
        NDS.2 (req) - Notification Date/Time (DTM)

    nds_3 : CWE
        NDS.3 (req) - Notification Alert Severity (CWE)

    nds_4 : CWE
        NDS.4 (req) - Notification Code (CWE)
    """

    nds_1: str = Field(
        validation_alias=AliasChoices(
            "nds_1",
            "notification_reference_number",
            "NDS.1",
        ),
        serialization_alias="NDS.1",
        title="Notification Reference Number",
        description="Item #1398",
    )

    nds_2: str = Field(
        validation_alias=AliasChoices(
            "nds_2",
            "notification_date_time",
            "NDS.2",
        ),
        serialization_alias="NDS.2",
        title="Notification Date/Time",
        description="Item #1399",
    )

    nds_3: CWE = Field(
        validation_alias=AliasChoices(
            "nds_3",
            "notification_alert_severity",
            "NDS.3",
        ),
        serialization_alias="NDS.3",
        title="Notification Alert Severity",
        description="Item #1400 | Table HL70367",
    )

    nds_4: CWE = Field(
        validation_alias=AliasChoices(
            "nds_4",
            "notification_code",
            "NDS.4",
        ),
        serialization_alias="NDS.4",
        title="Notification Code",
        description="Item #1401 | Table HL79999",
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
    def _validate_dtm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 datetime")
        return v

    model_config = {"populate_by_name": True}
