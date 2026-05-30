"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: NSC
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE
from ..datatypes.HD import HD


class NSC(HL7Model):
    """HL7 v2 NSC segment.

    Attributes
    ----------
    nsc_1 : CWE
        NSC.1 (req) - Application Change Type (CWE)

    nsc_2 : str | None
        NSC.2 (opt) - Current CPU (ST)

    nsc_3 : str | None
        NSC.3 (opt) - Current Fileserver (ST)

    nsc_4 : HD | None
        NSC.4 (opt) - Current Application (HD)

    nsc_5 : HD | None
        NSC.5 (opt) - Current Facility (HD)

    nsc_6 : str | None
        NSC.6 (opt) - New CPU (ST)

    nsc_7 : str | None
        NSC.7 (opt) - New Fileserver (ST)

    nsc_8 : HD | None
        NSC.8 (opt) - New Application (HD)

    nsc_9 : HD | None
        NSC.9 (opt) - New Facility (HD)
    """

    nsc_1: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "nsc_1",
            "application_change_type",
            "NSC.1",
        ),
        serialization_alias="NSC.1",
        title="Application Change Type",
        description="Item #1188 | Table HL70409",
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
        description="Item #1189",
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
        description="Item #1190",
    )

    nsc_4: Optional[HD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nsc_4",
            "current_application",
            "NSC.4",
        ),
        serialization_alias="NSC.4",
        title="Current Application",
        description="Item #1191 | Table HL70361",
    )

    nsc_5: Optional[HD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nsc_5",
            "current_facility",
            "NSC.5",
        ),
        serialization_alias="NSC.5",
        title="Current Facility",
        description="Item #1192 | Table HL70362",
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
        description="Item #1193",
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
        description="Item #1194",
    )

    nsc_8: Optional[HD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nsc_8",
            "new_application",
            "NSC.8",
        ),
        serialization_alias="NSC.8",
        title="New Application",
        description="Item #1195 | Table HL70361",
    )

    nsc_9: Optional[HD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nsc_9",
            "new_facility",
            "NSC.9",
        ),
        serialization_alias="NSC.9",
        title="New Facility",
        description="Item #1196 | Table HL70362",
    )

    model_config = {"populate_by_name": True}
