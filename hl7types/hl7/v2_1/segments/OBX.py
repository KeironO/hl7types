"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: OBX
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE

_RE_SI = re.compile(r'\d*')
_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class OBX(HL7Model):
    """RESULT (S7.3.1).

    Attributes
    ----------
    obx_1 : str | None
        OBX.1 - SET ID - OBSERVATION SIMPLE (SI) O S7-14

    obx_2 : str | None
        OBX.2 - VALUE TYPE (ID) O | 0125 - VALUE TYPE

    obx_3 : CE
        OBX.3 - OBSERVATION IDENTIFIER (CE) R

    obx_4 : str | None
        OBX.4 - OBSERVATION SUB-ID (NM) O

    obx_5 : str
        OBX.5 - OBSERVATION RESULTS (ST) R

    obx_6 : str | None
        OBX.6 - UNITS (ID) O

    obx_7 : str | None
        OBX.7 - REFERENCES RANGE (ST) O

    obx_8 : list[str] | None
        OBX.8 - ABNORMAL FLAGS (ST) O rep | 0078 - ABNORMAL FLAGS

    obx_9 : str | None
        OBX.9 - PROBABILITY (NM) O

    obx_10 : str | None
        OBX.10 - NATURE OF ABNORMAL TEST (ID) O | 0080 - NATURE OF ABNORMAL TESTING

    obx_11 : str | None
        OBX.11 - OBSERV RESULT STATUS (ID) O | 0085 - OBSERVATION RESULT STATUS

    obx_12 : str | None
        OBX.12 - DATE LAST OBS NORMAL VALUES (TS) O
    """

    obx_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_1",
            "set_id_observation_simple",
            "OBX.1",
        ),
        serialization_alias="OBX.1",
        title="SET ID - OBSERVATION SIMPLE",
        description="O | Item #00559 | LEN:4",
    )

    obx_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_2",
            "value_type",
            "OBX.2",
        ),
        serialization_alias="OBX.2",
        title="VALUE TYPE",
        description="O | Item #00676 | Table 0125 - VALUE TYPE | LEN:2",
    )

    obx_3: CE = Field(
        validation_alias=AliasChoices(
            "obx_3",
            "observation_identifier",
            "OBX.3",
        ),
        serialization_alias="OBX.3",
        title="OBSERVATION IDENTIFIER",
        description="R | Item #00560",
    )

    obx_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_4",
            "observation_sub_id",
            "OBX.4",
        ),
        serialization_alias="OBX.4",
        title="OBSERVATION SUB-ID",
        description="O | Item #00769 | LEN:20",
    )

    obx_5: str = Field(
        validation_alias=AliasChoices(
            "obx_5",
            "observation_results",
            "OBX.5",
        ),
        serialization_alias="OBX.5",
        title="OBSERVATION RESULTS",
        description="R | Item #00561 | LEN:65",
    )

    obx_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_6",
            "units",
            "OBX.6",
        ),
        serialization_alias="OBX.6",
        title="UNITS",
        description="O | Item #00562 | LEN:20",
    )

    obx_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_7",
            "references_range",
            "OBX.7",
        ),
        serialization_alias="OBX.7",
        title="REFERENCES RANGE",
        description="O | Item #00563 | LEN:60",
    )

    obx_8: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_8",
            "abnormal_flags",
            "OBX.8",
        ),
        serialization_alias="OBX.8",
        title="ABNORMAL FLAGS",
        description="O | Item #00564 | Table 0078 - ABNORMAL FLAGS | LEN:10",
    )

    obx_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_9",
            "probability",
            "OBX.9",
        ),
        serialization_alias="OBX.9",
        title="PROBABILITY",
        description="O | Item #00639 | LEN:5",
    )

    obx_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_10",
            "nature_of_abnormal_test",
            "OBX.10",
        ),
        serialization_alias="OBX.10",
        title="NATURE OF ABNORMAL TEST",
        description=(
            "O | Item #00565 | Table 0080 - NATURE OF ABNORMAL TESTING | LEN:5"
        ),
    )

    obx_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_11",
            "observ_result_status",
            "OBX.11",
        ),
        serialization_alias="OBX.11",
        title="OBSERV RESULT STATUS",
        description=(
            "O | Item #00566 | Table 0085 - OBSERVATION RESULT STATUS | LEN:2"
        ),
    )

    obx_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_12",
            "date_last_obs_normal_values",
            "OBX.12",
        ),
        serialization_alias="OBX.12",
        title="DATE LAST OBS NORMAL VALUES",
        description="O | Item #00567 | LEN:19",
    )

    @field_validator("obx_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        if not _RE_SI.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("obx_4", "obx_9", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
