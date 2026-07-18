"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: MRG
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field
from hl7types.hl7 import HL7Model


class MRG(HL7Model):
    """MERGE PATIENT INFORMATION (S3.3.8).

    Attributes
    ----------
    mrg_1 : str
        MRG.1 - Prior Patient ID - Internal (CM) R S3.3.8.1

    mrg_2 : str | None
        MRG.2 - Prior Alternate Patient ID (CM) NA S3.3.8.2

    mrg_3 : str | None
        MRG.3 - Prior Patient Account Number (CK) NA S3.3.8.3

    mrg_4 : str | None
        MRG.4 - Prior Patient ID - External (CK) NA S3.3.8.4
    """

    mrg_1: str = Field(
        validation_alias=AliasChoices(
            "mrg_1",
            "prior_patient_id_internal",
            "MRG.1",
        ),
        serialization_alias="MRG.1",
        title="Prior Patient ID - Internal",
        description="R | Item #00211",
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
        description="NA | Item #00212",
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
        description="NA | Item #00213 | LEN:20",
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
        description="NA | Item #00214 | LEN:16",
    )

    model_config = ConfigDict(populate_by_name=True)
