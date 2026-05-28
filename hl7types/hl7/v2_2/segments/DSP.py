"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: DSP
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.TX import TX


class DSP(BaseModel):
    """HL7 v2 DSP segment."""

    dsp_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dsp_1",
            "set_id_display_data",
            "DSP.1",
        ),
        serialization_alias="DSP.1",
        title="Set ID - Display Data",
        description="Item #61",
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
        description="Item #62",
    )

    dsp_3: TX = Field(
        default=...,
        validation_alias=AliasChoices(
            "dsp_3",
            "data_line",
            "DSP.3",
        ),
        serialization_alias="DSP.3",
        title="Data Line",
        description="Item #63",
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
        description="Item #64",
    )

    dsp_5: Optional[TX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dsp_5",
            "result_id",
            "DSP.5",
        ),
        serialization_alias="DSP.5",
        title="Result ID",
        description="Item #65",
    )

    model_config = {"populate_by_name": True}
