"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: CM_DLD
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from .TS import TS


class CM_DLD(HL7Model):
    """HL7 v2 CM_DLD data type.

    Attributes
    ----------
    cm_dld_1 : str | None
        CM_DLD.1 (opt) - discharge location (ID)

    cm_dld_2 : TS | None
        CM_DLD.2 (opt) - effective date (TS)
    """

    cm_dld_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_dld_1",
            "discharge_location",
            "CM_DLD.1",
        ),
        serialization_alias="CM_DLD.1",
        title="discharge location",
    )

    cm_dld_2: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_dld_2",
            "effective_date",
            "CM_DLD.2",
        ),
        serialization_alias="CM_DLD.2",
        title="effective date",
    )

    model_config = {"populate_by_name": True}
