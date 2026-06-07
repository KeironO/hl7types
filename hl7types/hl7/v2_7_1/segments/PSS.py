"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: PSS
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CP import CP
from ..datatypes.EI import EI


class PSS(HL7Model):
    """HL7 v2 PSS segment.

    Attributes
    ----------
    pss_1 : EI
        PSS.1 (req) - Provider Product/Service Section Number (EI)

    pss_2 : EI | None
        PSS.2 (opt) - Payer Product/Service Section Number (EI)

    pss_3 : str
        PSS.3 (req) - Product/Service Section Sequence Number (SI)

    pss_4 : CP
        PSS.4 (req) - Billed Amount (CP)

    pss_5 : str
        PSS.5 (req) - Section Description or Heading (ST)
    """

    pss_1: EI = Field(
        validation_alias=AliasChoices(
            "pss_1",
            "provider_product_service_section_number",
            "PSS.1",
        ),
        serialization_alias="PSS.1",
        title="Provider Product/Service Section Number",
        description="Item #1946",
    )

    pss_2: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pss_2",
            "payer_product_service_section_number",
            "PSS.2",
        ),
        serialization_alias="PSS.2",
        title="Payer Product/Service Section Number",
        description="Item #1947",
    )

    pss_3: str = Field(
        validation_alias=AliasChoices(
            "pss_3",
            "product_service_section_sequence_number",
            "PSS.3",
        ),
        serialization_alias="PSS.3",
        title="Product/Service Section Sequence Number",
        description="Item #1948",
    )

    pss_4: CP = Field(
        validation_alias=AliasChoices(
            "pss_4",
            "billed_amount",
            "PSS.4",
        ),
        serialization_alias="PSS.4",
        title="Billed Amount",
        description="Item #1949",
    )

    pss_5: str = Field(
        validation_alias=AliasChoices(
            "pss_5",
            "section_description_or_heading",
            "PSS.5",
        ),
        serialization_alias="PSS.5",
        title="Section Description or Heading",
        description="Item #2043",
    )

    @field_validator("pss_3", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    model_config = {"populate_by_name": True}
