"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: CM_SPD
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model


class CM_SPD(HL7Model):
    """HL7 v2 CM_SPD data type.

    Attributes
    ----------
    cm_spd_1 : str | None
        CM_SPD.1 (opt) - specialty name (ST)

    cm_spd_2 : str | None
        CM_SPD.2 (opt) - governing board (ST)

    cm_spd_3 : str | None
        CM_SPD.3 (opt) - eligible or certified (ID)

    cm_spd_4 : str | None
        CM_SPD.4 (opt) - date of certification (DT)
    """

    cm_spd_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_spd_1",
            "specialty_name",
            "CM_SPD.1",
        ),
        serialization_alias="CM_SPD.1",
        title="specialty name",
    )

    cm_spd_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_spd_2",
            "governing_board",
            "CM_SPD.2",
        ),
        serialization_alias="CM_SPD.2",
        title="governing board",
    )

    cm_spd_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_spd_3",
            "eligible_or_certified",
            "CM_SPD.3",
        ),
        serialization_alias="CM_SPD.3",
        title="eligible or certified",
    )

    cm_spd_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_spd_4",
            "date_of_certification",
            "CM_SPD.4",
        ),
        serialization_alias="CM_SPD.4",
        title="date of certification",
    )

    model_config = {"populate_by_name": True}
