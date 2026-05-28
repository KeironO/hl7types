"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: ARV
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CNE import CNE
from ..datatypes.CWE import CWE
from ..datatypes.DR import DR


class ARV(BaseModel):
    """HL7 v2 ARV segment."""

    arv_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "arv_1",
            "set_id",
            "ARV.1",
        ),
        serialization_alias="ARV.1",
        title="Set ID",
        description="Item #2143",
    )

    arv_2: CNE = Field(
        default=...,
        validation_alias=AliasChoices(
            "arv_2",
            "access_restriction_action_code",
            "ARV.2",
        ),
        serialization_alias="ARV.2",
        title="Access Restriction Action Code",
        description="Item #2144 | Table HL70206",
    )

    arv_3: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "arv_3",
            "access_restriction_value",
            "ARV.3",
        ),
        serialization_alias="ARV.3",
        title="Access Restriction Value",
        description="Item #2145 | Table HL70717",
    )

    arv_4: list[CWE] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "arv_4",
            "access_restriction_reason",
            "ARV.4",
        ),
        serialization_alias="ARV.4",
        title="Access Restriction Reason",
        description="Item #2146 | Table HL70719",
    )

    arv_5: list[str] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "arv_5",
            "special_access_restriction_instructions",
            "ARV.5",
        ),
        serialization_alias="ARV.5",
        title="Special Access Restriction Instructions",
        description="Item #2147",
    )

    arv_6: DR | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "arv_6",
            "access_restriction_date_range",
            "ARV.6",
        ),
        serialization_alias="ARV.6",
        title="Access Restriction Date Range",
        description="Item #2148",
    )

    model_config = {"populate_by_name": True}
