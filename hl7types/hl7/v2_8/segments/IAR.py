"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: IAR
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CWE import CWE


class IAR(BaseModel):
    """HL7 v2 IAR segment."""

    iar_1: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "iar_1",
            "allergy_reaction_code",
            "IAR.1",
        ),
        serialization_alias="IAR.1",
        title="Allergy Reaction Code",
        description="Item #3296",
    )

    iar_2: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "iar_2",
            "allergy_severity_code",
            "IAR.2",
        ),
        serialization_alias="IAR.2",
        title="Allergy Severity Code",
        description="Item #3297 | Table HL70128",
    )

    iar_3: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "iar_3",
            "sensitivity_to_causative_agent_code",
            "IAR.3",
        ),
        serialization_alias="IAR.3",
        title="Sensitivity to Causative Agent Code",
        description="Item #3298 | Table HL70436",
    )

    iar_4: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "iar_4",
            "management",
            "IAR.4",
        ),
        serialization_alias="IAR.4",
        title="Management",
        description="Item #3299",
    )

    model_config = {"populate_by_name": True}
