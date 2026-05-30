"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: VH
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model


class VH(HL7Model):
    """HL7 v2 VH data type.

    Attributes
    ----------
    vh_1 : str | None
        VH.1 (opt) - Start Day Range (ID)

    vh_2 : str | None
        VH.2 (opt) - End Day Range (ID)

    vh_3 : str | None
        VH.3 (opt) - Start Hour Range (TM)

    vh_4 : str | None
        VH.4 (opt) - End Hour Range (TM)
    """

    vh_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "vh_1",
            "start_day_range",
            "VH.1",
        ),
        serialization_alias="VH.1",
        title="Start Day Range",
    )

    vh_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "vh_2",
            "end_day_range",
            "VH.2",
        ),
        serialization_alias="VH.2",
        title="End Day Range",
    )

    vh_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "vh_3",
            "start_hour_range",
            "VH.3",
        ),
        serialization_alias="VH.3",
        title="Start Hour Range",
    )

    vh_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "vh_4",
            "end_hour_range",
            "VH.4",
        ),
        serialization_alias="VH.4",
        title="End Hour Range",
    )

    model_config = {"populate_by_name": True}
