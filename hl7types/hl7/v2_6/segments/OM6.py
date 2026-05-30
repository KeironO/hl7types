"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: OM6
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.TX import TX


class OM6(HL7Model):
    """HL7 v2 OM6 segment.

    Attributes
    ----------
    om6_1 : str | None
        OM6.1 (opt) - Sequence Number - Test/Observation Master File (NM)

    om6_2 : TX | None
        OM6.2 (opt) - Derivation Rule (TX)
    """

    om6_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om6_1",
            "sequence_number_test_observation_master_file",
            "OM6.1",
        ),
        serialization_alias="OM6.1",
        title="Sequence Number - Test/Observation Master File",
        description="Item #586",
    )

    om6_2: Optional[TX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om6_2",
            "derivation_rule",
            "OM6.2",
        ),
        serialization_alias="OM6.2",
        title="Derivation Rule",
        description="Item #657",
    )

    model_config = {"populate_by_name": True}
