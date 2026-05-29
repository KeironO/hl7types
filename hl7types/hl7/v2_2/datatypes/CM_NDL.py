"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: CM_NDL
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from .TS import TS


class CM_NDL(BaseModel):
    """HL7 v2 CM_NDL data type.

    Attributes
    ----------
    cm_ndl_1 : str | None
        CM_NDL.1 (opt) - interpreter / technician (CN)

    cm_ndl_2 : TS | None
        CM_NDL.2 (opt) - start date/time (TS)

    cm_ndl_3 : TS | None
        CM_NDL.3 (opt) - end date/time (TS)

    cm_ndl_4 : str | None
        CM_NDL.4 (opt) - location (CM)
    """

    cm_ndl_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_ndl_1",
            "interpreter_technician",
            "CM_NDL.1",
        ),
        serialization_alias="CM_NDL.1",
        title="interpreter / technician",
    )

    cm_ndl_2: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_ndl_2",
            "start_date_time",
            "CM_NDL.2",
        ),
        serialization_alias="CM_NDL.2",
        title="start date/time",
    )

    cm_ndl_3: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_ndl_3",
            "end_date_time",
            "CM_NDL.3",
        ),
        serialization_alias="CM_NDL.3",
        title="end date/time",
    )

    cm_ndl_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_ndl_4",
            "location",
            "CM_NDL.4",
        ),
        serialization_alias="CM_NDL.4",
        title="location",
    )

    model_config = {"populate_by_name": True}
