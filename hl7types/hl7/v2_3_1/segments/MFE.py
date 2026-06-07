"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: MFE
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.TS import TS


class MFE(HL7Model):
    """HL7 v2 MFE segment.

    Attributes
    ----------
    mfe_1 : str
        MFE.1 (req) - Record-Level Event Code (ID)

    mfe_2 : str | None
        MFE.2 (opt) - MFN Control ID (ST)

    mfe_3 : TS | None
        MFE.3 (opt) - Effective Date/Time (TS)

    mfe_4 : list[str]
        MFE.4 (req, rep) - Primary Key Value - MFE (*)

    mfe_5 : list[str]
        MFE.5 (req, rep) - Primary Key Value Type (ID)
    """

    mfe_1: str = Field(
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

    mfe_4: List[str] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "mfe_4",
            "primary_key_value_mfe",
            "MFE.4",
        ),
        serialization_alias="MFE.4",
        title="Primary Key Value - MFE",
        description="Item #667",
    )

    mfe_5: List[str] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "mfe_5",
            "primary_key_value_type",
            "MFE.5",
        ),
        serialization_alias="MFE.5",
        title="Primary Key Value Type",
        description="Item #1319 | Table HL70355",
    )

    model_config = {"populate_by_name": True}
