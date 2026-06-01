"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: OBX
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator

from ..datatypes.CE import CE
from ..datatypes.TS import TS
from ..datatypes.XCN import XCN


class OBX(HL7Model):
    """HL7 v2 OBX segment.

    Attributes
    ----------
    obx_1 : str | None
        OBX.1 (opt) - Set ID - OBX (SI)

    obx_2 : str
        OBX.2 (req) - Value Type (ID)

    obx_3 : CE
        OBX.3 (req) - Observation Identifier (CE)

    obx_4 : str
        OBX.4 (req) - Observation Sub-ID (ST)

    obx_5 : list[str] | None
        OBX.5 (opt, rep) - Observation Value (*)

    obx_6 : CE | None
        OBX.6 (opt) - Units (CE)

    obx_7 : str | None
        OBX.7 (opt) - References Range (ST)

    obx_8 : list[str] | None
        OBX.8 (opt, rep) - Abnormal Flags (ID)

    obx_9 : list[str] | None
        OBX.9 (opt, rep) - Probability (NM)

    obx_10 : str | None
        OBX.10 (opt) - Nature of Abnormal Test (ID)

    obx_11 : str
        OBX.11 (req) - Observation Result Status (ID)

    obx_12 : TS | None
        OBX.12 (opt) - Date Last Obs Normal Values (TS)

    obx_13 : str | None
        OBX.13 (opt) - User Defined Access Checks (ST)

    obx_14 : TS | None
        OBX.14 (opt) - Date/Time of the Observation (TS)

    obx_15 : CE | None
        OBX.15 (opt) - Producer's ID (CE)

    obx_16 : list[XCN] | None
        OBX.16 (opt, rep) - Responsible Observer (XCN)

    obx_17 : list[CE] | None
        OBX.17 (opt, rep) - Observation Method (CE)
    """

    obx_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_1",
            "set_id_obx",
            "OBX.1",
        ),
        serialization_alias="OBX.1",
        title="Set ID - OBX",
        description="Item #569",
    )

    obx_2: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "obx_2",
            "value_type",
            "OBX.2",
        ),
        serialization_alias="OBX.2",
        title="Value Type",
        description="Item #570 | Table HL70125",
    )

    obx_3: CE = Field(
        default=...,
        validation_alias=AliasChoices(
            "obx_3",
            "observation_identifier",
            "OBX.3",
        ),
        serialization_alias="OBX.3",
        title="Observation Identifier",
        description="Item #571",
    )

    obx_4: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "obx_4",
            "observation_sub_id",
            "OBX.4",
        ),
        serialization_alias="OBX.4",
        title="Observation Sub-ID",
        description="Item #572",
    )

    obx_5: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_5",
            "observation_value",
            "OBX.5",
        ),
        serialization_alias="OBX.5",
        title="Observation Value",
        description="Item #573",
    )

    obx_6: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_6",
            "units",
            "OBX.6",
        ),
        serialization_alias="OBX.6",
        title="Units",
        description="Item #574",
    )

    obx_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_7",
            "references_range",
            "OBX.7",
        ),
        serialization_alias="OBX.7",
        title="References Range",
        description="Item #575",
    )

    obx_8: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_8",
            "abnormal_flags",
            "OBX.8",
        ),
        serialization_alias="OBX.8",
        title="Abnormal Flags",
        description="Item #576 | Table HL70078",
    )

    obx_9: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_9",
            "probability",
            "OBX.9",
        ),
        serialization_alias="OBX.9",
        title="Probability",
        description="Item #577",
    )

    obx_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_10",
            "nature_of_abnormal_test",
            "OBX.10",
        ),
        serialization_alias="OBX.10",
        title="Nature of Abnormal Test",
        description="Item #578 | Table HL70080",
    )

    obx_11: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "obx_11",
            "observation_result_status",
            "OBX.11",
        ),
        serialization_alias="OBX.11",
        title="Observation Result Status",
        description="Item #579 | Table HL70085",
    )

    obx_12: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_12",
            "date_last_obs_normal_values",
            "OBX.12",
        ),
        serialization_alias="OBX.12",
        title="Date Last Obs Normal Values",
        description="Item #580",
    )

    obx_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_13",
            "user_defined_access_checks",
            "OBX.13",
        ),
        serialization_alias="OBX.13",
        title="User Defined Access Checks",
        description="Item #581",
    )

    obx_14: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_14",
            "date_time_of_the_observation",
            "OBX.14",
        ),
        serialization_alias="OBX.14",
        title="Date/Time of the Observation",
        description="Item #582",
    )

    obx_15: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_15",
            "producer_s_id",
            "OBX.15",
        ),
        serialization_alias="OBX.15",
        title="Producer's ID",
        description="Item #583",
    )

    obx_16: Optional[List[XCN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_16",
            "responsible_observer",
            "OBX.16",
        ),
        serialization_alias="OBX.16",
        title="Responsible Observer",
        description="Item #584",
    )

    obx_17: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_17",
            "observation_method",
            "OBX.17",
        ),
        serialization_alias="OBX.17",
        title="Observation Method",
        description="Item #936",
    )

    @field_validator("obx_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("obx_9", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
