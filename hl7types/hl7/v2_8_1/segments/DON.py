"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: DON
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CNE import CNE
from ..datatypes.EI import EI
from ..datatypes.XCN import XCN
from ..datatypes.XON import XON
from ..datatypes.XPN import XPN


class DON(HL7Model):
    """Donation (S4.17.1).

    Attributes
    ----------
    don_1 : EI | None
        DON.1 - Donation Identification Number - DIN (EI) C S4.17.1.1

    don_2 : CNE | None
        DON.2 - Donation Type (CNE) C S4.17.1.2

    don_3 : str
        DON.3 - Phlebotomy Start Date/Time (DTM) R S4.17.1.3

    don_4 : str
        DON.4 - Phlebotomy End Date/Time (DTM) R S4.17.1.4

    don_5 : str
        DON.5 - Donation Duration (NM) R S4.17.1.5

    don_6 : CNE
        DON.6 - Donation Duration Units (CNE) R S4.17.1.6 | 0932 - Donation Duration Units

    don_7 : list[CNE]
        DON.7 - Intended Procedure Type (CNE) R rep S4.17.1.7 | 0933 - Intended Procedure Type

    don_8 : list[CNE]
        DON.8 - Actual Procedure Type (CNE) R rep S4.17.1.8 | 0933 - Intended Procedure Type

    don_9 : str
        DON.9 - Donor Eligibility Flag (ID) R S4.17.1.9 | 0136 - Yes/no Indicator

    don_10 : list[CNE]
        DON.10 - Donor Eligibility Procedure Type (CNE) R rep S4.17.1.10 | 0933 - Intended Procedure Type

    don_11 : str
        DON.11 - Donor Eligibility Date (DTM) R S4.17.1.11

    don_12 : CNE
        DON.12 - Process Interruption (CNE) R S4.17.1.12 | 0923 - Process Interruption

    don_13 : CNE
        DON.13 - Process Interruption Reason (CNE) R S4.17.1.13 | 0935 - Process Interruption Reason

    don_14 : list[CNE]
        DON.14 - Phlebotomy Issue (CNE) R rep S4.17.1.14 | 0925 - Phlebotomy Issue

    don_15 : str
        DON.15 - Intended Recipient Blood Relative (ID) R S4.17.1.15 | 0136 - Yes/no Indicator

    don_16 : XPN
        DON.16 - Intended Recipient Name (XPN) R S4.17.1.16

    don_17 : str
        DON.17 - Intended Recipient DOB (DTM) R S4.17.1.17

    don_18 : XON
        DON.18 - Intended Recipient Facility (XON) R S4.17.1.18

    don_19 : str
        DON.19 - Intended Recipient Procedure Date (DTM) R S4.17.1.19

    don_20 : XPN
        DON.20 - Intended Recipient Ordering Provider (XPN) R S4.17.1.20

    don_21 : CNE
        DON.21 - Phlebotomy Status (CNE) R S4.17.1.21 | 0926 - Phlebotomy Status

    don_22 : CNE
        DON.22 - Arm Stick (CNE) R S4.17.1.22 | 0927 - Arm Stick

    don_23 : XPN
        DON.23 - Bleed Start Phlebotomist (XPN) R S4.17.1.23

    don_24 : XPN
        DON.24 - Bleed End Phlebotomist (XPN) R S4.17.1.24

    don_25 : str
        DON.25 - Aphaeresis Type Machine (ST) R S4.17.1.25

    don_26 : str
        DON.26 - Aphaeresis Machine Serial Number (ST) R S4.17.1.26

    don_27 : str
        DON.27 - Donor Reaction (ID) R S4.17.1.27 | 0136 - Yes/no Indicator

    don_28 : XPN
        DON.28 - Final Review Staff ID (XPN) R S4.17.1.28

    don_29 : str
        DON.29 - Final Review Date/Time (DTM) R S4.17.1.29

    don_30 : str
        DON.30 - Number of Tubes Collected (NM) R S4.17.1.30

    don_31 : list[EI]
        DON.31 - Donation Sample Identifier (EI) R rep S4.17.1.31

    don_32 : XCN
        DON.32 - Donation Accept Staff (XCN) R S4.17.1.32

    don_33 : list[XCN]
        DON.33 - Donation Material Review Staff (XCN) R rep S4.17.1.33
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
        description="C | Item #03340",
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
        description="C | Item #03341",
    )

    don_3: str = Field(
        validation_alias=AliasChoices(
            "don_3",
            "phlebotomy_start_date_time",
            "DON.3",
        ),
        serialization_alias="DON.3",
        title="Phlebotomy Start Date/Time",
        description="R | Item #03342",
    )

    don_4: str = Field(
        validation_alias=AliasChoices(
            "don_4",
            "phlebotomy_end_date_time",
            "DON.4",
        ),
        serialization_alias="DON.4",
        title="Phlebotomy End Date/Time",
        description="R | Item #03343",
    )

    don_5: str = Field(
        validation_alias=AliasChoices(
            "don_5",
            "donation_duration",
            "DON.5",
        ),
        serialization_alias="DON.5",
        title="Donation Duration",
        description="R | Item #03344",
    )

    don_6: CNE = Field(
        validation_alias=AliasChoices(
            "don_6",
            "donation_duration_units",
            "DON.6",
        ),
        serialization_alias="DON.6",
        title="Donation Duration Units",
        description="R | Item #03345 | Table 0932 - Donation Duration Units",
    )

    don_7: List[CNE] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "don_7",
            "intended_procedure_type",
            "DON.7",
        ),
        serialization_alias="DON.7",
        title="Intended Procedure Type",
        description="R | Item #03346 | Table 0933 - Intended Procedure Type",
    )

    don_8: List[CNE] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "don_8",
            "actual_procedure_type",
            "DON.8",
        ),
        serialization_alias="DON.8",
        title="Actual Procedure Type",
        description="R | Item #03347 | Table 0933 - Intended Procedure Type",
    )

    don_9: str = Field(
        validation_alias=AliasChoices(
            "don_9",
            "donor_eligibility_flag",
            "DON.9",
        ),
        serialization_alias="DON.9",
        title="Donor Eligibility Flag",
        description="R | Item #03348 | Table 0136 - Yes/no Indicator",
    )

    don_10: List[CNE] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "don_10",
            "donor_eligibility_procedure_type",
            "DON.10",
        ),
        serialization_alias="DON.10",
        title="Donor Eligibility Procedure Type",
        description="R | Item #03349 | Table 0933 - Intended Procedure Type",
    )

    don_11: str = Field(
        validation_alias=AliasChoices(
            "don_11",
            "donor_eligibility_date",
            "DON.11",
        ),
        serialization_alias="DON.11",
        title="Donor Eligibility Date",
        description="R | Item #03350",
    )

    don_12: CNE = Field(
        validation_alias=AliasChoices(
            "don_12",
            "process_interruption",
            "DON.12",
        ),
        serialization_alias="DON.12",
        title="Process Interruption",
        description="R | Item #03351 | Table 0923 - Process Interruption",
    )

    don_13: CNE = Field(
        validation_alias=AliasChoices(
            "don_13",
            "process_interruption_reason",
            "DON.13",
        ),
        serialization_alias="DON.13",
        title="Process Interruption Reason",
        description=(
            "R | Item #03352 | Table 0935 - Process Interruption Reason"
        ),
    )

    don_14: List[CNE] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "don_14",
            "phlebotomy_issue",
            "DON.14",
        ),
        serialization_alias="DON.14",
        title="Phlebotomy Issue",
        description="R | Item #03353 | Table 0925 - Phlebotomy Issue",
    )

    don_15: str = Field(
        validation_alias=AliasChoices(
            "don_15",
            "intended_recipient_blood_relative",
            "DON.15",
        ),
        serialization_alias="DON.15",
        title="Intended Recipient Blood Relative",
        description="R | Item #03354 | Table 0136 - Yes/no Indicator",
    )

    don_16: XPN = Field(
        validation_alias=AliasChoices(
            "don_16",
            "intended_recipient_name",
            "DON.16",
        ),
        serialization_alias="DON.16",
        title="Intended Recipient Name",
        description="R | Item #03355",
    )

    don_17: str = Field(
        validation_alias=AliasChoices(
            "don_17",
            "intended_recipient_dob",
            "DON.17",
        ),
        serialization_alias="DON.17",
        title="Intended Recipient DOB",
        description="R | Item #03356",
    )

    don_18: XON = Field(
        validation_alias=AliasChoices(
            "don_18",
            "intended_recipient_facility",
            "DON.18",
        ),
        serialization_alias="DON.18",
        title="Intended Recipient Facility",
        description="R | Item #03357",
    )

    don_19: str = Field(
        validation_alias=AliasChoices(
            "don_19",
            "intended_recipient_procedure_date",
            "DON.19",
        ),
        serialization_alias="DON.19",
        title="Intended Recipient Procedure Date",
        description="R | Item #03358",
    )

    don_20: XPN = Field(
        validation_alias=AliasChoices(
            "don_20",
            "intended_recipient_ordering_provider",
            "DON.20",
        ),
        serialization_alias="DON.20",
        title="Intended Recipient Ordering Provider",
        description="R | Item #03359",
    )

    don_21: CNE = Field(
        validation_alias=AliasChoices(
            "don_21",
            "phlebotomy_status",
            "DON.21",
        ),
        serialization_alias="DON.21",
        title="Phlebotomy Status",
        description="R | Item #03360 | Table 0926 - Phlebotomy Status",
    )

    don_22: CNE = Field(
        validation_alias=AliasChoices(
            "don_22",
            "arm_stick",
            "DON.22",
        ),
        serialization_alias="DON.22",
        title="Arm Stick",
        description="R | Item #03361 | Table 0927 - Arm Stick",
    )

    don_23: XPN = Field(
        validation_alias=AliasChoices(
            "don_23",
            "bleed_start_phlebotomist",
            "DON.23",
        ),
        serialization_alias="DON.23",
        title="Bleed Start Phlebotomist",
        description="R | Item #03362",
    )

    don_24: XPN = Field(
        validation_alias=AliasChoices(
            "don_24",
            "bleed_end_phlebotomist",
            "DON.24",
        ),
        serialization_alias="DON.24",
        title="Bleed End Phlebotomist",
        description="R | Item #03363",
    )

    don_25: str = Field(
        validation_alias=AliasChoices(
            "don_25",
            "aphaeresis_type_machine",
            "DON.25",
        ),
        serialization_alias="DON.25",
        title="Aphaeresis Type Machine",
        description="R | Item #03364",
    )

    don_26: str = Field(
        validation_alias=AliasChoices(
            "don_26",
            "aphaeresis_machine_serial_number",
            "DON.26",
        ),
        serialization_alias="DON.26",
        title="Aphaeresis Machine Serial Number",
        description="R | Item #03365",
    )

    don_27: str = Field(
        validation_alias=AliasChoices(
            "don_27",
            "donor_reaction",
            "DON.27",
        ),
        serialization_alias="DON.27",
        title="Donor Reaction",
        description="R | Item #03366 | Table 0136 - Yes/no Indicator",
    )

    don_28: XPN = Field(
        validation_alias=AliasChoices(
            "don_28",
            "final_review_staff_id",
            "DON.28",
        ),
        serialization_alias="DON.28",
        title="Final Review Staff ID",
        description="R | Item #03367",
    )

    don_29: str = Field(
        validation_alias=AliasChoices(
            "don_29",
            "final_review_date_time",
            "DON.29",
        ),
        serialization_alias="DON.29",
        title="Final Review Date/Time",
        description="R | Item #03368",
    )

    don_30: str = Field(
        validation_alias=AliasChoices(
            "don_30",
            "number_of_tubes_collected",
            "DON.30",
        ),
        serialization_alias="DON.30",
        title="Number of Tubes Collected",
        description="R | Item #03369",
    )

    don_31: List[EI] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "don_31",
            "donation_sample_identifier",
            "DON.31",
        ),
        serialization_alias="DON.31",
        title="Donation Sample Identifier",
        description="R | Item #03370",
    )

    don_32: XCN = Field(
        validation_alias=AliasChoices(
            "don_32",
            "donation_accept_staff",
            "DON.32",
        ),
        serialization_alias="DON.32",
        title="Donation Accept Staff",
        description="R | Item #03371",
    )

    don_33: List[XCN] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "don_33",
            "donation_material_review_staff",
            "DON.33",
        ),
        serialization_alias="DON.33",
        title="Donation Material Review Staff",
        description="R | Item #03372",
    )

    @field_validator("don_3", "don_4", "don_11", "don_17", "don_19", "don_29", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        import re
        if re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    @field_validator("don_5", "don_30", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
