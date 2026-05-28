"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: NK1
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.AD import AD
from ..datatypes.CE import CE
from ..datatypes.PN import PN


class NK1(BaseModel):
    """HL7 v2 NK1 segment."""

    nk1_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "nk1_1",
            "set_id_next_of_kin",
            "NK1.1",
        ),
        serialization_alias="NK1.1",
        title="Set ID - Next of Kin",
        description="Item #190",
    )

    nk1_2: Optional[PN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_2",
            "name",
            "NK1.2",
        ),
        serialization_alias="NK1.2",
        title="Name",
        description="Item #191",
    )

    nk1_3: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_3",
            "relationship",
            "NK1.3",
        ),
        serialization_alias="NK1.3",
        title="Relationship",
        description="Item #192 | Table HL70063",
    )

    nk1_4: Optional[AD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_4",
            "address",
            "NK1.4",
        ),
        serialization_alias="NK1.4",
        title="Address",
        description="Item #193",
    )

    nk1_5: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_5",
            "phone_number",
            "NK1.5",
        ),
        serialization_alias="NK1.5",
        title="Phone Number",
        description="Item #194",
    )

    nk1_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_6",
            "business_phone_number",
            "NK1.6",
        ),
        serialization_alias="NK1.6",
        title="Business Phone Number",
        description="Item #195",
    )

    nk1_7: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_7",
            "contact_role",
            "NK1.7",
        ),
        serialization_alias="NK1.7",
        title="Contact Role",
        description="Item #196 | Table HL70131",
    )

    nk1_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_8",
            "start_date",
            "NK1.8",
        ),
        serialization_alias="NK1.8",
        title="Start Date",
        description="Item #197",
    )

    nk1_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_9",
            "end_date",
            "NK1.9",
        ),
        serialization_alias="NK1.9",
        title="End Date",
        description="Item #198",
    )

    nk1_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_10",
            "next_of_kin",
            "NK1.10",
        ),
        serialization_alias="NK1.10",
        title="Next of Kin",
        description="Item #199",
    )

    nk1_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_11",
            "next_of_kin_job_code_class",
            "NK1.11",
        ),
        serialization_alias="NK1.11",
        title="Next of kin job code / class",
        description="Item #200",
    )

    nk1_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_12",
            "next_of_kin_employee_number",
            "NK1.12",
        ),
        serialization_alias="NK1.12",
        title="Next of Kin Employee Number",
        description="Item #201",
    )

    nk1_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "nk1_13",
            "organization_name",
            "NK1.13",
        ),
        serialization_alias="NK1.13",
        title="Organization Name",
        description="Item #202",
    )

    model_config = {"populate_by_name": True}
