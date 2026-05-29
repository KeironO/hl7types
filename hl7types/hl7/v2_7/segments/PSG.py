"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: PSG
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CP import CP
from ..datatypes.EI import EI


class PSG(BaseModel):
    """HL7 v2 PSG segment.

    Attributes
    ----------
    psg_1 : EI
        PSG.1 (req) - Provider Product/Service Group Number (EI)

    psg_2 : EI | None
        PSG.2 (opt) - Payer Product/Service Group Number (EI)

    psg_3 : str
        PSG.3 (req) - Product/Service Group Sequence Number (SI)

    psg_4 : str
        PSG.4 (req) - Adjudicate as Group (ID)

    psg_5 : CP
        PSG.5 (req) - Product/Service Group Billed Amount (CP)

    psg_6 : str
        PSG.6 (req) - Product/Service Group Description (ST)
    """

    psg_1: EI = Field(
        default=...,
        validation_alias=AliasChoices(
            "psg_1",
            "provider_product_service_group_number",
            "PSG.1",
        ),
        serialization_alias="PSG.1",
        title="Provider Product/Service Group Number",
        description="Item #1950",
    )

    psg_2: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psg_2",
            "payer_product_service_group_number",
            "PSG.2",
        ),
        serialization_alias="PSG.2",
        title="Payer Product/Service Group Number",
        description="Item #1951",
    )

    psg_3: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "psg_3",
            "product_service_group_sequence_number",
            "PSG.3",
        ),
        serialization_alias="PSG.3",
        title="Product/Service Group Sequence Number",
        description="Item #1952",
    )

    psg_4: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "psg_4",
            "adjudicate_as_group",
            "PSG.4",
        ),
        serialization_alias="PSG.4",
        title="Adjudicate as Group",
        description="Item #1953 | Table HL70136",
    )

    psg_5: CP = Field(
        default=...,
        validation_alias=AliasChoices(
            "psg_5",
            "product_service_group_billed_amount",
            "PSG.5",
        ),
        serialization_alias="PSG.5",
        title="Product/Service Group Billed Amount",
        description="Item #1954",
    )

    psg_6: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "psg_6",
            "product_service_group_description",
            "PSG.6",
        ),
        serialization_alias="PSG.6",
        title="Product/Service Group Description",
        description="Item #2044",
    )

    model_config = {"populate_by_name": True}
