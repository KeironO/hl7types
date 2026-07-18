"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: RXD
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.CQ import CQ
from ..datatypes.LA2 import LA2
from ..datatypes.TS import TS
from ..datatypes.XCN import XCN

_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class RXD(HL7Model):
    """RXD - pharmacy/treatment dispense segment (S4.8.10).

    Attributes
    ----------
    rxd_1 : str
        RXD.1 - Dispense Sub-ID Counter (NM) R S4.8.12.2

    rxd_2 : CE
        RXD.2 - Dispense/Give Code (CE) R S4.8.10.2 | 0292 - Vaccines administered

    rxd_3 : TS
        RXD.3 - Date/Time Dispensed (TS) R S4.8.10.3

    rxd_4 : str
        RXD.4 - Actual Dispense Amount (NM) R S4.8.10.4

    rxd_5 : CE | None
        RXD.5 - Actual Dispense Units (CE) C S4.8.10.5

    rxd_6 : CE | None
        RXD.6 - Actual Dosage Form (CE) O S4.8.10.6

    rxd_7 : str
        RXD.7 - Prescription Number (ST) R S4.8.10.7

    rxd_8 : str | None
        RXD.8 - Number of Refills Remaining (NM) C S4.8.10.8

    rxd_9 : list[str] | None
        RXD.9 - Dispense Notes (ST) O rep S4.8.10.9

    rxd_10 : list[XCN] | None
        RXD.10 - Dispensing Provider (XCN) O rep S4.8.10.10

    rxd_11 : str | None
        RXD.11 - Substitution Status (ID) O S4.8.12.10 | 0167 - Substitution status

    rxd_12 : CQ | None
        RXD.12 - Total Daily Dose (CQ) O S4.8.10.12

    rxd_13 : LA2 | None
        RXD.13 - Dispense-To Location (LA2) C S4.8.12.11

    rxd_14 : str | None
        RXD.14 - Needs Human Review (ID) O S4.8.12.12 | 0136 - Yes/no indicator

    rxd_15 : list[CE] | None
        RXD.15 - Pharmacy/Treatment Supplier’s Special Dispensing Instructions (CE) O rep S4.8.10.15

    rxd_16 : str | None
        RXD.16 - Actual Strength (NM) O S4.8.10.16

    rxd_17 : CE | None
        RXD.17 - Actual Strength Unit (CE) O S4.8.10.17

    rxd_18 : list[str] | None
        RXD.18 - Substance Lot Number (ST) O rep S4.8.14.15

    rxd_19 : list[TS] | None
        RXD.19 - Substance Expiration Date (TS) O rep S4.8.14.16

    rxd_20 : list[CE] | None
        RXD.20 - Substance Manufacturer Name (CE) O rep S4.8.14.17 | 0227 - Manufacturers of vaccines (code=MVX)

    rxd_21 : list[CE] | None
        RXD.21 - Indication (CE) O rep S4.8.14.19

    rxd_22 : str | None
        RXD.22 - Dispense Package Size (NM) O S4.8.10.22

    rxd_23 : CE | None
        RXD.23 - Dispense Package Size Unit (CE) O S4.8.10.23

    rxd_24 : str | None
        RXD.24 - Dispense Package Method (ID) O S4.8.10.24 | 0321 - Dispense method
    """

    rxd_1: str = Field(
        validation_alias=AliasChoices(
            "rxd_1",
            "dispense_sub_id_counter",
            "RXD.1",
        ),
        serialization_alias="RXD.1",
        title="Dispense Sub-ID Counter",
        description="R | Item #00334 | LEN:4",
    )

    rxd_2: CE = Field(
        validation_alias=AliasChoices(
            "rxd_2",
            "dispense_give_code",
            "RXD.2",
        ),
        serialization_alias="RXD.2",
        title="Dispense/Give Code",
        description="R | Item #00335 | Table 0292 - Vaccines administered",
    )

    rxd_3: TS = Field(
        validation_alias=AliasChoices(
            "rxd_3",
            "date_time_dispensed",
            "RXD.3",
        ),
        serialization_alias="RXD.3",
        title="Date/Time Dispensed",
        description="R | Item #00336",
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
        description="O | Item #00339",
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
        description="O | Item #00340 | LEN:200",
    )

    rxd_10: Optional[List[XCN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxd_10",
            "dispensing_provider",
            "RXD.10",
        ),
        serialization_alias="RXD.10",
        title="Dispensing Provider",
        description="O | Item #00341",
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
            "O | Item #00322 | Table 0167 - Substitution status | LEN:1"
        ),
    )

    rxd_12: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxd_12",
            "total_daily_dose",
            "RXD.12",
        ),
        serialization_alias="RXD.12",
        title="Total Daily Dose",
        description="O | Item #00329",
    )

    rxd_13: Optional[LA2] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxd_13",
            "dispense_to_location",
            "RXD.13",
        ),
        serialization_alias="RXD.13",
        title="Dispense-To Location",
        description="C | Item #01303",
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
        description="O | Item #00307 | Table 0136 - Yes/no indicator | LEN:1",
    )

    rxd_15: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxd_15",
            "pharmacy_treatment_supplier_s_special_dispensing_instructions",
            "RXD.15",
        ),
        serialization_alias="RXD.15",
        title="Pharmacy/Treatment Supplier’s Special Dispensing Instructions",
        description="O | Item #00330",
    )

    rxd_16: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxd_16",
            "actual_strength",
            "RXD.16",
        ),
        serialization_alias="RXD.16",
        title="Actual Strength",
        description="O | Item #01132 | LEN:20",
    )

    rxd_17: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxd_17",
            "actual_strength_unit",
            "RXD.17",
        ),
        serialization_alias="RXD.17",
        title="Actual Strength Unit",
        description="O | Item #01133",
    )

    rxd_18: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxd_18",
            "substance_lot_number",
            "RXD.18",
        ),
        serialization_alias="RXD.18",
        title="Substance Lot Number",
        description="O | Item #01129 | LEN:20",
    )

    rxd_19: Optional[List[TS]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxd_19",
            "substance_expiration_date",
            "RXD.19",
        ),
        serialization_alias="RXD.19",
        title="Substance Expiration Date",
        description="O | Item #01130",
    )

    rxd_20: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxd_20",
            "substance_manufacturer_name",
            "RXD.20",
        ),
        serialization_alias="RXD.20",
        title="Substance Manufacturer Name",
        description=(
            "O | Item #01131 | Table 0227 - Manufacturers of vaccines (code=MVX)"
        ),
    )

    rxd_21: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxd_21",
            "indication",
            "RXD.21",
        ),
        serialization_alias="RXD.21",
        title="Indication",
        description="O | Item #01123",
    )

    rxd_22: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxd_22",
            "dispense_package_size",
            "RXD.22",
        ),
        serialization_alias="RXD.22",
        title="Dispense Package Size",
        description="O | Item #01220 | LEN:20",
    )

    rxd_23: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxd_23",
            "dispense_package_size_unit",
            "RXD.23",
        ),
        serialization_alias="RXD.23",
        title="Dispense Package Size Unit",
        description="O | Item #01221",
    )

    rxd_24: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxd_24",
            "dispense_package_method",
            "RXD.24",
        ),
        serialization_alias="RXD.24",
        title="Dispense Package Method",
        description="O | Item #01222 | Table 0321 - Dispense method | LEN:2",
    )

    @field_validator("rxd_1", "rxd_4", "rxd_8", "rxd_16", "rxd_22", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
