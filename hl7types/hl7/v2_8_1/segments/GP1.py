"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: GP1
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CP import CP
from ..datatypes.CWE import CWE


class GP1(HL7Model):
    """HL7 v2 GP1 segment.

    Attributes
    ----------
    gp1_1 : CWE
        GP1.1 (req) - Type of Bill Code (CWE)

    gp1_2 : list[CWE] | None
        GP1.2 (opt, rep) - Revenue Code (CWE)

    gp1_3 : CWE | None
        GP1.3 (opt) - Overall Claim Disposition Code (CWE)

    gp1_4 : list[CWE] | None
        GP1.4 (opt, rep) - OCE Edits per Visit Code (CWE)

    gp1_5 : CP | None
        GP1.5 (opt) - Outlier Cost (CP)
    """

    gp1_1: CWE = Field(
        validation_alias=AliasChoices(
            "gp1_1",
            "type_of_bill_code",
            "GP1.1",
        ),
        serialization_alias="GP1.1",
        title="Type of Bill Code",
        description="Item #1599 | Table HL70455",
    )

    gp1_2: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gp1_2",
            "revenue_code",
            "GP1.2",
        ),
        serialization_alias="GP1.2",
        title="Revenue Code",
        description="Item #1600 | Table HL70456",
    )

    gp1_3: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gp1_3",
            "overall_claim_disposition_code",
            "GP1.3",
        ),
        serialization_alias="GP1.3",
        title="Overall Claim Disposition Code",
        description="Item #1601 | Table HL70457",
    )

    gp1_4: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gp1_4",
            "oce_edits_per_visit_code",
            "GP1.4",
        ),
        serialization_alias="GP1.4",
        title="OCE Edits per Visit Code",
        description="Item #1602 | Table HL70458",
    )

    gp1_5: Optional[CP] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gp1_5",
            "outlier_cost",
            "GP1.5",
        ),
        serialization_alias="GP1.5",
        title="Outlier Cost",
        description="Item #387",
    )

    model_config = {"populate_by_name": True}
