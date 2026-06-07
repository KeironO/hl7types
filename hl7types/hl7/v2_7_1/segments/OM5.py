"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: OM5
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE


class OM5(HL7Model):
    """HL7 v2 OM5 segment.

    Attributes
    ----------
    om5_1 : str | None
        OM5.1 (opt) - Sequence Number - Test/Observation Master File (NM)

    om5_2 : list[CWE] | None
        OM5.2 (opt, rep) - Test/Observations Included Within an Ordered Test Battery (CWE)

    om5_3 : str | None
        OM5.3 (opt) - Observation ID Suffixes (ST)
    """

    om5_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om5_1",
            "sequence_number_test_observation_master_file",
            "OM5.1",
        ),
        serialization_alias="OM5.1",
        title="Sequence Number - Test/Observation Master File",
        description="Item #586",
    )

    om5_2: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om5_2",
            "test_observations_included_within_an_ordered_test_battery",
            "OM5.2",
        ),
        serialization_alias="OM5.2",
        title="Test/Observations Included Within an Ordered Test Battery",
        description="Item #655 | Table HL79999",
    )

    om5_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om5_3",
            "observation_id_suffixes",
            "OM5.3",
        ),
        serialization_alias="OM5.3",
        title="Observation ID Suffixes",
        description="Item #656",
    )

    @field_validator("om5_1", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
