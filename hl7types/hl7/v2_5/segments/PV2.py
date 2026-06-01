"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: PV2
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator

from ..datatypes.CE import CE
from ..datatypes.PL import PL
from ..datatypes.TS import TS
from ..datatypes.XCN import XCN
from ..datatypes.XON import XON


class PV2(HL7Model):
    """HL7 v2 PV2 segment.

    Attributes
    ----------
    pv2_1 : PL | None
        PV2.1 (opt) - Prior Pending Location (PL)

    pv2_2 : CE | None
        PV2.2 (opt) - Accommodation Code (CE)

    pv2_3 : CE | None
        PV2.3 (opt) - Admit Reason (CE)

    pv2_4 : CE | None
        PV2.4 (opt) - Transfer Reason (CE)

    pv2_5 : list[str] | None
        PV2.5 (opt, rep) - Patient Valuables (ST)

    pv2_6 : str | None
        PV2.6 (opt) - Patient Valuables Location (ST)

    pv2_7 : list[str] | None
        PV2.7 (opt, rep) - Visit User Code (IS)

    pv2_8 : TS | None
        PV2.8 (opt) - Expected Admit Date/Time (TS)

    pv2_9 : TS | None
        PV2.9 (opt) - Expected Discharge Date/Time (TS)

    pv2_10 : str | None
        PV2.10 (opt) - Estimated Length of Inpatient Stay (NM)

    pv2_11 : str | None
        PV2.11 (opt) - Actual Length of Inpatient Stay (NM)

    pv2_12 : str | None
        PV2.12 (opt) - Visit Description (ST)

    pv2_13 : list[XCN] | None
        PV2.13 (opt, rep) - Referral Source Code (XCN)

    pv2_14 : str | None
        PV2.14 (opt) - Previous Service Date (DT)

    pv2_15 : str | None
        PV2.15 (opt) - Employment Illness Related Indicator (ID)

    pv2_16 : str | None
        PV2.16 (opt) - Purge Status Code (IS)

    pv2_17 : str | None
        PV2.17 (opt) - Purge Status Date (DT)

    pv2_18 : str | None
        PV2.18 (opt) - Special Program Code (IS)

    pv2_19 : str | None
        PV2.19 (opt) - Retention Indicator (ID)

    pv2_20 : str | None
        PV2.20 (opt) - Expected Number of Insurance Plans (NM)

    pv2_21 : str | None
        PV2.21 (opt) - Visit Publicity Code (IS)

    pv2_22 : str | None
        PV2.22 (opt) - Visit Protection Indicator (ID)

    pv2_23 : list[XON] | None
        PV2.23 (opt, rep) - Clinic Organization Name (XON)

    pv2_24 : str | None
        PV2.24 (opt) - Patient Status Code (IS)

    pv2_25 : str | None
        PV2.25 (opt) - Visit Priority Code (IS)

    pv2_26 : str | None
        PV2.26 (opt) - Previous Treatment Date (DT)

    pv2_27 : str | None
        PV2.27 (opt) - Expected Discharge Disposition (IS)

    pv2_28 : str | None
        PV2.28 (opt) - Signature on File Date (DT)

    pv2_29 : str | None
        PV2.29 (opt) - First Similar Illness Date (DT)

    pv2_30 : CE | None
        PV2.30 (opt) - Patient Charge Adjustment Code (CE)

    pv2_31 : str | None
        PV2.31 (opt) - Recurring Service Code (IS)

    pv2_32 : str | None
        PV2.32 (opt) - Billing Media Code (ID)

    pv2_33 : TS | None
        PV2.33 (opt) - Expected Surgery Date and Time (TS)

    pv2_34 : str | None
        PV2.34 (opt) - Military Partnership Code (ID)

    pv2_35 : str | None
        PV2.35 (opt) - Military Non-Availability Code (ID)

    pv2_36 : str | None
        PV2.36 (opt) - Newborn Baby Indicator (ID)

    pv2_37 : str | None
        PV2.37 (opt) - Baby Detained Indicator (ID)

    pv2_38 : CE | None
        PV2.38 (opt) - Mode of Arrival Code (CE)

    pv2_39 : list[CE] | None
        PV2.39 (opt, rep) - Recreational Drug Use Code (CE)

    pv2_40 : CE | None
        PV2.40 (opt) - Admission Level of Care Code (CE)

    pv2_41 : list[CE] | None
        PV2.41 (opt, rep) - Precaution Code (CE)

    pv2_42 : CE | None
        PV2.42 (opt) - Patient Condition Code (CE)

    pv2_43 : str | None
        PV2.43 (opt) - Living Will Code (IS)

    pv2_44 : str | None
        PV2.44 (opt) - Organ Donor Code (IS)

    pv2_45 : list[CE] | None
        PV2.45 (opt, rep) - Advance Directive Code (CE)

    pv2_46 : str | None
        PV2.46 (opt) - Patient Status Effective Date (DT)

    pv2_47 : TS | None
        PV2.47 (opt) - Expected LOA Return Date/Time (TS)

    pv2_48 : TS | None
        PV2.48 (opt) - Expected Pre-admission Testing Date/Time (TS)

    pv2_49 : list[str] | None
        PV2.49 (opt, rep) - Notify Clergy Code (IS)
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
        description="Item #181",
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
        description="Item #182 | Table HL70129",
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
        description="Item #183",
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
        description="Item #184",
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
        description="Item #185",
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
        description="Item #186",
    )

    pv2_7: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_7",
            "visit_user_code",
            "PV2.7",
        ),
        serialization_alias="PV2.7",
        title="Visit User Code",
        description="Item #187 | Table HL70130",
    )

    pv2_8: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_8",
            "expected_admit_date_time",
            "PV2.8",
        ),
        serialization_alias="PV2.8",
        title="Expected Admit Date/Time",
        description="Item #188",
    )

    pv2_9: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_9",
            "expected_discharge_date_time",
            "PV2.9",
        ),
        serialization_alias="PV2.9",
        title="Expected Discharge Date/Time",
        description="Item #189",
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
        description="Item #711",
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
        description="Item #712",
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
        description="Item #713",
    )

    pv2_13: Optional[List[XCN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_13",
            "referral_source_code",
            "PV2.13",
        ),
        serialization_alias="PV2.13",
        title="Referral Source Code",
        description="Item #714",
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
        description="Item #715",
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
        description="Item #716 | Table HL70136",
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
        description="Item #717 | Table HL70213",
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
        description="Item #718",
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
        description="Item #719 | Table HL70214",
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
        description="Item #720 | Table HL70136",
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
        description="Item #721",
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
        description="Item #722 | Table HL70215",
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
        description="Item #723 | Table HL70136",
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
        description="Item #724",
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
        description="Item #725 | Table HL70216",
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
        description="Item #726 | Table HL70217",
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
        description="Item #727",
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
        description="Item #728 | Table HL70112",
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
        description="Item #729",
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
        description="Item #730",
    )

    pv2_30: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_30",
            "patient_charge_adjustment_code",
            "PV2.30",
        ),
        serialization_alias="PV2.30",
        title="Patient Charge Adjustment Code",
        description="Item #731 | Table HL70218",
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
        description="Item #732 | Table HL70219",
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
        description="Item #733 | Table HL70136",
    )

    pv2_33: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_33",
            "expected_surgery_date_and_time",
            "PV2.33",
        ),
        serialization_alias="PV2.33",
        title="Expected Surgery Date and Time",
        description="Item #734",
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
        description="Item #735 | Table HL70136",
    )

    pv2_35: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_35",
            "military_non_availability_code",
            "PV2.35",
        ),
        serialization_alias="PV2.35",
        title="Military Non-Availability Code",
        description="Item #736 | Table HL70136",
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
        description="Item #737 | Table HL70136",
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
        description="Item #738 | Table HL70136",
    )

    pv2_38: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_38",
            "mode_of_arrival_code",
            "PV2.38",
        ),
        serialization_alias="PV2.38",
        title="Mode of Arrival Code",
        description="Item #1543 | Table HL70430",
    )

    pv2_39: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_39",
            "recreational_drug_use_code",
            "PV2.39",
        ),
        serialization_alias="PV2.39",
        title="Recreational Drug Use Code",
        description="Item #1544 | Table HL70431",
    )

    pv2_40: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_40",
            "admission_level_of_care_code",
            "PV2.40",
        ),
        serialization_alias="PV2.40",
        title="Admission Level of Care Code",
        description="Item #1545 | Table HL70432",
    )

    pv2_41: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_41",
            "precaution_code",
            "PV2.41",
        ),
        serialization_alias="PV2.41",
        title="Precaution Code",
        description="Item #1546 | Table HL70433",
    )

    pv2_42: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_42",
            "patient_condition_code",
            "PV2.42",
        ),
        serialization_alias="PV2.42",
        title="Patient Condition Code",
        description="Item #1547 | Table HL70434",
    )

    pv2_43: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_43",
            "living_will_code",
            "PV2.43",
        ),
        serialization_alias="PV2.43",
        title="Living Will Code",
        description="Item #759 | Table HL70315",
    )

    pv2_44: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_44",
            "organ_donor_code",
            "PV2.44",
        ),
        serialization_alias="PV2.44",
        title="Organ Donor Code",
        description="Item #760 | Table HL70316",
    )

    pv2_45: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_45",
            "advance_directive_code",
            "PV2.45",
        ),
        serialization_alias="PV2.45",
        title="Advance Directive Code",
        description="Item #1548 | Table HL70435",
    )

    pv2_46: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_46",
            "patient_status_effective_date",
            "PV2.46",
        ),
        serialization_alias="PV2.46",
        title="Patient Status Effective Date",
        description="Item #1549",
    )

    pv2_47: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_47",
            "expected_loa_return_date_time",
            "PV2.47",
        ),
        serialization_alias="PV2.47",
        title="Expected LOA Return Date/Time",
        description="Item #1550",
    )

    pv2_48: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_48",
            "expected_pre_admission_testing_date_time",
            "PV2.48",
        ),
        serialization_alias="PV2.48",
        title="Expected Pre-admission Testing Date/Time",
        description="Item #1841",
    )

    pv2_49: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_49",
            "notify_clergy_code",
            "PV2.49",
        ),
        serialization_alias="PV2.49",
        title="Notify Clergy Code",
        description="Item #1842 | Table HL70534",
    )

    @field_validator("pv2_10", "pv2_11", "pv2_20", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    @field_validator("pv2_14", "pv2_17", "pv2_26", "pv2_28", "pv2_29", "pv2_46", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2})?)?)?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    model_config = {"populate_by_name": True}
