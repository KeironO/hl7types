"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: CM_DTN
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class CM_DTN(BaseModel):
    """HL7 v2 CM_DTN data type.

    Attributes
    ----------
    cm_dtn_1 : str | None
        CM_DTN.1 (opt) - day type (ID)

    cm_dtn_2 : str | None
        CM_DTN.2 (opt) - number of days (NM)
    """

    cm_dtn_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_dtn_1",
            "day_type",
            "CM_DTN.1",
        ),
        serialization_alias="CM_DTN.1",
        title="day type",
    )

    cm_dtn_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_dtn_2",
            "number_of_days",
            "CM_DTN.2",
        ),
        serialization_alias="CM_DTN.2",
        title="number of days",
    )

    model_config = {"populate_by_name": True}
