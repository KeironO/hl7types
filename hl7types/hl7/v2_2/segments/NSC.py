"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: NSC
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model


class NSC(HL7Model):
    """HL7 v2 NSC segment.

    Attributes
    ----------
    nsc_1 : str
        NSC.1 (req) - Network Change Type (ID)

    nsc_2 : str | None
        NSC.2 (opt) - Current CPU (ST)

    nsc_3 : str | None
        NSC.3 (opt) - Current Fileserver (ST)

    nsc_4 : str | None
        NSC.4 (opt) - Current Application (ST)

    nsc_5 : str | None
        NSC.5 (opt) - Current Facility (ST)

    nsc_6 : str | None
        NSC.6 (opt) - New CPU (ST)

    nsc_7 : str | None
        NSC.7 (opt) - New Fileserver (ST)

    nsc_8 : str | None
        NSC.8 (opt) - New Application (ST)

    nsc_9 : str | None
        NSC.9 (opt) - New Facility (ST)
    """

    nsc_1: str = Field(
        validation_alias=AliasChoices(
            "nsc_1",
            "network_change_type",
            "NSC.1",
        ),
        serialization_alias="NSC.1",
        title="Network Change Type",
        description="Item #758",
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
        description="Item #759",
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
        description="Item #760",
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
        description="Item #761",
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
        description="Item #762",
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
        description="Item #763",
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
        description="Item #764",
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
        description="Item #765",
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
        description="Item #766",
    )

    model_config = {"populate_by_name": True}
