"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: ECD
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CWE import CWE
from ..datatypes.TX import TX


class ECD(BaseModel):
    """HL7 v2 ECD segment."""

    ecd_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "ecd_1",
            "reference_command_number",
            "ECD.1",
        ),
        serialization_alias="ECD.1",
        title="Reference Command Number",
        description="Item #1390",
    )

    ecd_2: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "ecd_2",
            "remote_control_command",
            "ECD.2",
        ),
        serialization_alias="ECD.2",
        title="Remote Control Command",
        description="Item #1391 | Table HL70368",
    )

    ecd_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ecd_3",
            "response_required",
            "ECD.3",
        ),
        serialization_alias="ECD.3",
        title="Response Required",
        description="Item #1392 | Table HL70136",
    )

    ecd_5: list[TX] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ecd_5",
            "parameters",
            "ECD.5",
        ),
        serialization_alias="ECD.5",
        title="Parameters",
        description="Item #1394",
    )

    model_config = {"populate_by_name": True}
