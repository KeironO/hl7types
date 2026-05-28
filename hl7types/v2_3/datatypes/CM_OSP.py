"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: CM_OSP
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from .CE import CE


class CM_OSP(BaseModel):
    """HL7 v2 CM_OSP data type."""

    cm_osp_1: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_osp_1",
            "occurrence_span_code",
            "CM_OSP.1",
        ),
        serialization_alias="CM_OSP.1",
        title="occurrence span code",
    )

    cm_osp_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_osp_2",
            "occurrence_span_start_date",
            "CM_OSP.2",
        ),
        serialization_alias="CM_OSP.2",
        title="occurrence span start date",
    )

    cm_osp_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_osp_3",
            "occurrence_span_stop_date",
            "CM_OSP.3",
        ),
        serialization_alias="CM_OSP.3",
        title="occurrence span stop date",
    )

    model_config = {"populate_by_name": True}
