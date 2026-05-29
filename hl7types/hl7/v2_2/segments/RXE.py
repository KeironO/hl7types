"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: RXE
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE
from ..datatypes.TQ import TQ
from ..datatypes.TS import TS


class RXE(BaseModel):
    """HL7 v2 RXE segment.

    Attributes
    ----------
    rxe_1 : list[TQ] | None
        RXE.1 (opt, rep) - Quantity / timing (TQ)

    rxe_2 : CE
        RXE.2 (req) - Give Code (CE)

    rxe_3 : str
        RXE.3 (req) - Give Amount - Minimum (NM)

    rxe_4 : str | None
        RXE.4 (opt) - Give Amount - Maximum (NM)

    rxe_5 : CE
        RXE.5 (req) - Give Units (CE)

    rxe_6 : CE | None
        RXE.6 (opt) - Give Dosage Form (CE)

    rxe_7 : list[CE] | None
        RXE.7 (opt, rep) - Provider's Administration Instructions (CE)

    rxe_8 : str | None
        RXE.8 (opt) - Deliver-to location (CM)

    rxe_9 : str | None
        RXE.9 (opt) - Substitution Status (ID)

    rxe_10 : str | None
        RXE.10 (opt) - Dispense Amount (NM)

    rxe_11 : CE | None
        RXE.11 (opt) - Dispense Units (CE)

    rxe_12 : str | None
        RXE.12 (opt) - Number of Refills (NM)

    rxe_13 : str | None
        RXE.13 (opt) - Ordering Provider's DEA Number (CN)

    rxe_14 : str | None
        RXE.14 (opt) - Pharmacist Verifier ID (CN)

    rxe_15 : str
        RXE.15 (req) - Prescription Number (ST)

    rxe_16 : str | None
        RXE.16 (opt) - Number of Refills Remaining (NM)

    rxe_17 : str | None
        RXE.17 (opt) - Number of refills / doses dispensed (NM)

    rxe_18 : TS | None
        RXE.18 (opt) - Date / time of most recent refill or dose dispensed (TS)

    rxe_19 : str | None
        RXE.19 (opt) - Total Daily Dose (CQ)

    rxe_20 : str | None
        RXE.20 (opt) - Needs Human Review (ID)

    rxe_21 : CE | None
        RXE.21 (opt) - Pharmacy Special Dispensing Instructions (CE)

    rxe_22 : str | None
        RXE.22 (opt) - Give Per (Time Unit) (ST)

    rxe_23 : CE | None
        RXE.23 (opt) - Give Rate Amount (CE)

    rxe_24 : CE | None
        RXE.24 (opt) - Give Rate Units (CE)
    """

    rxe_1: Optional[List[TQ]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_1",
            "quantity_timing",
            "RXE.1",
        ),
        serialization_alias="RXE.1",
        title="Quantity / timing",
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
        description="Item #317",
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

    rxe_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_8",
            "deliver_to_location",
            "RXE.8",
        ),
        serialization_alias="RXE.8",
        title="Deliver-to location",
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
        title="Number of Refills",
        description="Item #304",
    )

    rxe_13: Optional[str] = Field(
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

    rxe_14: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_14",
            "pharmacist_verifier_id",
            "RXE.14",
        ),
        serialization_alias="RXE.14",
        title="Pharmacist Verifier ID",
        description="Item #306",
    )

    rxe_15: str = Field(
        default=...,
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
        title="Number of refills / doses dispensed",
        description="Item #327",
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
        description="Item #328",
    )

    rxe_19: Optional[str] = Field(
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
        description="Item #307",
    )

    rxe_21: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxe_21",
            "pharmacy_special_dispensing_instructions",
            "RXE.21",
        ),
        serialization_alias="RXE.21",
        title="Pharmacy Special Dispensing Instructions",
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

    rxe_23: Optional[CE] = Field(
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

    model_config = {"populate_by_name": True}
