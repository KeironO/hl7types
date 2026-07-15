"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: RXO
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.CQ import CQ
from ..datatypes.LA1 import LA1
from ..datatypes.XCN import XCN


class RXO(HL7Model):
    """RXO - pharmacy/treatment order segment (S4.8.2).

    Attributes
    ----------
    rxo_1 : CE | None
        RXO.1 - Requested Give Code (CE) C S4.8.2.1

    rxo_2 : str | None
        RXO.2 - Requested Give Amount - Minimum (NM) C S4.8.2.2

    rxo_3 : str | None
        RXO.3 - Requested Give Amount - Maximum (NM) O S4.8.2.3

    rxo_4 : CE | None
        RXO.4 - Requested Give Units (CE) C S4.8.2.4

    rxo_5 : CE | None
        RXO.5 - Requested Dosage Form (CE) O S4.8.2.5

    rxo_6 : list[CE] | None
        RXO.6 - Provider’s Pharmacy/Treatment Instructions (CE) O rep S4.8.2.6

    rxo_7 : list[CE] | None
        RXO.7 - Provider’s Administration Instructions (CE) O rep S4.8.7.7

    rxo_8 : LA1 | None
        RXO.8 - Deliver-to Location (LA1) O S4.8.7.8

    rxo_9 : str | None
        RXO.9 - Allow Substitutions (ID) O S4.8.2.9 | 0161 - Allow substitution

    rxo_10 : CE | None
        RXO.10 - Requested Dispense Code (CE) O S4.8.2.10

    rxo_11 : str | None
        RXO.11 - Requested Dispense Amount (NM) O S4.8.2.11

    rxo_12 : CE | None
        RXO.12 - Requested Dispense Units (CE) O S4.8.2.12

    rxo_13 : str | None
        RXO.13 - Number Of Refills (NM) O S4.8.7.12

    rxo_14 : list[XCN] | None
        RXO.14 - Ordering Provider’s DEA Number (XCN) C rep S4.8.7.13

    rxo_15 : list[XCN] | None
        RXO.15 - Pharmacist/Treatment Supplier’s Verifier ID (XCN) C rep S4.8.7.14

    rxo_16 : str | None
        RXO.16 - Needs Human Review (ID) O S4.8.12.12 | 0136 - Yes/no indicator

    rxo_17 : str | None
        RXO.17 - Requested Give Per (Time Unit) (ST) C S4.8.2.17

    rxo_18 : str | None
        RXO.18 - Requested Give Strength (NM) O S4.8.2.18

    rxo_19 : CE | None
        RXO.19 - Requested Give Strength Units (CE) O S4.8.2.19

    rxo_20 : list[CE] | None
        RXO.20 - Indication (CE) O rep S4.8.14.19

    rxo_21 : str | None
        RXO.21 - Requested Give Rate Amount (ST) O S4.8.2.21

    rxo_22 : CE | None
        RXO.22 - Requested Give Rate Units (CE) O S4.8.2.22

    rxo_23 : CQ | None
        RXO.23 - Total Daily Dose (CQ) O S4.8.10.12
    """

    rxo_1: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_1",
            "requested_give_code",
            "RXO.1",
        ),
        serialization_alias="RXO.1",
        title="Requested Give Code",
        description="C | Item #00292",
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
        description="C | Item #00293 | LEN:20",
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
        description="O | Item #00294 | LEN:20",
    )

    rxo_4: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_4",
            "requested_give_units",
            "RXO.4",
        ),
        serialization_alias="RXO.4",
        title="Requested Give Units",
        description="C | Item #00295",
    )

    rxo_5: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_5",
            "requested_dosage_form",
            "RXO.5",
        ),
        serialization_alias="RXO.5",
        title="Requested Dosage Form",
        description="O | Item #00296",
    )

    rxo_6: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_6",
            "provider_s_pharmacy_treatment_instructions",
            "RXO.6",
        ),
        serialization_alias="RXO.6",
        title="Provider’s Pharmacy/Treatment Instructions",
        description="O | Item #00297",
    )

    rxo_7: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_7",
            "provider_s_administration_instructions",
            "RXO.7",
        ),
        serialization_alias="RXO.7",
        title="Provider’s Administration Instructions",
        description="O | Item #00298",
    )

    rxo_8: Optional[LA1] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_8",
            "deliver_to_location",
            "RXO.8",
        ),
        serialization_alias="RXO.8",
        title="Deliver-to Location",
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
        description="O | Item #00300 | Table 0161 - Allow substitution | LEN:1",
    )

    rxo_10: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_10",
            "requested_dispense_code",
            "RXO.10",
        ),
        serialization_alias="RXO.10",
        title="Requested Dispense Code",
        description="O | Item #00301",
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
        description="O | Item #00302 | LEN:20",
    )

    rxo_12: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_12",
            "requested_dispense_units",
            "RXO.12",
        ),
        serialization_alias="RXO.12",
        title="Requested Dispense Units",
        description="O | Item #00303",
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
        description="O | Item #00304 | LEN:3",
    )

    rxo_14: Optional[List[XCN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_14",
            "ordering_provider_s_dea_number",
            "RXO.14",
        ),
        serialization_alias="RXO.14",
        title="Ordering Provider’s DEA Number",
        description="C | Item #00305",
    )

    rxo_15: Optional[List[XCN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_15",
            "pharmacist_treatment_supplier_s_verifier_id",
            "RXO.15",
        ),
        serialization_alias="RXO.15",
        title="Pharmacist/Treatment Supplier’s Verifier ID",
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
        description="O | Item #00307 | Table 0136 - Yes/no indicator | LEN:1",
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
        description="C | Item #00308 | LEN:20",
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
        description="O | Item #01121 | LEN:20",
    )

    rxo_19: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_19",
            "requested_give_strength_units",
            "RXO.19",
        ),
        serialization_alias="RXO.19",
        title="Requested Give Strength Units",
        description="O | Item #01122",
    )

    rxo_20: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_20",
            "indication",
            "RXO.20",
        ),
        serialization_alias="RXO.20",
        title="Indication",
        description="O | Item #01123",
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
        description="O | Item #01218 | LEN:6",
    )

    rxo_22: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxo_22",
            "requested_give_rate_units",
            "RXO.22",
        ),
        serialization_alias="RXO.22",
        title="Requested Give Rate Units",
        description="O | Item #01219",
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

    @field_validator("rxo_2", "rxo_3", "rxo_11", "rxo_13", "rxo_18", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
