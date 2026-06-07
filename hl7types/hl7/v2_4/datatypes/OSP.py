"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: OSP
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from .CE import CE


class OSP(HL7Model):
    """HL7 v2 OSP data type.

    Attributes
    ----------
    osp_1 : CE | None
        OSP.1 (opt) - occurrence span code (CE)

    osp_2 : str | None
        OSP.2 (opt) - occurrence span start date (DT)

    osp_3 : str | None
        OSP.3 (opt) - occurrence span stop date (DT)
    """

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

    @field_validator("osp_2", "osp_3", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2})?)?)?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    model_config = {"populate_by_name": True}
