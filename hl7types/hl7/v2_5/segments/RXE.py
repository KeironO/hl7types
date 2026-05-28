"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: RXE
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE
from ..datatypes.CQ import CQ
from ..datatypes.CWE import CWE
from ..datatypes.LA1 import LA1
from ..datatypes.PL import PL
from ..datatypes.TQ import TQ
from ..datatypes.TS import TS
from ..datatypes.XAD import XAD
from ..datatypes.XCN import XCN


class RXE(BaseModel):
    """HL7 v2 RXE segment."""

    rxe_1: Optional[TQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_1",
            "quantity_timing",
            "RXE.1",
        ),
        serialization_alias="RXE.1",
        title="Quantity/Timing",
        description="Item #221",
    )

    rxe_2: CE = Field(
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

    rxe_5: CE = Field(
        default=...,
        validation_alias=AliasChoices(
            "rxe_5",
            "give_units",
            "RXE.5",
        ),
        serialization_alias="RXE.5",
        title="Give Units",
        description="Item #320",
    )

    rxe_6: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_6",
            "give_dosage_form",
            "RXE.6",
        ),
        serialization_alias="RXE.6",
        title="Give Dosage Form",
        description="Item #321",
    )

    rxe_7: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_7",
            "provider_s_administration_instructions",
            "RXE.7",
        ),
        serialization_alias="RXE.7",
        title="Provider's Administration Instructions",
        description="Item #298",
    )

    rxe_8: Optional[LA1] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_8",
            "deliver_to_location",
            "RXE.8",
        ),
        serialization_alias="RXE.8",
        title="Deliver-To Location",
        description="Item #299",
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

    rxe_11: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_11",
            "dispense_units",
            "RXE.11",
        ),
        serialization_alias="RXE.11",
        title="Dispense Units",
        description="Item #324",
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

    rxe_18: Optional[TS] = Field(
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

    rxe_21: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_21",
            "pharmacy_treatment_supplier_s_special_dispensing_instructions",
            "RXE.21",
        ),
        serialization_alias="RXE.21",
        title="Pharmacy/Treatment Supplier's Special Dispensing Instructions",
        description="Item #330",
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

    rxe_24: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_24",
            "give_rate_units",
            "RXE.24",
        ),
        serialization_alias="RXE.24",
        title="Give Rate Units",
        description="Item #333",
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

    rxe_26: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_26",
            "give_strength_units",
            "RXE.26",
        ),
        serialization_alias="RXE.26",
        title="Give Strength Units",
        description="Item #1127",
    )

    rxe_27: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_27",
            "give_indication",
            "RXE.27",
        ),
        serialization_alias="RXE.27",
        title="Give Indication",
        description="Item #1128",
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

    rxe_29: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_29",
            "dispense_package_size_unit",
            "RXE.29",
        ),
        serialization_alias="RXE.29",
        title="Dispense Package Size Unit",
        description="Item #1221",
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

    rxe_31: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_31",
            "supplementary_code",
            "RXE.31",
        ),
        serialization_alias="RXE.31",
        title="Supplementary Code",
        description="Item #1476",
    )

    rxe_32: Optional[TS] = Field(
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
        description="Item #1675",
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
        description="Item #1678",
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
        description="Item #1679",
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
        description="Item #1681",
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

    model_config = {"populate_by_name": True}
