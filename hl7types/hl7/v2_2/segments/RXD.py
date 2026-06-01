"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: RXD
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator

from ..datatypes.CE import CE
from ..datatypes.TS import TS


class RXD(HL7Model):
    """HL7 v2 RXD segment.

    Attributes
    ----------
    rxd_1 : str | None
        RXD.1 (opt) - Dispense Sub-ID Counter (NM)

    rxd_2 : CE
        RXD.2 (req) - Dispense / give code (CE)

    rxd_3 : TS | None
        RXD.3 (opt) - Date / time dispensed (TS)

    rxd_4 : str
        RXD.4 (req) - Actual Dispense Amount (NM)

    rxd_5 : CE | None
        RXD.5 (opt) - Actual Dispense Units (CE)

    rxd_6 : CE | None
        RXD.6 (opt) - Actual Dosage Form (CE)

    rxd_7 : str
        RXD.7 (req) - Prescription Number (ST)

    rxd_8 : str | None
        RXD.8 (opt) - Number of Refills Remaining (NM)

    rxd_9 : list[str] | None
        RXD.9 (opt, rep) - Dispense Notes (ST)

    rxd_10 : str | None
        RXD.10 (opt) - Dispensing Provider (CN)

    rxd_11 : str | None
        RXD.11 (opt) - Substitution Status (ID)

    rxd_12 : str | None
        RXD.12 (opt) - Total Daily Dose (CQ)

    rxd_13 : str | None
        RXD.13 (opt) - Deliver-to location (CM)

    rxd_14 : str | None
        RXD.14 (opt) - Needs Human Review (ID)

    rxd_15 : CE | None
        RXD.15 (opt) - Pharmacy Special Dispensing Instructions (CE)
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
        description="Item #334",
    )

    rxd_2: CE = Field(
        default=...,
        validation_alias=AliasChoices(
            "rxd_2",
            "dispense_give_code",
            "RXD.2",
        ),
        serialization_alias="RXD.2",
        title="Dispense / give code",
        description="Item #335",
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
        description="Item #336",
    )

    rxd_4: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "rxd_4",
            "actual_dispense_amount",
            "RXD.4",
        ),
        serialization_alias="RXD.4",
        title="Actual Dispense Amount",
        description="Item #337",
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
        description="Item #338",
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
        description="Item #339",
    )

    rxd_7: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "rxd_7",
            "prescription_number",
            "RXD.7",
        ),
        serialization_alias="RXD.7",
        title="Prescription Number",
        description="Item #325",
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
        description="Item #326",
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
        description="Item #340",
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
        description="Item #341",
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
        description="Item #322 | Table HL70167",
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
        description="Item #329",
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
        description="Item #299",
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
        description="Item #307",
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
        description="Item #330",
    )

    @field_validator("rxd_1", "rxd_4", "rxd_8", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
