"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: APR
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.SCV import SCV

_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class APR(HL7Model):
    """APR - appointment preferences segment (S10.5.8).

    Attributes
    ----------
    apr_1 : list[SCV] | None
        APR.1 - Time Selection Criteria (SCV) O rep S10.5.8.1 | 0294 - Time selection criteria parameter class codes

    apr_2 : list[SCV] | None
        APR.2 - Resource Selection Criteria (SCV) O rep S10.5.8.2 | 0294 - Time selection criteria parameter class codes

    apr_3 : list[SCV] | None
        APR.3 - Location Selection Criteria (SCV) O rep S10.5.8.3 | 0294 - Time selection criteria parameter class codes

    apr_4 : str | None
        APR.4 - Slot Spacing Criteria (NM) O S10.5.8.4

    apr_5 : list[SCV] | None
        APR.5 - Filler Override Criteria (SCV) O rep S10.5.8.5
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
        description=(
            "O | Item #00908 | Table 0294 - Time selection criteria parameter "
            "class codes"
        ),
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
        description=(
            "O | Item #00909 | Table 0294 - Time selection criteria parameter "
            "class codes"
        ),
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
        description=(
            "O | Item #00910 | Table 0294 - Time selection criteria parameter "
            "class codes"
        ),
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
        description="O | Item #00911 | LEN:5",
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
        description="O | Item #00912",
    )

    @field_validator("apr_4", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
