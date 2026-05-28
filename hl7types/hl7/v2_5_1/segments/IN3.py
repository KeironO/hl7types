"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: IN3
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE
from ..datatypes.CX import CX
from ..datatypes.DTN import DTN
from ..datatypes.ICD import ICD
from ..datatypes.MOP import MOP
from ..datatypes.TS import TS
from ..datatypes.XCN import XCN
from ..datatypes.XTN import XTN


class IN3(BaseModel):
    """HL7 v2 IN3 segment."""

    in3_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "in3_1",
            "set_id_in3",
            "IN3.1",
        ),
        serialization_alias="IN3.1",
        title="Set ID - IN3",
        description="Item #502",
    )

    in3_2: Optional[CX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in3_2",
            "certification_number",
            "IN3.2",
        ),
        serialization_alias="IN3.2",
        title="Certification Number",
        description="Item #503",
    )

    in3_3: Optional[List[XCN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in3_3",
            "certified_by",
            "IN3.3",
        ),
        serialization_alias="IN3.3",
        title="Certified By",
        description="Item #504",
    )

    in3_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in3_4",
            "certification_required",
            "IN3.4",
        ),
        serialization_alias="IN3.4",
        title="Certification Required",
        description="Item #505 | Table HL70136",
    )

    in3_5: Optional[MOP] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in3_5",
            "penalty",
            "IN3.5",
        ),
        serialization_alias="IN3.5",
        title="Penalty",
        description="Item #506",
    )

    in3_6: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in3_6",
            "certification_date_time",
            "IN3.6",
        ),
        serialization_alias="IN3.6",
        title="Certification Date/Time",
        description="Item #507",
    )

    in3_7: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in3_7",
            "certification_modify_date_time",
            "IN3.7",
        ),
        serialization_alias="IN3.7",
        title="Certification Modify Date/Time",
        description="Item #508",
    )

    in3_8: Optional[List[XCN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in3_8",
            "operator",
            "IN3.8",
        ),
        serialization_alias="IN3.8",
        title="Operator",
        description="Item #509",
    )

    in3_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in3_9",
            "certification_begin_date",
            "IN3.9",
        ),
        serialization_alias="IN3.9",
        title="Certification Begin Date",
        description="Item #510",
    )

    in3_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in3_10",
            "certification_end_date",
            "IN3.10",
        ),
        serialization_alias="IN3.10",
        title="Certification End Date",
        description="Item #511",
    )

    in3_11: Optional[DTN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in3_11",
            "days",
            "IN3.11",
        ),
        serialization_alias="IN3.11",
        title="Days",
        description="Item #512",
    )

    in3_12: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in3_12",
            "non_concur_code_description",
            "IN3.12",
        ),
        serialization_alias="IN3.12",
        title="Non-Concur Code/Description",
        description="Item #513 | Table HL70233",
    )

    in3_13: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in3_13",
            "non_concur_effective_date_time",
            "IN3.13",
        ),
        serialization_alias="IN3.13",
        title="Non-Concur Effective Date/Time",
        description="Item #514",
    )

    in3_14: Optional[List[XCN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in3_14",
            "physician_reviewer",
            "IN3.14",
        ),
        serialization_alias="IN3.14",
        title="Physician Reviewer",
        description="Item #515 | Table HL70010",
    )

    in3_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in3_15",
            "certification_contact",
            "IN3.15",
        ),
        serialization_alias="IN3.15",
        title="Certification Contact",
        description="Item #516",
    )

    in3_16: Optional[List[XTN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in3_16",
            "certification_contact_phone_number",
            "IN3.16",
        ),
        serialization_alias="IN3.16",
        title="Certification Contact Phone Number",
        description="Item #517",
    )

    in3_17: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in3_17",
            "appeal_reason",
            "IN3.17",
        ),
        serialization_alias="IN3.17",
        title="Appeal Reason",
        description="Item #518 | Table HL70345",
    )

    in3_18: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in3_18",
            "certification_agency",
            "IN3.18",
        ),
        serialization_alias="IN3.18",
        title="Certification Agency",
        description="Item #519 | Table HL70346",
    )

    in3_19: Optional[List[XTN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in3_19",
            "certification_agency_phone_number",
            "IN3.19",
        ),
        serialization_alias="IN3.19",
        title="Certification Agency Phone Number",
        description="Item #520",
    )

    in3_20: Optional[List[ICD]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in3_20",
            "pre_certification_requirement",
            "IN3.20",
        ),
        serialization_alias="IN3.20",
        title="Pre-Certification Requirement",
        description="Item #521",
    )

    in3_21: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in3_21",
            "case_manager",
            "IN3.21",
        ),
        serialization_alias="IN3.21",
        title="Case Manager",
        description="Item #522",
    )

    in3_22: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in3_22",
            "second_opinion_date",
            "IN3.22",
        ),
        serialization_alias="IN3.22",
        title="Second Opinion Date",
        description="Item #523",
    )

    in3_23: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in3_23",
            "second_opinion_status",
            "IN3.23",
        ),
        serialization_alias="IN3.23",
        title="Second Opinion Status",
        description="Item #524 | Table HL70151",
    )

    in3_24: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in3_24",
            "second_opinion_documentation_received",
            "IN3.24",
        ),
        serialization_alias="IN3.24",
        title="Second Opinion Documentation Received",
        description="Item #525 | Table HL70152",
    )

    in3_25: Optional[List[XCN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in3_25",
            "second_opinion_physician",
            "IN3.25",
        ),
        serialization_alias="IN3.25",
        title="Second Opinion Physician",
        description="Item #526 | Table HL70010",
    )

    model_config = {"populate_by_name": True}
