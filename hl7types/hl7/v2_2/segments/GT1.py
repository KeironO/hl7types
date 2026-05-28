"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: GT1
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.AD import AD
from ..datatypes.PN import PN


class GT1(BaseModel):
    """HL7 v2 GT1 segment."""

    gt1_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "gt1_1",
            "set_id_guarantor",
            "GT1.1",
        ),
        serialization_alias="GT1.1",
        title="Set ID - guarantor",
        description="Item #405",
    )

    gt1_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_2",
            "guarantor_number",
            "GT1.2",
        ),
        serialization_alias="GT1.2",
        title="Guarantor number",
        description="Item #406",
    )

    gt1_3: PN = Field(
        default=...,
        validation_alias=AliasChoices(
            "gt1_3",
            "guarantor_name",
            "GT1.3",
        ),
        serialization_alias="GT1.3",
        title="Guarantor name",
        description="Item #407",
    )

    gt1_4: PN | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_4",
            "guarantor_spouse_name",
            "GT1.4",
        ),
        serialization_alias="GT1.4",
        title="Guarantor spouse name",
        description="Item #408",
    )

    gt1_5: AD | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_5",
            "guarantor_address",
            "GT1.5",
        ),
        serialization_alias="GT1.5",
        title="Guarantor address",
        description="Item #409",
    )

    gt1_6: list[str] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_6",
            "guarantor_phone_number_home",
            "GT1.6",
        ),
        serialization_alias="GT1.6",
        title="Guarantor phone number - home",
        description="Item #410",
    )

    gt1_7: list[str] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_7",
            "guarantor_phone_number_business",
            "GT1.7",
        ),
        serialization_alias="GT1.7",
        title="Guarantor phone number - business",
        description="Item #411",
    )

    gt1_8: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_8",
            "guarantor_date_of_birth",
            "GT1.8",
        ),
        serialization_alias="GT1.8",
        title="Guarantor date of birth",
        description="Item #412",
    )

    gt1_9: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_9",
            "guarantor_sex",
            "GT1.9",
        ),
        serialization_alias="GT1.9",
        title="Guarantor sex",
        description="Item #413 | Table HL70001",
    )

    gt1_10: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_10",
            "guarantor_type",
            "GT1.10",
        ),
        serialization_alias="GT1.10",
        title="Guarantor type",
        description="Item #414 | Table HL70068",
    )

    gt1_11: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_11",
            "guarantor_relationship",
            "GT1.11",
        ),
        serialization_alias="GT1.11",
        title="Guarantor relationship",
        description="Item #415 | Table HL70063",
    )

    gt1_12: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_12",
            "guarantor_social_security_number",
            "GT1.12",
        ),
        serialization_alias="GT1.12",
        title="Guarantor social security number",
        description="Item #416",
    )

    gt1_13: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_13",
            "guarantor_date_begin",
            "GT1.13",
        ),
        serialization_alias="GT1.13",
        title="Guarantor date - begin",
        description="Item #417",
    )

    gt1_14: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_14",
            "guarantor_date_end",
            "GT1.14",
        ),
        serialization_alias="GT1.14",
        title="Guarantor date - end",
        description="Item #418",
    )

    gt1_15: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_15",
            "guarantor_priority",
            "GT1.15",
        ),
        serialization_alias="GT1.15",
        title="Guarantor priority",
        description="Item #419",
    )

    gt1_16: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_16",
            "guarantor_employer_name",
            "GT1.16",
        ),
        serialization_alias="GT1.16",
        title="Guarantor employer name",
        description="Item #420",
    )

    gt1_17: AD | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_17",
            "guarantor_employer_address",
            "GT1.17",
        ),
        serialization_alias="GT1.17",
        title="Guarantor employer address",
        description="Item #421",
    )

    gt1_18: list[str] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_18",
            "guarantor_employ_phone_number",
            "GT1.18",
        ),
        serialization_alias="GT1.18",
        title="Guarantor employ phone number",
        description="Item #422",
    )

    gt1_19: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_19",
            "guarantor_employee_id_number",
            "GT1.19",
        ),
        serialization_alias="GT1.19",
        title="Guarantor employee ID number",
        description="Item #423",
    )

    gt1_20: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_20",
            "guarantor_employment_status",
            "GT1.20",
        ),
        serialization_alias="GT1.20",
        title="Guarantor employment status",
        description="Item #424 | Table HL70066",
    )

    gt1_21: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "gt1_21",
            "guarantor_organization",
            "GT1.21",
        ),
        serialization_alias="GT1.21",
        title="Guarantor organization",
        description="Item #425",
    )

    model_config = {"populate_by_name": True}
