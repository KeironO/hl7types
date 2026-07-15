"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: NSC
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model


class NSC(HL7Model):
    """Application status change (SC.2.3.10).

    Attributes
    ----------
    nsc_1 : str | None
        NSC.1 - Network Change Type (IS) NA SC.2.3.1 | 0333 - Driver’s license issuing authority

    nsc_2 : str | None
        NSC.2 - Current CPU (ST) NA SC.2.3.2

    nsc_3 : str | None
        NSC.3 - Current Fileserver (ST) NA SC.2.3.3

    nsc_4 : str | None
        NSC.4 - Current Application (ST) NA SC.2.3.4

    nsc_5 : str | None
        NSC.5 - Current Facility (ST) NA SC.2.3.5

    nsc_6 : str | None
        NSC.6 - New CPU (ST) NA SC.2.3.6

    nsc_7 : str | None
        NSC.7 - New Fileserver (ST) NA SC.2.3.7

    nsc_8 : str | None
        NSC.8 - New Application (ST) NA SC.2.3.8

    nsc_9 : str | None
        NSC.9 - New Facility (ST) NA SC.2.3.9
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
        description=(
            "NA | Item #01188 | Table 0333 - Driver’s license issuing authority"
        ),
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
        description="NA | Item #01189",
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
        description="NA | Item #01190",
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
        description="NA | Item #01191",
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
        description="NA | Item #01192",
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
        description="NA | Item #01193",
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
        description="NA | Item #01194",
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
        description="NA | Item #01195",
    )

    nsc_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nsc_9",
            "new_facility",
            "NSC.9",
        ),
        serialization_alias="NSC.9",
        title="New Facility",
        description="NA | Item #01196",
    )

    model_config = {"populate_by_name": True}
