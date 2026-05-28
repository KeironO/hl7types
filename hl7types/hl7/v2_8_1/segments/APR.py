"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: APR
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.SCV import SCV


class APR(BaseModel):
    """HL7 v2 APR segment."""

    apr_1: Optional[List[SCV]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "apr_1",
            "time_selection_criteria",
            "APR.1",
        ),
        serialization_alias="APR.1",
        title="Time Selection Criteria",
        description="Item #908 | Table HL70294",
    )

    apr_2: Optional[List[SCV]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "apr_2",
            "resource_selection_criteria",
            "APR.2",
        ),
        serialization_alias="APR.2",
        title="Resource Selection Criteria",
        description="Item #909 | Table HL70294",
    )

    apr_3: Optional[List[SCV]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "apr_3",
            "location_selection_criteria",
            "APR.3",
        ),
        serialization_alias="APR.3",
        title="Location Selection Criteria",
        description="Item #910 | Table HL70294",
    )

    apr_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "apr_4",
            "slot_spacing_criteria",
            "APR.4",
        ),
        serialization_alias="APR.4",
        title="Slot Spacing Criteria",
        description="Item #911",
    )

    apr_5: Optional[List[SCV]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "apr_5",
            "filler_override_criteria",
            "APR.5",
        ),
        serialization_alias="APR.5",
        title="Filler Override Criteria",
        description="Item #912",
    )

    model_config = {"populate_by_name": True}
