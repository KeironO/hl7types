"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: AFF
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.DR import DR
from ..datatypes.XAD import XAD
from ..datatypes.XON import XON


class AFF(BaseModel):
    """HL7 v2 AFF segment."""

    aff_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "aff_1",
            "set_id_aff",
            "AFF.1",
        ),
        serialization_alias="AFF.1",
        title="Set ID - AFF",
        description="Item #1427",
    )

    aff_2: XON = Field(
        default=...,
        validation_alias=AliasChoices(
            "aff_2",
            "professional_organization",
            "AFF.2",
        ),
        serialization_alias="AFF.2",
        title="Professional Organization",
        description="Item #1444",
    )

    aff_3: Optional[XAD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aff_3",
            "professional_organization_address",
            "AFF.3",
        ),
        serialization_alias="AFF.3",
        title="Professional Organization Address",
        description="Item #1445",
    )

    aff_4: Optional[List[DR]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aff_4",
            "professional_organization_affiliation_date_range",
            "AFF.4",
        ),
        serialization_alias="AFF.4",
        title="Professional Organization Affiliation Date Range",
        description="Item #1446",
    )

    aff_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aff_5",
            "professional_affiliation_additional_information",
            "AFF.5",
        ),
        serialization_alias="AFF.5",
        title="Professional Affiliation Additional Information",
        description="Item #1447",
    )

    model_config = {"populate_by_name": True}
