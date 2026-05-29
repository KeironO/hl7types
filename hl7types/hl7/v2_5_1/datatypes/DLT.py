"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: DLT
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from .NR import NR


class DLT(BaseModel):
    """HL7 v2 DLT data type.

    Attributes
    ----------
    dlt_1 : NR | None
        DLT.1 (opt) - Normal Range (NR)

    dlt_2 : str | None
        DLT.2 (opt) - Numeric Threshold (NM)

    dlt_3 : str | None
        DLT.3 (opt) - Change Computation (ID)

    dlt_4 : str | None
        DLT.4 (opt) - Days Retained (NM)
    """

    dlt_1: Optional[NR] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dlt_1",
            "normal_range",
            "DLT.1",
        ),
        serialization_alias="DLT.1",
        title="Normal Range",
    )

    dlt_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dlt_2",
            "numeric_threshold",
            "DLT.2",
        ),
        serialization_alias="DLT.2",
        title="Numeric Threshold",
    )

    dlt_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dlt_3",
            "change_computation",
            "DLT.3",
        ),
        serialization_alias="DLT.3",
        title="Change Computation",
    )

    dlt_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dlt_4",
            "days_retained",
            "DLT.4",
        ),
        serialization_alias="DLT.4",
        title="Days Retained",
    )

    model_config = {"populate_by_name": True}
