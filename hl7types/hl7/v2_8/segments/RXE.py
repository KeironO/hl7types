"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: RXE
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator

from ..datatypes.CQ import CQ
from ..datatypes.CWE import CWE
from ..datatypes.PL import PL
from ..datatypes.XAD import XAD
from ..datatypes.XCN import XCN
from ..datatypes.XTN import XTN


class RXE(HL7Model):
    """HL7 v2 RXE segment.

    Attributes
    ----------
    rxe_2 : CWE
        RXE.2 (req) - Give Code (CWE)

    rxe_3 : str
        RXE.3 (req) - Give Amount - Minimum (NM)

    rxe_4 : str | None
        RXE.4 (opt) - Give Amount - Maximum (NM)

    rxe_5 : CWE
        RXE.5 (req) - Give Units (CWE)

    rxe_6 : CWE | None
        RXE.6 (opt) - Give Dosage Form (CWE)

    rxe_7 : list[CWE] | None
        RXE.7 (opt, rep) - Provider's Administration Instructions (CWE)

    rxe_9 : str | None
        RXE.9 (opt) - Substitution Status (ID)

    rxe_10 : str | None
        RXE.10 (opt) - Dispense Amount (NM)

    rxe_11 : CWE | None
        RXE.11 (opt) - Dispense Units (CWE)

    rxe_12 : str | None
        RXE.12 (opt) - Number Of Refills (NM)

    rxe_13 : list[XCN] | None
        RXE.13 (opt, rep) - Ordering Provider's DEA Number (XCN)

    rxe_14 : list[XCN] | None
        RXE.14 (opt, rep) - Pharmacist/Treatment Supplier's Verifier ID (XCN)

    rxe_15 : str | None
        RXE.15 (opt) - Prescription Number (ST)

    rxe_16 : str | None
        RXE.16 (opt) - Number of Refills Remaining (NM)

    rxe_17 : str | None
        RXE.17 (opt) - Number of Refills/Doses Dispensed (NM)

    rxe_18 : str | None
        RXE.18 (opt) - D/T of Most Recent Refill or Dose Dispensed (DTM)

    rxe_19 : CQ | None
        RXE.19 (opt) - Total Daily Dose (CQ)

    rxe_20 : str | None
        RXE.20 (opt) - Needs Human Review (ID)

    rxe_21 : list[CWE] | None
        RXE.21 (opt, rep) - Special Dispensing Instructions (CWE)

    rxe_22 : str | None
        RXE.22 (opt) - Give Per (Time Unit) (ST)

    rxe_23 : str | None
        RXE.23 (opt) - Give Rate Amount (ST)

    rxe_24 : CWE | None
        RXE.24 (opt) - Give Rate Units (CWE)

    rxe_25 : str | None
        RXE.25 (opt) - Give Strength (NM)

    rxe_26 : CWE | None
        RXE.26 (opt) - Give Strength Units (CWE)

    rxe_27 : list[CWE] | None
        RXE.27 (opt, rep) - Give Indication (CWE)

    rxe_28 : str | None
        RXE.28 (opt) - Dispense Package Size (NM)

    rxe_29 : CWE | None
        RXE.29 (opt) - Dispense Package Size Unit (CWE)

    rxe_30 : str | None
        RXE.30 (opt) - Dispense Package Method (ID)

    rxe_31 : list[CWE] | None
        RXE.31 (opt, rep) - Supplementary Code (CWE)

    rxe_32 : str | None
        RXE.32 (opt) - Original Order Date/Time (DTM)

    rxe_33 : str | None
        RXE.33 (opt) - Give Drug Strength Volume (NM)

    rxe_34 : CWE | None
        RXE.34 (opt) - Give Drug Strength Volume Units (CWE)

    rxe_35 : CWE | None
        RXE.35 (opt) - Controlled Substance Schedule (CWE)

    rxe_36 : str | None
        RXE.36 (opt) - Formulary Status (ID)

    rxe_37 : list[CWE] | None
        RXE.37 (opt, rep) - Pharmaceutical Substance Alternative (CWE)

    rxe_38 : CWE | None
        RXE.38 (opt) - Pharmacy of Most Recent Fill (CWE)

    rxe_39 : str | None
        RXE.39 (opt) - Initial Dispense Amount (NM)

    rxe_40 : CWE | None
        RXE.40 (opt) - Dispensing Pharmacy (CWE)

    rxe_41 : XAD | None
        RXE.41 (opt) - Dispensing Pharmacy Address (XAD)

    rxe_42 : PL | None
        RXE.42 (opt) - Deliver-to Patient Location (PL)

    rxe_43 : XAD | None
        RXE.43 (opt) - Deliver-to Address (XAD)

    rxe_44 : str | None
        RXE.44 (opt) - Pharmacy Order Type (ID)

    rxe_45 : list[XTN] | None
        RXE.45 (opt, rep) - Pharmacy Phone Number (XTN)
    """

    rxe_2: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "rxe_2",
            "give_code",
            "RXE.2",
        ),
        serialization_alias="RXE.2",
        title="Give Code",
        description="Item #317 | Table HL70292",
    )

    rxe_3: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "rxe_3",
            "give_amount_minimum",
            "RXE.3",
        ),
        serialization_alias="RXE.3",
        title="Give Amount - Minimum",
        description="Item #318",
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
        description="Item #319",
    )

    rxe_5: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "rxe_5",
            "give_units",
            "RXE.5",
        ),
        serialization_alias="RXE.5",
        title="Give Units",
        description="Item #320 | Table HL79999",
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
        description="Item #321 | Table HL79999",
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
        description="Item #298 | Table HL79999",
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
        description="Item #322 | Table HL70167",
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
        description="Item #323",
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
        description="Item #324 | Table HL79999",
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
        description="Item #304",
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
        description="Item #305",
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
        description="Item #306",
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
        description="Item #325",
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
        description="Item #326",
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
        description="Item #327",
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
        description="Item #328",
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
        description="Item #329",
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
        description="Item #307 | Table HL70136",
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
        description="Item #330 | Table HL79999",
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
        description="Item #331",
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
        description="Item #332",
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
        description="Item #333 | Table HL79999",
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
        description="Item #1126",
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
        description="Item #1127 | Table HL79999",
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
        description="Item #1128 | Table HL79999",
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
        description="Item #1220",
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
        description="Item #1221 | Table HL79999",
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
        description="Item #1222 | Table HL70321",
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
        description="Item #1476 | Table HL79999",
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
        description="Item #1673",
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
        description="Item #1674",
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
        description="Item #1675 | Table HL79999",
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
        description="Item #1676 | Table HL70477",
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
        description="Item #1677 | Table HL70478",
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
        description="Item #1678 | Table HL79999",
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
        description="Item #1679 | Table HL79999",
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
        description="Item #1680",
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
        description="Item #1681 | Table HL79999",
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
        description="Item #1682",
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
        description="Item #1683",
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
        description="Item #1684",
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
        description="Item #1685 | Table HL70480",
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
        description="Item #2310",
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
    def _validate_dtm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 datetime")
        return v

    model_config = {"populate_by_name": True}
