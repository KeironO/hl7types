"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: MRG
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model


class MRG(HL7Model):
    """HL7 v2 MRG segment.

    Attributes
    ----------
    mrg_1 : str
        MRG.1 (req) - Prior Patient ID - Internal (CM)

    mrg_2 : str | None
        MRG.2 (opt) - Prior Alternate Patient ID (CM)

    mrg_3 : str | None
        MRG.3 (opt) - Prior Patient Account Number (CK)

    mrg_4 : str | None
        MRG.4 (opt) - Prior Patient ID - External (CK)
    """

    mrg_1: str = Field(
        validation_alias=AliasChoices(
            "mrg_1",
            "prior_patient_id_internal",
            "MRG.1",
        ),
        serialization_alias="MRG.1",
        title="Prior Patient ID - Internal",
        description="Item #211",
    )

    mrg_2: Optional[str] = Field(
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

    mrg_3: Optional[str] = Field(
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

    mrg_4: Optional[str] = Field(
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

    model_config = {"populate_by_name": True}
