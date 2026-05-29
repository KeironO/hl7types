"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: ORG
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CWE import CWE
from ..datatypes.CX import CX
from ..datatypes.DR import DR


class ORG(BaseModel):
    """HL7 v2 ORG segment.

    Attributes
    ----------
    org_1 : str
        ORG.1 (req) - Set ID - ORG (SI)

    org_2 : CWE | None
        ORG.2 (opt) - Organization Unit Code (CWE)

    org_3 : CWE | None
        ORG.3 (opt) - Organization Unit Type Code (CWE)

    org_4 : str | None
        ORG.4 (opt) - Primary Org Unit Indicator (ID)

    org_5 : CX | None
        ORG.5 (opt) - Practitioner Org Unit Identifier (CX)

    org_6 : CWE | None
        ORG.6 (opt) - Health Care Provider Type Code (CWE)

    org_7 : CWE | None
        ORG.7 (opt) - Health Care Provider Classification Code (CWE)

    org_8 : CWE | None
        ORG.8 (opt) - Health Care Provider Area of Specialization Code (CWE)

    org_9 : DR | None
        ORG.9 (opt) - Effective Date Range (DR)

    org_10 : CWE | None
        ORG.10 (opt) - Employment Status Code (CWE)

    org_11 : str | None
        ORG.11 (opt) - Board Approval Indicator (ID)

    org_12 : str | None
        ORG.12 (opt) - Primary Care Physician Indicator (ID)

    org_13 : list[CWE] | None
        ORG.13 (opt, rep) - Cost Center Code (CWE)
    """

    org_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "org_1",
            "set_id_org",
            "ORG.1",
        ),
        serialization_alias="ORG.1",
        title="Set ID - ORG",
        description="Item #1459",
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
        description="Item #1460 | Table HL70405",
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
        description="Item #1625 | Table HL70474",
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
        description="Item #1462 | Table HL70136",
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
        description="Item #1463",
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
        description="Item #1464 | Table HL70452",
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
        description="Item #1614 | Table HL70453",
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
        description="Item #1615 | Table HL70454",
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
        description="Item #1465",
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
        description="Item #1276 | Table HL70066",
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
        description="Item #1467 | Table HL70136",
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
        description="Item #1468 | Table HL70136",
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
        description="Item #1891 | Table HL70539",
    )

    model_config = {"populate_by_name": True}
