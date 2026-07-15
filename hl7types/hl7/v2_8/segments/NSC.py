"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
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
    """Application Status Change (S14.4.2).

    Attributes
    ----------
    nsc_1 : CWE
        NSC.1 - Application Change Type (CWE) R S14.4.2.1 | 0409 - Application Change Type

    nsc_2 : str | None
        NSC.2 - Current CPU (ST) O S14.4.2.2

    nsc_3 : str | None
        NSC.3 - Current Fileserver (ST) O S14.4.2.3

    nsc_4 : HD | None
        NSC.4 - Current Application (HD) O S14.4.2.4 | 0361 - Application

    nsc_5 : HD | None
        NSC.5 - Current Facility (HD) O S14.4.2.5 | 0362 - Facility

    nsc_6 : str | None
        NSC.6 - New CPU (ST) O S14.4.2.6

    nsc_7 : str | None
        NSC.7 - New Fileserver (ST) O S14.4.2.7

    nsc_8 : HD | None
        NSC.8 - New Application (HD) O S14.4.2.8 | 0361 - Application

    nsc_9 : HD | None
        NSC.9 - New Facility (HD) O S14.4.2.9 | 0362 - Facility
    """

    nsc_1: CWE = Field(
        validation_alias=AliasChoices(
            "nsc_1",
            "application_change_type",
            "NSC.1",
        ),
        serialization_alias="NSC.1",
        title="Application Change Type",
        description="R | Item #01188 | Table 0409 - Application Change Type",
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
        description="O | Item #01189",
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
        description="O | Item #01190",
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
        description="O | Item #01191 | Table 0361 - Application",
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
        description="O | Item #01192 | Table 0362 - Facility",
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
        description="O | Item #01193",
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
        description="O | Item #01194",
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
        description="O | Item #01195 | Table 0361 - Application",
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
        description="O | Item #01196 | Table 0362 - Facility",
    )

    model_config = {"populate_by_name": True}
