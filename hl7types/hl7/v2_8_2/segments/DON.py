"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: DON
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator

from ..datatypes.CNE import CNE
from ..datatypes.EI import EI
from ..datatypes.XCN import XCN
from ..datatypes.XON import XON
from ..datatypes.XPN import XPN


class DON(HL7Model):
    """HL7 v2 DON segment.

    Attributes
    ----------
    don_1 : EI | None
        DON.1 (opt) - Donation Identification Number - DIN (EI)

    don_2 : CNE | None
        DON.2 (opt) - Donation Type (CNE)

    don_3 : str
        DON.3 (req) - Phlebotomy Start Date/Time (DTM)

    don_4 : str
        DON.4 (req) - Phlebotomy End Date/Time (DTM)

    don_5 : str
        DON.5 (req) - Donation Duration (NM)

    don_6 : CNE
        DON.6 (req) - Donation Duration Units (CNE)

    don_7 : list[CNE]
        DON.7 (req, rep) - Intended Procedure Type (CNE)

    don_8 : list[CNE]
        DON.8 (req, rep) - Actual Procedure Type (CNE)

    don_9 : str
        DON.9 (req) - Donor Eligibility Flag (ID)

    don_10 : list[CNE]
        DON.10 (req, rep) - Donor Eligibility Procedure Type (CNE)

    don_11 : str
        DON.11 (req) - Donor Eligibility Date (DTM)

    don_12 : CNE
        DON.12 (req) - Process Interruption (CNE)

    don_13 : CNE
        DON.13 (req) - Process Interruption Reason (CNE)

    don_14 : list[CNE]
        DON.14 (req, rep) - Phlebotomy Issue (CNE)

    don_15 : str
        DON.15 (req) - Intended Recipient Blood Relative (ID)

    don_16 : XPN
        DON.16 (req) - Intended Recipient Name (XPN)

    don_17 : str
        DON.17 (req) - Intended Recipient DOB (DTM)

    don_18 : XON
        DON.18 (req) - Intended Recipient Facility (XON)

    don_19 : str
        DON.19 (req) - Intended Recipient Procedure Date (DTM)

    don_20 : XPN
        DON.20 (req) - Intended Recipient Ordering Provider (XPN)

    don_21 : CNE
        DON.21 (req) - Phlebotomy Status (CNE)

    don_22 : CNE
        DON.22 (req) - Arm Stick (CNE)

    don_23 : XPN
        DON.23 (req) - Bleed Start Phlebotomist (XPN)

    don_24 : XPN
        DON.24 (req) - Bleed End Phlebotomist (XPN)

    don_25 : str
        DON.25 (req) - Aphaeresis Type Machine (ST)

    don_26 : str
        DON.26 (req) - Aphaeresis Machine Serial Number (ST)

    don_27 : str
        DON.27 (req) - Donor Reaction (ID)

    don_28 : XPN
        DON.28 (req) - Final Review Staff ID (XPN)

    don_29 : str
        DON.29 (req) - Final Review Date/Time (DTM)

    don_30 : str
        DON.30 (req) - Number of Tubes Collected (NM)

    don_31 : list[EI] | None
        DON.31 (req, rep) - Donation Sample Identifier (EI) [optional: EI has no required components]

    don_32 : XCN
        DON.32 (req) - Donation Accept Staff (XCN)

    don_33 : list[XCN] | None
        DON.33 (req, rep) - Donation Material Review Staff (XCN) [optional: XCN has no required components]
    """

    don_1: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "don_1",
            "donation_identification_number_din",
            "DON.1",
        ),
        serialization_alias="DON.1",
        title="Donation Identification Number - DIN",
        description="Item #3340",
    )

    don_2: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "don_2",
            "donation_type",
            "DON.2",
        ),
        serialization_alias="DON.2",
        title="Donation Type",
        description="Item #3341",
    )

    don_3: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "don_3",
            "phlebotomy_start_date_time",
            "DON.3",
        ),
        serialization_alias="DON.3",
        title="Phlebotomy Start Date/Time",
        description="Item #3342",
    )

    don_4: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "don_4",
            "phlebotomy_end_date_time",
            "DON.4",
        ),
        serialization_alias="DON.4",
        title="Phlebotomy End Date/Time",
        description="Item #3343",
    )

    don_5: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "don_5",
            "donation_duration",
            "DON.5",
        ),
        serialization_alias="DON.5",
        title="Donation Duration",
        description="Item #3344",
    )

    don_6: CNE = Field(
        default=...,
        validation_alias=AliasChoices(
            "don_6",
            "donation_duration_units",
            "DON.6",
        ),
        serialization_alias="DON.6",
        title="Donation Duration Units",
        description="Item #3345 | Table HL70932",
    )

    don_7: List[CNE] = Field(
        default=...,
        validation_alias=AliasChoices(
            "don_7",
            "intended_procedure_type",
            "DON.7",
        ),
        serialization_alias="DON.7",
        title="Intended Procedure Type",
        description="Item #3346 | Table HL70933",
    )

    don_8: List[CNE] = Field(
        default=...,
        validation_alias=AliasChoices(
            "don_8",
            "actual_procedure_type",
            "DON.8",
        ),
        serialization_alias="DON.8",
        title="Actual Procedure Type",
        description="Item #3347 | Table HL70933",
    )

    don_9: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "don_9",
            "donor_eligibility_flag",
            "DON.9",
        ),
        serialization_alias="DON.9",
        title="Donor Eligibility Flag",
        description="Item #3348 | Table HL70136",
    )

    don_10: List[CNE] = Field(
        default=...,
        validation_alias=AliasChoices(
            "don_10",
            "donor_eligibility_procedure_type",
            "DON.10",
        ),
        serialization_alias="DON.10",
        title="Donor Eligibility Procedure Type",
        description="Item #3349 | Table HL70933",
    )

    don_11: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "don_11",
            "donor_eligibility_date",
            "DON.11",
        ),
        serialization_alias="DON.11",
        title="Donor Eligibility Date",
        description="Item #3350",
    )

    don_12: CNE = Field(
        default=...,
        validation_alias=AliasChoices(
            "don_12",
            "process_interruption",
            "DON.12",
        ),
        serialization_alias="DON.12",
        title="Process Interruption",
        description="Item #3351 | Table HL70923",
    )

    don_13: CNE = Field(
        default=...,
        validation_alias=AliasChoices(
            "don_13",
            "process_interruption_reason",
            "DON.13",
        ),
        serialization_alias="DON.13",
        title="Process Interruption Reason",
        description="Item #3352 | Table HL70935",
    )

    don_14: List[CNE] = Field(
        default=...,
        validation_alias=AliasChoices(
            "don_14",
            "phlebotomy_issue",
            "DON.14",
        ),
        serialization_alias="DON.14",
        title="Phlebotomy Issue",
        description="Item #3353 | Table HL70925",
    )

    don_15: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "don_15",
            "intended_recipient_blood_relative",
            "DON.15",
        ),
        serialization_alias="DON.15",
        title="Intended Recipient Blood Relative",
        description="Item #3354 | Table HL70136",
    )

    don_16: XPN = Field(
        default=...,
        validation_alias=AliasChoices(
            "don_16",
            "intended_recipient_name",
            "DON.16",
        ),
        serialization_alias="DON.16",
        title="Intended Recipient Name",
        description="Item #3355",
    )

    don_17: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "don_17",
            "intended_recipient_dob",
            "DON.17",
        ),
        serialization_alias="DON.17",
        title="Intended Recipient DOB",
        description="Item #3356",
    )

    don_18: XON = Field(
        default=...,
        validation_alias=AliasChoices(
            "don_18",
            "intended_recipient_facility",
            "DON.18",
        ),
        serialization_alias="DON.18",
        title="Intended Recipient Facility",
        description="Item #3357",
    )

    don_19: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "don_19",
            "intended_recipient_procedure_date",
            "DON.19",
        ),
        serialization_alias="DON.19",
        title="Intended Recipient Procedure Date",
        description="Item #3358",
    )

    don_20: XPN = Field(
        default=...,
        validation_alias=AliasChoices(
            "don_20",
            "intended_recipient_ordering_provider",
            "DON.20",
        ),
        serialization_alias="DON.20",
        title="Intended Recipient Ordering Provider",
        description="Item #3359",
    )

    don_21: CNE = Field(
        default=...,
        validation_alias=AliasChoices(
            "don_21",
            "phlebotomy_status",
            "DON.21",
        ),
        serialization_alias="DON.21",
        title="Phlebotomy Status",
        description="Item #3360 | Table HL70926",
    )

    don_22: CNE = Field(
        default=...,
        validation_alias=AliasChoices(
            "don_22",
            "arm_stick",
            "DON.22",
        ),
        serialization_alias="DON.22",
        title="Arm Stick",
        description="Item #3361 | Table HL70927",
    )

    don_23: XPN = Field(
        default=...,
        validation_alias=AliasChoices(
            "don_23",
            "bleed_start_phlebotomist",
            "DON.23",
        ),
        serialization_alias="DON.23",
        title="Bleed Start Phlebotomist",
        description="Item #3362",
    )

    don_24: XPN = Field(
        default=...,
        validation_alias=AliasChoices(
            "don_24",
            "bleed_end_phlebotomist",
            "DON.24",
        ),
        serialization_alias="DON.24",
        title="Bleed End Phlebotomist",
        description="Item #3363",
    )

    don_25: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "don_25",
            "aphaeresis_type_machine",
            "DON.25",
        ),
        serialization_alias="DON.25",
        title="Aphaeresis Type Machine",
        description="Item #3364",
    )

    don_26: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "don_26",
            "aphaeresis_machine_serial_number",
            "DON.26",
        ),
        serialization_alias="DON.26",
        title="Aphaeresis Machine Serial Number",
        description="Item #3365",
    )

    don_27: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "don_27",
            "donor_reaction",
            "DON.27",
        ),
        serialization_alias="DON.27",
        title="Donor Reaction",
        description="Item #3366 | Table HL70136",
    )

    don_28: XPN = Field(
        default=...,
        validation_alias=AliasChoices(
            "don_28",
            "final_review_staff_id",
            "DON.28",
        ),
        serialization_alias="DON.28",
        title="Final Review Staff ID",
        description="Item #3367",
    )

    don_29: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "don_29",
            "final_review_date_time",
            "DON.29",
        ),
        serialization_alias="DON.29",
        title="Final Review Date/Time",
        description="Item #3368",
    )

    don_30: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "don_30",
            "number_of_tubes_collected",
            "DON.30",
        ),
        serialization_alias="DON.30",
        title="Number of Tubes Collected",
        description="Item #3369",
    )

    don_31: Optional[List[EI]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "don_31",
            "donation_sample_identifier",
            "DON.31",
        ),
        serialization_alias="DON.31",
        title="Donation Sample Identifier",
        description="Item #3370",
    )

    don_32: XCN = Field(
        default=...,
        validation_alias=AliasChoices(
            "don_32",
            "donation_accept_staff",
            "DON.32",
        ),
        serialization_alias="DON.32",
        title="Donation Accept Staff",
        description="Item #3371",
    )

    don_33: Optional[List[XCN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "don_33",
            "donation_material_review_staff",
            "DON.33",
        ),
        serialization_alias="DON.33",
        title="Donation Material Review Staff",
        description="Item #3372",
    )

    @field_validator("don_3", "don_4", "don_11", "don_17", "don_19", "don_29", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 datetime")
        return v

    @field_validator("don_5", "don_30", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
