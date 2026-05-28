"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: RXE
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CQ import CQ
from ..datatypes.CWE import CWE
from ..datatypes.PL import PL
from ..datatypes.XAD import XAD
from ..datatypes.XCN import XCN
from ..datatypes.XTN import XTN


class RXE(BaseModel):
    """HL7 v2 RXE segment."""

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

    rxe_4: str | None = Field(
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

    rxe_6: CWE | None = Field(
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

    rxe_7: list[CWE] | None = Field(
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

    rxe_9: str | None = Field(
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

    rxe_10: str | None = Field(
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

    rxe_11: CWE | None = Field(
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

    rxe_12: str | None = Field(
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

    rxe_13: list[XCN] | None = Field(
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

    rxe_14: list[XCN] | None = Field(
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

    rxe_15: str | None = Field(
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

    rxe_16: str | None = Field(
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

    rxe_17: str | None = Field(
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

    rxe_18: str | None = Field(
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

    rxe_19: CQ | None = Field(
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

    rxe_20: str | None = Field(
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

    rxe_21: list[CWE] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_21",
            "pharmacy_treatment_supplier_s_special_dispensing_instructions",
            "RXE.21",
        ),
        serialization_alias="RXE.21",
        title="Pharmacy/Treatment Supplier's Special Dispensing Instructions",
        description="Item #330 | Table HL79999",
    )

    rxe_22: str | None = Field(
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

    rxe_23: str | None = Field(
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

    rxe_24: CWE | None = Field(
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

    rxe_25: str | None = Field(
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

    rxe_26: CWE | None = Field(
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

    rxe_27: list[CWE] | None = Field(
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

    rxe_28: str | None = Field(
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

    rxe_29: CWE | None = Field(
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

    rxe_30: str | None = Field(
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

    rxe_31: list[CWE] | None = Field(
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

    rxe_32: str | None = Field(
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

    rxe_33: str | None = Field(
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

    rxe_34: CWE | None = Field(
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

    rxe_35: CWE | None = Field(
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

    rxe_36: str | None = Field(
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

    rxe_37: list[CWE] | None = Field(
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

    rxe_38: CWE | None = Field(
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

    rxe_39: str | None = Field(
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

    rxe_40: CWE | None = Field(
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

    rxe_41: XAD | None = Field(
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

    rxe_42: PL | None = Field(
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

    rxe_43: XAD | None = Field(
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

    rxe_44: str | None = Field(
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

    rxe_45: list[XTN] | None = Field(
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

    model_config = {"populate_by_name": True}
