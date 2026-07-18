"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: PR1
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.EI import EI
from ..datatypes.TS import TS
from ..datatypes.XCN import XCN

_RE_SI = re.compile(r'\d*')
_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class PR1(HL7Model):
    """Procedures (S6.5.4).

    Attributes
    ----------
    pr1_1 : str
        PR1.1 - Set ID - PR1 (SI) R S6.5.4.1

    pr1_2 : str | None
        PR1.2 - Procedure Coding Method (IS) R S6.5.4.2 | 0089 - Procedure Coding Method

    pr1_3 : CE
        PR1.3 - Procedure Code (CE) R S4.5.3.44 | 0088 - Procedure Code

    pr1_4 : str | None
        PR1.4 - Procedure Description (ST) O S6.5.4.4

    pr1_5 : TS
        PR1.5 - Procedure Date/Time (TS) R S6.5.4.5

    pr1_6 : str | None
        PR1.6 - Procedure Functional Type (IS) O S6.5.4.6 | 0230 - Procedure Functional Type

    pr1_7 : str | None
        PR1.7 - Procedure Minutes (NM) O S6.5.4.7

    pr1_8 : list[XCN] | None
        PR1.8 - Anesthesiologist (XCN) O rep S6.5.4.8 | 0010 - Physician ID

    pr1_9 : str | None
        PR1.9 - Anesthesia Code (IS) O S6.5.4.9 | 0019 - Anesthesia Code

    pr1_10 : str | None
        PR1.10 - Anesthesia Minutes (NM) O S6.5.4.10

    pr1_11 : list[XCN] | None
        PR1.11 - Surgeon (XCN) O rep S6.5.4.11 | 0010 - Physician ID

    pr1_12 : list[XCN] | None
        PR1.12 - Procedure Practitioner (XCN) O rep S6.5.4.12 | 0010 - Physician ID

    pr1_13 : CE | None
        PR1.13 - Consent Code (CE) O S6.5.4.13 | 0059 - Consent Code

    pr1_14 : str | None
        PR1.14 - Procedure Priority (ID) O S6.5.4.14 | 0418 - Procedure Priority

    pr1_15 : CE | None
        PR1.15 - Associated Diagnosis Code (CE) O S6.5.4.15 | 0051 - Diagnosis Code

    pr1_16 : list[CE] | None
        PR1.16 - Procedure Code Modifier (CE) O rep S4.5.3.45 | 0340 - Procedure code modifier

    pr1_17 : str | None
        PR1.17 - Procedure DRG Type (IS) O S6.5.4.17 | 0416 - Procedure DRG Type

    pr1_18 : list[CE] | None
        PR1.18 - Tissue Type Code (CE) O rep S6.5.4.18 | 0417 - Tissue Type Code

    pr1_19 : EI | None
        PR1.19 - Procedure Identifier (EI) C S6.5.4.19

    pr1_20 : str | None
        PR1.20 - Procedure Action Code (ID) C S6.5.4.20 | 0206 - Segment action code
    """

    pr1_1: str = Field(
        validation_alias=AliasChoices(
            "pr1_1",
            "set_id_pr1",
            "PR1.1",
        ),
        serialization_alias="PR1.1",
        title="Set ID - PR1",
        description="R | Item #00391 | LEN:4",
    )

    pr1_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_2",
            "procedure_coding_method",
            "PR1.2",
        ),
        serialization_alias="PR1.2",
        title="Procedure Coding Method",
        description=(
            "R | Item #00392 | Table 0089 - Procedure Coding Method | LEN:3"
        ),
    )

    pr1_3: CE = Field(
        validation_alias=AliasChoices(
            "pr1_3",
            "procedure_code",
            "PR1.3",
        ),
        serialization_alias="PR1.3",
        title="Procedure Code",
        description="R | Item #00393 | Table 0088 - Procedure Code",
    )

    pr1_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_4",
            "procedure_description",
            "PR1.4",
        ),
        serialization_alias="PR1.4",
        title="Procedure Description",
        description="O | Item #00394 | LEN:40",
    )

    pr1_5: TS = Field(
        validation_alias=AliasChoices(
            "pr1_5",
            "procedure_date_time",
            "PR1.5",
        ),
        serialization_alias="PR1.5",
        title="Procedure Date/Time",
        description="R | Item #00395",
    )

    pr1_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_6",
            "procedure_functional_type",
            "PR1.6",
        ),
        serialization_alias="PR1.6",
        title="Procedure Functional Type",
        description=(
            "O | Item #00396 | Table 0230 - Procedure Functional Type | LEN:2"
        ),
    )

    pr1_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_7",
            "procedure_minutes",
            "PR1.7",
        ),
        serialization_alias="PR1.7",
        title="Procedure Minutes",
        description="O | Item #00397 | LEN:4",
    )

    pr1_8: Optional[List[XCN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_8",
            "anesthesiologist",
            "PR1.8",
        ),
        serialization_alias="PR1.8",
        title="Anesthesiologist",
        description="O | Item #00398 | Table 0010 - Physician ID",
    )

    pr1_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_9",
            "anesthesia_code",
            "PR1.9",
        ),
        serialization_alias="PR1.9",
        title="Anesthesia Code",
        description="O | Item #00399 | Table 0019 - Anesthesia Code | LEN:2",
    )

    pr1_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_10",
            "anesthesia_minutes",
            "PR1.10",
        ),
        serialization_alias="PR1.10",
        title="Anesthesia Minutes",
        description="O | Item #00400 | LEN:4",
    )

    pr1_11: Optional[List[XCN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_11",
            "surgeon",
            "PR1.11",
        ),
        serialization_alias="PR1.11",
        title="Surgeon",
        description="O | Item #00401 | Table 0010 - Physician ID",
    )

    pr1_12: Optional[List[XCN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_12",
            "procedure_practitioner",
            "PR1.12",
        ),
        serialization_alias="PR1.12",
        title="Procedure Practitioner",
        description="O | Item #00402 | Table 0010 - Physician ID",
    )

    pr1_13: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_13",
            "consent_code",
            "PR1.13",
        ),
        serialization_alias="PR1.13",
        title="Consent Code",
        description="O | Item #00403 | Table 0059 - Consent Code",
    )

    pr1_14: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_14",
            "procedure_priority",
            "PR1.14",
        ),
        serialization_alias="PR1.14",
        title="Procedure Priority",
        description="O | Item #00404 | Table 0418 - Procedure Priority | LEN:2",
    )

    pr1_15: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_15",
            "associated_diagnosis_code",
            "PR1.15",
        ),
        serialization_alias="PR1.15",
        title="Associated Diagnosis Code",
        description="O | Item #00772 | Table 0051 - Diagnosis Code",
    )

    pr1_16: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_16",
            "procedure_code_modifier",
            "PR1.16",
        ),
        serialization_alias="PR1.16",
        title="Procedure Code Modifier",
        description="O | Item #01316 | Table 0340 - Procedure code modifier",
    )

    pr1_17: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_17",
            "procedure_drg_type",
            "PR1.17",
        ),
        serialization_alias="PR1.17",
        title="Procedure DRG Type",
        description=(
            "O | Item #01501 | Table 0416 - Procedure DRG Type | LEN:20"
        ),
    )

    pr1_18: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_18",
            "tissue_type_code",
            "PR1.18",
        ),
        serialization_alias="PR1.18",
        title="Tissue Type Code",
        description="O | Item #01502 | Table 0417 - Tissue Type Code",
    )

    pr1_19: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_19",
            "procedure_identifier",
            "PR1.19",
        ),
        serialization_alias="PR1.19",
        title="Procedure Identifier",
        description="C | Item #01848",
    )

    pr1_20: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pr1_20",
            "procedure_action_code",
            "PR1.20",
        ),
        serialization_alias="PR1.20",
        title="Procedure Action Code",
        description=(
            "C | Item #01849 | Table 0206 - Segment action code | LEN:1"
        ),
    )

    @field_validator("pr1_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        if not _RE_SI.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("pr1_7", "pr1_10", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
