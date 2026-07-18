"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: IN3
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, ValidationInfo, field_validator
from hl7types.hl7 import HL7Model
from hl7types.hl7._validators import _apply_dt_fallback

from ..datatypes.CWE import CWE
from ..datatypes.CX import CX
from ..datatypes.DTN import DTN
from ..datatypes.ICD import ICD
from ..datatypes.MOP import MOP
from ..datatypes.XCN import XCN
from ..datatypes.XTN import XTN

_RE_SI = re.compile(r'\d*')
_RE_DTM = re.compile(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?')
_RE_DT = re.compile(r'(\d{4}([01]\d(\d{2})?)?)?')


class IN3(HL7Model):
    """Insurance Additional Information, Certification (S6.5.8).

    Attributes
    ----------
    in3_1 : str
        IN3.1 - Set ID - IN3 (SI) R S6.5.8.1

    in3_2 : CX | None
        IN3.2 - Certification Number (CX) O S6.5.8.2

    in3_3 : list[XCN] | None
        IN3.3 - Certified By (XCN) O rep S6.5.8.3

    in3_4 : str | None
        IN3.4 - Certification Required (ID) O S6.5.8.4 | 0136 - Yes/no Indicator

    in3_5 : MOP | None
        IN3.5 - Penalty (MOP) O S6.5.8.5

    in3_6 : str | None
        IN3.6 - Certification Date/Time (DTM) O S6.5.8.6

    in3_7 : str | None
        IN3.7 - Certification Modify Date/Time (DTM) O S6.5.8.7

    in3_8 : list[XCN] | None
        IN3.8 - Operator (XCN) O rep S6.5.8.8

    in3_9 : str | None
        IN3.9 - Certification Begin Date (DT) O S6.5.8.9

    in3_10 : str | None
        IN3.10 - Certification End Date (DT) O S6.5.8.10

    in3_11 : DTN | None
        IN3.11 - Days (DTN) O S6.5.8.11

    in3_12 : CWE | None
        IN3.12 - Non-Concur Code/Description (CWE) O S6.5.8.12 | 0233 - Non-Concur Code/Description

    in3_13 : str | None
        IN3.13 - Non-Concur Effective Date/Time (DTM) O S6.5.8.13

    in3_14 : list[XCN] | None
        IN3.14 - Physician Reviewer (XCN) O rep S6.5.8.14 | 0010 - Physician ID

    in3_15 : str | None
        IN3.15 - Certification Contact (ST) O S6.5.8.15

    in3_16 : list[XTN] | None
        IN3.16 - Certification Contact Phone Number (XTN) O rep S6.5.8.16

    in3_17 : CWE | None
        IN3.17 - Appeal Reason (CWE) O S6.5.8.17 | 0345 - Appeal Reason

    in3_18 : CWE | None
        IN3.18 - Certification Agency (CWE) O S6.5.8.18 | 0346 - Certification Agency

    in3_19 : list[XTN] | None
        IN3.19 - Certification Agency Phone Number (XTN) O rep S6.5.8.19

    in3_20 : list[ICD] | None
        IN3.20 - Pre-Certification Requirement (ICD) O rep S6.5.8.20

    in3_21 : str | None
        IN3.21 - Case Manager (ST) O S6.5.8.21

    in3_22 : str | None
        IN3.22 - Second Opinion Date (DT) O S6.5.8.22

    in3_23 : CWE | None
        IN3.23 - Second Opinion Status (CWE) O S6.5.8.23 | 0151 - Second Opinion Status

    in3_24 : list[CWE] | None
        IN3.24 - Second Opinion Documentation Received (CWE) O rep S6.5.8.24 | 0152 - Second Opinion Documentation Received

    in3_25 : list[XCN] | None
        IN3.25 - Second Opinion Physician (XCN) O rep S6.5.8.25 | 0010 - Physician ID
    """

    in3_1: str = Field(
        validation_alias=AliasChoices(
            "in3_1",
            "set_id_in3",
            "IN3.1",
        ),
        serialization_alias="IN3.1",
        title="Set ID - IN3",
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
        description="O | Item #00505 | Table 0136 - Yes/no Indicator | LEN:1",
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
        description="O | Item #00506",
    )

    in3_6: Optional[str] = Field(
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

    in3_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in3_7",
            "certification_modify_date_time",
            "IN3.7",
        ),
        serialization_alias="IN3.7",
        title="Certification Modify Date/Time",
        description="O | Item #00508",
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
        description="O | Item #00509",
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
        description="O | Item #00510",
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
        description="O | Item #00511",
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
        description="O | Item #00512",
    )

    in3_12: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in3_12",
            "non_concur_code_description",
            "IN3.12",
        ),
        serialization_alias="IN3.12",
        title="Non-Concur Code/Description",
        description=(
            "O | Item #00513 | Table 0233 - Non-Concur Code/Description"
        ),
    )

    in3_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in3_13",
            "non_concur_effective_date_time",
            "IN3.13",
        ),
        serialization_alias="IN3.13",
        title="Non-Concur Effective Date/Time",
        description="O | Item #00514",
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
        description="O | Item #00515 | Table 0010 - Physician ID",
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
        description="O | Item #00516",
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
        description="O | Item #00517",
    )

    in3_17: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in3_17",
            "appeal_reason",
            "IN3.17",
        ),
        serialization_alias="IN3.17",
        title="Appeal Reason",
        description="O | Item #00518 | Table 0345 - Appeal Reason",
    )

    in3_18: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in3_18",
            "certification_agency",
            "IN3.18",
        ),
        serialization_alias="IN3.18",
        title="Certification Agency",
        description="O | Item #00519 | Table 0346 - Certification Agency",
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
        description="O | Item #00520",
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
        description="O | Item #00521",
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
        description="O | Item #00522",
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
        description="O | Item #00523",
    )

    in3_23: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in3_23",
            "second_opinion_status",
            "IN3.23",
        ),
        serialization_alias="IN3.23",
        title="Second Opinion Status",
        description="O | Item #00524 | Table 0151 - Second Opinion Status",
    )

    in3_24: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in3_24",
            "second_opinion_documentation_received",
            "IN3.24",
        ),
        serialization_alias="IN3.24",
        title="Second Opinion Documentation Received",
        description=(
            "O | Item #00525 | Table 0152 - Second Opinion Documentation Received"
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
        description="O | Item #00526 | Table 0010 - Physician ID",
    )

    @field_validator("in3_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        if not _RE_SI.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("in3_6", "in3_7", "in3_13", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        if _RE_DTM.fullmatch(v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    @field_validator("in3_9", "in3_10", "in3_22", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        if not _RE_DT.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    model_config = ConfigDict(populate_by_name=True)
