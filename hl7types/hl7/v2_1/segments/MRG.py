"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: MRG
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field
from hl7types.hl7 import HL7Model


class MRG(HL7Model):
    """MERGE PATIENT INFORMATION.

    Attributes
    ----------
    mrg_1 : str
        MRG.1 - PRIOR PATIENT ID - INTERNAL (CK) R S3-13 | 0061 - CHECK DIGIT SCHEME

    mrg_2 : str | None
        MRG.2 - PRIOR ALTERNATE PATIENT ID (CK) O | 0061 - CHECK DIGIT SCHEME

    mrg_3 : str | None
        MRG.3 - PRIOR PATIENT ACCOUNT NUMBER (CK) O | 0061 - CHECK DIGIT SCHEME
    """

    mrg_1: str = Field(
        validation_alias=AliasChoices(
            "mrg_1",
            "prior_patient_id_internal",
            "MRG.1",
        ),
        serialization_alias="MRG.1",
        title="PRIOR PATIENT ID - INTERNAL",
        description=(
            "R | Item #00576 | Table 0061 - CHECK DIGIT SCHEME | LEN:16"
        ),
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
        description=(
            "O | Item #00577 | Table 0061 - CHECK DIGIT SCHEME | LEN:16"
        ),
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
        description=(
            "O | Item #00578 | Table 0061 - CHECK DIGIT SCHEME | LEN:20"
        ),
    )

    model_config = ConfigDict(populate_by_name=True)
