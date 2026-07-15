"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: ECD
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.TQ import TQ


class ECD(HL7Model):
    """Equipment Command (S13.4.5).

    Attributes
    ----------
    ecd_1 : str
        ECD.1 - Reference Command Number (NM) R S13.4.5.1

    ecd_2 : CE
        ECD.2 - Remote Control Command (CE) R S13.4.5.2 | 0368 - Remote control command

    ecd_3 : str | None
        ECD.3 - Response Required (ID) O S13.4.5.3 | 0136 - Yes/no indicator

    ecd_4 : TQ | None
        ECD.4 - Requested Completion Time (TQ) O S13.4.5.4

    ecd_5 : list[str] | None
        ECD.5 - Parameters (ST) O rep S13.4.5.5
    """

    ecd_1: str = Field(
        validation_alias=AliasChoices(
            "ecd_1",
            "reference_command_number",
            "ECD.1",
        ),
        serialization_alias="ECD.1",
        title="Reference Command Number",
        description="R | Item #01390 | LEN:20",
    )

    ecd_2: CE = Field(
        validation_alias=AliasChoices(
            "ecd_2",
            "remote_control_command",
            "ECD.2",
        ),
        serialization_alias="ECD.2",
        title="Remote Control Command",
        description="R | Item #01391 | Table 0368 - Remote control command",
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
        description="O | Item #01392 | Table 0136 - Yes/no indicator | LEN:80",
    )

    ecd_4: Optional[TQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ecd_4",
            "requested_completion_time",
            "ECD.4",
        ),
        serialization_alias="ECD.4",
        title="Requested Completion Time",
        description="O | Item #01393",
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
        description="O | Item #01394 | LEN:65536",
    )

    @field_validator("ecd_1", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
