"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: AFF
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.DR import DR
from ..datatypes.XAD import XAD
from ..datatypes.XON import XON


class AFF(HL7Model):
    """Professional Affiliation (S15.4.1).

    Attributes
    ----------
    aff_1 : str
        AFF.1 - Set ID - AFF (SI) R S15.4.1.1

    aff_2 : XON
        AFF.2 - Professional Organization (XON) R S15.4.1.2

    aff_3 : XAD | None
        AFF.3 - Professional Organization Address (XAD) O S15.4.1.3

    aff_4 : list[DR] | None
        AFF.4 - Professional Organization Affiliation Date Range (DR) O rep S15.4.1.4

    aff_5 : str | None
        AFF.5 - Professional Affiliation Additional Information (ST) O S15.4.1.5
    """

    aff_1: str = Field(
        validation_alias=AliasChoices(
            "aff_1",
            "set_id_aff",
            "AFF.1",
        ),
        serialization_alias="AFF.1",
        title="Set ID - AFF",
        description="R | Item #01427 | LEN:60",
    )

    aff_2: XON = Field(
        validation_alias=AliasChoices(
            "aff_2",
            "professional_organization",
            "AFF.2",
        ),
        serialization_alias="AFF.2",
        title="Professional Organization",
        description="R | Item #01444",
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
        description="O | Item #01445",
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
        description="O | Item #01446",
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
        description="O | Item #01447 | LEN:60",
    )

    @field_validator("aff_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    model_config = {"populate_by_name": True}
