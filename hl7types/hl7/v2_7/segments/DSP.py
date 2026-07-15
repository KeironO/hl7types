"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: DSP
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model


class DSP(HL7Model):
    """Display Data (S5.5.1).

    Attributes
    ----------
    dsp_1 : str | None
        DSP.1 - Set ID - DSP (SI) O S5.5.1.1

    dsp_2 : str | None
        DSP.2 - Display Level (SI) O S5.5.1.2

    dsp_3 : str
        DSP.3 - Data Line (TX) R S5.5.1.3

    dsp_4 : str | None
        DSP.4 - Logical Break Point (ST) O S5.5.1.4

    dsp_5 : str | None
        DSP.5 - Result ID (TX) O S5.5.1.5
    """

    dsp_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dsp_1",
            "set_id_dsp",
            "DSP.1",
        ),
        serialization_alias="DSP.1",
        title="Set ID - DSP",
        description="O | Item #00061 | LEN:4",
    )

    dsp_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dsp_2",
            "display_level",
            "DSP.2",
        ),
        serialization_alias="DSP.2",
        title="Display Level",
        description="O | Item #00062 | LEN:4",
    )

    dsp_3: str = Field(
        validation_alias=AliasChoices(
            "dsp_3",
            "data_line",
            "DSP.3",
        ),
        serialization_alias="DSP.3",
        title="Data Line",
        description="R | Item #00063",
    )

    dsp_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dsp_4",
            "logical_break_point",
            "DSP.4",
        ),
        serialization_alias="DSP.4",
        title="Logical Break Point",
        description="O | Item #00064",
    )

    dsp_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dsp_5",
            "result_id",
            "DSP.5",
        ),
        serialization_alias="DSP.5",
        title="Result ID",
        description="O | Item #00065",
    )

    @field_validator("dsp_1", "dsp_2", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    model_config = {"populate_by_name": True}
