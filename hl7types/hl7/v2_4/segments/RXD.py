"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RXD
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator

from ..datatypes.CE import CE
from ..datatypes.CQ import CQ
from ..datatypes.LA2 import LA2
from ..datatypes.TS import TS
from ..datatypes.XCN import XCN


class RXD(HL7Model):
    """HL7 v2 RXD segment.

    Attributes
    ----------
    rxd_1 : str
        RXD.1 (req) - Dispense Sub-ID Counter (NM)

    rxd_2 : CE
        RXD.2 (req) - Dispense/Give Code (CE)

    rxd_3 : TS
        RXD.3 (req) - Date/Time Dispensed (TS)

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

    rxd_10 : list[XCN] | None
        RXD.10 (opt, rep) - Dispensing Provider (XCN)

    rxd_11 : str | None
        RXD.11 (opt) - Substitution Status (ID)

    rxd_12 : CQ | None
        RXD.12 (opt) - Total Daily Dose (CQ)

    rxd_13 : LA2 | None
        RXD.13 (opt) - Dispense-To Location (LA2)

    rxd_14 : str | None
        RXD.14 (opt) - Needs Human Review (ID)

    rxd_15 : list[CE] | None
        RXD.15 (opt, rep) - Pharmacy/Treatment Supplier's Special Dispensing Instructions (CE)

    rxd_16 : str | None
        RXD.16 (opt) - Actual Strength (NM)

    rxd_17 : CE | None
        RXD.17 (opt) - Actual Strength Unit (CE)

    rxd_18 : list[str] | None
        RXD.18 (opt, rep) - Substance Lot Number (ST)

    rxd_19 : list[TS] | None
        RXD.19 (opt, rep) - Substance Expiration Date (TS)

    rxd_20 : list[CE] | None
        RXD.20 (opt, rep) - Substance Manufacturer Name (CE)

    rxd_21 : list[CE] | None
        RXD.21 (opt, rep) - Indication (CE)

    rxd_22 : str | None
        RXD.22 (opt) - Dispense Package Size (NM)

    rxd_23 : CE | None
        RXD.23 (opt) - Dispense Package Size Unit (CE)

    rxd_24 : str | None
        RXD.24 (opt) - Dispense Package Method (ID)

    rxd_25 : list[CE] | None
        RXD.25 (opt, rep) - Supplementary Code (CE)

    rxd_26 : CE | None
        RXD.26 (opt) - Initiating Location (CE)

    rxd_27 : CE | None
        RXD.27 (opt) - Packaging/Assembly Location (CE)
    """

    rxd_1: str = Field(
        default=...,
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
        title="Dispense/Give Code",
        description="Item #335 | Table HL70292",
    )

    rxd_3: TS = Field(
        default=...,
        validation_alias=AliasChoices(
            "rxd_3",
            "date_time_dispensed",
            "RXD.3",
        ),
        serialization_alias="RXD.3",
        title="Date/Time Dispensed",
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

    rxd_10: Optional[List[XCN]] = Field(
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

    rxd_12: Optional[CQ] = Field(
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

    rxd_13: Optional[LA2] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxd_13",
            "dispense_to_location",
            "RXD.13",
        ),
        serialization_alias="RXD.13",
        title="Dispense-To Location",
        description="Item #1303",
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
        description="Item #307 | Table HL70136",
    )

    rxd_15: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxd_15",
            "pharmacy_treatment_supplier_s_special_dispensing_instructions",
            "RXD.15",
        ),
        serialization_alias="RXD.15",
        title="Pharmacy/Treatment Supplier's Special Dispensing Instructions",
        description="Item #330",
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
        description="Item #1132",
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
        description="Item #1133",
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
        description="Item #1129",
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
        description="Item #1130",
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
        description="Item #1131 | Table HL70227",
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
        description="Item #1123",
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
        description="Item #1220",
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
        description="Item #1221",
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
        description="Item #1222 | Table HL70321",
    )

    rxd_25: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxd_25",
            "supplementary_code",
            "RXD.25",
        ),
        serialization_alias="RXD.25",
        title="Supplementary Code",
        description="Item #1476",
    )

    rxd_26: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxd_26",
            "initiating_location",
            "RXD.26",
        ),
        serialization_alias="RXD.26",
        title="Initiating Location",
        description="Item #1477",
    )

    rxd_27: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxd_27",
            "packaging_assembly_location",
            "RXD.27",
        ),
        serialization_alias="RXD.27",
        title="Packaging/Assembly Location",
        description="Item #1478",
    )

    @field_validator("rxd_1", "rxd_4", "rxd_8", "rxd_16", "rxd_22", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
