"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: CSR
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE
from ..datatypes.CX import CX
from ..datatypes.EI import EI
from ..datatypes.XCN import XCN


class CSR(HL7Model):
    """Clinical Study Registration (S7.8.1).

    Attributes
    ----------
    csr_1 : EI
        CSR.1 - Sponsor Study ID (EI) R S7.8.1.1

    csr_2 : EI | None
        CSR.2 - Alternate Study ID (EI) O S7.8.1.2

    csr_3 : CWE | None
        CSR.3 - Institution Registering the Patient (CWE) O S7.8.1.3 | 9999 - no table for CE

    csr_4 : CX
        CSR.4 - Sponsor Patient ID (CX) R S7.8.1.4

    csr_5 : CX | None
        CSR.5 - Alternate Patient ID - CSR (CX) O S7.8.1.5

    csr_6 : str
        CSR.6 - Date/Time of Patient Study Registration (DTM) R S7.8.1.6

    csr_7 : list[XCN] | None
        CSR.7 - Person Performing Study Registration (XCN) O rep S7.8.1.7

    csr_8 : list[XCN]
        CSR.8 - Study Authorizing Provider (XCN) R rep S7.8.1.8

    csr_9 : str | None
        CSR.9 - Date/Time Patient Study Consent Signed (DTM) C S7.8.1.9

    csr_10 : CWE | None
        CSR.10 - Patient Study Eligibility Status (CWE) C S7.8.1.10 | 9999 - no table for CE

    csr_11 : list[str] | None
        CSR.11 - Study Randomization Date/time (DTM) O rep S7.8.1.11

    csr_12 : list[CWE] | None
        CSR.12 - Randomized Study Arm (CWE) O rep S7.8.1.12 | 9999 - no table for CE

    csr_13 : list[CWE] | None
        CSR.13 - Stratum for Study Randomization (CWE) O rep S7.8.1.13 | 9999 - no table for CE

    csr_14 : CWE | None
        CSR.14 - Patient Evaluability Status (CWE) C S7.8.1.14 | 9999 - no table for CE

    csr_15 : str | None
        CSR.15 - Date/Time Ended Study (DTM) C S7.8.1.15

    csr_16 : CWE | None
        CSR.16 - Reason Ended Study (CWE) C S7.8.1.16 | 9999 - no table for CE
    """

    csr_1: EI = Field(
        validation_alias=AliasChoices(
            "csr_1",
            "sponsor_study_id",
            "CSR.1",
        ),
        serialization_alias="CSR.1",
        title="Sponsor Study ID",
        description="R | Item #01011",
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
        description="O | Item #01036",
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
        description="O | Item #01037 | Table 9999 - no table for CE",
    )

    csr_4: CX = Field(
        validation_alias=AliasChoices(
            "csr_4",
            "sponsor_patient_id",
            "CSR.4",
        ),
        serialization_alias="CSR.4",
        title="Sponsor Patient ID",
        description="R | Item #01038",
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
        description="O | Item #01039",
    )

    csr_6: str = Field(
        validation_alias=AliasChoices(
            "csr_6",
            "date_time_of_patient_study_registration",
            "CSR.6",
        ),
        serialization_alias="CSR.6",
        title="Date/Time of Patient Study Registration",
        description="R | Item #01040",
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
        description="O | Item #01041",
    )

    csr_8: List[XCN] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "csr_8",
            "study_authorizing_provider",
            "CSR.8",
        ),
        serialization_alias="CSR.8",
        title="Study Authorizing Provider",
        description="R | Item #01042",
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
        description="C | Item #01043",
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
        description="C | Item #01044 | Table 9999 - no table for CE",
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
        description="O | Item #01045",
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
        description="O | Item #01046 | Table 9999 - no table for CE",
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
        description="O | Item #01047 | Table 9999 - no table for CE",
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
        description="C | Item #01048 | Table 9999 - no table for CE",
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
        description="C | Item #01049",
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
        description="C | Item #01050 | Table 9999 - no table for CE",
    )

    @field_validator("csr_6", "csr_9", "csr_11", "csr_15", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        import re
        if re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = {"populate_by_name": True}
