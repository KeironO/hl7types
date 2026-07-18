"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: GP1
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CP import CP


class GP1(HL7Model):
    """Grouping/Reimbursement - Visit (S6.5.15).

    Attributes
    ----------
    gp1_1 : str
        GP1.1 - Type of Bill Code (IS) R S6.5.15.1 | 0455 - Type of Bill Code

    gp1_2 : list[str] | None
        GP1.2 - Revenue Code (IS) O rep S6.5.15.2 | 0456 - Revenue code

    gp1_3 : str | None
        GP1.3 - Overall Claim Disposition Code (IS) O S6.5.15.3 | 0457 - Overall Claim Disposition Code

    gp1_4 : list[str] | None
        GP1.4 - OCE Edits per Visit Code (IS) O rep S6.5.15.4 | 0458 - OCE Edit Code

    gp1_5 : CP | None
        GP1.5 - Outlier Cost (CP) O S6.5.15.5
    """

    gp1_1: str = Field(
        validation_alias=AliasChoices(
            "gp1_1",
            "type_of_bill_code",
            "GP1.1",
        ),
        serialization_alias="GP1.1",
        title="Type of Bill Code",
        description="R | Item #01599 | Table 0455 - Type of Bill Code | LEN:3",
    )

    gp1_2: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gp1_2",
            "revenue_code",
            "GP1.2",
        ),
        serialization_alias="GP1.2",
        title="Revenue Code",
        description="O | Item #01600 | Table 0456 - Revenue code | LEN:3",
    )

    gp1_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gp1_3",
            "overall_claim_disposition_code",
            "GP1.3",
        ),
        serialization_alias="GP1.3",
        title="Overall Claim Disposition Code",
        description=(
            "O | Item #01601 | Table 0457 - Overall Claim Disposition Code | "
            "LEN:1"
        ),
    )

    gp1_4: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "gp1_4",
            "oce_edits_per_visit_code",
            "GP1.4",
        ),
        serialization_alias="GP1.4",
        title="OCE Edits per Visit Code",
        description="O | Item #01602 | Table 0458 - OCE Edit Code | LEN:2",
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
        description="O | Item #00387",
    )

    model_config = ConfigDict(populate_by_name=True)
