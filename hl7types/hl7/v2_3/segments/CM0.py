"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: CM0
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.EI import EI
from ..datatypes.XAD import XAD
from ..datatypes.XCN import XCN
from ..datatypes.XTN import XTN

_RE_SI = re.compile(r'\d*')
_RE_DT = re.compile(r'(\d{4}([01]\d(\d{2})?)?)?')
_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class CM0(HL7Model):
    """Clinical Study Master (S8.10.2).

    Attributes
    ----------
    cm0_1 : str | None
        CM0.1 - CM0 - Set ID (SI) O S8.10.2

    cm0_2 : EI
        CM0.2 - Sponsor Study ID (EI) R S8.10.2.2

    cm0_3 : list[CE] | None
        CM0.3 - Alternate Study ID (CE) O rep S8.10.2.3

    cm0_4 : str
        CM0.4 - Title of Study (ST) R S8.10.2.4

    cm0_5 : XCN | None
        CM0.5 - Chairman of Study (XCN) O S8.10.2.5

    cm0_6 : str | None
        CM0.6 - Last IRB Approval Date (DT) O S8.10.2.6

    cm0_7 : str | None
        CM0.7 - Total Accrual to Date (NM) O S8.10.2.7

    cm0_8 : str | None
        CM0.8 - Last Accrual Date (DT) O S8.10.2.8

    cm0_9 : XCN | None
        CM0.9 - Contact for Study (XCN) O S8.10.2.9

    cm0_10 : XTN | None
        CM0.10 - Contact's Tel. Number (XTN) O S8.10.2.10

    cm0_11 : XAD | None
        CM0.11 - Contact's Address (XAD) O S8.10.2.11
    """

    cm0_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm0_1",
            "cm0_set_id",
            "CM0.1",
        ),
        serialization_alias="CM0.1",
        title="CM0 - Set ID",
        description="O | Item #01010 | LEN:4",
    )

    cm0_2: EI = Field(
        validation_alias=AliasChoices(
            "cm0_2",
            "sponsor_study_id",
            "CM0.2",
        ),
        serialization_alias="CM0.2",
        title="Sponsor Study ID",
        description="R | Item #01011",
    )

    cm0_3: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm0_3",
            "alternate_study_id",
            "CM0.3",
        ),
        serialization_alias="CM0.3",
        title="Alternate Study ID",
        description="O | Item #01012",
    )

    cm0_4: str = Field(
        validation_alias=AliasChoices(
            "cm0_4",
            "title_of_study",
            "CM0.4",
        ),
        serialization_alias="CM0.4",
        title="Title of Study",
        description="R | Item #01013 | LEN:300",
    )

    cm0_5: Optional[XCN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm0_5",
            "chairman_of_study",
            "CM0.5",
        ),
        serialization_alias="CM0.5",
        title="Chairman of Study",
        description="O | Item #01014",
    )

    cm0_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm0_6",
            "last_irb_approval_date",
            "CM0.6",
        ),
        serialization_alias="CM0.6",
        title="Last IRB Approval Date",
        description="O | Item #01015 | LEN:8",
    )

    cm0_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm0_7",
            "total_accrual_to_date",
            "CM0.7",
        ),
        serialization_alias="CM0.7",
        title="Total Accrual to Date",
        description="O | Item #01016 | LEN:8",
    )

    cm0_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm0_8",
            "last_accrual_date",
            "CM0.8",
        ),
        serialization_alias="CM0.8",
        title="Last Accrual Date",
        description="O | Item #01017 | LEN:8",
    )

    cm0_9: Optional[XCN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm0_9",
            "contact_for_study",
            "CM0.9",
        ),
        serialization_alias="CM0.9",
        title="Contact for Study",
        description="O | Item #01018",
    )

    cm0_10: Optional[XTN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm0_10",
            "contact_s_tel_number",
            "CM0.10",
        ),
        serialization_alias="CM0.10",
        title="Contact's Tel. Number",
        description="O | Item #01019",
    )

    cm0_11: Optional[XAD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm0_11",
            "contact_s_address",
            "CM0.11",
        ),
        serialization_alias="CM0.11",
        title="Contact's Address",
        description="O | Item #01020",
    )

    @field_validator("cm0_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        if not _RE_SI.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("cm0_6", "cm0_8", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        if not _RE_DT.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    @field_validator("cm0_7", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
