"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: DRG
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.CP import CP
from ..datatypes.TS import TS


class DRG(HL7Model):
    """DRG - diagnosis related group segment (S6.4.3.8).

    Attributes
    ----------
    drg_1 : CE | None
        DRG.1 - Diagnostic Related Group (CE) O S6.4.3.1 | 0055 - Diagnostic Related Group

    drg_2 : TS | None
        DRG.2 - DRG Assigned Date/Time (TS) O S6.4.3.2

    drg_3 : str | None
        DRG.3 - DRG Approval Indicator (ID) O S6.4.3.3 | 0136 - Yes/no indicator

    drg_4 : str | None
        DRG.4 - DRG Grouper Review Code (IS) O S6.4.3.4 | 0056 - DRG Grouper Review Code

    drg_5 : CE | None
        DRG.5 - Outlier Type (CE) O S6.4.3.5 | 0083 - Outlier Type

    drg_6 : str | None
        DRG.6 - Outlier Days (NM) O S6.4.3.6

    drg_7 : CP | None
        DRG.7 - Outlier Cost (CP) O S6.4.3.7

    drg_8 : str | None
        DRG.8 - DRG Payor (IS) O S6.4.3.8 | 0229 - DRG payor

    drg_9 : CP | None
        DRG.9 - Outlier Reimbursement (CP) O S6.4.3.9

    drg_10 : str | None
        DRG.10 - Confidential Indicator (ID) O S6.4.3.10 | 0136 - Yes/no indicator
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
        description="O | Item #00382 | Table 0055 - Diagnostic Related Group",
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
        description="O | Item #00769",
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
        description="O | Item #00383 | Table 0136 - Yes/no indicator | LEN:1",
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
        description=(
            "O | Item #00384 | Table 0056 - DRG Grouper Review Code | LEN:2"
        ),
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
        description="O | Item #00385 | Table 0083 - Outlier Type",
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
        description="O | Item #00386 | LEN:3",
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
        description="O | Item #00387",
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
        description="O | Item #00770 | Table 0229 - DRG payor | LEN:1",
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
        description="O | Item #00771",
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
        description="O | Item #00767 | Table 0136 - Yes/no indicator | LEN:1",
    )

    @field_validator("drg_6", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
