"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: RXE
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.CN import CN
from ..datatypes.CQ import CQ
from ..datatypes.TQ import TQ
from ..datatypes.TS import TS

_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class RXE(HL7Model):
    """Pharmacy encoded order segment (S4.8.7).

    Attributes
    ----------
    rxe_1 : TQ
        RXE.1 - Quantity/Timing (TQ) R S4.3.1

    rxe_2 : CE
        RXE.2 - Give Code (CE) R S4.8.7

    rxe_3 : str
        RXE.3 - Give Amount - Minimum (NM) R S4.8.7

    rxe_4 : str | None
        RXE.4 - Give Amount - Maximum (NM) O S4.8.7

    rxe_5 : CE
        RXE.5 - Give Units (CE) R S4.8.7

    rxe_6 : CE | None
        RXE.6 - Give Dosage Form (CE) O S4.8.7

    rxe_7 : list[CE] | None
        RXE.7 - Provider's Administration Instructions (CE) O rep S4.8.2

    rxe_8 : str | None
        RXE.8 - Deliver To Location (CM) O S4.8.2

    rxe_9 : str | None
        RXE.9 - Substitution Status (ID) O S4.8.7 | 0167 - Substitution Status

    rxe_10 : str | None
        RXE.10 - Dispense Amount (NM) C S4.8.7

    rxe_11 : CE | None
        RXE.11 - Dispense Units (CE) C S4.8.7.11

    rxe_12 : str | None
        RXE.12 - Number of Refills (NM) O S4.8.2

    rxe_13 : CN | None
        RXE.13 - Ordering Provider's DEA Number (CN) C S4.8.2

    rxe_14 : CN | None
        RXE.14 - Pharmacist/Treatment Supplier's Verifier ID (CN) C S4.8.2

    rxe_15 : str | None
        RXE.15 - Prescription Number (ST) C S4.8.7

    rxe_16 : str | None
        RXE.16 - Number of Refills Remaining (NM) C S4.8.7

    rxe_17 : str | None
        RXE.17 - Number of Refills/Doses Dispensed (NM) C S4.8.7.17

    rxe_18 : TS | None
        RXE.18 - Date / time of most recent refill or dose dispensed (TS) O S4.8.7.18

    rxe_19 : CQ | None
        RXE.19 - Total Daily Dose (CQ) C S4.8.7

    rxe_20 : str | None
        RXE.20 - Needs Human Review (ID) O S4.8.2 | 0136 - Yes/No Indicator

    rxe_21 : list[CE] | None
        RXE.21 - Pharmacy/Treatment Supplier's Special Dispensing Instructions (CE) O rep S4.8.7

    rxe_22 : str | None
        RXE.22 - Give Per (Time Unit) (ST) C S4.8.12.14

    rxe_23 : str | None
        RXE.23 - Give Rate Amount (ST) O S4.8.7

    rxe_24 : CE | None
        RXE.24 - Give Rate Units (CE) O S4.8.7

    rxe_25 : str | None
        RXE.25 - Give Strength (NM) O S4.8.7

    rxe_26 : CE | None
        RXE.26 - Give Strength Units (CE) O S4.8.7

    rxe_27 : CE | None
        RXE.27 - Give Indication (CE) O S4.8.7

    rxe_28 : str | None
        RXE.28 - Dispense Package Size (NM) O S4.8.7

    rxe_29 : CE | None
        RXE.29 - Dispense Package Size Unit (CE) O S4.8.7

    rxe_30 : str | None
        RXE.30 - Dispense Package Method (ID) O S4.8.7 | 0321 - Dispense Method
    """

    rxe_1: TQ = Field(
        validation_alias=AliasChoices(
            "rxe_1",
            "quantity_timing",
            "RXE.1",
        ),
        serialization_alias="RXE.1",
        title="Quantity/Timing",
        description="R | Item #00221",
    )

    rxe_2: CE = Field(
        validation_alias=AliasChoices(
            "rxe_2",
            "give_code",
            "RXE.2",
        ),
        serialization_alias="RXE.2",
        title="Give Code",
        description="R | Item #00317",
    )

    rxe_3: str = Field(
        validation_alias=AliasChoices(
            "rxe_3",
            "give_amount_minimum",
            "RXE.3",
        ),
        serialization_alias="RXE.3",
        title="Give Amount - Minimum",
        description="R | Item #00318 | LEN:20",
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
        description="O | Item #00319 | LEN:20",
    )

    rxe_5: CE = Field(
        validation_alias=AliasChoices(
            "rxe_5",
            "give_units",
            "RXE.5",
        ),
        serialization_alias="RXE.5",
        title="Give Units",
        description="R | Item #00320",
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
        description="O | Item #00321",
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
        description="O | Item #00298",
    )

    rxe_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_8",
            "deliver_to_location",
            "RXE.8",
        ),
        serialization_alias="RXE.8",
        title="Deliver To Location",
        description="O | Item #00299",
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
        description="C | Item #00323 | LEN:20",
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
        description="C | Item #00324",
    )

    rxe_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_12",
            "number_of_refills",
            "RXE.12",
        ),
        serialization_alias="RXE.12",
        title="Number of Refills",
        description="O | Item #00304 | LEN:3",
    )

    rxe_13: Optional[CN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_13",
            "ordering_provider_s_dea_number",
            "RXE.13",
        ),
        serialization_alias="RXE.13",
        title="Ordering Provider's DEA Number",
        description="C | Item #00305",
    )

    rxe_14: Optional[CN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_14",
            "pharmacist_treatment_supplier_s_verifier_id",
            "RXE.14",
        ),
        serialization_alias="RXE.14",
        title="Pharmacist/Treatment Supplier's Verifier ID",
        description="C | Item #00306",
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
        description="C | Item #00325 | LEN:20",
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
        description="C | Item #00326 | LEN:20",
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
        description="C | Item #00327 | LEN:20",
    )

    rxe_18: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_18",
            "date_time_of_most_recent_refill_or_dose_dispensed",
            "RXE.18",
        ),
        serialization_alias="RXE.18",
        title="Date / time of most recent refill or dose dispensed",
        description="O | Item #00328",
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
        description="O | Item #00307 | Table 0136 - Yes/No Indicator | LEN:1",
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
        description="O | Item #00330",
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
        description="C | Item #00331 | LEN:20",
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
        description="O | Item #00332 | LEN:6",
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
        description="O | Item #00333",
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
        description="O | Item #01126 | LEN:20",
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
        description="O | Item #01127",
    )

    rxe_27: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_27",
            "give_indication",
            "RXE.27",
        ),
        serialization_alias="RXE.27",
        title="Give Indication",
        description="O | Item #01128",
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
        description="O | Item #01220 | LEN:20",
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
        description="O | Item #01221",
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

    @field_validator("rxe_3", "rxe_4", "rxe_10", "rxe_12", "rxe_16", "rxe_17", "rxe_25", "rxe_28", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
