"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: DSP
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model


class DSP(HL7Model):
    """HL7 v2 DSP segment.

    Attributes
    ----------
    dsp_1 : str | None
        DSP.1 (opt) - SET ID - DISPLAY DATA (SI)

    dsp_2 : str | None
        DSP.2 (opt) - DISPLAY LEVEL (SI)

    dsp_3 : str
        DSP.3 (req) - DATA LINE (TX)

    dsp_4 : str | None
        DSP.4 (opt) - LOGICAL BREAK POINT (ST)

    dsp_5 : str | None
        DSP.5 (opt) - RESULT ID (TX)
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
        description="Item #570",
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
        description="Item #571",
    )

    dsp_3: str = Field(
        validation_alias=AliasChoices(
            "dsp_3",
            "data_line",
            "DSP.3",
        ),
        serialization_alias="DSP.3",
        title="DATA LINE",
        description="Item #153",
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
        description="Item #154",
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
        description="Item #599",
    )

    @field_validator("dsp_1", "dsp_2", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    model_config = {"populate_by_name": True}
