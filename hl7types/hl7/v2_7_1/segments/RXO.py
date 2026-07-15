"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
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
from ..datatypes.XTN import XTN


class RXO(HL7Model):
    """Pharmacy/Treatment Order (S4.A.1).

    Attributes
    ----------
    rxo_1 : CWE | None
        RXO.1 - Requested Give Code (CWE) C S4.A.1.1 | 9999 - no table for CE

    rxo_2 : str | None
        RXO.2 - Requested Give Amount - Minimum (NM) C S4.A.1.2

    rxo_3 : str | None
        RXO.3 - Requested Give Amount - Maximum (NM) O S4.A.1.3

    rxo_4 : CWE | None
        RXO.4 - Requested Give Units (CWE) C S4.A.1.4 | 9999 - no table for CE

    rxo_5 : CWE | None
        RXO.5 - Requested Dosage Form (CWE) C S4.A.1.5 | 9999 - no table for CE

    rxo_6 : list[CWE] | None
        RXO.6 - Provider's Pharmacy/Treatment Instructions (CWE) O rep S4.A.1.6 | 9999 - no table for CE

    rxo_7 : list[CWE] | None
        RXO.7 - Provider's Administration Instructions (CWE) O rep S4.A.1.7 | 9999 - no table for CE

    rxo_8 : LA1 | None
        RXO.8 - Deliver-To Location (LA1) O S4.A.1.8

    rxo_9 : str | None
        RXO.9 - Allow Substitutions (ID) O S4.A.1.9 | 0161 - Allow Substitution

    rxo_10 : CWE | None
        RXO.10 - Requested Dispense Code (CWE) O S4.A.1.10 | 9999 - no table for CE

    rxo_11 : str | None
        RXO.11 - Requested Dispense Amount (NM) O S4.A.1.11

    rxo_12 : CWE | None
        RXO.12 - Requested Dispense Units (CWE) O S4.A.1.12 | 9999 - no table for CE

    rxo_13 : str | None
        RXO.13 - Number Of Refills (NM) O S4.A.1.13

    rxo_14 : list[XCN] | None
        RXO.14 - Ordering Provider's DEA Number (XCN) O rep S4.A.1.14

    rxo_15 : list[XCN] | None
        RXO.15 - Pharmacist/Treatment Supplier's Verifier ID (XCN) C rep S4.A.1.15

    rxo_16 : str | None
        RXO.16 - Needs Human Review (ID) O S4.A.1.16 | 0136 - Yes/no Indicator

    rxo_17 : str | None
        RXO.17 - Requested Give Per (Time Unit) (ST) C S4.A.1.17

    rxo_18 : str | None
        RXO.18 - Requested Give Strength (NM) O S4.A.1.18

    rxo_19 : CWE | None
        RXO.19 - Requested Give Strength Units (CWE) O S4.A.1.19 | 9999 - no table for CE

    rxo_20 : list[CWE] | None
        RXO.20 - Indication (CWE) O rep S4.A.1.19 | 9999 - no table for CE

    rxo_21 : str | None
        RXO.21 - Requested Give Rate Amount (ST) O S4.A.1.21

    rxo_22 : CWE | None
        RXO.22 - Requested Give Rate Units (CWE) O S4.A.1.22 | 9999 - no table for CE

    rxo_23 : CQ | None
        RXO.23 - Total Daily Dose (CQ) O S4.A.1.23

    rxo_24 : list[CWE] | None
        RXO.24 - Supplementary Code (CWE) O rep S4.A.1.24 | 9999 - no table for CE

    rxo_25 : str | None
        RXO.25 - Requested Drug Strength Volume (NM) O S4.A.1.25

    rxo_26 : CWE | None
        RXO.26 - Requested Drug Strength Volume Units (CWE) O S4.A.1.26 | 9999 - no table for CE

    rxo_27 : str | None
        RXO.27 - Pharmacy Order Type (ID) O S4.A.1.27 | 0480 - Pharmacy Order Types

    rxo_28 : str | None
        RXO.28 - Dispensing Interval (NM) O S4.A.1.28

    rxo_29 : EI | None
        RXO.29 - Medication Instance Identifier (EI) O S4.A.1.29

    rxo_30 : EI | None
        RXO.30 - Segment Instance Identifier (EI) O S4.A.1.30

    rxo_31 : CNE | None
        RXO.31 - Mood Code (CNE) C S4.A.1.31 | 0725 - Mood Codes

    rxo_32 : CWE | None
        RXO.32 - Dispensing Pharmacy (CWE) O S4.A.1.32 | 9999 - no table for CE

    rxo_33 : XAD | None
        RXO.33 - Dispensing Pharmacy Address (XAD) O S4.A.1.33

    rxo_34 : PL | None
        RXO.34 - Deliver-to Patient Location (PL) O S4.A.1.34

    rxo_35 : XAD | None
        RXO.35 - Deliver-to Address (XAD) O S4.A.1.35

    rxo_36 : list[XTN] | None
        RXO.36 - Pharmacy Phone Number (XTN) O rep S4.A.1.36
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
        description="C | Item #00292 | Table 9999 - no table for CE",
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
        description="C | Item #00293",
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
        description="O | Item #00294",
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
        description="C | Item #00295 | Table 9999 - no table for CE",
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
        description="C | Item #00296 | Table 9999 - no table for CE",
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
        description="O | Item #00297 | Table 9999 - no table for CE",
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
        description="O | Item #00298 | Table 9999 - no table for CE",
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
        description="O | Item #00299",
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
        description="O | Item #00300 | Table 0161 - Allow Substitution | LEN:1",
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
        description="O | Item #00301 | Table 9999 - no table for CE",
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
        description="O | Item #00302",
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
        description="O | Item #00303 | Table 9999 - no table for CE",
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
        description="O | Item #00304",
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
        description="O | Item #00305",
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
        description="C | Item #00306",
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
        description="O | Item #00307 | Table 0136 - Yes/no Indicator | LEN:1",
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
        description="C | Item #00308",
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
        description="O | Item #01121",
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
        description="O | Item #01122 | Table 9999 - no table for CE",
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
        description="O | Item #01123 | Table 9999 - no table for CE",
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
        description="O | Item #01218",
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
        description="O | Item #01219 | Table 9999 - no table for CE",
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
        description="O | Item #00329",
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
        description="O | Item #01476 | Table 9999 - no table for CE",
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
        description="O | Item #01666",
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
        description="O | Item #01667 | Table 9999 - no table for CE",
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
        description=(
            "O | Item #01668 | Table 0480 - Pharmacy Order Types | LEN:1"
        ),
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
        description="O | Item #01669",
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
        description="O | Item #02149",
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
        description="O | Item #02150",
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
        description="C | Item #02151 | Table 0725 - Mood Codes",
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
        description="O | Item #01681 | Table 9999 - no table for CE",
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
        description="O | Item #01682",
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
        description="O | Item #01683",
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
        description="O | Item #01684",
    )

    rxo_36: Optional[List[XTN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_36",
            "pharmacy_phone_number",
            "RXO.36",
        ),
        serialization_alias="RXO.36",
        title="Pharmacy Phone Number",
        description="O | Item #02309",
    )

    @field_validator("rxo_2", "rxo_3", "rxo_11", "rxo_13", "rxo_18", "rxo_25", "rxo_28", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
