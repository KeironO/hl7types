"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: OSP
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from .CE import CE


class OSP(BaseModel):
    """HL7 v2 OSP data type."""

    osp_1: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "osp_1",
            "occurrence_span_code",
            "OSP.1",
        ),
        serialization_alias="OSP.1",
        title="occurrence span code",
    )

    osp_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "osp_2",
            "occurrence_span_start_date",
            "OSP.2",
        ),
        serialization_alias="OSP.2",
        title="occurrence span start date",
    )

    osp_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "osp_3",
            "occurrence_span_stop_date",
            "OSP.3",
        ),
        serialization_alias="OSP.3",
        title="occurrence span stop date",
    )

    model_config = {"populate_by_name": True}
