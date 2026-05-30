"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: CSR
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE
from ..datatypes.CX import CX
from ..datatypes.EI import EI
from ..datatypes.XCN import XCN


class CSR(HL7Model):
    """HL7 v2 CSR segment.

    Attributes
    ----------
    csr_1 : EI
        CSR.1 (req) - Sponsor Study ID (EI)

    csr_2 : EI | None
        CSR.2 (opt) - Alternate Study ID (EI)

    csr_3 : CWE | None
        CSR.3 (opt) - Institution Registering the Patient (CWE)

    csr_4 : CX
        CSR.4 (req) - Sponsor Patient ID (CX)

    csr_5 : CX | None
        CSR.5 (opt) - Alternate Patient ID - CSR (CX)

    csr_6 : str
        CSR.6 (req) - Date/Time of Patient Study Registration (DTM)

    csr_7 : list[XCN] | None
        CSR.7 (opt, rep) - Person Performing Study Registration (XCN)

    csr_8 : list[XCN]
        CSR.8 (req, rep) - Study Authorizing Provider (XCN)

    csr_9 : str | None
        CSR.9 (opt) - Date/Time Patient Study Consent Signed (DTM)

    csr_10 : CWE | None
        CSR.10 (opt) - Patient Study Eligibility Status (CWE)

    csr_11 : list[str] | None
        CSR.11 (opt, rep) - Study Randomization Date/time (DTM)

    csr_12 : list[CWE] | None
        CSR.12 (opt, rep) - Randomized Study Arm (CWE)

    csr_13 : list[CWE] | None
        CSR.13 (opt, rep) - Stratum for Study Randomization (CWE)

    csr_14 : CWE | None
        CSR.14 (opt) - Patient Evaluability Status (CWE)

    csr_15 : str | None
        CSR.15 (opt) - Date/Time Ended Study (DTM)

    csr_16 : CWE | None
        CSR.16 (opt) - Reason Ended Study (CWE)
    """

    csr_1: EI = Field(
        default=...,
        validation_alias=AliasChoices(
            "csr_1",
            "sponsor_study_id",
            "CSR.1",
        ),
        serialization_alias="CSR.1",
        title="Sponsor Study ID",
        description="Item #1011",
    )

    csr_2: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "csr_2",
            "alternate_study_id",
            "CSR.2",
        ),
        serialization_alias="CSR.2",
        title="Alternate Study ID",
        description="Item #1036",
    )

    csr_3: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "csr_3",
            "institution_registering_the_patient",
            "CSR.3",
        ),
        serialization_alias="CSR.3",
        title="Institution Registering the Patient",
        description="Item #1037 | Table HL79999",
    )

    csr_4: CX = Field(
        default=...,
        validation_alias=AliasChoices(
            "csr_4",
            "sponsor_patient_id",
            "CSR.4",
        ),
        serialization_alias="CSR.4",
        title="Sponsor Patient ID",
        description="Item #1038",
    )

    csr_5: Optional[CX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "csr_5",
            "alternate_patient_id_csr",
            "CSR.5",
        ),
        serialization_alias="CSR.5",
        title="Alternate Patient ID - CSR",
        description="Item #1039",
    )

    csr_6: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "csr_6",
            "date_time_of_patient_study_registration",
            "CSR.6",
        ),
        serialization_alias="CSR.6",
        title="Date/Time of Patient Study Registration",
        description="Item #1040",
    )

    csr_7: Optional[List[XCN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "csr_7",
            "person_performing_study_registration",
            "CSR.7",
        ),
        serialization_alias="CSR.7",
        title="Person Performing Study Registration",
        description="Item #1041",
    )

    csr_8: List[XCN] = Field(
        default=...,
        validation_alias=AliasChoices(
            "csr_8",
            "study_authorizing_provider",
            "CSR.8",
        ),
        serialization_alias="CSR.8",
        title="Study Authorizing Provider",
        description="Item #1042",
    )

    csr_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "csr_9",
            "date_time_patient_study_consent_signed",
            "CSR.9",
        ),
        serialization_alias="CSR.9",
        title="Date/Time Patient Study Consent Signed",
        description="Item #1043",
    )

    csr_10: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "csr_10",
            "patient_study_eligibility_status",
            "CSR.10",
        ),
        serialization_alias="CSR.10",
        title="Patient Study Eligibility Status",
        description="Item #1044 | Table HL79999",
    )

    csr_11: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "csr_11",
            "study_randomization_date_time",
            "CSR.11",
        ),
        serialization_alias="CSR.11",
        title="Study Randomization Date/time",
        description="Item #1045",
    )

    csr_12: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "csr_12",
            "randomized_study_arm",
            "CSR.12",
        ),
        serialization_alias="CSR.12",
        title="Randomized Study Arm",
        description="Item #1046 | Table HL79999",
    )

    csr_13: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "csr_13",
            "stratum_for_study_randomization",
            "CSR.13",
        ),
        serialization_alias="CSR.13",
        title="Stratum for Study Randomization",
        description="Item #1047 | Table HL79999",
    )

    csr_14: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "csr_14",
            "patient_evaluability_status",
            "CSR.14",
        ),
        serialization_alias="CSR.14",
        title="Patient Evaluability Status",
        description="Item #1048 | Table HL79999",
    )

    csr_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "csr_15",
            "date_time_ended_study",
            "CSR.15",
        ),
        serialization_alias="CSR.15",
        title="Date/Time Ended Study",
        description="Item #1049",
    )

    csr_16: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "csr_16",
            "reason_ended_study",
            "CSR.16",
        ),
        serialization_alias="CSR.16",
        title="Reason Ended Study",
        description="Item #1050 | Table HL79999",
    )

    model_config = {"populate_by_name": True}
