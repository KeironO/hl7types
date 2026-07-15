"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: RXE
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CQ import CQ
from ..datatypes.CWE import CWE
from ..datatypes.PL import PL
from ..datatypes.XAD import XAD
from ..datatypes.XCN import XCN
from ..datatypes.XTN import XTN


class RXE(HL7Model):
    """Pharmacy/Treatment Encoded Order (S4.A.4).

    Attributes
    ----------
    rxe_2 : CWE
        RXE.2 - Give Code (CWE) R S4.A.4.2 | 0292 - Vaccines administered

    rxe_3 : str
        RXE.3 - Give Amount - Minimum (NM) R S4.A.4.3

    rxe_4 : str | None
        RXE.4 - Give Amount - Maximum (NM) O S4.A.4.4

    rxe_5 : CWE
        RXE.5 - Give Units (CWE) R S4.A.4.5 | 9999 - no table for CE

    rxe_6 : CWE | None
        RXE.6 - Give Dosage Form (CWE) O S4.A.4.6 | 9999 - no table for CE

    rxe_7 : list[CWE] | None
        RXE.7 - Provider's Administration Instructions (CWE) O rep S4.A.1.7 | 9999 - no table for CE

    rxe_9 : str | None
        RXE.9 - Substitution Status (ID) O S4.A.4.9 | 0167 - Substitution Status

    rxe_10 : str | None
        RXE.10 - Dispense Amount (NM) C S4.A.4.10

    rxe_11 : CWE | None
        RXE.11 - Dispense Units (CWE) C S4.A.4.11 | 9999 - no table for CE

    rxe_12 : str | None
        RXE.12 - Number Of Refills (NM) O S4.A.1.13

    rxe_13 : list[XCN] | None
        RXE.13 - Ordering Provider's DEA Number (XCN) O rep S4.A.1.14

    rxe_14 : list[XCN] | None
        RXE.14 - Pharmacist/Treatment Supplier's Verifier ID (XCN) O rep S4.A.1.15

    rxe_15 : str | None
        RXE.15 - Prescription Number (ST) C S4.A.4.15

    rxe_16 : str | None
        RXE.16 - Number of Refills Remaining (NM) C S4.A.4.16

    rxe_17 : str | None
        RXE.17 - Number of Refills/Doses Dispensed (NM) C S4.A.4.17

    rxe_18 : str | None
        RXE.18 - D/T of Most Recent Refill or Dose Dispensed (DTM) C S4.A.4.18

    rxe_19 : CQ | None
        RXE.19 - Total Daily Dose (CQ) C S4.A.1.23

    rxe_20 : str | None
        RXE.20 - Needs Human Review (ID) O S4.A.1.16 | 0136 - Yes/no Indicator

    rxe_21 : list[CWE] | None
        RXE.21 - Special Dispensing Instructions (CWE) O rep S4.A.4.21 | 9999 - no table for CE

    rxe_22 : str | None
        RXE.22 - Give Per (Time Unit) (ST) C S4.A.4.22

    rxe_23 : str | None
        RXE.23 - Give Rate Amount (ST) O S4.A.4.23

    rxe_24 : CWE | None
        RXE.24 - Give Rate Units (CWE) O S4.A.4.24 | 9999 - no table for CE

    rxe_25 : str | None
        RXE.25 - Give Strength (NM) O S4.A.4.25

    rxe_26 : CWE | None
        RXE.26 - Give Strength Units (CWE) O S4.A.4.26 | 9999 - no table for CE

    rxe_27 : list[CWE] | None
        RXE.27 - Give Indication (CWE) O rep S4.A.4.27 | 9999 - no table for CE

    rxe_28 : str | None
        RXE.28 - Dispense Package Size (NM) O S4.A.4.28

    rxe_29 : CWE | None
        RXE.29 - Dispense Package Size Unit (CWE) O S4.A.4.29 | 9999 - no table for CE

    rxe_30 : str | None
        RXE.30 - Dispense Package Method (ID) O S4.A.4.30 | 0321 - Dispense Method

    rxe_31 : list[CWE] | None
        RXE.31 - Supplementary Code (CWE) O rep S4.A.1.24 | 9999 - no table for CE

    rxe_32 : str | None
        RXE.32 - Original Order Date/Time (DTM) O S4.A.4.32

    rxe_33 : str | None
        RXE.33 - Give Drug Strength Volume (NM) O S4.A.4.33

    rxe_34 : CWE | None
        RXE.34 - Give Drug Strength Volume Units (CWE) O S4.A.4.34 | 9999 - no table for CE

    rxe_35 : CWE | None
        RXE.35 - Controlled Substance Schedule (CWE) O S4.A.4.35 | 0477 - Controlled Substance Schedule*

    rxe_36 : str | None
        RXE.36 - Formulary Status (ID) O S4.A.4.36 | 0478 - Formulary Status

    rxe_37 : list[CWE] | None
        RXE.37 - Pharmaceutical Substance Alternative (CWE) O rep S4.A.4.37 | 9999 - no table for CE

    rxe_38 : CWE | None
        RXE.38 - Pharmacy of Most Recent Fill (CWE) O S4.A.4.38 | 9999 - no table for CE

    rxe_39 : str | None
        RXE.39 - Initial Dispense Amount (NM) O S4.A.4.39

    rxe_40 : CWE | None
        RXE.40 - Dispensing Pharmacy (CWE) O S4.A.1.32 | 9999 - no table for CE

    rxe_41 : XAD | None
        RXE.41 - Dispensing Pharmacy Address (XAD) O S4.A.1.33

    rxe_42 : PL | None
        RXE.42 - Deliver-to Patient Location (PL) O S4.A.1.34

    rxe_43 : XAD | None
        RXE.43 - Deliver-to Address (XAD) O S4.A.1.35

    rxe_44 : str | None
        RXE.44 - Pharmacy Order Type (ID) O S4.A.4.44 | 0480 - Pharmacy Order Types

    rxe_45 : list[XTN] | None
        RXE.45 - Pharmacy Phone Number (XTN) O rep S4.A.4.45
    """

    rxe_2: CWE = Field(
        validation_alias=AliasChoices(
            "rxe_2",
            "give_code",
            "RXE.2",
        ),
        serialization_alias="RXE.2",
        title="Give Code",
        description="R | Item #00317 | Table 0292 - Vaccines administered",
    )

    rxe_3: str = Field(
        validation_alias=AliasChoices(
            "rxe_3",
            "give_amount_minimum",
            "RXE.3",
        ),
        serialization_alias="RXE.3",
        title="Give Amount - Minimum",
        description="R | Item #00318",
    )

    rxe_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_4",
            "give_amount_maximum",
            "RXE.4",
        ),
        serialization_alias="RXE.4",
        title="Give Amount - Maximum",
        description="O | Item #00319",
    )

    rxe_5: CWE = Field(
        validation_alias=AliasChoices(
            "rxe_5",
            "give_units",
            "RXE.5",
        ),
        serialization_alias="RXE.5",
        title="Give Units",
        description="R | Item #00320 | Table 9999 - no table for CE",
    )

    rxe_6: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_6",
            "give_dosage_form",
            "RXE.6",
        ),
        serialization_alias="RXE.6",
        title="Give Dosage Form",
        description="O | Item #00321 | Table 9999 - no table for CE",
    )

    rxe_7: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_7",
            "provider_s_administration_instructions",
            "RXE.7",
        ),
        serialization_alias="RXE.7",
        title="Provider's Administration Instructions",
        description="O | Item #00298 | Table 9999 - no table for CE",
    )

    rxe_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_9",
            "substitution_status",
            "RXE.9",
        ),
        serialization_alias="RXE.9",
        title="Substitution Status",
        description=(
            "O | Item #00322 | Table 0167 - Substitution Status | LEN:1"
        ),
    )

    rxe_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_10",
            "dispense_amount",
            "RXE.10",
        ),
        serialization_alias="RXE.10",
        title="Dispense Amount",
        description="C | Item #00323",
    )

    rxe_11: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_11",
            "dispense_units",
            "RXE.11",
        ),
        serialization_alias="RXE.11",
        title="Dispense Units",
        description="C | Item #00324 | Table 9999 - no table for CE",
    )

    rxe_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_12",
            "number_of_refills",
            "RXE.12",
        ),
        serialization_alias="RXE.12",
        title="Number Of Refills",
        description="O | Item #00304",
    )

    rxe_13: Optional[List[XCN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_13",
            "ordering_provider_s_dea_number",
            "RXE.13",
        ),
        serialization_alias="RXE.13",
        title="Ordering Provider's DEA Number",
        description="O | Item #00305",
    )

    rxe_14: Optional[List[XCN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_14",
            "pharmacist_treatment_supplier_s_verifier_id",
            "RXE.14",
        ),
        serialization_alias="RXE.14",
        title="Pharmacist/Treatment Supplier's Verifier ID",
        description="O | Item #00306",
    )

    rxe_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_15",
            "prescription_number",
            "RXE.15",
        ),
        serialization_alias="RXE.15",
        title="Prescription Number",
        description="C | Item #00325",
    )

    rxe_16: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_16",
            "number_of_refills_remaining",
            "RXE.16",
        ),
        serialization_alias="RXE.16",
        title="Number of Refills Remaining",
        description="C | Item #00326",
    )

    rxe_17: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_17",
            "number_of_refills_doses_dispensed",
            "RXE.17",
        ),
        serialization_alias="RXE.17",
        title="Number of Refills/Doses Dispensed",
        description="C | Item #00327",
    )

    rxe_18: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_18",
            "d_t_of_most_recent_refill_or_dose_dispensed",
            "RXE.18",
        ),
        serialization_alias="RXE.18",
        title="D/T of Most Recent Refill or Dose Dispensed",
        description="C | Item #00328",
    )

    rxe_19: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_19",
            "total_daily_dose",
            "RXE.19",
        ),
        serialization_alias="RXE.19",
        title="Total Daily Dose",
        description="C | Item #00329",
    )

    rxe_20: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_20",
            "needs_human_review",
            "RXE.20",
        ),
        serialization_alias="RXE.20",
        title="Needs Human Review",
        description="O | Item #00307 | Table 0136 - Yes/no Indicator | LEN:1",
    )

    rxe_21: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_21",
            "special_dispensing_instructions",
            "RXE.21",
        ),
        serialization_alias="RXE.21",
        title="Special Dispensing Instructions",
        description="O | Item #00330 | Table 9999 - no table for CE",
    )

    rxe_22: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_22",
            "give_per_time_unit",
            "RXE.22",
        ),
        serialization_alias="RXE.22",
        title="Give Per (Time Unit)",
        description="C | Item #00331",
    )

    rxe_23: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_23",
            "give_rate_amount",
            "RXE.23",
        ),
        serialization_alias="RXE.23",
        title="Give Rate Amount",
        description="O | Item #00332",
    )

    rxe_24: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_24",
            "give_rate_units",
            "RXE.24",
        ),
        serialization_alias="RXE.24",
        title="Give Rate Units",
        description="O | Item #00333 | Table 9999 - no table for CE",
    )

    rxe_25: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_25",
            "give_strength",
            "RXE.25",
        ),
        serialization_alias="RXE.25",
        title="Give Strength",
        description="O | Item #01126",
    )

    rxe_26: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_26",
            "give_strength_units",
            "RXE.26",
        ),
        serialization_alias="RXE.26",
        title="Give Strength Units",
        description="O | Item #01127 | Table 9999 - no table for CE",
    )

    rxe_27: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_27",
            "give_indication",
            "RXE.27",
        ),
        serialization_alias="RXE.27",
        title="Give Indication",
        description="O | Item #01128 | Table 9999 - no table for CE",
    )

    rxe_28: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_28",
            "dispense_package_size",
            "RXE.28",
        ),
        serialization_alias="RXE.28",
        title="Dispense Package Size",
        description="O | Item #01220",
    )

    rxe_29: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_29",
            "dispense_package_size_unit",
            "RXE.29",
        ),
        serialization_alias="RXE.29",
        title="Dispense Package Size Unit",
        description="O | Item #01221 | Table 9999 - no table for CE",
    )

    rxe_30: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_30",
            "dispense_package_method",
            "RXE.30",
        ),
        serialization_alias="RXE.30",
        title="Dispense Package Method",
        description="O | Item #01222 | Table 0321 - Dispense Method | LEN:2",
    )

    rxe_31: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_31",
            "supplementary_code",
            "RXE.31",
        ),
        serialization_alias="RXE.31",
        title="Supplementary Code",
        description="O | Item #01476 | Table 9999 - no table for CE",
    )

    rxe_32: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_32",
            "original_order_date_time",
            "RXE.32",
        ),
        serialization_alias="RXE.32",
        title="Original Order Date/Time",
        description="O | Item #01673",
    )

    rxe_33: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_33",
            "give_drug_strength_volume",
            "RXE.33",
        ),
        serialization_alias="RXE.33",
        title="Give Drug Strength Volume",
        description="O | Item #01674",
    )

    rxe_34: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_34",
            "give_drug_strength_volume_units",
            "RXE.34",
        ),
        serialization_alias="RXE.34",
        title="Give Drug Strength Volume Units",
        description="O | Item #01675 | Table 9999 - no table for CE",
    )

    rxe_35: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_35",
            "controlled_substance_schedule",
            "RXE.35",
        ),
        serialization_alias="RXE.35",
        title="Controlled Substance Schedule",
        description=(
            "O | Item #01676 | Table 0477 - Controlled Substance Schedule*"
        ),
    )

    rxe_36: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_36",
            "formulary_status",
            "RXE.36",
        ),
        serialization_alias="RXE.36",
        title="Formulary Status",
        description="O | Item #01677 | Table 0478 - Formulary Status | LEN:1",
    )

    rxe_37: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_37",
            "pharmaceutical_substance_alternative",
            "RXE.37",
        ),
        serialization_alias="RXE.37",
        title="Pharmaceutical Substance Alternative",
        description="O | Item #01678 | Table 9999 - no table for CE",
    )

    rxe_38: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_38",
            "pharmacy_of_most_recent_fill",
            "RXE.38",
        ),
        serialization_alias="RXE.38",
        title="Pharmacy of Most Recent Fill",
        description="O | Item #01679 | Table 9999 - no table for CE",
    )

    rxe_39: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_39",
            "initial_dispense_amount",
            "RXE.39",
        ),
        serialization_alias="RXE.39",
        title="Initial Dispense Amount",
        description="O | Item #01680",
    )

    rxe_40: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_40",
            "dispensing_pharmacy",
            "RXE.40",
        ),
        serialization_alias="RXE.40",
        title="Dispensing Pharmacy",
        description="O | Item #01681 | Table 9999 - no table for CE",
    )

    rxe_41: Optional[XAD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_41",
            "dispensing_pharmacy_address",
            "RXE.41",
        ),
        serialization_alias="RXE.41",
        title="Dispensing Pharmacy Address",
        description="O | Item #01682",
    )

    rxe_42: Optional[PL] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_42",
            "deliver_to_patient_location",
            "RXE.42",
        ),
        serialization_alias="RXE.42",
        title="Deliver-to Patient Location",
        description="O | Item #01683",
    )

    rxe_43: Optional[XAD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_43",
            "deliver_to_address",
            "RXE.43",
        ),
        serialization_alias="RXE.43",
        title="Deliver-to Address",
        description="O | Item #01684",
    )

    rxe_44: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_44",
            "pharmacy_order_type",
            "RXE.44",
        ),
        serialization_alias="RXE.44",
        title="Pharmacy Order Type",
        description=(
            "O | Item #01685 | Table 0480 - Pharmacy Order Types | LEN:1"
        ),
    )

    rxe_45: Optional[List[XTN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_45",
            "pharmacy_phone_number",
            "RXE.45",
        ),
        serialization_alias="RXE.45",
        title="Pharmacy Phone Number",
        description="O | Item #02310",
    )

    @field_validator("rxe_3", "rxe_4", "rxe_10", "rxe_12", "rxe_16", "rxe_17", "rxe_25", "rxe_28", "rxe_33", "rxe_39", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    @field_validator("rxe_18", "rxe_32", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        import re
        if re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = {"populate_by_name": True}
