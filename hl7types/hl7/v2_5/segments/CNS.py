"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: CNS
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.TS import TS


class CNS(HL7Model):
    """Clear Notification (S13.4.8).

    Attributes
    ----------
    cns_1 : str | None
        CNS.1 (opt) - Starting Notification Reference Number (NM) S13.4.8.1

    cns_2 : str | None
        CNS.2 (opt) - Ending Notification Reference Number (NM) S13.4.8.2

    cns_3 : TS | None
        CNS.3 (opt) - Starting Notification Date/Time (TS) S13.4.8.3

    cns_4 : TS | None
        CNS.4 (opt) - Ending Notification Date/Time (TS) S13.4.8.4

    cns_5 : CE | None
        CNS.5 (opt) - Starting Notification Code (CE) S13.4.8.5

    cns_6 : CE | None
        CNS.6 (opt) - Ending Notification Code (CE) S13.4.8.6
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
        description="Item #1402",
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
        description="Item #1403",
    )

    cns_3: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cns_3",
            "starting_notification_date_time",
            "CNS.3",
        ),
        serialization_alias="CNS.3",
        title="Starting Notification Date/Time",
        description="Item #1404",
    )

    cns_4: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cns_4",
            "ending_notification_date_time",
            "CNS.4",
        ),
        serialization_alias="CNS.4",
        title="Ending Notification Date/Time",
        description="Item #1405",
    )

    cns_5: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cns_5",
            "starting_notification_code",
            "CNS.5",
        ),
        serialization_alias="CNS.5",
        title="Starting Notification Code",
        description="Item #1406",
    )

    cns_6: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cns_6",
            "ending_notification_code",
            "CNS.6",
        ),
        serialization_alias="CNS.6",
        title="Ending Notification Code",
        description="Item #1407",
    )

    @field_validator("cns_1", "cns_2", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
