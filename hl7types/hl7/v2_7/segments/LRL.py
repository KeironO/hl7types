"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: LRL
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CWE import CWE
from ..datatypes.EI import EI
from ..datatypes.PL import PL
from ..datatypes.XON import XON


class LRL(BaseModel):
    """HL7 v2 LRL segment."""

    lrl_1: PL = Field(
        default=...,
        validation_alias=AliasChoices(
            "lrl_1",
            "primary_key_value_lrl",
            "LRL.1",
        ),
        serialization_alias="LRL.1",
        title="Primary Key Value - LRL",
        description="Item #943",
    )

    lrl_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "lrl_2",
            "segment_action_code",
            "LRL.2",
        ),
        serialization_alias="LRL.2",
        title="Segment Action Code",
        description="Item #763 | Table HL70206",
    )

    lrl_3: EI | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "lrl_3",
            "segment_unique_key",
            "LRL.3",
        ),
        serialization_alias="LRL.3",
        title="Segment Unique Key",
        description="Item #764",
    )

    lrl_4: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "lrl_4",
            "location_relationship_id",
            "LRL.4",
        ),
        serialization_alias="LRL.4",
        title="Location Relationship ID",
        description="Item #1277 | Table HL70325",
    )

    lrl_5: list[XON] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "lrl_5",
            "organizational_location_relationship_value",
            "LRL.5",
        ),
        serialization_alias="LRL.5",
        title="Organizational Location Relationship Value",
        description="Item #1301",
    )

    lrl_6: PL | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "lrl_6",
            "patient_location_relationship_value",
            "LRL.6",
        ),
        serialization_alias="LRL.6",
        title="Patient Location Relationship Value",
        description="Item #1292",
    )

    model_config = {"populate_by_name": True}
