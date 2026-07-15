"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: MRG
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CX import CX
from ..datatypes.XPN import XPN


class MRG(HL7Model):
    """Merge Patient Information (S3.4.10).

    Attributes
    ----------
    mrg_1 : list[CX]
        MRG.1 - Prior Patient Identifier List (CX) R rep S3.4.10.1 | 0061 - Check Digit Scheme

    mrg_3 : CX | None
        MRG.3 - Prior Patient Account Number (CX) O S3.4.10.3 | 0061 - Check Digit Scheme

    mrg_5 : CX | None
        MRG.5 - Prior Visit Number (CX) O S3.4.10.5 | 0061 - Check Digit Scheme

    mrg_6 : list[CX] | None
        MRG.6 - Prior Alternate Visit ID (CX) O rep S3.4.10.6 | 0061 - Check Digit Scheme

    mrg_7 : list[XPN] | None
        MRG.7 - Prior Patient Name (XPN) O rep S3.4.10.7 | 0200 - Name Type
    """

    mrg_1: List[CX] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "mrg_1",
            "prior_patient_identifier_list",
            "MRG.1",
        ),
        serialization_alias="MRG.1",
        title="Prior Patient Identifier List",
        description="R | Item #00211 | Table 0061 - Check Digit Scheme",
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
        description="O | Item #00213 | Table 0061 - Check Digit Scheme",
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
        description="O | Item #01279 | Table 0061 - Check Digit Scheme",
    )

    mrg_6: Optional[List[CX]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "mrg_6",
            "prior_alternate_visit_id",
            "MRG.6",
        ),
        serialization_alias="MRG.6",
        title="Prior Alternate Visit ID",
        description="O | Item #01280 | Table 0061 - Check Digit Scheme",
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
        description="O | Item #01281 | Table 0200 - Name Type",
    )

    model_config = {"populate_by_name": True}
