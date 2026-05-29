"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: DRG
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE
from ..datatypes.CP import CP
from ..datatypes.TS import TS


class DRG(BaseModel):
    """HL7 v2 DRG segment.

    Attributes
    ----------
    drg_1 : CE | None
        DRG.1 (opt) - Diagnostic Related Group (CE)

    drg_2 : TS | None
        DRG.2 (opt) - DRG Assigned Date/Time (TS)

    drg_3 : str | None
        DRG.3 (opt) - DRG Approval Indicator (ID)

    drg_4 : str | None
        DRG.4 (opt) - DRG Grouper Review Code (IS)

    drg_5 : CE | None
        DRG.5 (opt) - Outlier Type (CE)

    drg_6 : str | None
        DRG.6 (opt) - Outlier Days (NM)

    drg_7 : CP | None
        DRG.7 (opt) - Outlier Cost (CP)

    drg_8 : str | None
        DRG.8 (opt) - DRG Payor (IS)

    drg_9 : CP | None
        DRG.9 (opt) - Outlier Reimbursement (CP)

    drg_10 : str | None
        DRG.10 (opt) - Confidential Indicator (ID)
    """

    drg_1: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "drg_1",
            "diagnostic_related_group",
            "DRG.1",
        ),
        serialization_alias="DRG.1",
        title="Diagnostic Related Group",
        description="Item #382 | Table HL70055",
    )

    drg_2: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "drg_2",
            "drg_assigned_date_time",
            "DRG.2",
        ),
        serialization_alias="DRG.2",
        title="DRG Assigned Date/Time",
        description="Item #769",
    )

    drg_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "drg_3",
            "drg_approval_indicator",
            "DRG.3",
        ),
        serialization_alias="DRG.3",
        title="DRG Approval Indicator",
        description="Item #383 | Table HL70136",
    )

    drg_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "drg_4",
            "drg_grouper_review_code",
            "DRG.4",
        ),
        serialization_alias="DRG.4",
        title="DRG Grouper Review Code",
        description="Item #384 | Table HL70056",
    )

    drg_5: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "drg_5",
            "outlier_type",
            "DRG.5",
        ),
        serialization_alias="DRG.5",
        title="Outlier Type",
        description="Item #385 | Table HL70083",
    )

    drg_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "drg_6",
            "outlier_days",
            "DRG.6",
        ),
        serialization_alias="DRG.6",
        title="Outlier Days",
        description="Item #386",
    )

    drg_7: Optional[CP] = Field(
        default=None,
        validation_alias=AliasChoices(
            "drg_7",
            "outlier_cost",
            "DRG.7",
        ),
        serialization_alias="DRG.7",
        title="Outlier Cost",
        description="Item #387",
    )

    drg_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "drg_8",
            "drg_payor",
            "DRG.8",
        ),
        serialization_alias="DRG.8",
        title="DRG Payor",
        description="Item #770 | Table HL70229",
    )

    drg_9: Optional[CP] = Field(
        default=None,
        validation_alias=AliasChoices(
            "drg_9",
            "outlier_reimbursement",
            "DRG.9",
        ),
        serialization_alias="DRG.9",
        title="Outlier Reimbursement",
        description="Item #771",
    )

    drg_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "drg_10",
            "confidential_indicator",
            "DRG.10",
        ),
        serialization_alias="DRG.10",
        title="Confidential Indicator",
        description="Item #767 | Table HL70136",
    )

    model_config = {"populate_by_name": True}
