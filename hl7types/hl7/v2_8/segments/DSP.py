"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: DSP
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.TX import TX


class DSP(HL7Model):
    """HL7 v2 DSP segment.

    Attributes
    ----------
    dsp_1 : str | None
        DSP.1 (opt) - Set ID - DSP (SI)

    dsp_2 : str | None
        DSP.2 (opt) - Display Level (SI)

    dsp_3 : TX
        DSP.3 (req) - Data Line (TX)

    dsp_4 : str | None
        DSP.4 (opt) - Logical Break Point (ST)

    dsp_5 : TX | None
        DSP.5 (opt) - Result ID (TX)
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
