"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: MRG
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class MRG(BaseModel):
    """HL7 v2 MRG segment.

    Attributes
    ----------
    mrg_1 : str
        MRG.1 (req) - PRIOR PATIENT ID - INTERNAL (CK)

    mrg_2 : str | None
        MRG.2 (opt) - PRIOR ALTERNATE PATIENT ID (CK)

    mrg_3 : str | None
        MRG.3 (opt) - PRIOR PATIENT ACCOUNT NUMBER (CK)
    """

    mrg_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "mrg_1",
            "prior_patient_id_internal",
            "MRG.1",
        ),
        serialization_alias="MRG.1",
        title="PRIOR PATIENT ID - INTERNAL",
        description="Item #576 | Table HL70061",
    )

    mrg_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "mrg_2",
            "prior_alternate_patient_id",
            "MRG.2",
        ),
        serialization_alias="MRG.2",
        title="PRIOR ALTERNATE PATIENT ID",
        description="Item #577 | Table HL70061",
    )

    mrg_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "mrg_3",
            "prior_patient_account_number",
            "MRG.3",
        ),
        serialization_alias="MRG.3",
        title="PRIOR PATIENT ACCOUNT NUMBER",
        description="Item #578 | Table HL70061",
    )

    model_config = {"populate_by_name": True}
