"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: RXD
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.TS import TS


class RXD(HL7Model):
    """PHARMACY DISPENSE (S4.8.10).

    Attributes
    ----------
    rxd_1 : str | None
        RXD.1 - Dispense Sub-ID Counter (NM) NA S4.8.12.2

    rxd_2 : CE
        RXD.2 - Dispense / give code (CE) R S4.8.10.2

    rxd_3 : TS | None
        RXD.3 - Date / time dispensed (TS) NA S4.8.10.3

    rxd_4 : str
        RXD.4 - Actual Dispense Amount (NM) R S4.8.10.4

    rxd_5 : CE | None
        RXD.5 - Actual Dispense Units (CE) C S4.8.10.5

    rxd_6 : CE | None
        RXD.6 - Actual Dosage Form (CE) NA S4.8.10.6

    rxd_7 : str
        RXD.7 - Prescription Number (ST) R S4.8.10.7

    rxd_8 : str | None
        RXD.8 - Number of Refills Remaining (NM) C S4.8.10.8

    rxd_9 : list[str] | None
        RXD.9 - Dispense Notes (ST) C rep S4.8.10.9

    rxd_10 : str | None
        RXD.10 - Dispensing Provider (CN) NA S4.8.10.10

    rxd_11 : str | None
        RXD.11 - Substitution Status (ID) NA S4.8.12.10 | 0167 - SUBSTITUTION STATUS

    rxd_12 : str | None
        RXD.12 - Total Daily Dose (CQ) NA S4.8.7.19

    rxd_13 : str | None
        RXD.13 - Deliver-to location (CM) C S4.8.12.11

    rxd_14 : str | None
        RXD.14 - Needs Human Review (ID) NA S4.8.12.12

    rxd_15 : CE | None
        RXD.15 - Pharmacy Special Dispensing Instructions (CE) NA S4.8.10.15
    """

    rxd_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxd_1",
            "dispense_sub_id_counter",
            "RXD.1",
        ),
        serialization_alias="RXD.1",
        title="Dispense Sub-ID Counter",
        description="NA | Item #00334 | LEN:4",
    )

    rxd_2: CE = Field(
        validation_alias=AliasChoices(
            "rxd_2",
            "dispense_give_code",
            "RXD.2",
        ),
        serialization_alias="RXD.2",
        title="Dispense / give code",
        description="R | Item #00335",
    )

    rxd_3: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxd_3",
            "date_time_dispensed",
            "RXD.3",
        ),
        serialization_alias="RXD.3",
        title="Date / time dispensed",
        description="NA | Item #00336",
    )

    rxd_4: str = Field(
        validation_alias=AliasChoices(
            "rxd_4",
            "actual_dispense_amount",
            "RXD.4",
        ),
        serialization_alias="RXD.4",
        title="Actual Dispense Amount",
        description="R | Item #00337 | LEN:20",
    )

    rxd_5: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxd_5",
            "actual_dispense_units",
            "RXD.5",
        ),
        serialization_alias="RXD.5",
        title="Actual Dispense Units",
        description="C | Item #00338",
    )

    rxd_6: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxd_6",
            "actual_dosage_form",
            "RXD.6",
        ),
        serialization_alias="RXD.6",
        title="Actual Dosage Form",
        description="NA | Item #00339",
    )

    rxd_7: str = Field(
        validation_alias=AliasChoices(
            "rxd_7",
            "prescription_number",
            "RXD.7",
        ),
        serialization_alias="RXD.7",
        title="Prescription Number",
        description="R | Item #00325 | LEN:20",
    )

    rxd_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxd_8",
            "number_of_refills_remaining",
            "RXD.8",
        ),
        serialization_alias="RXD.8",
        title="Number of Refills Remaining",
        description="C | Item #00326 | LEN:20",
    )

    rxd_9: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxd_9",
            "dispense_notes",
            "RXD.9",
        ),
        serialization_alias="RXD.9",
        title="Dispense Notes",
        description="C | Item #00340 | LEN:200",
    )

    rxd_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxd_10",
            "dispensing_provider",
            "RXD.10",
        ),
        serialization_alias="RXD.10",
        title="Dispensing Provider",
        description="NA | Item #00341",
    )

    rxd_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxd_11",
            "substitution_status",
            "RXD.11",
        ),
        serialization_alias="RXD.11",
        title="Substitution Status",
        description=(
            "NA | Item #00322 | Table 0167 - SUBSTITUTION STATUS | LEN:1"
        ),
    )

    rxd_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxd_12",
            "total_daily_dose",
            "RXD.12",
        ),
        serialization_alias="RXD.12",
        title="Total Daily Dose",
        description="NA | Item #00329",
    )

    rxd_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxd_13",
            "deliver_to_location",
            "RXD.13",
        ),
        serialization_alias="RXD.13",
        title="Deliver-to location",
        description="C | Item #00299",
    )

    rxd_14: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxd_14",
            "needs_human_review",
            "RXD.14",
        ),
        serialization_alias="RXD.14",
        title="Needs Human Review",
        description="NA | Item #00307 | LEN:1",
    )

    rxd_15: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxd_15",
            "pharmacy_special_dispensing_instructions",
            "RXD.15",
        ),
        serialization_alias="RXD.15",
        title="Pharmacy Special Dispensing Instructions",
        description="NA | Item #00330",
    )

    @field_validator("rxd_1", "rxd_4", "rxd_8", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
