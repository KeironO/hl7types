"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: IN3
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE
from ..datatypes.TS import TS


class IN3(BaseModel):
    """HL7 v2 IN3 segment.

    Attributes
    ----------
    in3_1 : str
        IN3.1 (req) - Set ID - insurance certification (SI)

    in3_2 : str | None
        IN3.2 (opt) - Certification number (ST)

    in3_3 : str | None
        IN3.3 (opt) - Certified by (CN)

    in3_4 : str | None
        IN3.4 (opt) - Certification required (ID)

    in3_5 : str | None
        IN3.5 (opt) - Penalty (CM)

    in3_6 : TS | None
        IN3.6 (opt) - Certification date / time (TS)

    in3_7 : TS | None
        IN3.7 (opt) - Certification modify date / time (TS)

    in3_8 : str | None
        IN3.8 (opt) - Operator (CN)

    in3_9 : str | None
        IN3.9 (opt) - Certification begin date (DT)

    in3_10 : str | None
        IN3.10 (opt) - Certification end date (DT)

    in3_11 : str | None
        IN3.11 (opt) - Days (CM)

    in3_12 : CE | None
        IN3.12 (opt) - Non-concur code / description (CE)

    in3_13 : TS | None
        IN3.13 (opt) - Non-concur effective date / time (TS)

    in3_14 : str | None
        IN3.14 (opt) - Physician reviewer (CN)

    in3_15 : str | None
        IN3.15 (opt) - Certification contact (ST)

    in3_16 : list[str] | None
        IN3.16 (opt, rep) - Certification contact phone number (TN)

    in3_17 : CE | None
        IN3.17 (opt) - Appeal reason (CE)

    in3_18 : CE | None
        IN3.18 (opt) - Certification agency (CE)

    in3_19 : list[str] | None
        IN3.19 (opt, rep) - Certification agency phone number (TN)

    in3_20 : list[str] | None
        IN3.20 (opt, rep) - Pre-certification required / window (CM)

    in3_21 : str | None
        IN3.21 (opt) - Case manager (ST)

    in3_22 : str | None
        IN3.22 (opt) - Second opinion date (DT)

    in3_23 : str | None
        IN3.23 (opt) - Second opinion status (ID)

    in3_24 : str | None
        IN3.24 (opt) - Second opinion documentation received (ID)

    in3_25 : str | None
        IN3.25 (opt) - Second opinion practitioner (CN)
    """

    in3_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "in3_1",
            "set_id_insurance_certification",
            "IN3.1",
        ),
        serialization_alias="IN3.1",
        title="Set ID - insurance certification",
        description="Item #502",
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
        description="Item #503",
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
        title="Certification required",
        description="Item #505 | Table HL70136",
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
        description="Item #506 | Table HL70148",
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
        title="Certification modify date / time",
        description="Item #508",
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
        title="Certification begin date",
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
        title="Certification end date",
        description="Item #511",
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
        description="Item #512 | Table HL70149",
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
        description="Item #513",
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
        description="Item #514",
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
        description="Item #515",
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
        description="Item #516",
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
        title="Appeal reason",
        description="Item #518",
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
        description="Item #519",
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
        description="Item #520",
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
        description="Item #521 | Table HL70150",
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
        title="Second opinion date",
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
        title="Second opinion status",
        description="Item #524 | Table HL70151",
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
        description="Item #525 | Table HL70152",
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
        description="Item #526",
    )

    model_config = {"populate_by_name": True}
