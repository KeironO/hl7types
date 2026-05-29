"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: MFE
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE
from ..datatypes.TS import TS


class MFE(BaseModel):
    """HL7 v2 MFE segment.

    Attributes
    ----------
    mfe_1 : str
        MFE.1 (req) - Record-Level Event Code (ID)

    mfe_2 : str | None
        MFE.2 (opt) - MFN Control ID (ST)

    mfe_3 : TS | None
        MFE.3 (opt) - Effective Date/Time (TS)

    mfe_4 : list[CE]
        MFE.4 (req, rep) - Primary Key Value (CE)
    """

    mfe_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "mfe_1",
            "record_level_event_code",
            "MFE.1",
        ),
        serialization_alias="MFE.1",
        title="Record-Level Event Code",
        description="Item #664 | Table HL70180",
    )

    mfe_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "mfe_2",
            "mfn_control_id",
            "MFE.2",
        ),
        serialization_alias="MFE.2",
        title="MFN Control ID",
        description="Item #665",
    )

    mfe_3: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "mfe_3",
            "effective_date_time",
            "MFE.3",
        ),
        serialization_alias="MFE.3",
        title="Effective Date/Time",
        description="Item #662",
    )

    mfe_4: List[CE] = Field(
        default=...,
        validation_alias=AliasChoices(
            "mfe_4",
            "primary_key_value",
            "MFE.4",
        ),
        serialization_alias="MFE.4",
        title="Primary Key Value",
        description="Item #667",
    )

    model_config = {"populate_by_name": True}
