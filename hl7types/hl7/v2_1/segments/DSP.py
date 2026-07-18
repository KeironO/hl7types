"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: DSP
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

_RE_SI = re.compile(r'\d*')


class DSP(HL7Model):
    """DISPLAY DATA (S5.3.2).

    Attributes
    ----------
    dsp_1 : str | None
        DSP.1 - SET ID - DISPLAY DATA (SI) O

    dsp_2 : str | None
        DSP.2 - DISPLAY LEVEL (SI) O

    dsp_3 : str
        DSP.3 - DATA LINE (TX) R

    dsp_4 : str | None
        DSP.4 - LOGICAL BREAK POINT (ST) O

    dsp_5 : str | None
        DSP.5 - RESULT ID (TX) O
    """

    dsp_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dsp_1",
            "set_id_display_data",
            "DSP.1",
        ),
        serialization_alias="DSP.1",
        title="SET ID - DISPLAY DATA",
        description="O | Item #00570 | LEN:4",
    )

    dsp_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dsp_2",
            "display_level",
            "DSP.2",
        ),
        serialization_alias="DSP.2",
        title="DISPLAY LEVEL",
        description="O | Item #00571 | LEN:4",
    )

    dsp_3: str = Field(
        validation_alias=AliasChoices(
            "dsp_3",
            "data_line",
            "DSP.3",
        ),
        serialization_alias="DSP.3",
        title="DATA LINE",
        description="R | Item #00153",
    )

    dsp_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dsp_4",
            "logical_break_point",
            "DSP.4",
        ),
        serialization_alias="DSP.4",
        title="LOGICAL BREAK POINT",
        description="O | Item #00154 | LEN:2",
    )

    dsp_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dsp_5",
            "result_id",
            "DSP.5",
        ),
        serialization_alias="DSP.5",
        title="RESULT ID",
        description="O | Item #00599",
    )

    @field_validator("dsp_1", "dsp_2", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        if not _RE_SI.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    model_config = ConfigDict(populate_by_name=True)
