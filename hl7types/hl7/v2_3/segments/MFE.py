"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: MFE
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.TS import TS


class MFE(HL7Model):
    """Master file entry segment (S8.4.2).

    Attributes
    ----------
    mfe_1 : str
        MFE.1 - Record-Level Event Code (ID) R S8.4.2 | 0180 - Record Level Event Code

    mfe_2 : str | None
        MFE.2 - MFN Control ID (ST) C S8.4.2

    mfe_3 : TS | None
        MFE.3 - Effective Date/Time (TS) NA S8.4.1

    mfe_4 : list[CE]
        MFE.4 - Primary Key Value (CE) R rep S8.4.2.4
    """

    mfe_1: str = Field(
        validation_alias=AliasChoices(
            "mfe_1",
            "record_level_event_code",
            "MFE.1",
        ),
        serialization_alias="MFE.1",
        title="Record-Level Event Code",
        description=(
            "R | Item #00664 | Table 0180 - Record Level Event Code | LEN:3"
        ),
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
        description="C | Item #00665 | LEN:20",
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
        description="NA | Item #00662",
    )

    mfe_4: List[CE] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "mfe_4",
            "primary_key_value",
            "MFE.4",
        ),
        serialization_alias="MFE.4",
        title="Primary Key Value",
        description="R | Item #00667",
    )

    model_config = {"populate_by_name": True}
