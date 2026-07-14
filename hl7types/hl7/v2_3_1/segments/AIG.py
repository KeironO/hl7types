"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
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
    """AIG - appointment information - general resource segment (S10.5.5).

    Attributes
    ----------
    aig_1 : str
        AIG.1 (req) - Set ID - AIG (SI) S10.5.5.1

    aig_2 : str | None
        AIG.2 (opt) - Segment Action Code (ID) S10.5.7.2 | 0206 - Segment action code

    aig_3 : CE | None
        AIG.3 (opt) - Resource ID (CE) S10.5.5.3

    aig_4 : CE
        AIG.4 (req) - Resource Type (CE) S10.5.5.4

    aig_5 : list[CE] | None
        AIG.5 (opt, rep) - Resource Group (CE) S10.5.7.5

    aig_6 : str | None
        AIG.6 (opt) - Resource Quantity (NM) S10.5.5.6

    aig_7 : CE | None
        AIG.7 (opt) - Resource Quantity Units (CE) S10.5.5.7

    aig_8 : TS | None
        AIG.8 (opt) - Start Date/Time (TS) S10.5.7.6

    aig_9 : str | None
        AIG.9 (opt) - Start Date/Time Offset (NM) S10.5.7.7

    aig_10 : CE | None
        AIG.10 (opt) - Start Date/Time Offset Units (CE) S10.5.7.8

    aig_11 : str | None
        AIG.11 (opt) - Duration (NM) S10.5.7.9

    aig_12 : CE | None
        AIG.12 (opt) - Duration Units (CE) S10.5.7.10

    aig_13 : str | None
        AIG.13 (opt) - Allow Substitution Code (IS) S10.5.7.11 | 0279 - Allow substitution codes

    aig_14 : CE | None
        AIG.14 (opt) - Filler Status Code (CE) S10.5.7.12 | 0278 - Filler status codes
    """

    aig_1: str = Field(
        validation_alias=AliasChoices(
            "aig_1",
            "set_id_aig",
            "AIG.1",
        ),
        serialization_alias="AIG.1",
        title="Set ID - AIG",
        description="Item #896",
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
        description="Item #763 | Table HL70206",
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
        description="Item #897",
    )

    aig_4: CE = Field(
        validation_alias=AliasChoices(
            "aig_4",
            "resource_type",
            "AIG.4",
        ),
        serialization_alias="AIG.4",
        title="Resource Type",
        description="Item #898",
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
        description="Item #899",
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
        description="Item #900",
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
        description="Item #901",
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
        description="Item #1202",
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
        description="Item #891",
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
        description="Item #892",
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
        description="Item #893",
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
        description="Item #894",
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
        description="Item #895 | Table HL70279",
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
        description="Item #889 | Table HL70278",
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
