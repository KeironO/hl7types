"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: GT1
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

_RE_SI = re.compile(r'\d*')
_RE_DT = re.compile(r'(\d{4}([01]\d(\d{2})?)?)?')
_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class GT1(HL7Model):
    """GUARANTOR (S6.3.4).

    Attributes
    ----------
    gt1_1 : str
        GT1.1 - SET ID - GUARANTOR (SI) R S6-8

    gt1_2 : str | None
        GT1.2 - GUARANTOR NUMBER (ID) O

    gt1_3 : str
        GT1.3 - GUARANTOR NAME (PN) R

    gt1_4 : str | None
        GT1.4 - GUARANTOR SPOUSE NAME (PN) O

    gt1_5 : str | None
        GT1.5 - GUARANTOR ADDRESS (AD) O

    gt1_6 : str | None
        GT1.6 - GUARANTOR PH. NUM.- HOME (TN) O

    gt1_7 : str | None
        GT1.7 - GUARANTOR PH. NUM-BUSINESS (TN) O

    gt1_8 : str | None
        GT1.8 - GUARANTOR DATE OF BIRTH (DT) O

    gt1_9 : str | None
        GT1.9 - GUARANTOR SEX (ID) O | 0001 - SEX

    gt1_10 : str | None
        GT1.10 - GUARANTOR TYPE (ID) O | 0068 - GUARANTOR TYPE

    gt1_11 : str | None
        GT1.11 - GUARANTOR RELATIONSHIP (ID) O | 0063 - RELATIONSHIP

    gt1_12 : str | None
        GT1.12 - GUARANTOR SSN (ST) O

    gt1_13 : str | None
        GT1.13 - GUARANTOR DATE - BEGIN (DT) O

    gt1_14 : str | None
        GT1.14 - GUARANTOR DATE - END (DT) O

    gt1_15 : str | None
        GT1.15 - GUARANTOR PRIORITY (NM) O

    gt1_16 : str | None
        GT1.16 - GUARANTOR EMPLOYER NAME (ST) O

    gt1_17 : str | None
        GT1.17 - GUARANTOR EMPLOYER ADDRESS (AD) O

    gt1_18 : str | None
        GT1.18 - GUARANTOR EMPLOY PHONE # (TN) O

    gt1_19 : str | None
        GT1.19 - GUARANTOR EMPLOYEE ID NUM (ST) O

    gt1_20 : str | None
        GT1.20 - GUARANTOR EMPLOYMENT STATUS (ID) O | 0066 - EMPLOYMENT STATUS
    """

    gt1_1: str = Field(
        validation_alias=AliasChoices(
            "gt1_1",
            "set_id_guarantor",
            "GT1.1",
        ),
        serialization_alias="GT1.1",
        title="SET ID - GUARANTOR",
        description="R | Item #00321 | LEN:4",
    )

    gt1_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_2",
            "guarantor_number",
            "GT1.2",
        ),
        serialization_alias="GT1.2",
        title="GUARANTOR NUMBER",
        description="O | Item #00322 | LEN:20",
    )

    gt1_3: str = Field(
        validation_alias=AliasChoices(
            "gt1_3",
            "guarantor_name",
            "GT1.3",
        ),
        serialization_alias="GT1.3",
        title="GUARANTOR NAME",
        description="R | Item #00323 | LEN:48",
    )

    gt1_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_4",
            "guarantor_spouse_name",
            "GT1.4",
        ),
        serialization_alias="GT1.4",
        title="GUARANTOR SPOUSE NAME",
        description="O | Item #00707 | LEN:48",
    )

    gt1_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_5",
            "guarantor_address",
            "GT1.5",
        ),
        serialization_alias="GT1.5",
        title="GUARANTOR ADDRESS",
        description="O | Item #00324 | LEN:106",
    )

    gt1_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_6",
            "guarantor_ph_num_home",
            "GT1.6",
        ),
        serialization_alias="GT1.6",
        title="GUARANTOR PH. NUM.- HOME",
        description="O | Item #00329 | LEN:40",
    )

    gt1_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_7",
            "guarantor_ph_num_business",
            "GT1.7",
        ),
        serialization_alias="GT1.7",
        title="GUARANTOR PH. NUM-BUSINESS",
        description="O | Item #00330 | LEN:40",
    )

    gt1_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_8",
            "guarantor_date_of_birth",
            "GT1.8",
        ),
        serialization_alias="GT1.8",
        title="GUARANTOR DATE OF BIRTH",
        description="O | Item #00331 | LEN:8",
    )

    gt1_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_9",
            "guarantor_sex",
            "GT1.9",
        ),
        serialization_alias="GT1.9",
        title="GUARANTOR SEX",
        description="O | Item #00332 | Table 0001 - SEX | LEN:1",
    )

    gt1_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_10",
            "guarantor_type",
            "GT1.10",
        ),
        serialization_alias="GT1.10",
        title="GUARANTOR TYPE",
        description="O | Item #00333 | Table 0068 - GUARANTOR TYPE | LEN:2",
    )

    gt1_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_11",
            "guarantor_relationship",
            "GT1.11",
        ),
        serialization_alias="GT1.11",
        title="GUARANTOR RELATIONSHIP",
        description="O | Item #00334 | Table 0063 - RELATIONSHIP | LEN:2",
    )

    gt1_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_12",
            "guarantor_ssn",
            "GT1.12",
        ),
        serialization_alias="GT1.12",
        title="GUARANTOR SSN",
        description="O | Item #00335 | LEN:11",
    )

    gt1_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_13",
            "guarantor_date_begin",
            "GT1.13",
        ),
        serialization_alias="GT1.13",
        title="GUARANTOR DATE - BEGIN",
        description="O | Item #00338 | LEN:8",
    )

    gt1_14: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_14",
            "guarantor_date_end",
            "GT1.14",
        ),
        serialization_alias="GT1.14",
        title="GUARANTOR DATE - END",
        description="O | Item #00339 | LEN:8",
    )

    gt1_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_15",
            "guarantor_priority",
            "GT1.15",
        ),
        serialization_alias="GT1.15",
        title="GUARANTOR PRIORITY",
        description="O | Item #00340 | LEN:2",
    )

    gt1_16: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_16",
            "guarantor_employer_name",
            "GT1.16",
        ),
        serialization_alias="GT1.16",
        title="GUARANTOR EMPLOYER NAME",
        description="O | Item #00341 | LEN:45",
    )

    gt1_17: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_17",
            "guarantor_employer_address",
            "GT1.17",
        ),
        serialization_alias="GT1.17",
        title="GUARANTOR EMPLOYER ADDRESS",
        description="O | Item #00342 | LEN:106",
    )

    gt1_18: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_18",
            "guarantor_employ_phone",
            "GT1.18",
        ),
        serialization_alias="GT1.18",
        title="GUARANTOR EMPLOY PHONE #",
        description="O | Item #00347 | LEN:40",
    )

    gt1_19: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_19",
            "guarantor_employee_id_num",
            "GT1.19",
        ),
        serialization_alias="GT1.19",
        title="GUARANTOR EMPLOYEE ID NUM",
        description="O | Item #00391 | LEN:20",
    )

    gt1_20: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_20",
            "guarantor_employment_status",
            "GT1.20",
        ),
        serialization_alias="GT1.20",
        title="GUARANTOR EMPLOYMENT STATUS",
        description="O | Item #00392 | Table 0066 - EMPLOYMENT STATUS | LEN:2",
    )

    @field_validator("gt1_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        if not _RE_SI.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("gt1_8", "gt1_13", "gt1_14", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        if not _RE_DT.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    @field_validator("gt1_15", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
