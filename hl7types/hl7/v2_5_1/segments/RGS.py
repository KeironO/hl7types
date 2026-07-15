"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: RGS
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE


class RGS(HL7Model):
    """Resource Group (S10.6.3).

    Attributes
    ----------
    rgs_1 : str
        RGS.1 - Set ID - RGS (SI) R S10.6.3.1

    rgs_2 : str | None
        RGS.2 - Segment Action Code (ID) C S10.6.3.2 | 0206 - Segment action code

    rgs_3 : CE | None
        RGS.3 - Resource Group ID (CE) O S10.6.3.3
    """

    rgs_1: str = Field(
        validation_alias=AliasChoices(
            "rgs_1",
            "set_id_rgs",
            "RGS.1",
        ),
        serialization_alias="RGS.1",
        title="Set ID - RGS",
        description="R | Item #01203 | LEN:4",
    )

    rgs_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rgs_2",
            "segment_action_code",
            "RGS.2",
        ),
        serialization_alias="RGS.2",
        title="Segment Action Code",
        description=(
            "C | Item #00763 | Table 0206 - Segment action code | LEN:3"
        ),
    )

    rgs_3: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rgs_3",
            "resource_group_id",
            "RGS.3",
        ),
        serialization_alias="RGS.3",
        title="Resource Group ID",
        description="O | Item #01204",
    )

    @field_validator("rgs_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    model_config = {"populate_by_name": True}
