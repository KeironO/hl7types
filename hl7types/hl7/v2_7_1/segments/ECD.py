"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: ECD
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE

_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class ECD(HL7Model):
    """Equipment Command (S13.4.5).

    Attributes
    ----------
    ecd_1 : str
        ECD.1 - Reference Command Number (NM) R S13.4.5.1

    ecd_2 : CWE
        ECD.2 - Remote Control Command (CWE) R S13.4.5.2 | 0368 - Remote Control Command

    ecd_3 : str | None
        ECD.3 - Response Required (ID) O S13.4.5.3 | 0136 - Yes/no Indicator

    ecd_5 : list[str] | None
        ECD.5 - Parameters (TX) O rep S13.4.5.5
    """

    ecd_1: str = Field(
        validation_alias=AliasChoices(
            "ecd_1",
            "reference_command_number",
            "ECD.1",
        ),
        serialization_alias="ECD.1",
        title="Reference Command Number",
        description="R | Item #01390",
    )

    ecd_2: CWE = Field(
        validation_alias=AliasChoices(
            "ecd_2",
            "remote_control_command",
            "ECD.2",
        ),
        serialization_alias="ECD.2",
        title="Remote Control Command",
        description="R | Item #01391 | Table 0368 - Remote Control Command",
    )

    ecd_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ecd_3",
            "response_required",
            "ECD.3",
        ),
        serialization_alias="ECD.3",
        title="Response Required",
        description="O | Item #01392 | Table 0136 - Yes/no Indicator | LEN:1",
    )

    ecd_5: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ecd_5",
            "parameters",
            "ECD.5",
        ),
        serialization_alias="ECD.5",
        title="Parameters",
        description="O | Item #01394",
    )

    @field_validator("ecd_1", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
