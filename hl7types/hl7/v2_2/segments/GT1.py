"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: GT1
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.AD import AD
from ..datatypes.PN import PN


class GT1(HL7Model):
    """GUARANTOR (S6.4.4).

    Attributes
    ----------
    gt1_1 : str
        GT1.1 - Set ID - guarantor (SI) R S6.4.4.1

    gt1_2 : str | None
        GT1.2 - Guarantor number (CK) NA S6.4.4.2

    gt1_3 : PN
        GT1.3 - Guarantor name (PN) R S6.4.4.3

    gt1_4 : PN | None
        GT1.4 - Guarantor spouse name (PN) NA S6.4.4.4

    gt1_5 : AD | None
        GT1.5 - Guarantor address (AD) NA S6.4.4.5

    gt1_6 : list[str] | None
        GT1.6 - Guarantor phone number - home (TN) NA rep S6.4.4.6

    gt1_7 : list[str] | None
        GT1.7 - Guarantor phone number - business (TN) NA rep S6.4.4.7

    gt1_8 : str | None
        GT1.8 - Guarantor date of birth (DT) NA S6.4.4.8

    gt1_9 : str | None
        GT1.9 - Guarantor sex (ID) NA S6.4.4.9 | 0001 - SEX

    gt1_10 : str | None
        GT1.10 - Guarantor type (ID) NA S6.4.4.10 | 0068 - GUARANTOR TYPE

    gt1_11 : str | None
        GT1.11 - Guarantor relationship (ID) NA S6.4.4.11 | 0063 - RELATIONSHIP

    gt1_12 : str | None
        GT1.12 - Guarantor social security number (ST) NA S6.4.4.12

    gt1_13 : str | None
        GT1.13 - Guarantor date - begin (DT) NA S6.4.4.13

    gt1_14 : str | None
        GT1.14 - Guarantor date - end (DT) NA S6.4.4.14

    gt1_15 : str | None
        GT1.15 - Guarantor priority (NM) NA S6.4.4.15

    gt1_16 : str | None
        GT1.16 - Guarantor employer name (ST) NA S6.4.4.16

    gt1_17 : AD | None
        GT1.17 - Guarantor employer address (AD) NA S6.4.4.17

    gt1_18 : list[str] | None
        GT1.18 - Guarantor employ phone number (TN) NA rep S6.4.4.18

    gt1_19 : str | None
        GT1.19 - Guarantor employee ID number (ST) NA S6.4.4.19

    gt1_20 : str | None
        GT1.20 - Guarantor employment status (ID) NA S6.4.4.20 | 0066 - EMPLOYMENT STATUS

    gt1_21 : str | None
        GT1.21 - Guarantor organization (ST) NA S6.4.4.21
    """

    gt1_1: str = Field(
        validation_alias=AliasChoices(
            "gt1_1",
            "set_id_guarantor",
            "GT1.1",
        ),
        serialization_alias="GT1.1",
        title="Set ID - guarantor",
        description="R | Item #00405 | LEN:4",
    )

    gt1_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_2",
            "guarantor_number",
            "GT1.2",
        ),
        serialization_alias="GT1.2",
        title="Guarantor number",
        description="NA | Item #00406 | LEN:20",
    )

    gt1_3: PN = Field(
        validation_alias=AliasChoices(
            "gt1_3",
            "guarantor_name",
            "GT1.3",
        ),
        serialization_alias="GT1.3",
        title="Guarantor name",
        description="R | Item #00407",
    )

    gt1_4: Optional[PN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_4",
            "guarantor_spouse_name",
            "GT1.4",
        ),
        serialization_alias="GT1.4",
        title="Guarantor spouse name",
        description="NA | Item #00408",
    )

    gt1_5: Optional[AD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_5",
            "guarantor_address",
            "GT1.5",
        ),
        serialization_alias="GT1.5",
        title="Guarantor address",
        description="NA | Item #00409",
    )

    gt1_6: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_6",
            "guarantor_phone_number_home",
            "GT1.6",
        ),
        serialization_alias="GT1.6",
        title="Guarantor phone number - home",
        description="NA | Item #00410 | LEN:40",
    )

    gt1_7: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_7",
            "guarantor_phone_number_business",
            "GT1.7",
        ),
        serialization_alias="GT1.7",
        title="Guarantor phone number - business",
        description="NA | Item #00411 | LEN:40",
    )

    gt1_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_8",
            "guarantor_date_of_birth",
            "GT1.8",
        ),
        serialization_alias="GT1.8",
        title="Guarantor date of birth",
        description="NA | Item #00412 | LEN:8",
    )

    gt1_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_9",
            "guarantor_sex",
            "GT1.9",
        ),
        serialization_alias="GT1.9",
        title="Guarantor sex",
        description="NA | Item #00413 | Table 0001 - SEX | LEN:1",
    )

    gt1_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_10",
            "guarantor_type",
            "GT1.10",
        ),
        serialization_alias="GT1.10",
        title="Guarantor type",
        description="NA | Item #00414 | Table 0068 - GUARANTOR TYPE | LEN:2",
    )

    gt1_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_11",
            "guarantor_relationship",
            "GT1.11",
        ),
        serialization_alias="GT1.11",
        title="Guarantor relationship",
        description="NA | Item #00415 | Table 0063 - RELATIONSHIP | LEN:2",
    )

    gt1_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_12",
            "guarantor_social_security_number",
            "GT1.12",
        ),
        serialization_alias="GT1.12",
        title="Guarantor social security number",
        description="NA | Item #00416 | LEN:11",
    )

    gt1_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_13",
            "guarantor_date_begin",
            "GT1.13",
        ),
        serialization_alias="GT1.13",
        title="Guarantor date - begin",
        description="NA | Item #00417 | LEN:8",
    )

    gt1_14: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_14",
            "guarantor_date_end",
            "GT1.14",
        ),
        serialization_alias="GT1.14",
        title="Guarantor date - end",
        description="NA | Item #00418 | LEN:8",
    )

    gt1_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_15",
            "guarantor_priority",
            "GT1.15",
        ),
        serialization_alias="GT1.15",
        title="Guarantor priority",
        description="NA | Item #00419 | LEN:2",
    )

    gt1_16: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_16",
            "guarantor_employer_name",
            "GT1.16",
        ),
        serialization_alias="GT1.16",
        title="Guarantor employer name",
        description="NA | Item #00420 | LEN:45",
    )

    gt1_17: Optional[AD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_17",
            "guarantor_employer_address",
            "GT1.17",
        ),
        serialization_alias="GT1.17",
        title="Guarantor employer address",
        description="NA | Item #00421",
    )

    gt1_18: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_18",
            "guarantor_employ_phone_number",
            "GT1.18",
        ),
        serialization_alias="GT1.18",
        title="Guarantor employ phone number",
        description="NA | Item #00422 | LEN:40",
    )

    gt1_19: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_19",
            "guarantor_employee_id_number",
            "GT1.19",
        ),
        serialization_alias="GT1.19",
        title="Guarantor employee ID number",
        description="NA | Item #00423 | LEN:20",
    )

    gt1_20: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_20",
            "guarantor_employment_status",
            "GT1.20",
        ),
        serialization_alias="GT1.20",
        title="Guarantor employment status",
        description="NA | Item #00424 | Table 0066 - EMPLOYMENT STATUS | LEN:2",
    )

    gt1_21: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_21",
            "guarantor_organization",
            "GT1.21",
        ),
        serialization_alias="GT1.21",
        title="Guarantor organization",
        description="NA | Item #00425 | LEN:60",
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
