"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: ADJ
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CP import CP
from ..datatypes.CQ import CQ
from ..datatypes.CWE import CWE
from ..datatypes.EI import EI
from ..datatypes.XON import XON


class ADJ(BaseModel):
    """HL7 v2 ADJ segment."""

    adj_1: EI = Field(
        default=...,
        validation_alias=AliasChoices(
            "adj_1",
            "provider_adjustment_number",
            "ADJ.1",
        ),
        serialization_alias="ADJ.1",
        title="Provider Adjustment Number",
        description="Item #2003",
    )

    adj_2: EI = Field(
        default=...,
        validation_alias=AliasChoices(
            "adj_2",
            "payer_adjustment_number",
            "ADJ.2",
        ),
        serialization_alias="ADJ.2",
        title="Payer Adjustment Number",
        description="Item #2004",
    )

    adj_3: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "adj_3",
            "adjustment_sequence_number",
            "ADJ.3",
        ),
        serialization_alias="ADJ.3",
        title="Adjustment Sequence Number",
        description="Item #2005",
    )

    adj_4: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "adj_4",
            "adjustment_category",
            "ADJ.4",
        ),
        serialization_alias="ADJ.4",
        title="Adjustment Category",
        description="Item #2006 | Table HL70564",
    )

    adj_5: list[CP] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "adj_5",
            "adjustment_amount",
            "ADJ.5",
        ),
        serialization_alias="ADJ.5",
        title="Adjustment Amount",
        description="Item #2007",
    )

    adj_6: CQ | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "adj_6",
            "adjustment_quantity",
            "ADJ.6",
        ),
        serialization_alias="ADJ.6",
        title="Adjustment Quantity",
        description="Item #2008 | Table HL70560",
    )

    adj_7: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "adj_7",
            "adjustment_reason_pa",
            "ADJ.7",
        ),
        serialization_alias="ADJ.7",
        title="Adjustment Reason PA",
        description="Item #2009 | Table HL70565",
    )

    adj_8: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "adj_8",
            "adjustment_description",
            "ADJ.8",
        ),
        serialization_alias="ADJ.8",
        title="Adjustment Description",
        description="Item #2010",
    )

    adj_9: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "adj_9",
            "original_value",
            "ADJ.9",
        ),
        serialization_alias="ADJ.9",
        title="Original Value",
        description="Item #2011",
    )

    adj_10: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "adj_10",
            "substitute_value",
            "ADJ.10",
        ),
        serialization_alias="ADJ.10",
        title="Substitute Value",
        description="Item #2012",
    )

    adj_11: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "adj_11",
            "adjustment_action",
            "ADJ.11",
        ),
        serialization_alias="ADJ.11",
        title="Adjustment Action",
        description="Item #2013 | Table HL70569",
    )

    adj_12: EI | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "adj_12",
            "provider_adjustment_number_cross_reference",
            "ADJ.12",
        ),
        serialization_alias="ADJ.12",
        title="Provider Adjustment Number Cross Reference",
        description="Item #2014",
    )

    adj_13: EI | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "adj_13",
            "provider_product_service_line_item_number_cross_reference",
            "ADJ.13",
        ),
        serialization_alias="ADJ.13",
        title="Provider Product/Service Line Item Number Cross Reference",
        description="Item #2015",
    )

    adj_14: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "adj_14",
            "adjustment_date",
            "ADJ.14",
        ),
        serialization_alias="ADJ.14",
        title="Adjustment Date",
        description="Item #2016",
    )

    adj_15: XON | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "adj_15",
            "responsible_organization",
            "ADJ.15",
        ),
        serialization_alias="ADJ.15",
        title="Responsible Organization",
        description="Item #2017",
    )

    model_config = {"populate_by_name": True}
