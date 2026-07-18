"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: PV2
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.PL import PL
from ..datatypes.TS import TS
from ..datatypes.XCN import XCN
from ..datatypes.XON import XON

_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')
_RE_DT = re.compile(r'(\d{4}([01]\d(\d{2})?)?)?')


class PV2(HL7Model):
    """Patient visit - additional information (S3.3.4).

    Attributes
    ----------
    pv2_1 : PL | None
        PV2.1 - Prior Pending Location (PL) O S3.3.4.1

    pv2_2 : CE | None
        PV2.2 - Accommodation Code (CE) O S3.3.4.2 | 0129 - Accommodation Code

    pv2_3 : CE | None
        PV2.3 - Admit Reason (CE) O S3.3.4.3

    pv2_4 : CE | None
        PV2.4 - Transfer Reason (CE) O S3.3.4.4

    pv2_5 : list[str] | None
        PV2.5 - Patient Valuables (ST) O rep S3.3.4.5

    pv2_6 : str | None
        PV2.6 - Patient Valuables Location (ST) O S3.3.4.6

    pv2_7 : str | None
        PV2.7 - Visit User Code (IS) O S3.3.4.7 | 0130 - Visit User Code

    pv2_8 : TS | None
        PV2.8 - Expected Admit Date (TS) O S3.3.4.8

    pv2_9 : TS | None
        PV2.9 - Expected Discharge Date (TS) O S3.3.4.9

    pv2_10 : str | None
        PV2.10 - Estimated Length of Inpatient Stay (NM) O S3.3.4.10

    pv2_11 : str | None
        PV2.11 - Actual Length of Inpatient Stay (NM) O S3.3.4.11

    pv2_12 : str | None
        PV2.12 - Visit Description (ST) O S3.3.4.12

    pv2_13 : XCN | None
        PV2.13 - Referral Source Code (XCN) O S3.3.4.13

    pv2_14 : str | None
        PV2.14 - Previous Service Date (DT) O S3.3.4.14

    pv2_15 : str | None
        PV2.15 - Employment Illness Related Indicator (ID) O S3.3.4.15 | 0136 - Yes/No Indicator

    pv2_16 : str | None
        PV2.16 - Purge Status Code (IS) O S3.3.4.16 | 0213 - Purge Status

    pv2_17 : str | None
        PV2.17 - Purge Status Date (DT) O S3.3.4.17

    pv2_18 : str | None
        PV2.18 - Special Program Code (IS) O S3.3.4.18 | 0214 - Special Program Codes

    pv2_19 : str | None
        PV2.19 - Retention Indicator (ID) O S3.3.4.19 | 0136 - Yes/No Indicator

    pv2_20 : str | None
        PV2.20 - Expected Number of Insurance Plans (NM) O S3.3.4.20

    pv2_21 : str | None
        PV2.21 - Visit Publicity Code (IS) O S3.3.4.21 | 0215 - Publicity Code

    pv2_22 : str | None
        PV2.22 - Visit Protection Indicator (ID) O S3.3.4.22 | 0136 - Yes/No Indicator

    pv2_23 : list[XON] | None
        PV2.23 - Clinic Organization Name (XON) O rep S3.3.4.23

    pv2_24 : str | None
        PV2.24 - Patient Status Code (IS) O S3.3.4.24 | 0216 - Patient Status

    pv2_25 : str | None
        PV2.25 - Visit Priority Code (IS) O S3.3.4.25 | 0217 - Visit Priority

    pv2_26 : str | None
        PV2.26 - Previous Treatment Date (DT) O S3.3.4.26

    pv2_27 : str | None
        PV2.27 - Expected Discharge Disposition (IS) O S3.3.4.27 | 0112 - Discharged Disposition

    pv2_28 : str | None
        PV2.28 - Signature on File Date (DT) O S3.3.4.28

    pv2_29 : str | None
        PV2.29 - First Similar Illness Date (DT) O S3.3.4.29

    pv2_30 : str | None
        PV2.30 - Patient Charge Adjustment Code (IS) O S3.3.4.30 | 0218 - Charge Adjustment

    pv2_31 : str | None
        PV2.31 - Recurring Service Code (IS) O S3.3.4.31 | 0219 - Recurring Service

    pv2_32 : str | None
        PV2.32 - Billing Media Code (ID) O S3.3.4.32 | 0136 - Yes/No Indicator

    pv2_33 : TS | None
        PV2.33 - Expected Surgery Date & Time (TS) O S3.3.4.33

    pv2_34 : str | None
        PV2.34 - Military Partnership Code (ID) O S3.3.4.34 | 0136 - Yes/No Indicator

    pv2_35 : str | None
        PV2.35 - Military Non-Availabiltiy Code (ID) O S3.3.4.35 | 0136 - Yes/No Indicator

    pv2_36 : str | None
        PV2.36 - Newborn Baby Indicator (ID) O S3.3.4.36 | 0136 - Yes/No Indicator

    pv2_37 : str | None
        PV2.37 - Baby Detained Indicator (ID) O S3.3.4.37 | 0136 - Yes/No Indicator
    """

    pv2_1: Optional[PL] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_1",
            "prior_pending_location",
            "PV2.1",
        ),
        serialization_alias="PV2.1",
        title="Prior Pending Location",
        description="O | Item #00181",
    )

    pv2_2: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_2",
            "accommodation_code",
            "PV2.2",
        ),
        serialization_alias="PV2.2",
        title="Accommodation Code",
        description="O | Item #00182 | Table 0129 - Accommodation Code",
    )

    pv2_3: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_3",
            "admit_reason",
            "PV2.3",
        ),
        serialization_alias="PV2.3",
        title="Admit Reason",
        description="O | Item #00183",
    )

    pv2_4: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_4",
            "transfer_reason",
            "PV2.4",
        ),
        serialization_alias="PV2.4",
        title="Transfer Reason",
        description="O | Item #00184",
    )

    pv2_5: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_5",
            "patient_valuables",
            "PV2.5",
        ),
        serialization_alias="PV2.5",
        title="Patient Valuables",
        description="O | Item #00185 | LEN:25",
    )

    pv2_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_6",
            "patient_valuables_location",
            "PV2.6",
        ),
        serialization_alias="PV2.6",
        title="Patient Valuables Location",
        description="O | Item #00186 | LEN:25",
    )

    pv2_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_7",
            "visit_user_code",
            "PV2.7",
        ),
        serialization_alias="PV2.7",
        title="Visit User Code",
        description="O | Item #00187 | Table 0130 - Visit User Code | LEN:2",
    )

    pv2_8: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_8",
            "expected_admit_date",
            "PV2.8",
        ),
        serialization_alias="PV2.8",
        title="Expected Admit Date",
        description="O | Item #00188",
    )

    pv2_9: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_9",
            "expected_discharge_date",
            "PV2.9",
        ),
        serialization_alias="PV2.9",
        title="Expected Discharge Date",
        description="O | Item #00189",
    )

    pv2_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_10",
            "estimated_length_of_inpatient_stay",
            "PV2.10",
        ),
        serialization_alias="PV2.10",
        title="Estimated Length of Inpatient Stay",
        description="O | Item #00711 | LEN:3",
    )

    pv2_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_11",
            "actual_length_of_inpatient_stay",
            "PV2.11",
        ),
        serialization_alias="PV2.11",
        title="Actual Length of Inpatient Stay",
        description="O | Item #00712 | LEN:3",
    )

    pv2_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_12",
            "visit_description",
            "PV2.12",
        ),
        serialization_alias="PV2.12",
        title="Visit Description",
        description="O | Item #00713 | LEN:50",
    )

    pv2_13: Optional[XCN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_13",
            "referral_source_code",
            "PV2.13",
        ),
        serialization_alias="PV2.13",
        title="Referral Source Code",
        description="O | Item #00714",
    )

    pv2_14: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_14",
            "previous_service_date",
            "PV2.14",
        ),
        serialization_alias="PV2.14",
        title="Previous Service Date",
        description="O | Item #00715 | LEN:8",
    )

    pv2_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_15",
            "employment_illness_related_indicator",
            "PV2.15",
        ),
        serialization_alias="PV2.15",
        title="Employment Illness Related Indicator",
        description="O | Item #00716 | Table 0136 - Yes/No Indicator | LEN:1",
    )

    pv2_16: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_16",
            "purge_status_code",
            "PV2.16",
        ),
        serialization_alias="PV2.16",
        title="Purge Status Code",
        description="O | Item #00717 | Table 0213 - Purge Status | LEN:1",
    )

    pv2_17: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_17",
            "purge_status_date",
            "PV2.17",
        ),
        serialization_alias="PV2.17",
        title="Purge Status Date",
        description="O | Item #00718 | LEN:8",
    )

    pv2_18: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_18",
            "special_program_code",
            "PV2.18",
        ),
        serialization_alias="PV2.18",
        title="Special Program Code",
        description=(
            "O | Item #00719 | Table 0214 - Special Program Codes | LEN:2"
        ),
    )

    pv2_19: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_19",
            "retention_indicator",
            "PV2.19",
        ),
        serialization_alias="PV2.19",
        title="Retention Indicator",
        description="O | Item #00720 | Table 0136 - Yes/No Indicator | LEN:1",
    )

    pv2_20: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_20",
            "expected_number_of_insurance_plans",
            "PV2.20",
        ),
        serialization_alias="PV2.20",
        title="Expected Number of Insurance Plans",
        description="O | Item #00721 | LEN:1",
    )

    pv2_21: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_21",
            "visit_publicity_code",
            "PV2.21",
        ),
        serialization_alias="PV2.21",
        title="Visit Publicity Code",
        description="O | Item #00722 | Table 0215 - Publicity Code | LEN:1",
    )

    pv2_22: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_22",
            "visit_protection_indicator",
            "PV2.22",
        ),
        serialization_alias="PV2.22",
        title="Visit Protection Indicator",
        description="O | Item #00723 | Table 0136 - Yes/No Indicator | LEN:1",
    )

    pv2_23: Optional[List[XON]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_23",
            "clinic_organization_name",
            "PV2.23",
        ),
        serialization_alias="PV2.23",
        title="Clinic Organization Name",
        description="O | Item #00724",
    )

    pv2_24: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_24",
            "patient_status_code",
            "PV2.24",
        ),
        serialization_alias="PV2.24",
        title="Patient Status Code",
        description="O | Item #00725 | Table 0216 - Patient Status | LEN:2",
    )

    pv2_25: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_25",
            "visit_priority_code",
            "PV2.25",
        ),
        serialization_alias="PV2.25",
        title="Visit Priority Code",
        description="O | Item #00726 | Table 0217 - Visit Priority | LEN:1",
    )

    pv2_26: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_26",
            "previous_treatment_date",
            "PV2.26",
        ),
        serialization_alias="PV2.26",
        title="Previous Treatment Date",
        description="O | Item #00727 | LEN:8",
    )

    pv2_27: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_27",
            "expected_discharge_disposition",
            "PV2.27",
        ),
        serialization_alias="PV2.27",
        title="Expected Discharge Disposition",
        description=(
            "O | Item #00728 | Table 0112 - Discharged Disposition | LEN:2"
        ),
    )

    pv2_28: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_28",
            "signature_on_file_date",
            "PV2.28",
        ),
        serialization_alias="PV2.28",
        title="Signature on File Date",
        description="O | Item #00729 | LEN:8",
    )

    pv2_29: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_29",
            "first_similar_illness_date",
            "PV2.29",
        ),
        serialization_alias="PV2.29",
        title="First Similar Illness Date",
        description="O | Item #00730 | LEN:8",
    )

    pv2_30: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_30",
            "patient_charge_adjustment_code",
            "PV2.30",
        ),
        serialization_alias="PV2.30",
        title="Patient Charge Adjustment Code",
        description="O | Item #00731 | Table 0218 - Charge Adjustment | LEN:3",
    )

    pv2_31: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_31",
            "recurring_service_code",
            "PV2.31",
        ),
        serialization_alias="PV2.31",
        title="Recurring Service Code",
        description="O | Item #00732 | Table 0219 - Recurring Service | LEN:2",
    )

    pv2_32: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_32",
            "billing_media_code",
            "PV2.32",
        ),
        serialization_alias="PV2.32",
        title="Billing Media Code",
        description="O | Item #00733 | Table 0136 - Yes/No Indicator | LEN:1",
    )

    pv2_33: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_33",
            "expected_surgery_date_time",
            "PV2.33",
        ),
        serialization_alias="PV2.33",
        title="Expected Surgery Date & Time",
        description="O | Item #00734",
    )

    pv2_34: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_34",
            "military_partnership_code",
            "PV2.34",
        ),
        serialization_alias="PV2.34",
        title="Military Partnership Code",
        description="O | Item #00735 | Table 0136 - Yes/No Indicator | LEN:2",
    )

    pv2_35: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_35",
            "military_non_availabiltiy_code",
            "PV2.35",
        ),
        serialization_alias="PV2.35",
        title="Military Non-Availabiltiy Code",
        description="O | Item #00736 | Table 0136 - Yes/No Indicator | LEN:2",
    )

    pv2_36: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_36",
            "newborn_baby_indicator",
            "PV2.36",
        ),
        serialization_alias="PV2.36",
        title="Newborn Baby Indicator",
        description="O | Item #00737 | Table 0136 - Yes/No Indicator | LEN:1",
    )

    pv2_37: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_37",
            "baby_detained_indicator",
            "PV2.37",
        ),
        serialization_alias="PV2.37",
        title="Baby Detained Indicator",
        description="O | Item #00738 | Table 0136 - Yes/No Indicator | LEN:1",
    )

    @field_validator("pv2_10", "pv2_11", "pv2_20", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    @field_validator("pv2_14", "pv2_17", "pv2_26", "pv2_28", "pv2_29", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        if not _RE_DT.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    model_config = ConfigDict(populate_by_name=True)
