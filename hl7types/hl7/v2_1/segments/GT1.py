"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: GT1
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator


class GT1(HL7Model):
    """HL7 v2 GT1 segment.

    Attributes
    ----------
    gt1_1 : str
        GT1.1 (req) - SET ID - GUARANTOR (SI)

    gt1_2 : str | None
        GT1.2 (opt) - GUARANTOR NUMBER (ID)

    gt1_3 : str
        GT1.3 (req) - GUARANTOR NAME (PN)

    gt1_4 : str | None
        GT1.4 (opt) - GUARANTOR SPOUSE NAME (PN)

    gt1_5 : str | None
        GT1.5 (opt) - GUARANTOR ADDRESS (AD)

    gt1_6 : str | None
        GT1.6 (opt) - GUARANTOR PH. NUM.- HOME (TN)

    gt1_7 : str | None
        GT1.7 (opt) - GUARANTOR PH. NUM-BUSINESS (TN)

    gt1_8 : str | None
        GT1.8 (opt) - GUARANTOR DATE OF BIRTH (DT)

    gt1_9 : str | None
        GT1.9 (opt) - GUARANTOR SEX (ID)

    gt1_10 : str | None
        GT1.10 (opt) - GUARANTOR TYPE (ID)

    gt1_11 : str | None
        GT1.11 (opt) - GUARANTOR RELATIONSHIP (ID)

    gt1_12 : str | None
        GT1.12 (opt) - GUARANTOR SSN (ST)

    gt1_13 : str | None
        GT1.13 (opt) - GUARANTOR DATE - BEGIN (DT)

    gt1_14 : str | None
        GT1.14 (opt) - GUARANTOR DATE - END (DT)

    gt1_15 : str | None
        GT1.15 (opt) - GUARANTOR PRIORITY (NM)

    gt1_16 : str | None
        GT1.16 (opt) - GUARANTOR EMPLOYER NAME (ST)

    gt1_17 : str | None
        GT1.17 (opt) - GUARANTOR EMPLOYER ADDRESS (AD)

    gt1_18 : str | None
        GT1.18 (opt) - GUARANTOR EMPLOY PHONE # (TN)

    gt1_19 : str | None
        GT1.19 (opt) - GUARANTOR EMPLOYEE ID NUM (ST)

    gt1_20 : str | None
        GT1.20 (opt) - GUARANTOR EMPLOYMENT STATUS (ID)
    """

    gt1_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "gt1_1",
            "set_id_guarantor",
            "GT1.1",
        ),
        serialization_alias="GT1.1",
        title="SET ID - GUARANTOR",
        description="Item #321",
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
        description="Item #322",
    )

    gt1_3: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "gt1_3",
            "guarantor_name",
            "GT1.3",
        ),
        serialization_alias="GT1.3",
        title="GUARANTOR NAME",
        description="Item #323",
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
        description="Item #707",
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
        description="Item #324",
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
        description="Item #329",
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
        description="Item #330",
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
        description="Item #331",
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
        description="Item #332 | Table HL70001",
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
        description="Item #333 | Table HL70068",
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
        description="Item #334 | Table HL70063",
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
        description="Item #335",
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
        description="Item #338",
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
        description="Item #339",
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
        description="Item #340",
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
        description="Item #341",
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
        description="Item #342",
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
        description="Item #347",
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
        description="Item #391",
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
        description="Item #392 | Table HL70066",
    )

    @field_validator("gt1_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("gt1_8", "gt1_13", "gt1_14", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2})?)?)?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    @field_validator("gt1_15", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
