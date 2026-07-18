"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: OBX
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.TS import TS
from ..datatypes.XCN import XCN

_RE_SI = re.compile(r'\d*')
_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class OBX(HL7Model):
    """OBX - observation/result segment (S9.5.2).

    Attributes
    ----------
    obx_1 : str | None
        OBX.1 - Set ID - OBX (SI) O S7.3.2.1

    obx_2 : str
        OBX.2 - Value Type (ID) C S8.7.5.7 | 0125 - Value type

    obx_3 : CE
        OBX.3 - Observation Identifier (CE) R S7.3.2.3

    obx_4 : str
        OBX.4 - Observation Sub-ID (ST) C S7.3.2.4

    obx_5 : list[str] | None
        OBX.5 - Observation Value (*) C rep S7.3.2.5

    obx_6 : CE | None
        OBX.6 - Units (CE) O S7.3.2.6

    obx_7 : str | None
        OBX.7 - References Range (ST) O S7.3.2.7

    obx_8 : list[str] | None
        OBX.8 - Abnormal Flags (ID) O rep S7.3.2.8 | 0078 - Abnormal flags

    obx_9 : list[str] | None
        OBX.9 - Probability (NM) O rep S7.3.2.9

    obx_10 : str | None
        OBX.10 - Nature of Abnormal Test (ID) O S7.3.2.10 | 0080 - Nature of abnormal testing

    obx_11 : str
        OBX.11 - Observation Result Status (ID) R S7.3.2.11 | 0085 - Observation result status codes interpretation

    obx_12 : TS | None
        OBX.12 - Date Last Obs Normal Values (TS) O S7.3.2.12

    obx_13 : str | None
        OBX.13 - User Defined Access Checks (ST) O S7.3.2.13

    obx_14 : TS | None
        OBX.14 - Date/Time of the Observation (TS) O S7.3.2.14

    obx_15 : CE | None
        OBX.15 - Producer's ID (CE) O S7.3.2.15

    obx_16 : list[XCN] | None
        OBX.16 - Responsible Observer (XCN) O rep S7.3.2.16

    obx_17 : list[CE] | None
        OBX.17 - Observation Method (CE) O rep S7.3.2.17
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
        description="O | Item #00569 | LEN:4",
    )

    obx_2: str = Field(
        validation_alias=AliasChoices(
            "obx_2",
            "value_type",
            "OBX.2",
        ),
        serialization_alias="OBX.2",
        title="Value Type",
        description="C | Item #00570 | Table 0125 - Value type | LEN:3",
    )

    obx_3: CE = Field(
        validation_alias=AliasChoices(
            "obx_3",
            "observation_identifier",
            "OBX.3",
        ),
        serialization_alias="OBX.3",
        title="Observation Identifier",
        description="R | Item #00571",
    )

    obx_4: str = Field(
        validation_alias=AliasChoices(
            "obx_4",
            "observation_sub_id",
            "OBX.4",
        ),
        serialization_alias="OBX.4",
        title="Observation Sub-ID",
        description="C | Item #00572 | LEN:20",
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
        description="C | Item #00573",
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
        description="O | Item #00574",
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
        description="O | Item #00575 | LEN:60",
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
        description="O | Item #00576 | Table 0078 - Abnormal flags | LEN:5",
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
        description="O | Item #00577 | LEN:5",
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
        description=(
            "O | Item #00578 | Table 0080 - Nature of abnormal testing | LEN:2"
        ),
    )

    obx_11: str = Field(
        validation_alias=AliasChoices(
            "obx_11",
            "observation_result_status",
            "OBX.11",
        ),
        serialization_alias="OBX.11",
        title="Observation Result Status",
        description=(
            "R | Item #00579 | Table 0085 - Observation result status codes "
            "interpretation | LEN:1"
        ),
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
        description="O | Item #00580",
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
        description="O | Item #00581 | LEN:20",
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
        description="O | Item #00582",
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
        description="O | Item #00583",
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
        description="O | Item #00584",
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
        description="O | Item #00936",
    )

    @field_validator("obx_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        if not _RE_SI.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("obx_9", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
