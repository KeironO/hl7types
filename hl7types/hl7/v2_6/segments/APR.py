"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: APR
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator

from ..datatypes.SCV import SCV


class APR(HL7Model):
    """HL7 v2 APR segment.

    Attributes
    ----------
    apr_1 : list[SCV] | None
        APR.1 (opt, rep) - Time Selection Criteria (SCV)

    apr_2 : list[SCV] | None
        APR.2 (opt, rep) - Resource Selection Criteria (SCV)

    apr_3 : list[SCV] | None
        APR.3 (opt, rep) - Location Selection Criteria (SCV)

    apr_4 : str | None
        APR.4 (opt) - Slot Spacing Criteria (NM)

    apr_5 : list[SCV] | None
        APR.5 (opt, rep) - Filler Override Criteria (SCV)
    """

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

    @field_validator("apr_4", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
