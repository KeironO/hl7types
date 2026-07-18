"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: IAM
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, ValidationInfo, field_validator
from hl7types.hl7 import HL7Model
from hl7types.hl7._validators import _apply_dt_fallback

from ..datatypes.CNE import CNE
from ..datatypes.CWE import CWE
from ..datatypes.EI import EI
from ..datatypes.XCN import XCN
from ..datatypes.XON import XON
from ..datatypes.XPN import XPN

_RE_SI = re.compile(r'\d*')
_RE_DT = re.compile(r'(\d{4}([01]\d(\d{2})?)?)?')
_RE_DTM = re.compile(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?')


class IAM(HL7Model):
    """Patient Adverse Reaction Information (S3.4.7).

    Attributes
    ----------
    iam_1 : str
        IAM.1 - Set ID - IAM (SI) R S3.4.7.1

    iam_2 : CWE | None
        IAM.2 - Allergen Type Code (CWE) O S3.4.6.2 | 0127 - Allergen Type

    iam_3 : CWE
        IAM.3 - Allergen Code/Mnemonic/Description (CWE) R S3.4.6.3

    iam_4 : CWE | None
        IAM.4 - Allergy Severity Code (CWE) O S3.4.6.4 | 0128 - Allergy Severity

    iam_5 : list[str] | None
        IAM.5 - Allergy Reaction Code (ST) O rep S3.4.6.5

    iam_6 : CNE
        IAM.6 - Allergy Action Code (CNE) R S3.4.7.6 | 0206 - Segment Action Code

    iam_7 : EI | None
        IAM.7 - Allergy Unique Identifier (EI) C S3.4.7.7

    iam_8 : str | None
        IAM.8 - Action Reason (ST) O S3.4.7.8

    iam_9 : CWE | None
        IAM.9 - Sensitivity to Causative Agent Code (CWE) O S3.4.7.9 | 0436 - Sensitivity to Causative Agent Code

    iam_10 : CWE | None
        IAM.10 - Allergen Group Code/Mnemonic/Description (CWE) O S3.4.7.10

    iam_11 : str | None
        IAM.11 - Onset Date (DT) O S3.4.7.11

    iam_12 : str | None
        IAM.12 - Onset Date Text (ST) O S3.4.7.12

    iam_13 : str | None
        IAM.13 - Reported Date/Time (DTM) O S3.4.7.13

    iam_14 : XPN | None
        IAM.14 - Reported By (XPN) O S3.4.7.14

    iam_15 : CWE | None
        IAM.15 - Relationship to Patient Code (CWE) O S3.4.7.15 | 0063 - Relationship

    iam_16 : CWE | None
        IAM.16 - Alert Device Code (CWE) O S3.4.7.16 | 0437 - Alert Device Code

    iam_17 : CWE | None
        IAM.17 - Allergy Clinical Status Code (CWE) O S3.4.7.17 | 0438 - Allergy Clinical Status

    iam_18 : XCN | None
        IAM.18 - Statused by Person (XCN) O S3.4.7.18

    iam_19 : XON | None
        IAM.19 - Statused by Organization (XON) O S3.4.7.19

    iam_20 : str | None
        IAM.20 - Statused at Date/Time (DTM) O S3.4.7.20

    iam_21 : XCN | None
        IAM.21 - Inactivated by Person (XCN) O S3.4.7.21

    iam_22 : str | None
        IAM.22 - Inactivated Date/Time (DTM) O S3.4.7.22

    iam_23 : XCN | None
        IAM.23 - Initially Recorded by Person (XCN) O S3.4.7.23

    iam_24 : str | None
        IAM.24 - Initially Recorded Date/Time (DTM) O S3.4.7.24

    iam_25 : XCN | None
        IAM.25 - Modified by Person (XCN) O S3.4.7.25

    iam_26 : str | None
        IAM.26 - Modified Date/Time (DTM) O S3.4.7.26

    iam_27 : CWE | None
        IAM.27 - Clinician Identified Code (CWE) O S3.4.7.27

    iam_28 : XON | None
        IAM.28 - Initially Recorded by Organization (XON) O S3.4.7.28

    iam_29 : XON | None
        IAM.29 - Modified by Organization (XON) O S3.4.7.29

    iam_30 : XON | None
        IAM.30 - Inactivated by Organization (XON) O S3.4.7.30
    """

    iam_1: str = Field(
        validation_alias=AliasChoices(
            "iam_1",
            "set_id_iam",
            "IAM.1",
        ),
        serialization_alias="IAM.1",
        title="Set ID - IAM",
        description="R | Item #01612 | LEN:4",
    )

    iam_2: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "iam_2",
            "allergen_type_code",
            "IAM.2",
        ),
        serialization_alias="IAM.2",
        title="Allergen Type Code",
        description="O | Item #00204 | Table 0127 - Allergen Type",
    )

    iam_3: CWE = Field(
        validation_alias=AliasChoices(
            "iam_3",
            "allergen_code_mnemonic_description",
            "IAM.3",
        ),
        serialization_alias="IAM.3",
        title="Allergen Code/Mnemonic/Description",
        description="R | Item #00205",
    )

    iam_4: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "iam_4",
            "allergy_severity_code",
            "IAM.4",
        ),
        serialization_alias="IAM.4",
        title="Allergy Severity Code",
        description="O | Item #00206 | Table 0128 - Allergy Severity",
    )

    iam_5: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "iam_5",
            "allergy_reaction_code",
            "IAM.5",
        ),
        serialization_alias="IAM.5",
        title="Allergy Reaction Code",
        description="O | Item #00207",
    )

    iam_6: CNE = Field(
        validation_alias=AliasChoices(
            "iam_6",
            "allergy_action_code",
            "IAM.6",
        ),
        serialization_alias="IAM.6",
        title="Allergy Action Code",
        description="R | Item #01551 | Table 0206 - Segment Action Code",
    )

    iam_7: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "iam_7",
            "allergy_unique_identifier",
            "IAM.7",
        ),
        serialization_alias="IAM.7",
        title="Allergy Unique Identifier",
        description="C | Item #01552",
    )

    iam_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "iam_8",
            "action_reason",
            "IAM.8",
        ),
        serialization_alias="IAM.8",
        title="Action Reason",
        description="O | Item #01553",
    )

    iam_9: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "iam_9",
            "sensitivity_to_causative_agent_code",
            "IAM.9",
        ),
        serialization_alias="IAM.9",
        title="Sensitivity to Causative Agent Code",
        description=(
            "O | Item #01554 | Table 0436 - Sensitivity to Causative Agent Code"
        ),
    )

    iam_10: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "iam_10",
            "allergen_group_code_mnemonic_description",
            "IAM.10",
        ),
        serialization_alias="IAM.10",
        title="Allergen Group Code/Mnemonic/Description",
        description="O | Item #01555",
    )

    iam_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "iam_11",
            "onset_date",
            "IAM.11",
        ),
        serialization_alias="IAM.11",
        title="Onset Date",
        description="O | Item #01556",
    )

    iam_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "iam_12",
            "onset_date_text",
            "IAM.12",
        ),
        serialization_alias="IAM.12",
        title="Onset Date Text",
        description="O | Item #01557",
    )

    iam_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "iam_13",
            "reported_date_time",
            "IAM.13",
        ),
        serialization_alias="IAM.13",
        title="Reported Date/Time",
        description="O | Item #01558",
    )

    iam_14: Optional[XPN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "iam_14",
            "reported_by",
            "IAM.14",
        ),
        serialization_alias="IAM.14",
        title="Reported By",
        description="O | Item #01559",
    )

    iam_15: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "iam_15",
            "relationship_to_patient_code",
            "IAM.15",
        ),
        serialization_alias="IAM.15",
        title="Relationship to Patient Code",
        description="O | Item #01560 | Table 0063 - Relationship",
    )

    iam_16: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "iam_16",
            "alert_device_code",
            "IAM.16",
        ),
        serialization_alias="IAM.16",
        title="Alert Device Code",
        description="O | Item #01561 | Table 0437 - Alert Device Code",
    )

    iam_17: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "iam_17",
            "allergy_clinical_status_code",
            "IAM.17",
        ),
        serialization_alias="IAM.17",
        title="Allergy Clinical Status Code",
        description="O | Item #01562 | Table 0438 - Allergy Clinical Status",
    )

    iam_18: Optional[XCN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "iam_18",
            "statused_by_person",
            "IAM.18",
        ),
        serialization_alias="IAM.18",
        title="Statused by Person",
        description="O | Item #01563",
    )

    iam_19: Optional[XON] = Field(
        default=None,
        validation_alias=AliasChoices(
            "iam_19",
            "statused_by_organization",
            "IAM.19",
        ),
        serialization_alias="IAM.19",
        title="Statused by Organization",
        description="O | Item #01564",
    )

    iam_20: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "iam_20",
            "statused_at_date_time",
            "IAM.20",
        ),
        serialization_alias="IAM.20",
        title="Statused at Date/Time",
        description="O | Item #01565",
    )

    iam_21: Optional[XCN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "iam_21",
            "inactivated_by_person",
            "IAM.21",
        ),
        serialization_alias="IAM.21",
        title="Inactivated by Person",
        description="O | Item #02294",
    )

    iam_22: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "iam_22",
            "inactivated_date_time",
            "IAM.22",
        ),
        serialization_alias="IAM.22",
        title="Inactivated Date/Time",
        description="O | Item #02295",
    )

    iam_23: Optional[XCN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "iam_23",
            "initially_recorded_by_person",
            "IAM.23",
        ),
        serialization_alias="IAM.23",
        title="Initially Recorded by Person",
        description="O | Item #02296",
    )

    iam_24: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "iam_24",
            "initially_recorded_date_time",
            "IAM.24",
        ),
        serialization_alias="IAM.24",
        title="Initially Recorded Date/Time",
        description="O | Item #02297",
    )

    iam_25: Optional[XCN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "iam_25",
            "modified_by_person",
            "IAM.25",
        ),
        serialization_alias="IAM.25",
        title="Modified by Person",
        description="O | Item #02298",
    )

    iam_26: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "iam_26",
            "modified_date_time",
            "IAM.26",
        ),
        serialization_alias="IAM.26",
        title="Modified Date/Time",
        description="O | Item #02299",
    )

    iam_27: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "iam_27",
            "clinician_identified_code",
            "IAM.27",
        ),
        serialization_alias="IAM.27",
        title="Clinician Identified Code",
        description="O | Item #02300",
    )

    iam_28: Optional[XON] = Field(
        default=None,
        validation_alias=AliasChoices(
            "iam_28",
            "initially_recorded_by_organization",
            "IAM.28",
        ),
        serialization_alias="IAM.28",
        title="Initially Recorded by Organization",
        description="O | Item #03293",
    )

    iam_29: Optional[XON] = Field(
        default=None,
        validation_alias=AliasChoices(
            "iam_29",
            "modified_by_organization",
            "IAM.29",
        ),
        serialization_alias="IAM.29",
        title="Modified by Organization",
        description="O | Item #03294",
    )

    iam_30: Optional[XON] = Field(
        default=None,
        validation_alias=AliasChoices(
            "iam_30",
            "inactivated_by_organization",
            "IAM.30",
        ),
        serialization_alias="IAM.30",
        title="Inactivated by Organization",
        description="O | Item #03295",
    )

    @field_validator("iam_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        if not _RE_SI.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("iam_11", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        if not _RE_DT.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    @field_validator("iam_13", "iam_20", "iam_22", "iam_24", "iam_26", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        if _RE_DTM.fullmatch(v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = ConfigDict(populate_by_name=True)
