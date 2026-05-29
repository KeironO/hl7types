"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: DLD
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from .TS import TS


class DLD(BaseModel):
    """HL7 v2 DLD data type.

    Attributes
    ----------
    dld_1 : str | None
        DLD.1 (opt) - discharge location (IS)

    dld_2 : TS | None
        DLD.2 (opt) - effective date (TS)
    """

    dld_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dld_1",
            "discharge_location",
            "DLD.1",
        ),
        serialization_alias="DLD.1",
        title="discharge location",
    )

    dld_2: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dld_2",
            "effective_date",
            "DLD.2",
        ),
        serialization_alias="DLD.2",
        title="effective date",
    )

    model_config = {"populate_by_name": True}
