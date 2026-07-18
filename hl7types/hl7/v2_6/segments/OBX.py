"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: OBX
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, ValidationInfo, field_validator
from hl7types.hl7 import HL7Model
from hl7types.hl7._validators import _apply_dt_fallback

from ..datatypes.CNE import CNE
from ..datatypes.CWE import CWE
from ..datatypes.EI import EI
from ..datatypes.XAD import XAD
from ..datatypes.XCN import XCN
from ..datatypes.XON import XON
from ..datatypes.varies import varies

_RE_SI = re.compile(r'\d*')
_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')
_RE_DTM = re.compile(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?')


class OBX(HL7Model):
    """Observation/Result (S7.4.2).

    Attributes
    ----------
    obx_1 : str | None
        OBX.1 - Set ID - OBX (SI) O S7.4.2.1

    obx_2 : str | None
        OBX.2 - Value Type (ID) C S7.4.2.2 | 0125 - Value type

    obx_3 : CWE
        OBX.3 - Observation Identifier (CWE) R S7.4.2.3 | 9999 - no table for CE

    obx_4 : str | None
        OBX.4 - Observation Sub-ID (ST) C S7.4.2.4

    obx_5 : list[varies] | None
        OBX.5 - Observation Value (varies) C rep S7.4.2.5

    obx_6 : CWE | None
        OBX.6 - Units (CWE) O S7.4.2.6 | 9999 - no table for CE

    obx_7 : str | None
        OBX.7 - References Range (ST) O S7.4.2.7

    obx_8 : list[str] | None
        OBX.8 - Abnormal Flags (IS) O rep S7.4.2.8 | 0078 - Abnormal flags

    obx_9 : str | None
        OBX.9 - Probability (NM) O S7.4.2.9

    obx_10 : list[str] | None
        OBX.10 - Nature of Abnormal Test (ID) O rep S7.4.2.10 | 0080 - Nature of Abnormal Testing

    obx_11 : str
        OBX.11 - Observation Result Status (ID) R S7.4.2.11 | 0085 - Observation result status codes interpretation

    obx_12 : str | None
        OBX.12 - Effective Date of Reference Range (DTM) O S7.4.2.12

    obx_13 : str | None
        OBX.13 - User Defined Access Checks (ST) O S7.4.2.13

    obx_14 : str | None
        OBX.14 - Date/Time of the Observation (DTM) O S7.4.2.14

    obx_15 : CWE | None
        OBX.15 - Producer's ID (CWE) O S7.4.2.15 | 9999 - no table for CE

    obx_16 : list[XCN] | None
        OBX.16 - Responsible Observer (XCN) O rep S7.4.2.16

    obx_17 : list[CWE] | None
        OBX.17 - Observation Method (CWE) O rep S7.4.2.17 | 9999 - no table for CE

    obx_18 : list[EI] | None
        OBX.18 - Equipment Instance Identifier (EI) O rep S7.4.2.18

    obx_19 : str | None
        OBX.19 - Date/Time of the Analysis (DTM) O S7.4.2.19

    obx_20 : list[CWE] | None
        OBX.20 - Observation Site (CWE) O rep S7.4.2.20 | 0163 - Body site

    obx_21 : EI | None
        OBX.21 - Observation Instance Identifier (EI) O S7.4.2.21

    obx_22 : CNE | None
        OBX.22 - Mood Code (CNE) C S7.4.2.22 | 0725 - Mood Codes

    obx_23 : XON | None
        OBX.23 - Performing Organization Name (XON) O S7.4.2.23

    obx_24 : XAD | None
        OBX.24 - Performing Organization Address (XAD) O S7.4.2.24

    obx_25 : XCN | None
        OBX.25 - Performing Organization Medical Director (XCN) O S7.4.2.25
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
        description="C | Item #00570 | Table 0125 - Value type | LEN:3",
    )

    obx_3: CWE = Field(
        validation_alias=AliasChoices(
            "obx_3",
            "observation_identifier",
            "OBX.3",
        ),
        serialization_alias="OBX.3",
        title="Observation Identifier",
        description="R | Item #00571 | Table 9999 - no table for CE",
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

    obx_5: Optional[List[varies]] = Field(
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

    obx_6: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_6",
            "units",
            "OBX.6",
        ),
        serialization_alias="OBX.6",
        title="Units",
        description="O | Item #00574 | Table 9999 - no table for CE",
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

    obx_9: Optional[str] = Field(
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

    obx_10: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_10",
            "nature_of_abnormal_test",
            "OBX.10",
        ),
        serialization_alias="OBX.10",
        title="Nature of Abnormal Test",
        description=(
            "O | Item #00578 | Table 0080 - Nature of Abnormal Testing | LEN:2"
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

    obx_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_12",
            "effective_date_of_reference_range",
            "OBX.12",
        ),
        serialization_alias="OBX.12",
        title="Effective Date of Reference Range",
        description="O | Item #00580 | LEN:24",
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

    obx_14: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_14",
            "date_time_of_the_observation",
            "OBX.14",
        ),
        serialization_alias="OBX.14",
        title="Date/Time of the Observation",
        description="O | Item #00582 | LEN:24",
    )

    obx_15: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_15",
            "producer_s_id",
            "OBX.15",
        ),
        serialization_alias="OBX.15",
        title="Producer's ID",
        description="O | Item #00583 | Table 9999 - no table for CE",
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

    obx_17: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_17",
            "observation_method",
            "OBX.17",
        ),
        serialization_alias="OBX.17",
        title="Observation Method",
        description="O | Item #00936 | Table 9999 - no table for CE",
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

    obx_19: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_19",
            "date_time_of_the_analysis",
            "OBX.19",
        ),
        serialization_alias="OBX.19",
        title="Date/Time of the Analysis",
        description="O | Item #01480 | LEN:24",
    )

    obx_20: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_20",
            "observation_site",
            "OBX.20",
        ),
        serialization_alias="OBX.20",
        title="Observation Site",
        description="O | Item #02179 | Table 0163 - Body site",
    )

    obx_21: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_21",
            "observation_instance_identifier",
            "OBX.21",
        ),
        serialization_alias="OBX.21",
        title="Observation Instance Identifier",
        description="O | Item #02180",
    )

    obx_22: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_22",
            "mood_code",
            "OBX.22",
        ),
        serialization_alias="OBX.22",
        title="Mood Code",
        description="C | Item #02182 | Table 0725 - Mood Codes",
    )

    obx_23: Optional[XON] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_23",
            "performing_organization_name",
            "OBX.23",
        ),
        serialization_alias="OBX.23",
        title="Performing Organization Name",
        description="O | Item #02283",
    )

    obx_24: Optional[XAD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_24",
            "performing_organization_address",
            "OBX.24",
        ),
        serialization_alias="OBX.24",
        title="Performing Organization Address",
        description="O | Item #02284",
    )

    obx_25: Optional[XCN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_25",
            "performing_organization_medical_director",
            "OBX.25",
        ),
        serialization_alias="OBX.25",
        title="Performing Organization Medical Director",
        description="O | Item #02285",
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

    @field_validator("obx_12", "obx_14", "obx_19", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        if _RE_DTM.fullmatch(v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = ConfigDict(populate_by_name=True)
