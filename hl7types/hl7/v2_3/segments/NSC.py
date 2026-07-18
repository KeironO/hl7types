"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: NSC
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field
from hl7types.hl7 import HL7Model


class NSC(HL7Model):
    """STATUS CHANGE (SC.2.3).

    Attributes
    ----------
    nsc_1 : str | None
        NSC.1 - Network Change Type (ID) NA SC.2.3.1

    nsc_2 : str | None
        NSC.2 - Current CPU (ST) NA SC.2.3.2

    nsc_3 : str | None
        NSC.3 - Current Fileserver (ST) NA SC.2.3.3

    nsc_4 : str | None
        NSC.4 - Current Application (ST) NA SC.2.3.4

    nsc_5 : str | None
        NSC.5 - Current Facility (ST) NA SC.2.3.5

    nsc_6 : str | None
        NSC.6 - New CPU (ST) C SC.2.3.6 | 0206 - Segment Action Code

    nsc_7 : str | None
        NSC.7 - New Fileserver (ST) NA SC.2.3.7

    nsc_8 : str | None
        NSC.8 - New Application (ST) NA SC.2.3.8
    """

    nsc_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nsc_1",
            "network_change_type",
            "NSC.1",
        ),
        serialization_alias="NSC.1",
        title="Network Change Type",
        description="NA | Item #01188 | LEN:4",
    )

    nsc_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nsc_2",
            "current_cpu",
            "NSC.2",
        ),
        serialization_alias="NSC.2",
        title="Current CPU",
        description="NA | Item #01189 | LEN:30",
    )

    nsc_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nsc_3",
            "current_fileserver",
            "NSC.3",
        ),
        serialization_alias="NSC.3",
        title="Current Fileserver",
        description="NA | Item #01190 | LEN:30",
    )

    nsc_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nsc_4",
            "current_application",
            "NSC.4",
        ),
        serialization_alias="NSC.4",
        title="Current Application",
        description="NA | Item #01191 | LEN:30",
    )

    nsc_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nsc_5",
            "current_facility",
            "NSC.5",
        ),
        serialization_alias="NSC.5",
        title="Current Facility",
        description="NA | Item #01192 | LEN:30",
    )

    nsc_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nsc_6",
            "new_cpu",
            "NSC.6",
        ),
        serialization_alias="NSC.6",
        title="New CPU",
        description=(
            "C | Item #01193 | Table 0206 - Segment Action Code | LEN:30"
        ),
    )

    nsc_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nsc_7",
            "new_fileserver",
            "NSC.7",
        ),
        serialization_alias="NSC.7",
        title="New Fileserver",
        description="NA | Item #01194 | LEN:30",
    )

    nsc_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nsc_8",
            "new_application",
            "NSC.8",
        ),
        serialization_alias="NSC.8",
        title="New Application",
        description="NA | Item #01195 | LEN:30",
    )

    model_config = ConfigDict(populate_by_name=True)
