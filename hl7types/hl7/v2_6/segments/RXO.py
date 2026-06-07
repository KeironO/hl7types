"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: RXO
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CNE import CNE
from ..datatypes.CQ import CQ
from ..datatypes.CWE import CWE
from ..datatypes.EI import EI
from ..datatypes.LA1 import LA1
from ..datatypes.PL import PL
from ..datatypes.XAD import XAD
from ..datatypes.XCN import XCN


class RXO(HL7Model):
    """HL7 v2 RXO segment.

    Attributes
    ----------
    rxo_1 : CWE | None
        RXO.1 (opt) - Requested Give Code (CWE)

    rxo_2 : str | None
        RXO.2 (opt) - Requested Give Amount - Minimum (NM)

    rxo_3 : str | None
        RXO.3 (opt) - Requested Give Amount - Maximum (NM)

    rxo_4 : CWE | None
        RXO.4 (opt) - Requested Give Units (CWE)

    rxo_5 : CWE | None
        RXO.5 (opt) - Requested Dosage Form (CWE)

    rxo_6 : list[CWE] | None
        RXO.6 (opt, rep) - Provider's Pharmacy/Treatment Instructions (CWE)

    rxo_7 : list[CWE] | None
        RXO.7 (opt, rep) - Provider's Administration Instructions (CWE)

    rxo_8 : LA1 | None
        RXO.8 (opt) - Deliver-To Location (LA1)

    rxo_9 : str | None
        RXO.9 (opt) - Allow Substitutions (ID)

    rxo_10 : CWE | None
        RXO.10 (opt) - Requested Dispense Code (CWE)

    rxo_11 : str | None
        RXO.11 (opt) - Requested Dispense Amount (NM)

    rxo_12 : CWE | None
        RXO.12 (opt) - Requested Dispense Units (CWE)

    rxo_13 : str | None
        RXO.13 (opt) - Number Of Refills (NM)

    rxo_14 : list[XCN] | None
        RXO.14 (opt, rep) - Ordering Provider's DEA Number (XCN)

    rxo_15 : list[XCN] | None
        RXO.15 (opt, rep) - Pharmacist/Treatment Supplier's Verifier ID (XCN)

    rxo_16 : str | None
        RXO.16 (opt) - Needs Human Review (ID)

    rxo_17 : str | None
        RXO.17 (opt) - Requested Give Per (Time Unit) (ST)

    rxo_18 : str | None
        RXO.18 (opt) - Requested Give Strength (NM)

    rxo_19 : CWE | None
        RXO.19 (opt) - Requested Give Strength Units (CWE)

    rxo_20 : list[CWE] | None
        RXO.20 (opt, rep) - Indication (CWE)

    rxo_21 : str | None
        RXO.21 (opt) - Requested Give Rate Amount (ST)

    rxo_22 : CWE | None
        RXO.22 (opt) - Requested Give Rate Units (CWE)

    rxo_23 : CQ | None
        RXO.23 (opt) - Total Daily Dose (CQ)

    rxo_24 : list[CWE] | None
        RXO.24 (opt, rep) - Supplementary Code (CWE)

    rxo_25 : str | None
        RXO.25 (opt) - Requested Drug Strength Volume (NM)

    rxo_26 : CWE | None
        RXO.26 (opt) - Requested Drug Strength Volume Units (CWE)

    rxo_27 : str | None
        RXO.27 (opt) - Pharmacy Order Type (ID)

    rxo_28 : str | None
        RXO.28 (opt) - Dispensing Interval (NM)

    rxo_29 : EI | None
        RXO.29 (opt) - Medication Instance Identifier (EI)

    rxo_30 : EI | None
        RXO.30 (opt) - Segment Instance Identifier (EI)

    rxo_31 : CNE | None
        RXO.31 (opt) - Mood Code (CNE)

    rxo_32 : CWE | None
        RXO.32 (opt) - Dispensing Pharmacy (CWE)

    rxo_33 : XAD | None
        RXO.33 (opt) - Dispensing Pharmacy Address (XAD)

    rxo_34 : PL | None
        RXO.34 (opt) - Deliver-to Patient Location (PL)

    rxo_35 : XAD | None
        RXO.35 (opt) - Deliver-to Address (XAD)
    """

    rxo_1: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_1",
            "requested_give_code",
            "RXO.1",
        ),
        serialization_alias="RXO.1",
        title="Requested Give Code",
        description="Item #292 | Table HL79999",
    )

    rxo_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_2",
            "requested_give_amount_minimum",
            "RXO.2",
        ),
        serialization_alias="RXO.2",
        title="Requested Give Amount - Minimum",
        description="Item #293",
    )

    rxo_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_3",
            "requested_give_amount_maximum",
            "RXO.3",
        ),
        serialization_alias="RXO.3",
        title="Requested Give Amount - Maximum",
        description="Item #294",
    )

    rxo_4: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_4",
            "requested_give_units",
            "RXO.4",
        ),
        serialization_alias="RXO.4",
        title="Requested Give Units",
        description="Item #295 | Table HL79999",
    )

    rxo_5: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_5",
            "requested_dosage_form",
            "RXO.5",
        ),
        serialization_alias="RXO.5",
        title="Requested Dosage Form",
        description="Item #296 | Table HL79999",
    )

    rxo_6: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_6",
            "provider_s_pharmacy_treatment_instructions",
            "RXO.6",
        ),
        serialization_alias="RXO.6",
        title="Provider's Pharmacy/Treatment Instructions",
        description="Item #297 | Table HL79999",
    )

    rxo_7: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_7",
            "provider_s_administration_instructions",
            "RXO.7",
        ),
        serialization_alias="RXO.7",
        title="Provider's Administration Instructions",
        description="Item #298 | Table HL79999",
    )

    rxo_8: Optional[LA1] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_8",
            "deliver_to_location",
            "RXO.8",
        ),
        serialization_alias="RXO.8",
        title="Deliver-To Location",
        description="Item #299",
    )

    rxo_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_9",
            "allow_substitutions",
            "RXO.9",
        ),
        serialization_alias="RXO.9",
        title="Allow Substitutions",
        description="Item #300 | Table HL70161",
    )

    rxo_10: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_10",
            "requested_dispense_code",
            "RXO.10",
        ),
        serialization_alias="RXO.10",
        title="Requested Dispense Code",
        description="Item #301 | Table HL79999",
    )

    rxo_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_11",
            "requested_dispense_amount",
            "RXO.11",
        ),
        serialization_alias="RXO.11",
        title="Requested Dispense Amount",
        description="Item #302",
    )

    rxo_12: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_12",
            "requested_dispense_units",
            "RXO.12",
        ),
        serialization_alias="RXO.12",
        title="Requested Dispense Units",
        description="Item #303 | Table HL79999",
    )

    rxo_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_13",
            "number_of_refills",
            "RXO.13",
        ),
        serialization_alias="RXO.13",
        title="Number Of Refills",
        description="Item #304",
    )

    rxo_14: Optional[List[XCN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_14",
            "ordering_provider_s_dea_number",
            "RXO.14",
        ),
        serialization_alias="RXO.14",
        title="Ordering Provider's DEA Number",
        description="Item #305",
    )

    rxo_15: Optional[List[XCN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_15",
            "pharmacist_treatment_supplier_s_verifier_id",
            "RXO.15",
        ),
        serialization_alias="RXO.15",
        title="Pharmacist/Treatment Supplier's Verifier ID",
        description="Item #306",
    )

    rxo_16: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_16",
            "needs_human_review",
            "RXO.16",
        ),
        serialization_alias="RXO.16",
        title="Needs Human Review",
        description="Item #307 | Table HL70136",
    )

    rxo_17: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_17",
            "requested_give_per_time_unit",
            "RXO.17",
        ),
        serialization_alias="RXO.17",
        title="Requested Give Per (Time Unit)",
        description="Item #308",
    )

    rxo_18: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_18",
            "requested_give_strength",
            "RXO.18",
        ),
        serialization_alias="RXO.18",
        title="Requested Give Strength",
        description="Item #1121",
    )

    rxo_19: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_19",
            "requested_give_strength_units",
            "RXO.19",
        ),
        serialization_alias="RXO.19",
        title="Requested Give Strength Units",
        description="Item #1122 | Table HL79999",
    )

    rxo_20: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_20",
            "indication",
            "RXO.20",
        ),
        serialization_alias="RXO.20",
        title="Indication",
        description="Item #1123 | Table HL79999",
    )

    rxo_21: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_21",
            "requested_give_rate_amount",
            "RXO.21",
        ),
        serialization_alias="RXO.21",
        title="Requested Give Rate Amount",
        description="Item #1218",
    )

    rxo_22: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_22",
            "requested_give_rate_units",
            "RXO.22",
        ),
        serialization_alias="RXO.22",
        title="Requested Give Rate Units",
        description="Item #1219 | Table HL79999",
    )

    rxo_23: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_23",
            "total_daily_dose",
            "RXO.23",
        ),
        serialization_alias="RXO.23",
        title="Total Daily Dose",
        description="Item #329",
    )

    rxo_24: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_24",
            "supplementary_code",
            "RXO.24",
        ),
        serialization_alias="RXO.24",
        title="Supplementary Code",
        description="Item #1476 | Table HL79999",
    )

    rxo_25: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_25",
            "requested_drug_strength_volume",
            "RXO.25",
        ),
        serialization_alias="RXO.25",
        title="Requested Drug Strength Volume",
        description="Item #1666",
    )

    rxo_26: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_26",
            "requested_drug_strength_volume_units",
            "RXO.26",
        ),
        serialization_alias="RXO.26",
        title="Requested Drug Strength Volume Units",
        description="Item #1667 | Table HL79999",
    )

    rxo_27: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_27",
            "pharmacy_order_type",
            "RXO.27",
        ),
        serialization_alias="RXO.27",
        title="Pharmacy Order Type",
        description="Item #1668 | Table HL70480",
    )

    rxo_28: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_28",
            "dispensing_interval",
            "RXO.28",
        ),
        serialization_alias="RXO.28",
        title="Dispensing Interval",
        description="Item #1669",
    )

    rxo_29: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_29",
            "medication_instance_identifier",
            "RXO.29",
        ),
        serialization_alias="RXO.29",
        title="Medication Instance Identifier",
        description="Item #2149",
    )

    rxo_30: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_30",
            "segment_instance_identifier",
            "RXO.30",
        ),
        serialization_alias="RXO.30",
        title="Segment Instance Identifier",
        description="Item #2150",
    )

    rxo_31: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_31",
            "mood_code",
            "RXO.31",
        ),
        serialization_alias="RXO.31",
        title="Mood Code",
        description="Item #2151 | Table HL70725",
    )

    rxo_32: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_32",
            "dispensing_pharmacy",
            "RXO.32",
        ),
        serialization_alias="RXO.32",
        title="Dispensing Pharmacy",
        description="Item #1681 | Table HL79999",
    )

    rxo_33: Optional[XAD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_33",
            "dispensing_pharmacy_address",
            "RXO.33",
        ),
        serialization_alias="RXO.33",
        title="Dispensing Pharmacy Address",
        description="Item #1682",
    )

    rxo_34: Optional[PL] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_34",
            "deliver_to_patient_location",
            "RXO.34",
        ),
        serialization_alias="RXO.34",
        title="Deliver-to Patient Location",
        description="Item #1683",
    )

    rxo_35: Optional[XAD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_35",
            "deliver_to_address",
            "RXO.35",
        ),
        serialization_alias="RXO.35",
        title="Deliver-to Address",
        description="Item #1684",
    )

    @field_validator("rxo_2", "rxo_3", "rxo_11", "rxo_13", "rxo_18", "rxo_25", "rxo_28", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
