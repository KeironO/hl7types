"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: RMI
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.TS import TS


class RMI(HL7Model):
    """Risk Management Incident (S6.5.14).

    Attributes
    ----------
    rmi_1 : CE | None
        RMI.1 - Risk Management Incident Code (CE) O S6.5.14.1 | 0427 - Risk Management Incident Code

    rmi_2 : TS | None
        RMI.2 - Date/Time Incident (TS) O S6.5.14.2

    rmi_3 : CE | None
        RMI.3 - Incident Type Code (CE) O S6.5.14.3 | 0428 - Incident Type Code
    """

    rmi_1: Optional[CE] = Field(
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

    rmi_2: Optional[TS] = Field(
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

    rmi_3: Optional[CE] = Field(
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

    model_config = {"populate_by_name": True}
