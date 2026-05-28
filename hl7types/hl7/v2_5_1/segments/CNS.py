"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: CNS
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE
from ..datatypes.TS import TS


class CNS(BaseModel):
    """HL7 v2 CNS segment."""

    cns_1: str | None = Field(
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

    cns_2: str | None = Field(
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

    cns_3: TS | None = Field(
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

    cns_4: TS | None = Field(
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

    cns_5: CE | None = Field(
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

    cns_6: CE | None = Field(
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

    model_config = {"populate_by_name": True}
