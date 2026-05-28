"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: MRG
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CX import CX


class MRG(BaseModel):
    """HL7 v2 MRG segment."""

    mrg_1: list[CX] = Field(
        default=...,
        validation_alias=AliasChoices(
            "mrg_1",
            "prior_patient_id_internal",
            "MRG.1",
        ),
        serialization_alias="MRG.1",
        title="Prior Patient ID - Internal",
        description="Item #211",
    )

    mrg_2: list[CX] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "mrg_2",
            "prior_alternate_patient_id",
            "MRG.2",
        ),
        serialization_alias="MRG.2",
        title="Prior Alternate Patient ID",
        description="Item #212",
    )

    mrg_3: CX | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "mrg_3",
            "prior_patient_account_number",
            "MRG.3",
        ),
        serialization_alias="MRG.3",
        title="Prior Patient Account Number",
        description="Item #213",
    )

    mrg_4: CX | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "mrg_4",
            "prior_patient_id_external",
            "MRG.4",
        ),
        serialization_alias="MRG.4",
        title="Prior Patient ID - External",
        description="Item #214",
    )

    mrg_5: CX | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "mrg_5",
            "prior_visit_number",
            "MRG.5",
        ),
        serialization_alias="MRG.5",
        title="Prior Visit Number",
        description="Item #1279",
    )

    mrg_6: CX | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "mrg_6",
            "prior_alternate_visit_id",
            "MRG.6",
        ),
        serialization_alias="MRG.6",
        title="Prior Alternate Visit ID",
        description="Item #1280",
    )

    mrg_7: CX | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "mrg_7",
            "prior_patient_name",
            "MRG.7",
        ),
        serialization_alias="MRG.7",
        title="Prior Patient Name",
        description="Item #1281",
    )

    model_config = {"populate_by_name": True}
