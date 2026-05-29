"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: MRG
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CX import CX
from ..datatypes.XPN import XPN


class MRG(BaseModel):
    """HL7 v2 MRG segment.

    Attributes
    ----------
    mrg_1 : list[CX]
        MRG.1 (req, rep) - Prior Patient Identifier List (CX)

    mrg_3 : CX | None
        MRG.3 (opt) - Prior Patient Account Number (CX)

    mrg_5 : CX | None
        MRG.5 (opt) - Prior Visit Number (CX)

    mrg_6 : CX | None
        MRG.6 (opt) - Prior Alternate Visit ID (CX)

    mrg_7 : list[XPN] | None
        MRG.7 (opt, rep) - Prior Patient Name (XPN)
    """

    mrg_1: List[CX] = Field(
        default=...,
        validation_alias=AliasChoices(
            "mrg_1",
            "prior_patient_identifier_list",
            "MRG.1",
        ),
        serialization_alias="MRG.1",
        title="Prior Patient Identifier List",
        description="Item #211 | Table HL70061",
    )

    mrg_3: Optional[CX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "mrg_3",
            "prior_patient_account_number",
            "MRG.3",
        ),
        serialization_alias="MRG.3",
        title="Prior Patient Account Number",
        description="Item #213 | Table HL70061",
    )

    mrg_5: Optional[CX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "mrg_5",
            "prior_visit_number",
            "MRG.5",
        ),
        serialization_alias="MRG.5",
        title="Prior Visit Number",
        description="Item #1279 | Table HL70061",
    )

    mrg_6: Optional[CX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "mrg_6",
            "prior_alternate_visit_id",
            "MRG.6",
        ),
        serialization_alias="MRG.6",
        title="Prior Alternate Visit ID",
        description="Item #1280 | Table HL70061",
    )

    mrg_7: Optional[List[XPN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "mrg_7",
            "prior_patient_name",
            "MRG.7",
        ),
        serialization_alias="MRG.7",
        title="Prior Patient Name",
        description="Item #1281 | Table HL70200",
    )

    model_config = {"populate_by_name": True}
