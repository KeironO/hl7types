"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: OCD
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from .CNE import CNE


class OCD(HL7Model):
    """HL7 v2 OCD data type.

    Attributes
    ----------
    ocd_1 : CNE | None
        OCD.1 (opt) - Occurrence Code (CNE)

    ocd_2 : str | None
        OCD.2 (opt) - Occurrence Date (DT)
    """

    ocd_1: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ocd_1",
            "occurrence_code",
            "OCD.1",
        ),
        serialization_alias="OCD.1",
        title="Occurrence Code",
    )

    ocd_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ocd_2",
            "occurrence_date",
            "OCD.2",
        ),
        serialization_alias="OCD.2",
        title="Occurrence Date",
    )

    model_config = {"populate_by_name": True}
