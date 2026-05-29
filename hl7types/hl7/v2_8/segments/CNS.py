"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: CNS
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CWE import CWE


class CNS(BaseModel):
    """HL7 v2 CNS segment.

    Attributes
    ----------
    cns_1 : str | None
        CNS.1 (opt) - Starting Notification Reference Number (NM)

    cns_2 : str | None
        CNS.2 (opt) - Ending Notification Reference Number (NM)

    cns_3 : str | None
        CNS.3 (opt) - Starting Notification Date/Time (DTM)

    cns_4 : str | None
        CNS.4 (opt) - Ending Notification Date/Time (DTM)

    cns_5 : CWE | None
        CNS.5 (opt) - Starting Notification Code (CWE)

    cns_6 : CWE | None
        CNS.6 (opt) - Ending Notification Code (CWE)
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

    cns_3: Optional[str] = Field(
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

    cns_4: Optional[str] = Field(
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

    cns_5: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cns_5",
            "starting_notification_code",
            "CNS.5",
        ),
        serialization_alias="CNS.5",
        title="Starting Notification Code",
        description="Item #1406 | Table HL79999",
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
        description="Item #1407 | Table HL79999",
    )

    model_config = {"populate_by_name": True}
