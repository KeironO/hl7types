"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: PSH
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CQ import CQ
from ..datatypes.FT import FT


class PSH(BaseModel):
    """HL7 v2 PSH segment."""

    psh_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "psh_1",
            "report_type",
            "PSH.1",
        ),
        serialization_alias="PSH.1",
        title="Report Type",
        description="Item #1233",
    )

    psh_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psh_2",
            "report_form_identifier",
            "PSH.2",
        ),
        serialization_alias="PSH.2",
        title="Report Form Identifier",
        description="Item #1297",
    )

    psh_3: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "psh_3",
            "report_date",
            "PSH.3",
        ),
        serialization_alias="PSH.3",
        title="Report Date",
        description="Item #1235",
    )

    psh_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psh_4",
            "report_interval_start_date",
            "PSH.4",
        ),
        serialization_alias="PSH.4",
        title="Report Interval Start Date",
        description="Item #1236",
    )

    psh_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psh_5",
            "report_interval_end_date",
            "PSH.5",
        ),
        serialization_alias="PSH.5",
        title="Report Interval End Date",
        description="Item #1237",
    )

    psh_6: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psh_6",
            "quantity_manufactured",
            "PSH.6",
        ),
        serialization_alias="PSH.6",
        title="Quantity Manufactured",
        description="Item #1238",
    )

    psh_7: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psh_7",
            "quantity_distributed",
            "PSH.7",
        ),
        serialization_alias="PSH.7",
        title="Quantity Distributed",
        description="Item #1239",
    )

    psh_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psh_8",
            "quantity_distributed_method",
            "PSH.8",
        ),
        serialization_alias="PSH.8",
        title="Quantity Distributed Method",
        description="Item #1240 | Table HL70329",
    )

    psh_9: Optional[FT] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psh_9",
            "quantity_distributed_comment",
            "PSH.9",
        ),
        serialization_alias="PSH.9",
        title="Quantity Distributed Comment",
        description="Item #1241",
    )

    psh_10: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psh_10",
            "quantity_in_use",
            "PSH.10",
        ),
        serialization_alias="PSH.10",
        title="Quantity in Use",
        description="Item #1242",
    )

    psh_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psh_11",
            "quantity_in_use_method",
            "PSH.11",
        ),
        serialization_alias="PSH.11",
        title="Quantity in Use Method",
        description="Item #1243 | Table HL70329",
    )

    psh_12: Optional[FT] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psh_12",
            "quantity_in_use_comment",
            "PSH.12",
        ),
        serialization_alias="PSH.12",
        title="Quantity in Use Comment",
        description="Item #1244",
    )

    psh_13: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psh_13",
            "number_of_product_experience_reports_filed_by_facility",
            "PSH.13",
        ),
        serialization_alias="PSH.13",
        title="Number of Product Experience Reports Filed by Facility",
        description="Item #1245",
    )

    psh_14: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "psh_14",
            "number_of_product_experience_reports_filed_by_distributor",
            "PSH.14",
        ),
        serialization_alias="PSH.14",
        title="Number of Product Experience Reports Filed by Distributor",
        description="Item #1246",
    )

    model_config = {"populate_by_name": True}
