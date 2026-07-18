"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: IAM
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.CNE import CNE
from ..datatypes.EI import EI
from ..datatypes.TS import TS
from ..datatypes.XCN import XCN
from ..datatypes.XON import XON
from ..datatypes.XPN import XPN

_RE_SI = re.compile(r'\d*')
_RE_DT = re.compile(r'(\d{4}([01]\d(\d{2})?)?)?')


class IAM(HL7Model):
    """Patient adverse reaction information - unique iden (S3.4.7).

    Attributes
    ----------
    iam_1 : str
        IAM.1 - Set ID - IAM (SI) R S3.4.7.1

    iam_2 : CE | None
        IAM.2 - Allergen Type Code (CE) O S3.4.7.2 | 0127 - Allergen type

    iam_3 : CE
        IAM.3 - Allergen Code/Mnemonic/Description (CE) R S3.4.7.3

    iam_4 : CE | None
        IAM.4 - Allergy Severity Code (CE) O S3.4.7.4 | 0128 - Allergy severity

    iam_5 : list[str] | None
        IAM.5 - Allergy Reaction Code (ST) O rep S3.4.7.5

    iam_6 : CNE
        IAM.6 - Allergy Action Code (CNE) R S3.4.7.6 | 0323 - Action code

    iam_7 : EI
        IAM.7 - Allergy Unique Identifier (EI) R S3.4.7.7

    iam_8 : str | None
        IAM.8 - Action Reason (ST) O S3.4.7.8

    iam_9 : CE | None
        IAM.9 - Sensitivity to Causative Agent Code (CE) O S3.4.7.9 | 0436 - Sensitivity to Causative Agent code

    iam_10 : CE | None
        IAM.10 - Allergen Group Code/Mnemonic/Description (CE) O S3.4.7.10

    iam_11 : str | None
        IAM.11 - Onset Date (DT) O S3.4.7.11

    iam_12 : str | None
        IAM.12 - Onset Date Text (ST) O S3.4.7.12

    iam_13 : TS | None
        IAM.13 - Reported Date/Time (TS) O S3.4.7.13

    iam_14 : XPN | None
        IAM.14 - Reported By (XPN) O S3.4.7.14

    iam_15 : CE | None
        IAM.15 - Relationship to Patient Code (CE) O S3.4.7.15 | 0063 - Relationship

    iam_16 : CE | None
        IAM.16 - Alert Device Code (CE) O S3.4.7.16 | 0437 - Alert device code

    iam_17 : CE | None
        IAM.17 - Allergy Clinical Status Code (CE) O S3.4.7.17 | 0438 - Allergy clinical status

    iam_18 : XCN | None
        IAM.18 - Statused by Person (XCN) O S3.4.7.18

    iam_19 : XON | None
        IAM.19 - Statused by Organization (XON) O S3.4.7.19

    iam_20 : TS | None
        IAM.20 - Statused at Date/Time (TS) O S3.4.7.20
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

    iam_2: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "iam_2",
            "allergen_type_code",
            "IAM.2",
        ),
        serialization_alias="IAM.2",
        title="Allergen Type Code",
        description="O | Item #00204 | Table 0127 - Allergen type",
    )

    iam_3: CE = Field(
        validation_alias=AliasChoices(
            "iam_3",
            "allergen_code_mnemonic_description",
            "IAM.3",
        ),
        serialization_alias="IAM.3",
        title="Allergen Code/Mnemonic/Description",
        description="R | Item #00205",
    )

    iam_4: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "iam_4",
            "allergy_severity_code",
            "IAM.4",
        ),
        serialization_alias="IAM.4",
        title="Allergy Severity Code",
        description="O | Item #00206 | Table 0128 - Allergy severity",
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
        description="O | Item #00207 | LEN:15",
    )

    iam_6: CNE = Field(
        validation_alias=AliasChoices(
            "iam_6",
            "allergy_action_code",
            "IAM.6",
        ),
        serialization_alias="IAM.6",
        title="Allergy Action Code",
        description="R | Item #01551 | Table 0323 - Action code",
    )

    iam_7: EI = Field(
        validation_alias=AliasChoices(
            "iam_7",
            "allergy_unique_identifier",
            "IAM.7",
        ),
        serialization_alias="IAM.7",
        title="Allergy Unique Identifier",
        description="R | Item #01552",
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
        description="O | Item #01553 | LEN:60",
    )

    iam_9: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "iam_9",
            "sensitivity_to_causative_agent_code",
            "IAM.9",
        ),
        serialization_alias="IAM.9",
        title="Sensitivity to Causative Agent Code",
        description=(
            "O | Item #01554 | Table 0436 - Sensitivity to Causative Agent code"
        ),
    )

    iam_10: Optional[CE] = Field(
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
        description="O | Item #01556 | LEN:8",
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
        description="O | Item #01557 | LEN:60",
    )

    iam_13: Optional[TS] = Field(
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

    iam_15: Optional[CE] = Field(
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

    iam_16: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "iam_16",
            "alert_device_code",
            "IAM.16",
        ),
        serialization_alias="IAM.16",
        title="Alert Device Code",
        description="O | Item #01561 | Table 0437 - Alert device code",
    )

    iam_17: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "iam_17",
            "allergy_clinical_status_code",
            "IAM.17",
        ),
        serialization_alias="IAM.17",
        title="Allergy Clinical Status Code",
        description="O | Item #01562 | Table 0438 - Allergy clinical status",
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

    iam_20: Optional[TS] = Field(
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

    model_config = ConfigDict(populate_by_name=True)
