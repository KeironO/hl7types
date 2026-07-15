"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: AIG
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.TS import TS


class AIG(HL7Model):
    """Appointment Information - General Resource (S10.6.5).

    Attributes
    ----------
    aig_1 : str
        AIG.1 - Set ID - AIG (SI) R S10.6.5.1

    aig_2 : str | None
        AIG.2 - Segment Action Code (ID) C S10.6.7.2 | 0206 - Segment action code

    aig_3 : CE | None
        AIG.3 - Resource ID (CE) C S10.6.5.3

    aig_4 : CE
        AIG.4 - Resource Type (CE) R S10.6.5.4

    aig_5 : list[CE] | None
        AIG.5 - Resource Group (CE) O rep S10.6.7.5

    aig_6 : str | None
        AIG.6 - Resource Quantity (NM) O S10.6.5.6

    aig_7 : CE | None
        AIG.7 - Resource Quantity Units (CE) O S10.6.5.7

    aig_8 : TS | None
        AIG.8 - Start Date/Time (TS) C S13.4.12.3

    aig_9 : str | None
        AIG.9 - Start Date/Time Offset (NM) C S10.6.7.7

    aig_10 : CE | None
        AIG.10 - Start Date/Time Offset Units (CE) C S10.6.7.8

    aig_11 : str | None
        AIG.11 - Duration (NM) O S10.6.7.9

    aig_12 : CE | None
        AIG.12 - Duration Units (CE) O S10.6.7.10

    aig_13 : str | None
        AIG.13 - Allow Substitution Code (IS) C S10.6.7.11 | 0279 - Allow substitution codes

    aig_14 : CE | None
        AIG.14 - Filler Status Code (CE) C S10.6.7.12 | 0278 - Filler status codes
    """

    aig_1: str = Field(
        validation_alias=AliasChoices(
            "aig_1",
            "set_id_aig",
            "AIG.1",
        ),
        serialization_alias="AIG.1",
        title="Set ID - AIG",
        description="R | Item #00896 | LEN:4",
    )

    aig_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aig_2",
            "segment_action_code",
            "AIG.2",
        ),
        serialization_alias="AIG.2",
        title="Segment Action Code",
        description=(
            "C | Item #00763 | Table 0206 - Segment action code | LEN:3"
        ),
    )

    aig_3: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aig_3",
            "resource_id",
            "AIG.3",
        ),
        serialization_alias="AIG.3",
        title="Resource ID",
        description="C | Item #00897",
    )

    aig_4: CE = Field(
        validation_alias=AliasChoices(
            "aig_4",
            "resource_type",
            "AIG.4",
        ),
        serialization_alias="AIG.4",
        title="Resource Type",
        description="R | Item #00898",
    )

    aig_5: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aig_5",
            "resource_group",
            "AIG.5",
        ),
        serialization_alias="AIG.5",
        title="Resource Group",
        description="O | Item #00899",
    )

    aig_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aig_6",
            "resource_quantity",
            "AIG.6",
        ),
        serialization_alias="AIG.6",
        title="Resource Quantity",
        description="O | Item #00900 | LEN:5",
    )

    aig_7: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aig_7",
            "resource_quantity_units",
            "AIG.7",
        ),
        serialization_alias="AIG.7",
        title="Resource Quantity Units",
        description="O | Item #00901",
    )

    aig_8: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aig_8",
            "start_date_time",
            "AIG.8",
        ),
        serialization_alias="AIG.8",
        title="Start Date/Time",
        description="C | Item #01202",
    )

    aig_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aig_9",
            "start_date_time_offset",
            "AIG.9",
        ),
        serialization_alias="AIG.9",
        title="Start Date/Time Offset",
        description="C | Item #00891 | LEN:20",
    )

    aig_10: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aig_10",
            "start_date_time_offset_units",
            "AIG.10",
        ),
        serialization_alias="AIG.10",
        title="Start Date/Time Offset Units",
        description="C | Item #00892",
    )

    aig_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aig_11",
            "duration",
            "AIG.11",
        ),
        serialization_alias="AIG.11",
        title="Duration",
        description="O | Item #00893 | LEN:20",
    )

    aig_12: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aig_12",
            "duration_units",
            "AIG.12",
        ),
        serialization_alias="AIG.12",
        title="Duration Units",
        description="O | Item #00894",
    )

    aig_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aig_13",
            "allow_substitution_code",
            "AIG.13",
        ),
        serialization_alias="AIG.13",
        title="Allow Substitution Code",
        description=(
            "C | Item #00895 | Table 0279 - Allow substitution codes | LEN:10"
        ),
    )

    aig_14: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aig_14",
            "filler_status_code",
            "AIG.14",
        ),
        serialization_alias="AIG.14",
        title="Filler Status Code",
        description="C | Item #00889 | Table 0278 - Filler status codes",
    )

    @field_validator("aig_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("aig_6", "aig_9", "aig_11", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
