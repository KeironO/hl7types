"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: AFF
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator

from ..datatypes.DR import DR
from ..datatypes.XAD import XAD
from ..datatypes.XON import XON


class AFF(HL7Model):
    """HL7 v2 AFF segment.

    Attributes
    ----------
    aff_1 : str
        AFF.1 (req) - Set ID - AFF (SI)

    aff_2 : XON
        AFF.2 (req) - Professional Organization (XON)

    aff_3 : XAD | None
        AFF.3 (opt) - Professional Organization Address (XAD)

    aff_4 : list[DR] | None
        AFF.4 (opt, rep) - Professional Organization Affiliation Date Range (DR)

    aff_5 : str | None
        AFF.5 (opt) - Professional Affiliation Additional Information (ST)
    """

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

    @field_validator("aff_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    model_config = {"populate_by_name": True}
