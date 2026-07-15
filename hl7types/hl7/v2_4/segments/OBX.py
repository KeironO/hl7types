"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: OBX
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.EI import EI
from ..datatypes.TS import TS
from ..datatypes.XCN import XCN


class OBX(HL7Model):
    """Observation/Result (S7.4.2).

    Attributes
    ----------
    obx_1 : str | None
        OBX.1 - Set ID - OBX (SI) O S7.4.2.1

    obx_2 : str | None
        OBX.2 - Value Type (ID) C S8.8.5.7 | 0125 - Value type

    obx_3 : CE
        OBX.3 - Observation Identifier (CE) R S7.4.2.3

    obx_4 : str | None
        OBX.4 - Observation Sub-Id (ST) C S7.4.2.4

    obx_5 : list[str] | None
        OBX.5 - Observation Value (*) C rep S7.4.2.5

    obx_6 : CE | None
        OBX.6 - Units (CE) O S13.4.9.13

    obx_7 : str | None
        OBX.7 - References Range (ST) O S7.4.2.7

    obx_8 : str | None
        OBX.8 - Abnormal Flags (IS) O S7.4.2.8 | 0078 - Abnormal flags

    obx_9 : list[str] | None
        OBX.9 - Probability (NM) O rep S7.4.2.9

    obx_10 : str | None
        OBX.10 - Nature of Abnormal Test (ID) O S7.4.2.10 | 0080 - Nature of abnormal testing

    obx_11 : str
        OBX.11 - Observation Result Status (ID) R S7.4.2.11 | 0085 - Observation result status codes interpretation

    obx_12 : TS | None
        OBX.12 - Date Last Observation Normal Value (TS) O S7.4.2.12

    obx_13 : str | None
        OBX.13 - User Defined Access Checks (ST) O S7.4.2.13

    obx_14 : TS | None
        OBX.14 - Date/Time of the Observation (TS) O S7.4.2.14

    obx_15 : CE | None
        OBX.15 - Producer's ID (CE) O S7.4.2.15

    obx_16 : XCN | None
        OBX.16 - Responsible Observer (XCN) O S7.4.2.16

    obx_17 : list[CE] | None
        OBX.17 - Observation Method (CE) O rep S7.4.2.17

    obx_18 : list[EI] | None
        OBX.18 - Equipment Instance Identifier (EI) O rep S13.4.1.1

    obx_19 : TS | None
        OBX.19 - Date/Time of the Analysis (TS) O S7.4.2.19
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

    obx_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_2",
            "value_type",
            "OBX.2",
        ),
        serialization_alias="OBX.2",
        title="Value Type",
        description="C | Item #00570 | Table 0125 - Value type | LEN:2",
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
        title="Observation Sub-Id",
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

    obx_8: Optional[str] = Field(
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
            "date_last_observation_normal_value",
            "OBX.12",
        ),
        serialization_alias="OBX.12",
        title="Date Last Observation Normal Value",
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

    obx_16: Optional[XCN] = Field(
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

    obx_18: Optional[List[EI]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_18",
            "equipment_instance_identifier",
            "OBX.18",
        ),
        serialization_alias="OBX.18",
        title="Equipment Instance Identifier",
        description="O | Item #01479",
    )

    obx_19: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_19",
            "date_time_of_the_analysis",
            "OBX.19",
        ),
        serialization_alias="OBX.19",
        title="Date/Time of the Analysis",
        description="O | Item #01480",
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
