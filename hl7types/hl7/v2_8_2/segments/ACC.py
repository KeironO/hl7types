"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: ACC
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, ValidationInfo, field_validator
from hl7types.hl7 import HL7Model
from hl7types.hl7._validators import _apply_dt_fallback

from ..datatypes.CWE import CWE
from ..datatypes.EI import EI
from ..datatypes.XAD import XAD
from ..datatypes.XCN import XCN

_RE_DTM = re.compile(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?')
_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class ACC(HL7Model):
    """Accident (S6.5.9).

    Attributes
    ----------
    acc_1 : str | None
        ACC.1 - Accident Date/Time (DTM) O S6.5.9.1

    acc_2 : CWE | None
        ACC.2 - Accident Code (CWE) O S6.5.9.2 | 0050 - Accident Code

    acc_3 : str | None
        ACC.3 - Accident Location (ST) O S6.5.9.3

    acc_4 : CWE | None
        ACC.4 - Auto Accident State (CWE) O S6.5.9.4 | 0347 - State/Province

    acc_5 : str | None
        ACC.5 - Accident Job Related Indicator (ID) O S6.5.9.5 | 0136 - Yes/no Indicator

    acc_6 : str | None
        ACC.6 - Accident Death Indicator (ID) O S6.5.9.6 | 0136 - Yes/no Indicator

    acc_7 : XCN | None
        ACC.7 - Entered By (XCN) O S2.14.10.5

    acc_8 : str | None
        ACC.8 - Accident Description (ST) O S6.5.9.8

    acc_9 : str | None
        ACC.9 - Brought In By (ST) O S6.5.9.9

    acc_10 : str | None
        ACC.10 - Police Notified Indicator (ID) O S6.5.9.10 | 0136 - Yes/no Indicator

    acc_11 : XAD | None
        ACC.11 - Accident Address (XAD) O S6.5.9.11

    acc_12 : str | None
        ACC.12 - Degree of patient liability (NM) O S6.5.9.12

    acc_13 : list[EI] | None
        ACC.13 - Accident Identifier (EI) O rep S6.5.9.13
    """

    acc_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "acc_1",
            "accident_date_time",
            "ACC.1",
        ),
        serialization_alias="ACC.1",
        title="Accident Date/Time",
        description="O | Item #00527",
    )

    acc_2: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "acc_2",
            "accident_code",
            "ACC.2",
        ),
        serialization_alias="ACC.2",
        title="Accident Code",
        description="O | Item #00528 | Table 0050 - Accident Code",
    )

    acc_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "acc_3",
            "accident_location",
            "ACC.3",
        ),
        serialization_alias="ACC.3",
        title="Accident Location",
        description="O | Item #00529",
    )

    acc_4: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "acc_4",
            "auto_accident_state",
            "ACC.4",
        ),
        serialization_alias="ACC.4",
        title="Auto Accident State",
        description="O | Item #00812 | Table 0347 - State/Province",
    )

    acc_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "acc_5",
            "accident_job_related_indicator",
            "ACC.5",
        ),
        serialization_alias="ACC.5",
        title="Accident Job Related Indicator",
        description="O | Item #00813 | Table 0136 - Yes/no Indicator | LEN:1",
    )

    acc_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "acc_6",
            "accident_death_indicator",
            "ACC.6",
        ),
        serialization_alias="ACC.6",
        title="Accident Death Indicator",
        description="O | Item #00814 | Table 0136 - Yes/no Indicator | LEN:1",
    )

    acc_7: Optional[XCN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "acc_7",
            "entered_by",
            "ACC.7",
        ),
        serialization_alias="ACC.7",
        title="Entered By",
        description="O | Item #00224",
    )

    acc_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "acc_8",
            "accident_description",
            "ACC.8",
        ),
        serialization_alias="ACC.8",
        title="Accident Description",
        description="O | Item #01503",
    )

    acc_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "acc_9",
            "brought_in_by",
            "ACC.9",
        ),
        serialization_alias="ACC.9",
        title="Brought In By",
        description="O | Item #01504",
    )

    acc_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "acc_10",
            "police_notified_indicator",
            "ACC.10",
        ),
        serialization_alias="ACC.10",
        title="Police Notified Indicator",
        description="O | Item #01505 | Table 0136 - Yes/no Indicator | LEN:1",
    )

    acc_11: Optional[XAD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "acc_11",
            "accident_address",
            "ACC.11",
        ),
        serialization_alias="ACC.11",
        title="Accident Address",
        description="O | Item #01853",
    )

    acc_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "acc_12",
            "degree_of_patient_liability",
            "ACC.12",
        ),
        serialization_alias="ACC.12",
        title="Degree of patient liability",
        description="O | Item #02374",
    )

    acc_13: Optional[List[EI]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "acc_13",
            "accident_identifier",
            "ACC.13",
        ),
        serialization_alias="ACC.13",
        title="Accident Identifier",
        description="O | Item #03338",
    )

    @field_validator("acc_1", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        if _RE_DTM.fullmatch(v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    @field_validator("acc_12", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
