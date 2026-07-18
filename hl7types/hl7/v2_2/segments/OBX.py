"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
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

_RE_SI = re.compile(r'\d*')
_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class OBX(HL7Model):
    """OBSERVATION RESULT (S7.3.2).

    Attributes
    ----------
    obx_1 : str | None
        OBX.1 - Set ID - Observational Simple (SI) NA S7.3.2.1

    obx_2 : str
        OBX.2 - Value Type (ID) R S7.3.2.2 | 0125 - VALUE TYPE

    obx_3 : CE
        OBX.3 - Observation Identifier (CE) R S7.3.2.3

    obx_4 : str | None
        OBX.4 - Observation Sub-ID (ST) C S7.3.2.4

    obx_5 : str | None
        OBX.5 - Observation Value (*) C S7.3.2.5

    obx_6 : CE | None
        OBX.6 - Units (CE) NA S7.3.2.6

    obx_7 : str | None
        OBX.7 - References Range (ST) NA S7.3.2.7

    obx_8 : list[str] | None
        OBX.8 - Abnormal Flags (ID) NA rep S7.3.2.8 | 0078 - ABNORMAL FLAGS

    obx_9 : str | None
        OBX.9 - Probability (NM) NA S7.3.2.9

    obx_10 : str | None
        OBX.10 - Nature of Abnormal Test (ID) O S7.3.2.10 | 0080 - NATURE OF ABNORMAL TESTING

    obx_11 : str
        OBX.11 - Observation result status (ID) R S7.3.2.11 | 0085 - OBSERVATION RESULT STATUS CODES INTERPRETATION

    obx_12 : TS | None
        OBX.12 - Effective date last observation normal values (TS) NA S7.3.2.12

    obx_13 : str | None
        OBX.13 - User Defined Access Checks (ST) NA S7.3.2.13

    obx_14 : TS | None
        OBX.14 - Date / time of the observation (TS) NA S7.3.2.14

    obx_15 : CE | None
        OBX.15 - Producer's ID (CE) NA S7.3.2.15

    obx_16 : str | None
        OBX.16 - Responsible Observer (CN) NA S7.3.2.16
    """

    obx_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_1",
            "set_id_observational_simple",
            "OBX.1",
        ),
        serialization_alias="OBX.1",
        title="Set ID - Observational Simple",
        description="NA | Item #00569 | LEN:4",
    )

    obx_2: str = Field(
        validation_alias=AliasChoices(
            "obx_2",
            "value_type",
            "OBX.2",
        ),
        serialization_alias="OBX.2",
        title="Value Type",
        description="R | Item #00570 | Table 0125 - VALUE TYPE | LEN:2",
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

    obx_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_4",
            "observation_sub_id",
            "OBX.4",
        ),
        serialization_alias="OBX.4",
        title="Observation Sub-ID",
        description="C | Item #00572 | LEN:20",
    )

    obx_5: Optional[str] = Field(
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
        description="NA | Item #00574",
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
        description="NA | Item #00575 | LEN:60",
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
        description="NA | Item #00576 | Table 0078 - ABNORMAL FLAGS | LEN:10",
    )

    obx_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_9",
            "probability",
            "OBX.9",
        ),
        serialization_alias="OBX.9",
        title="Probability",
        description="NA | Item #00577 | LEN:5",
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
            "O | Item #00578 | Table 0080 - NATURE OF ABNORMAL TESTING | LEN:5"
        ),
    )

    obx_11: str = Field(
        validation_alias=AliasChoices(
            "obx_11",
            "observation_result_status",
            "OBX.11",
        ),
        serialization_alias="OBX.11",
        title="Observation result status",
        description=(
            "R | Item #00579 | Table 0085 - OBSERVATION RESULT STATUS CODES "
            "INTERPRETATION | LEN:2"
        ),
    )

    obx_12: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_12",
            "effective_date_last_observation_normal_values",
            "OBX.12",
        ),
        serialization_alias="OBX.12",
        title="Effective date last observation normal values",
        description="NA | Item #00580",
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
        description="NA | Item #00581 | LEN:20",
    )

    obx_14: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_14",
            "date_time_of_the_observation",
            "OBX.14",
        ),
        serialization_alias="OBX.14",
        title="Date / time of the observation",
        description="NA | Item #00582",
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
        description="NA | Item #00583",
    )

    obx_16: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_16",
            "responsible_observer",
            "OBX.16",
        ),
        serialization_alias="OBX.16",
        title="Responsible Observer",
        description="NA | Item #00584",
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
