"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: ECD
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator

from ..datatypes.CWE import CWE
from ..datatypes.TX import TX


class ECD(HL7Model):
    """HL7 v2 ECD segment.

    Attributes
    ----------
    ecd_1 : str
        ECD.1 (req) - Reference Command Number (NM)

    ecd_2 : CWE
        ECD.2 (req) - Remote Control Command (CWE)

    ecd_3 : str | None
        ECD.3 (opt) - Response Required (ID)

    ecd_5 : list[TX] | None
        ECD.5 (opt, rep) - Parameters (TX)
    """

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

    ecd_3: Optional[str] = Field(
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

    ecd_5: Optional[List[TX]] = Field(
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

    @field_validator("ecd_1", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
