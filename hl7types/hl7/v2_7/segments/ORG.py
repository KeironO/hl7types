"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: ORG
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE
from ..datatypes.CX import CX
from ..datatypes.DR import DR

_RE_SI = re.compile(r'\d*')


class ORG(HL7Model):
    """Practitioner Organization Unit s (S15.4.5).

    Attributes
    ----------
    org_1 : str
        ORG.1 - Set ID - ORG (SI) R S15.4.5.1

    org_2 : CWE | None
        ORG.2 - Organization Unit Code (CWE) O S15.4.5.2 | 0405 - Organization Unit

    org_3 : CWE | None
        ORG.3 - Organization Unit Type Code (CWE) O S15.4.5.3 | 0474 - Organization Unit Type

    org_4 : str | None
        ORG.4 - Primary Org Unit Indicator (ID) O S15.4.5.4 | 0136 - Yes/no Indicator

    org_5 : CX | None
        ORG.5 - Practitioner Org Unit Identifier (CX) O S15.4.5.5

    org_6 : CWE | None
        ORG.6 - Health Care Provider Type Code (CWE) O S15.4.5.6 | 0452 - Health Care Provider Type Code

    org_7 : CWE | None
        ORG.7 - Health Care Provider Classification Code (CWE) O S15.4.5.7 | 0453 - Health Care Provider Classification

    org_8 : CWE | None
        ORG.8 - Health Care Provider Area of Specialization Code (CWE) O S15.4.5.8 | 0454 - Health Care Provider Area of Specialization

    org_9 : DR | None
        ORG.9 - Effective Date Range (DR) O S15.4.5.9

    org_10 : CWE | None
        ORG.10 - Employment Status Code (CWE) O S15.4.5.10 | 0066 - Employment Status

    org_11 : str | None
        ORG.11 - Board Approval Indicator (ID) O S15.4.5.11 | 0136 - Yes/no Indicator

    org_12 : str | None
        ORG.12 - Primary Care Physician Indicator (ID) O S15.4.5.12 | 0136 - Yes/no Indicator

    org_13 : list[CWE] | None
        ORG.13 - Cost Center Code (CWE) O rep S15.4.5.13 | 0539 - Cost Center Code
    """

    org_1: str = Field(
        validation_alias=AliasChoices(
            "org_1",
            "set_id_org",
            "ORG.1",
        ),
        serialization_alias="ORG.1",
        title="Set ID - ORG",
        description="R | Item #01459 | LEN:4",
    )

    org_2: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "org_2",
            "organization_unit_code",
            "ORG.2",
        ),
        serialization_alias="ORG.2",
        title="Organization Unit Code",
        description="O | Item #01460 | Table 0405 - Organization Unit",
    )

    org_3: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "org_3",
            "organization_unit_type_code",
            "ORG.3",
        ),
        serialization_alias="ORG.3",
        title="Organization Unit Type Code",
        description="O | Item #01625 | Table 0474 - Organization Unit Type",
    )

    org_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "org_4",
            "primary_org_unit_indicator",
            "ORG.4",
        ),
        serialization_alias="ORG.4",
        title="Primary Org Unit Indicator",
        description="O | Item #01462 | Table 0136 - Yes/no Indicator | LEN:1",
    )

    org_5: Optional[CX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "org_5",
            "practitioner_org_unit_identifier",
            "ORG.5",
        ),
        serialization_alias="ORG.5",
        title="Practitioner Org Unit Identifier",
        description="O | Item #01463",
    )

    org_6: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "org_6",
            "health_care_provider_type_code",
            "ORG.6",
        ),
        serialization_alias="ORG.6",
        title="Health Care Provider Type Code",
        description=(
            "O | Item #01464 | Table 0452 - Health Care Provider Type Code"
        ),
    )

    org_7: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "org_7",
            "health_care_provider_classification_code",
            "ORG.7",
        ),
        serialization_alias="ORG.7",
        title="Health Care Provider Classification Code",
        description=(
            "O | Item #01614 | Table 0453 - Health Care Provider Classification"
        ),
    )

    org_8: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "org_8",
            "health_care_provider_area_of_specialization_code",
            "ORG.8",
        ),
        serialization_alias="ORG.8",
        title="Health Care Provider Area of Specialization Code",
        description=(
            "O | Item #01615 | Table 0454 - Health Care Provider Area of "
            "Specialization"
        ),
    )

    org_9: Optional[DR] = Field(
        default=None,
        validation_alias=AliasChoices(
            "org_9",
            "effective_date_range",
            "ORG.9",
        ),
        serialization_alias="ORG.9",
        title="Effective Date Range",
        description="O | Item #01465",
    )

    org_10: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "org_10",
            "employment_status_code",
            "ORG.10",
        ),
        serialization_alias="ORG.10",
        title="Employment Status Code",
        description="O | Item #01276 | Table 0066 - Employment Status",
    )

    org_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "org_11",
            "board_approval_indicator",
            "ORG.11",
        ),
        serialization_alias="ORG.11",
        title="Board Approval Indicator",
        description="O | Item #01467 | Table 0136 - Yes/no Indicator | LEN:1",
    )

    org_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "org_12",
            "primary_care_physician_indicator",
            "ORG.12",
        ),
        serialization_alias="ORG.12",
        title="Primary Care Physician Indicator",
        description="O | Item #01468 | Table 0136 - Yes/no Indicator | LEN:1",
    )

    org_13: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "org_13",
            "cost_center_code",
            "ORG.13",
        ),
        serialization_alias="ORG.13",
        title="Cost Center Code",
        description="O | Item #01891 | Table 0539 - Cost Center Code",
    )

    @field_validator("org_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        if not _RE_SI.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    model_config = ConfigDict(populate_by_name=True)
