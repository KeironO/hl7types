"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: RP
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from .HD import HD


class RP(BaseModel):
    """HL7 v2 RP data type.

    Attributes
    ----------
    rp_1 : str | None
        RP.1 (opt) - pointer (ST)

    rp_2 : HD | None
        RP.2 (opt) - application ID (HD)

    rp_3 : str | None
        RP.3 (opt) - type of data (ID)

    rp_4 : str | None
        RP.4 (opt) - subtype (ID)
    """

    rp_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rp_1",
            "pointer",
            "RP.1",
        ),
        serialization_alias="RP.1",
        title="pointer",
    )

    rp_2: Optional[HD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rp_2",
            "application_id",
            "RP.2",
        ),
        serialization_alias="RP.2",
        title="application ID",
    )

    rp_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rp_3",
            "type_of_data",
            "RP.3",
        ),
        serialization_alias="RP.3",
        title="type of data",
    )

    rp_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rp_4",
            "subtype",
            "RP.4",
        ),
        serialization_alias="RP.4",
        title="subtype",
    )

    model_config = {"populate_by_name": True}
