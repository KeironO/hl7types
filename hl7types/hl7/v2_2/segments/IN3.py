"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: IN3
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.TS import TS


class IN3(HL7Model):
    """INSURANCE ADDITIONAL INFO-CERTIFICATION (S6.4.7).

    Attributes
    ----------
    in3_1 : str
        IN3.1 - Set ID - insurance certification (SI) R S6.4.7.1

    in3_2 : str | None
        IN3.2 - Certification number (ST) NA S6.4.7.2

    in3_3 : str | None
        IN3.3 - Certified by (CN) NA S6.4.7.3

    in3_4 : str | None
        IN3.4 - Certification required (ID) NA S6.4.7.4 | 0136 - Y/N Indicator

    in3_5 : str | None
        IN3.5 - Penalty (CM) NA S6.4.7.5 | 0148 - PENALTY TYPE

    in3_6 : TS | None
        IN3.6 - Certification date / time (TS) NA S6.4.7.6

    in3_7 : TS | None
        IN3.7 - Certification modify date / time (TS) NA S6.4.7.7

    in3_8 : str | None
        IN3.8 - Operator (CN) NA S6.4.7.8

    in3_9 : str | None
        IN3.9 - Certification begin date (DT) NA S6.4.7.9

    in3_10 : str | None
        IN3.10 - Certification end date (DT) NA S6.4.7.10

    in3_11 : str | None
        IN3.11 - Days (CM) NA S6.4.7.11 | 0149 - DAY TYPE

    in3_12 : CE | None
        IN3.12 - Non-concur code / description (CE) NA S6.4.7.12

    in3_13 : TS | None
        IN3.13 - Non-concur effective date / time (TS) NA S6.4.7.13

    in3_14 : str | None
        IN3.14 - Physician reviewer (CN) NA S6.4.7.14

    in3_15 : str | None
        IN3.15 - Certification contact (ST) NA S6.4.7.15

    in3_16 : list[str] | None
        IN3.16 - Certification contact phone number (TN) NA rep S6.4.7.16

    in3_17 : CE | None
        IN3.17 - Appeal reason (CE) NA S6.4.7.17

    in3_18 : CE | None
        IN3.18 - Certification agency (CE) NA S6.4.7.18

    in3_19 : list[str] | None
        IN3.19 - Certification agency phone number (TN) NA rep S6.4.7.19

    in3_20 : list[str] | None
        IN3.20 - Pre-certification required / window (CM) NA rep S6.4.7.20 | 0150 - PRECERTIFICATION PATIENT TYPE

    in3_21 : str | None
        IN3.21 - Case manager (ST) NA S6.4.7.21

    in3_22 : str | None
        IN3.22 - Second opinion date (DT) NA S6.4.7.22

    in3_23 : str | None
        IN3.23 - Second opinion status (ID) NA S6.4.7.23 | 0151 - SECOND OPINION STATUS

    in3_24 : str | None
        IN3.24 - Second opinion documentation received (ID) NA S6.4.7.24 | 0152 - SECOND OPINION DOCUMENTATION RECEIVED

    in3_25 : str | None
        IN3.25 - Second opinion practitioner (CN) NA S6.4.7.25
    """

    in3_1: str = Field(
        validation_alias=AliasChoices(
            "in3_1",
            "set_id_insurance_certification",
            "IN3.1",
        ),
        serialization_alias="IN3.1",
        title="Set ID - insurance certification",
        description="R | Item #00502 | LEN:4",
    )

    in3_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in3_2",
            "certification_number",
            "IN3.2",
        ),
        serialization_alias="IN3.2",
        title="Certification number",
        description="NA | Item #00503 | LEN:25",
    )

    in3_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in3_3",
            "certified_by",
            "IN3.3",
        ),
        serialization_alias="IN3.3",
        title="Certified by",
        description="NA | Item #00504",
    )

    in3_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in3_4",
            "certification_required",
            "IN3.4",
        ),
        serialization_alias="IN3.4",
        title="Certification required",
        description="NA | Item #00505 | Table 0136 - Y/N Indicator | LEN:1",
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
        description="NA | Item #00506 | Table 0148 - PENALTY TYPE",
    )

    in3_6: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in3_6",
            "certification_date_time",
            "IN3.6",
        ),
        serialization_alias="IN3.6",
        title="Certification date / time",
        description="NA | Item #00507",
    )

    in3_7: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in3_7",
            "certification_modify_date_time",
            "IN3.7",
        ),
        serialization_alias="IN3.7",
        title="Certification modify date / time",
        description="NA | Item #00508",
    )

    in3_8: Optional[str] = Field(
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
        title="Certification begin date",
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
        title="Certification end date",
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
        description="NA | Item #00512 | Table 0149 - DAY TYPE",
    )

    in3_12: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in3_12",
            "non_concur_code_description",
            "IN3.12",
        ),
        serialization_alias="IN3.12",
        title="Non-concur code / description",
        description="NA | Item #00513",
    )

    in3_13: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in3_13",
            "non_concur_effective_date_time",
            "IN3.13",
        ),
        serialization_alias="IN3.13",
        title="Non-concur effective date / time",
        description="NA | Item #00514",
    )

    in3_14: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in3_14",
            "physician_reviewer",
            "IN3.14",
        ),
        serialization_alias="IN3.14",
        title="Physician reviewer",
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
        title="Certification contact",
        description="NA | Item #00516 | LEN:48",
    )

    in3_16: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in3_16",
            "certification_contact_phone_number",
            "IN3.16",
        ),
        serialization_alias="IN3.16",
        title="Certification contact phone number",
        description="NA | Item #00517 | LEN:40",
    )

    in3_17: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in3_17",
            "appeal_reason",
            "IN3.17",
        ),
        serialization_alias="IN3.17",
        title="Appeal reason",
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
        title="Certification agency",
        description="NA | Item #00519",
    )

    in3_19: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in3_19",
            "certification_agency_phone_number",
            "IN3.19",
        ),
        serialization_alias="IN3.19",
        title="Certification agency phone number",
        description="NA | Item #00520 | LEN:40",
    )

    in3_20: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in3_20",
            "pre_certification_required_window",
            "IN3.20",
        ),
        serialization_alias="IN3.20",
        title="Pre-certification required / window",
        description=(
            "NA | Item #00521 | Table 0150 - PRECERTIFICATION PATIENT TYPE"
        ),
    )

    in3_21: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in3_21",
            "case_manager",
            "IN3.21",
        ),
        serialization_alias="IN3.21",
        title="Case manager",
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
        title="Second opinion date",
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
        title="Second opinion status",
        description=(
            "NA | Item #00524 | Table 0151 - SECOND OPINION STATUS | LEN:1"
        ),
    )

    in3_24: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in3_24",
            "second_opinion_documentation_received",
            "IN3.24",
        ),
        serialization_alias="IN3.24",
        title="Second opinion documentation received",
        description=(
            "NA | Item #00525 | Table 0152 - SECOND OPINION DOCUMENTATION "
            "RECEIVED | LEN:1"
        ),
    )

    in3_25: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "in3_25",
            "second_opinion_practitioner",
            "IN3.25",
        ),
        serialization_alias="IN3.25",
        title="Second opinion practitioner",
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
