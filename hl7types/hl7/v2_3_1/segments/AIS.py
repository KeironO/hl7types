"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: AIS
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.TS import TS


class AIS(HL7Model):
    """AIS - appointment information - service segment (S10.5.4).

    Attributes
    ----------
    ais_1 : str
        AIS.1 - Set ID - AIS (SI) R S10.5.4.1

    ais_2 : str | None
        AIS.2 - Segment Action Code (ID) C S10.5.7.2 | 0206 - Segment action code

    ais_3 : CE
        AIS.3 - Universal Service ID (CE) R S10.5.4.3

    ais_4 : TS | None
        AIS.4 - Start Date/Time (TS) C S10.5.7.6

    ais_5 : str | None
        AIS.5 - Start Date/Time Offset (NM) C S10.5.7.7

    ais_6 : CE | None
        AIS.6 - Start Date/Time Offset Units (CE) C S10.5.7.8

    ais_7 : str | None
        AIS.7 - Duration (NM) O S10.5.7.9

    ais_8 : CE | None
        AIS.8 - Duration Units (CE) O S10.5.7.10

    ais_9 : str | None
        AIS.9 - Allow Substitution Code (IS) C S10.5.7.11 | 0279 - Allow substitution codes

    ais_10 : CE | None
        AIS.10 - Filler Status Code (CE) C S10.5.7.12 | 0278 - Filler status codes
    """

    ais_1: str = Field(
        validation_alias=AliasChoices(
            "ais_1",
            "set_id_ais",
            "AIS.1",
        ),
        serialization_alias="AIS.1",
        title="Set ID - AIS",
        description="R | Item #00890 | LEN:4",
    )

    ais_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ais_2",
            "segment_action_code",
            "AIS.2",
        ),
        serialization_alias="AIS.2",
        title="Segment Action Code",
        description=(
            "C | Item #00763 | Table 0206 - Segment action code | LEN:3"
        ),
    )

    ais_3: CE = Field(
        validation_alias=AliasChoices(
            "ais_3",
            "universal_service_id",
            "AIS.3",
        ),
        serialization_alias="AIS.3",
        title="Universal Service ID",
        description="R | Item #00238",
    )

    ais_4: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ais_4",
            "start_date_time",
            "AIS.4",
        ),
        serialization_alias="AIS.4",
        title="Start Date/Time",
        description="C | Item #01202",
    )

    ais_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ais_5",
            "start_date_time_offset",
            "AIS.5",
        ),
        serialization_alias="AIS.5",
        title="Start Date/Time Offset",
        description="C | Item #00891 | LEN:20",
    )

    ais_6: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ais_6",
            "start_date_time_offset_units",
            "AIS.6",
        ),
        serialization_alias="AIS.6",
        title="Start Date/Time Offset Units",
        description="C | Item #00892",
    )

    ais_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ais_7",
            "duration",
            "AIS.7",
        ),
        serialization_alias="AIS.7",
        title="Duration",
        description="O | Item #00893 | LEN:20",
    )

    ais_8: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ais_8",
            "duration_units",
            "AIS.8",
        ),
        serialization_alias="AIS.8",
        title="Duration Units",
        description="O | Item #00894",
    )

    ais_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ais_9",
            "allow_substitution_code",
            "AIS.9",
        ),
        serialization_alias="AIS.9",
        title="Allow Substitution Code",
        description=(
            "C | Item #00895 | Table 0279 - Allow substitution codes | LEN:10"
        ),
    )

    ais_10: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ais_10",
            "filler_status_code",
            "AIS.10",
        ),
        serialization_alias="AIS.10",
        title="Filler Status Code",
        description="C | Item #00889 | Table 0278 - Filler status codes",
    )

    @field_validator("ais_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("ais_5", "ais_7", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
