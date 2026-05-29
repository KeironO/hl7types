"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: SN
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class SN(BaseModel):
    """HL7 v2 SN data type.

    Attributes
    ----------
    sn_1 : str | None
        SN.1 (opt) - comparator (ST)

    sn_2 : str | None
        SN.2 (opt) - num1 (NM)

    sn_3 : str | None
        SN.3 (opt) - separator/suffix (ST)

    sn_4 : str | None
        SN.4 (opt) - num2 (NM)
    """

    sn_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sn_1",
            "comparator",
            "SN.1",
        ),
        serialization_alias="SN.1",
        title="comparator",
    )

    sn_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sn_2",
            "num1",
            "SN.2",
        ),
        serialization_alias="SN.2",
        title="num1",
    )

    sn_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sn_3",
            "separator_suffix",
            "SN.3",
        ),
        serialization_alias="SN.3",
        title="separator/suffix",
    )

    sn_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sn_4",
            "num2",
            "SN.4",
        ),
        serialization_alias="SN.4",
        title="num2",
    )

    model_config = {"populate_by_name": True}
