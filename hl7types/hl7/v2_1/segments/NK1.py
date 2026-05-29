"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: NK1
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field


class NK1(BaseModel):
    """HL7 v2 NK1 segment.

    Attributes
    ----------
    nk1_1 : str
        NK1.1 (req) - SET ID - NEXT OF KIN (SI)

    nk1_2 : str | None
        NK1.2 (opt) - NEXT OF KIN NAME (PN)

    nk1_3 : str | None
        NK1.3 (opt) - NEXT OF KIN RELATIONSHIP (ST)

    nk1_4 : str | None
        NK1.4 (opt) - NEXT OF KIN - ADDRESS (AD)

    nk1_5 : list[str] | None
        NK1.5 (opt, rep) - NEXT OF KIN - PHONE NUMBER (TN)
    """

    nk1_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "nk1_1",
            "set_id_next_of_kin",
            "NK1.1",
        ),
        serialization_alias="NK1.1",
        title="SET ID - NEXT OF KIN",
        description="Item #712",
    )

    nk1_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_2",
            "next_of_kin_name",
            "NK1.2",
        ),
        serialization_alias="NK1.2",
        title="NEXT OF KIN NAME",
        description="Item #48",
    )

    nk1_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_3",
            "next_of_kin_relationship",
            "NK1.3",
        ),
        serialization_alias="NK1.3",
        title="NEXT OF KIN RELATIONSHIP",
        description="Item #47 | Table HL70063",
    )

    nk1_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_4",
            "next_of_kin_address",
            "NK1.4",
        ),
        serialization_alias="NK1.4",
        title="NEXT OF KIN - ADDRESS",
        description="Item #225",
    )

    nk1_5: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_5",
            "next_of_kin_phone_number",
            "NK1.5",
        ),
        serialization_alias="NK1.5",
        title="NEXT OF KIN - PHONE NUMBER",
        description="Item #230",
    )

    model_config = {"populate_by_name": True}
