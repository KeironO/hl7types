"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: IN3
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.CX import CX
from ..datatypes.TS import TS
from ..datatypes.XCN import XCN
from ..datatypes.XTN import XTN


class IN3(HL7Model):
    """Insurance additional info - certification (S6.4.8).

    Attributes
    ----------
    in3_1 : str
        IN3.1 - Set ID - Insurance Certification (SI) R S6.4.8.1

    in3_2 : CX | None
        IN3.2 - Certification Number (CX) O S6.4.8.2

    in3_3 : list[XCN] | None
        IN3.3 - Certified By (XCN) O rep S6.4.8.3

    in3_4 : str | None
        IN3.4 - Certification Required (ID) O S6.4.8.4 | 0136 - Yes/No Indicator

    in3_5 : str | None
        IN3.5 - Penalty (CM) O S6.4.8.5 | 0148 - Penalty Type

    in3_6 : TS | None
        IN3.6 - Certification Date/Time (TS) O S6.4.8.6

    in3_7 : TS | None
        IN3.7 - Certification Modify Date/Time (TS) NA S6.4.8.7

    in3_8 : list[XCN] | None
        IN3.8 - Operator (XCN) NA rep S6.4.8.8

    in3_9 : str | None
        IN3.9 - Certification Begin Date (DT) NA S6.4.8.9

    in3_10 : str | None
        IN3.10 - Certification End Date (DT) NA S6.4.8.10

    in3_11 : str | None
        IN3.11 - Days (CM) NA S6.4.8.11 | 0149 - Day Type

    in3_12 : CE | None
        IN3.12 - Non-Concur Code/Description (CE) NA S6.4.8.12 | 0233 - Non-concur Code/Description

    in3_13 : TS | None
        IN3.13 - Non-Concur Effective Date/Time (TS) NA S6.4.8.13

    in3_14 : list[XCN] | None
        IN3.14 - Physician Reviewer (XCN) NA rep S6.4.8.14

    in3_15 : str | None
        IN3.15 - Certification Contact (ST) NA S6.4.8.15

    in3_16 : list[XTN] | None
        IN3.16 - Certification Contact Phone Number (XTN) NA rep S6.4.8.16

    in3_17 : CE | None
        IN3.17 - Appeal Reason (CE) NA S6.4.8.17

    in3_18 : CE | None
        IN3.18 - Certification Agency (CE) NA S6.4.8.18

    in3_19 : list[XTN] | None
        IN3.19 - Certification Agency Phone Number (XTN) NA rep S6.4.8.19

    in3_20 : list[str] | None
        IN3.20 - Pre-Certification required/Window (CM) NA rep S6.4.8.20

    in3_21 : str | None
        IN3.21 - Case Manager (ST) NA S6.4.8.21

    in3_22 : str | None
        IN3.22 - Second Opinion Date (DT) NA S6.4.8.22

    in3_23 : str | None
        IN3.23 - Second Opinion Status (IS) NA S6.4.8.23 | 0151 - Second Opinion Status

    in3_24 : list[str] | None
        IN3.24 - Second Opinion Documentation Received (IS) NA rep S6.4.8.24 | 0152 - Second Opinion Documentation Received

    in3_25 : list[XCN] | None
        IN3.25 - Second Opinion Physician (XCN) NA rep S6.4.8.25
    """

    in3_1: str = Field(
        validation_alias=AliasChoices(
            "in3_1",
            "set_id_insurance_certification",
            "IN3.1",
        ),
        serialization_alias="IN3.1",
        title="Set ID - Insurance Certification",
        description="R | Item #00502 | LEN:4",
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
        description="O | Item #00503",
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
        description="O | Item #00504",
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
        description="O | Item #00505 | Table 0136 - Yes/No Indicator | LEN:1",
    )

    in3_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in3_5",
            "penalty",
            "IN3.5",
        ),
        serialization_alias="IN3.5",
        title="Penalty",
        description="O | Item #00506 | Table 0148 - Penalty Type",
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
        description="O | Item #00507",
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
        description="NA | Item #00508",
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
        description="NA | Item #00509",
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
        description="NA | Item #00510 | LEN:8",
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
        description="NA | Item #00511 | LEN:8",
    )

    in3_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in3_11",
            "days",
            "IN3.11",
        ),
        serialization_alias="IN3.11",
        title="Days",
        description="NA | Item #00512 | Table 0149 - Day Type",
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
        description=(
            "NA | Item #00513 | Table 0233 - Non-concur Code/Description"
        ),
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
        description="NA | Item #00514",
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
        description="NA | Item #00515",
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
        description="NA | Item #00516 | LEN:48",
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
        description="NA | Item #00517",
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
        description="NA | Item #00518",
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
        description="NA | Item #00519",
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
        description="NA | Item #00520",
    )

    in3_20: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in3_20",
            "pre_certification_required_window",
            "IN3.20",
        ),
        serialization_alias="IN3.20",
        title="Pre-Certification required/Window",
        description="NA | Item #00521",
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
        description="NA | Item #00522 | LEN:48",
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
        description="NA | Item #00523 | LEN:8",
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
        description=(
            "NA | Item #00524 | Table 0151 - Second Opinion Status | LEN:1"
        ),
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
        description=(
            "NA | Item #00525 | Table 0152 - Second Opinion Documentation "
            "Received | LEN:1"
        ),
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
        description="NA | Item #00526",
    )

    @field_validator("in3_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("in3_9", "in3_10", "in3_22", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2})?)?)?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    model_config = {"populate_by_name": True}
