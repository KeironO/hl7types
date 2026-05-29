"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: RMI
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CWE import CWE


class RMI(BaseModel):
    """HL7 v2 RMI segment.

    Attributes
    ----------
    rmi_1 : CWE | None
        RMI.1 (opt) - Risk Management Incident Code (CWE)

    rmi_2 : str | None
        RMI.2 (opt) - Date/Time Incident (DTM)

    rmi_3 : CWE | None
        RMI.3 (opt) - Incident Type Code (CWE)
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
        description="Item #1530 | Table HL70427",
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
        description="Item #1531",
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
        description="Item #1533 | Table HL70428",
    )

    model_config = {"populate_by_name": True}
