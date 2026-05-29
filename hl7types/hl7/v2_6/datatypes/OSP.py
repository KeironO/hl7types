"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: OSP
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from .CNE import CNE


class OSP(BaseModel):
    """HL7 v2 OSP data type.

    Attributes
    ----------
    osp_1 : CNE
        OSP.1 (req) - Occurrence Span Code (CNE)

    osp_2 : str | None
        OSP.2 (opt) - Occurrence Span Start Date (DT)

    osp_3 : str | None
        OSP.3 (opt) - Occurrence Span Stop Date (DT)
    """

    osp_1: CNE = Field(
        default=...,
        validation_alias=AliasChoices(
            "osp_1",
            "occurrence_span_code",
            "OSP.1",
        ),
        serialization_alias="OSP.1",
        title="Occurrence Span Code",
    )

    osp_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "osp_2",
            "occurrence_span_start_date",
            "OSP.2",
        ),
        serialization_alias="OSP.2",
        title="Occurrence Span Start Date",
    )

    osp_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "osp_3",
            "occurrence_span_stop_date",
            "OSP.3",
        ),
        serialization_alias="OSP.3",
        title="Occurrence Span Stop Date",
    )

    model_config = {"populate_by_name": True}
