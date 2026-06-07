"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: CM_OSP
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model


class CM_OSP(HL7Model):
    """HL7 v2 CM_OSP data type.

    Attributes
    ----------
    cm_osp_1 : str | None
        CM_OSP.1 (opt) - occurrence span code (ID)

    cm_osp_2 : str | None
        CM_OSP.2 (opt) - occurrence span start date (DT)

    cm_osp_3 : str | None
        CM_OSP.3 (opt) - occurrence span stop date (DT)
    """

    cm_osp_1: Optional[str] = Field(
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

    @field_validator("cm_osp_2", "cm_osp_3", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2})?)?)?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    model_config = {"populate_by_name": True}
