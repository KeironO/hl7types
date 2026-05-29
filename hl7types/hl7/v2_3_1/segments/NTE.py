"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: NTE
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE
from ..datatypes.FT import FT


class NTE(BaseModel):
    """HL7 v2 NTE segment.

    Attributes
    ----------
    nte_1 : str | None
        NTE.1 (opt) - Set ID - NTE (SI)

    nte_2 : str | None
        NTE.2 (opt) - Source of Comment (ID)

    nte_3 : list[FT] | None
        NTE.3 (opt, rep) - Comment (FT)

    nte_4 : CE | None
        NTE.4 (opt) - Comment Type (CE)
    """

    nte_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nte_1",
            "set_id_nte",
            "NTE.1",
        ),
        serialization_alias="NTE.1",
        title="Set ID - NTE",
        description="Item #96",
    )

    nte_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nte_2",
            "source_of_comment",
            "NTE.2",
        ),
        serialization_alias="NTE.2",
        title="Source of Comment",
        description="Item #97 | Table HL70105",
    )

    nte_3: Optional[List[FT]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nte_3",
            "comment",
            "NTE.3",
        ),
        serialization_alias="NTE.3",
        title="Comment",
        description="Item #98",
    )

    nte_4: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nte_4",
            "comment_type",
            "NTE.4",
        ),
        serialization_alias="NTE.4",
        title="Comment Type",
        description="Item #1318 | Table HL70364",
    )

    model_config = {"populate_by_name": True}
