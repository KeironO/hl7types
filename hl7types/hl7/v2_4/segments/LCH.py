"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: LCH
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE
from ..datatypes.EI import EI
from ..datatypes.PL import PL


class LCH(BaseModel):
    """HL7 v2 LCH segment.

    Attributes
    ----------
    lch_1 : PL
        LCH.1 (req) - Primary Key Value - LCH (PL)

    lch_2 : str | None
        LCH.2 (opt) - Segment Action Code (ID)

    lch_3 : EI | None
        LCH.3 (opt) - Segment Unique Key (EI)

    lch_4 : CE
        LCH.4 (req) - Location Characteristic ID (CE)

    lch_5 : CE
        LCH.5 (req) - Location Characteristic Value-LCH (CE)
    """

    lch_1: PL = Field(
        default=...,
        validation_alias=AliasChoices(
            "lch_1",
            "primary_key_value_lch",
            "LCH.1",
        ),
        serialization_alias="LCH.1",
        title="Primary Key Value - LCH",
        description="Item #1305",
    )

    lch_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "lch_2",
            "segment_action_code",
            "LCH.2",
        ),
        serialization_alias="LCH.2",
        title="Segment Action Code",
        description="Item #763 | Table HL70206",
    )

    lch_3: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "lch_3",
            "segment_unique_key",
            "LCH.3",
        ),
        serialization_alias="LCH.3",
        title="Segment Unique Key",
        description="Item #764",
    )

    lch_4: CE = Field(
        default=...,
        validation_alias=AliasChoices(
            "lch_4",
            "location_characteristic_id",
            "LCH.4",
        ),
        serialization_alias="LCH.4",
        title="Location Characteristic ID",
        description="Item #1295 | Table HL70324",
    )

    lch_5: CE = Field(
        default=...,
        validation_alias=AliasChoices(
            "lch_5",
            "location_characteristic_value_lch",
            "LCH.5",
        ),
        serialization_alias="LCH.5",
        title="Location Characteristic Value-LCH",
        description="Item #1294 | Table HL70136",
    )

    model_config = {"populate_by_name": True}
