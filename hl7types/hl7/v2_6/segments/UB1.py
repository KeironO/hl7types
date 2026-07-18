"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: UB1
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE
from ..datatypes.OCD import OCD
from ..datatypes.UVC import UVC

_RE_SI = re.compile(r'\d*')
_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')
_RE_DT = re.compile(r'(\d{4}([01]\d(\d{2})?)?)?')


class UB1(HL7Model):
    """UB82 (S6.5.10).

    Attributes
    ----------
    ub1_1 : str | None
        UB1.1 - Set ID - UB1 (SI) O S6.5.10.1

    ub1_3 : str | None
        UB1.3 - Blood Furnished-Pints (NM) O S6.5.10.3

    ub1_4 : str | None
        UB1.4 - Blood Replaced-Pints (NM) O S6.5.10.4

    ub1_5 : str | None
        UB1.5 - Blood Not Replaced-Pints (NM) O S6.5.10.5

    ub1_6 : str | None
        UB1.6 - Co-Insurance Days (NM) O S6.5.10.6

    ub1_7 : list[str] | None
        UB1.7 - Condition Code (IS) O rep S6.5.10.7 | 0043 - Condition Code

    ub1_8 : str | None
        UB1.8 - Covered Days (NM) O S6.5.10.8

    ub1_9 : str | None
        UB1.9 - Non Covered Days (NM) O S6.5.10.9

    ub1_10 : list[UVC] | None
        UB1.10 - Value Amount & Code (UVC) O rep S6.5.10.10

    ub1_11 : str | None
        UB1.11 - Number Of Grace Days (NM) O S6.5.10.11

    ub1_12 : CWE | None
        UB1.12 - Special Program Indicator (CWE) O S6.5.10.12 | 0348 - Special Program Indicator

    ub1_13 : CWE | None
        UB1.13 - PSRO/UR Approval Indicator (CWE) O S6.5.10.13 | 0349 - PSRO/UR Approval Indicator

    ub1_14 : str | None
        UB1.14 - PSRO/UR Approved Stay-Fm (DT) O S6.5.10.14

    ub1_15 : str | None
        UB1.15 - PSRO/UR Approved Stay-To (DT) O S6.5.10.15

    ub1_16 : list[OCD] | None
        UB1.16 - Occurrence (OCD) O rep S6.5.10.16

    ub1_17 : CWE | None
        UB1.17 - Occurrence Span (CWE) O S6.5.10.17 | 0351 - Occurrence span

    ub1_18 : str | None
        UB1.18 - Occur Span Start Date (DT) O S6.5.10.18

    ub1_19 : str | None
        UB1.19 - Occur Span End Date (DT) O S6.5.10.19

    ub1_20 : str | None
        UB1.20 - UB-82 Locator 2 (ST) O S6.5.10.20

    ub1_21 : str | None
        UB1.21 - UB-82 Locator 9 (ST) O S6.5.10.21

    ub1_22 : str | None
        UB1.22 - UB-82 Locator 27 (ST) O S6.5.10.22

    ub1_23 : str | None
        UB1.23 - UB-82 Locator 45 (ST) O S6.5.10.23
    """

    ub1_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_1",
            "set_id_ub1",
            "UB1.1",
        ),
        serialization_alias="UB1.1",
        title="Set ID - UB1",
        description="O | Item #00530 | LEN:4",
    )

    ub1_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_3",
            "blood_furnished_pints",
            "UB1.3",
        ),
        serialization_alias="UB1.3",
        title="Blood Furnished-Pints",
        description="O | Item #00532 | LEN:2",
    )

    ub1_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_4",
            "blood_replaced_pints",
            "UB1.4",
        ),
        serialization_alias="UB1.4",
        title="Blood Replaced-Pints",
        description="O | Item #00533 | LEN:2",
    )

    ub1_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_5",
            "blood_not_replaced_pints",
            "UB1.5",
        ),
        serialization_alias="UB1.5",
        title="Blood Not Replaced-Pints",
        description="O | Item #00534 | LEN:2",
    )

    ub1_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_6",
            "co_insurance_days",
            "UB1.6",
        ),
        serialization_alias="UB1.6",
        title="Co-Insurance Days",
        description="O | Item #00535",
    )

    ub1_7: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_7",
            "condition_code",
            "UB1.7",
        ),
        serialization_alias="UB1.7",
        title="Condition Code",
        description="O | Item #00536 | Table 0043 - Condition Code",
    )

    ub1_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_8",
            "covered_days",
            "UB1.8",
        ),
        serialization_alias="UB1.8",
        title="Covered Days",
        description="O | Item #00537",
    )

    ub1_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_9",
            "non_covered_days",
            "UB1.9",
        ),
        serialization_alias="UB1.9",
        title="Non Covered Days",
        description="O | Item #00538",
    )

    ub1_10: Optional[List[UVC]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_10",
            "value_amount_code",
            "UB1.10",
        ),
        serialization_alias="UB1.10",
        title="Value Amount & Code",
        description="O | Item #00539",
    )

    ub1_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_11",
            "number_of_grace_days",
            "UB1.11",
        ),
        serialization_alias="UB1.11",
        title="Number Of Grace Days",
        description="O | Item #00540 | LEN:2",
    )

    ub1_12: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_12",
            "special_program_indicator",
            "UB1.12",
        ),
        serialization_alias="UB1.12",
        title="Special Program Indicator",
        description="O | Item #00541 | Table 0348 - Special Program Indicator",
    )

    ub1_13: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_13",
            "psro_ur_approval_indicator",
            "UB1.13",
        ),
        serialization_alias="UB1.13",
        title="PSRO/UR Approval Indicator",
        description="O | Item #00542 | Table 0349 - PSRO/UR Approval Indicator",
    )

    ub1_14: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_14",
            "psro_ur_approved_stay_fm",
            "UB1.14",
        ),
        serialization_alias="UB1.14",
        title="PSRO/UR Approved Stay-Fm",
        description="O | Item #00543 | LEN:8",
    )

    ub1_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_15",
            "psro_ur_approved_stay_to",
            "UB1.15",
        ),
        serialization_alias="UB1.15",
        title="PSRO/UR Approved Stay-To",
        description="O | Item #00544 | LEN:8",
    )

    ub1_16: Optional[List[OCD]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_16",
            "occurrence",
            "UB1.16",
        ),
        serialization_alias="UB1.16",
        title="Occurrence",
        description="O | Item #00545",
    )

    ub1_17: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_17",
            "occurrence_span",
            "UB1.17",
        ),
        serialization_alias="UB1.17",
        title="Occurrence Span",
        description="O | Item #00546 | Table 0351 - Occurrence span",
    )

    ub1_18: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_18",
            "occur_span_start_date",
            "UB1.18",
        ),
        serialization_alias="UB1.18",
        title="Occur Span Start Date",
        description="O | Item #00547",
    )

    ub1_19: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_19",
            "occur_span_end_date",
            "UB1.19",
        ),
        serialization_alias="UB1.19",
        title="Occur Span End Date",
        description="O | Item #00548",
    )

    ub1_20: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_20",
            "ub_82_locator_2",
            "UB1.20",
        ),
        serialization_alias="UB1.20",
        title="UB-82 Locator 2",
        description="O | Item #00549",
    )

    ub1_21: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_21",
            "ub_82_locator_9",
            "UB1.21",
        ),
        serialization_alias="UB1.21",
        title="UB-82 Locator 9",
        description="O | Item #00550",
    )

    ub1_22: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_22",
            "ub_82_locator_27",
            "UB1.22",
        ),
        serialization_alias="UB1.22",
        title="UB-82 Locator 27",
        description="O | Item #00551",
    )

    ub1_23: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ub1_23",
            "ub_82_locator_45",
            "UB1.23",
        ),
        serialization_alias="UB1.23",
        title="UB-82 Locator 45",
        description="O | Item #00552",
    )

    @field_validator("ub1_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        if not _RE_SI.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("ub1_3", "ub1_4", "ub1_5", "ub1_6", "ub1_8", "ub1_9", "ub1_11", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    @field_validator("ub1_14", "ub1_15", "ub1_18", "ub1_19", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        if not _RE_DT.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    model_config = ConfigDict(populate_by_name=True)
