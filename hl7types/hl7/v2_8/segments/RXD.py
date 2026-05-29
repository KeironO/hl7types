"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: RXD
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CQ import CQ
from ..datatypes.CWE import CWE
from ..datatypes.EI import EI
from ..datatypes.XAD import XAD
from ..datatypes.XCN import XCN
from ..datatypes.XTN import XTN


class RXD(BaseModel):
    """HL7 v2 RXD segment.

    Attributes
    ----------
    rxd_1 : str
        RXD.1 (req) - Dispense Sub-ID Counter (NM)

    rxd_2 : CWE
        RXD.2 (req) - Dispense/Give Code (CWE)

    rxd_3 : str
        RXD.3 (req) - Date/Time Dispensed (DTM)

    rxd_4 : str
        RXD.4 (req) - Actual Dispense Amount (NM)

    rxd_5 : CWE | None
        RXD.5 (opt) - Actual Dispense Units (CWE)

    rxd_6 : CWE | None
        RXD.6 (opt) - Actual Dosage Form (CWE)

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

    rxd_14 : str | None
        RXD.14 (opt) - Needs Human Review (ID)

    rxd_15 : list[CWE] | None
        RXD.15 (opt, rep) - Special Dispensing Instructions (CWE)

    rxd_16 : str | None
        RXD.16 (opt) - Actual Strength (NM)

    rxd_17 : CWE | None
        RXD.17 (opt) - Actual Strength Unit (CWE)

    rxd_18 : list[str] | None
        RXD.18 (opt, rep) - Substance Lot Number (ST)

    rxd_19 : list[str] | None
        RXD.19 (opt, rep) - Substance Expiration Date (DTM)

    rxd_20 : list[CWE] | None
        RXD.20 (opt, rep) - Substance Manufacturer Name (CWE)

    rxd_21 : list[CWE] | None
        RXD.21 (opt, rep) - Indication (CWE)

    rxd_22 : str | None
        RXD.22 (opt) - Dispense Package Size (NM)

    rxd_23 : CWE | None
        RXD.23 (opt) - Dispense Package Size Unit (CWE)

    rxd_24 : str | None
        RXD.24 (opt) - Dispense Package Method (ID)

    rxd_25 : list[CWE] | None
        RXD.25 (opt, rep) - Supplementary Code (CWE)

    rxd_26 : CWE | None
        RXD.26 (opt) - Initiating Location (CWE)

    rxd_27 : CWE | None
        RXD.27 (opt) - Packaging/Assembly Location (CWE)

    rxd_28 : str | None
        RXD.28 (opt) - Actual Drug Strength Volume (NM)

    rxd_29 : CWE | None
        RXD.29 (opt) - Actual Drug Strength Volume Units (CWE)

    rxd_30 : CWE | None
        RXD.30 (opt) - Dispense to Pharmacy (CWE)

    rxd_31 : XAD | None
        RXD.31 (opt) - Dispense to Pharmacy Address (XAD)

    rxd_32 : str | None
        RXD.32 (opt) - Pharmacy Order Type (ID)

    rxd_33 : CWE | None
        RXD.33 (opt) - Dispense Type (CWE)

    rxd_34 : list[XTN] | None
        RXD.34 (opt, rep) - Pharmacy Phone Number (XTN)

    rxd_35 : list[EI] | None
        RXD.35 (opt, rep) - Dispense Tag Identifier (EI)
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

    rxd_2: CWE = Field(
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

    rxd_3: str = Field(
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

    rxd_5: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxd_5",
            "actual_dispense_units",
            "RXD.5",
        ),
        serialization_alias="RXD.5",
        title="Actual Dispense Units",
        description="Item #338 | Table HL79999",
    )

    rxd_6: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxd_6",
            "actual_dosage_form",
            "RXD.6",
        ),
        serialization_alias="RXD.6",
        title="Actual Dosage Form",
        description="Item #339 | Table HL79999",
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

    rxd_15: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxd_15",
            "special_dispensing_instructions",
            "RXD.15",
        ),
        serialization_alias="RXD.15",
        title="Special Dispensing Instructions",
        description="Item #330 | Table HL79999",
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

    rxd_17: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxd_17",
            "actual_strength_unit",
            "RXD.17",
        ),
        serialization_alias="RXD.17",
        title="Actual Strength Unit",
        description="Item #1133 | Table HL79999",
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

    rxd_19: Optional[List[str]] = Field(
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

    rxd_20: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxd_20",
            "substance_manufacturer_name",
            "RXD.20",
        ),
        serialization_alias="RXD.20",
        title="Substance Manufacturer Name",
        description="Item #1131",
    )

    rxd_21: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxd_21",
            "indication",
            "RXD.21",
        ),
        serialization_alias="RXD.21",
        title="Indication",
        description="Item #1123 | Table HL79999",
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

    rxd_23: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxd_23",
            "dispense_package_size_unit",
            "RXD.23",
        ),
        serialization_alias="RXD.23",
        title="Dispense Package Size Unit",
        description="Item #1221 | Table HL79999",
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

    rxd_25: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxd_25",
            "supplementary_code",
            "RXD.25",
        ),
        serialization_alias="RXD.25",
        title="Supplementary Code",
        description="Item #1476 | Table HL79999",
    )

    rxd_26: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxd_26",
            "initiating_location",
            "RXD.26",
        ),
        serialization_alias="RXD.26",
        title="Initiating Location",
        description="Item #1477 | Table HL79999",
    )

    rxd_27: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxd_27",
            "packaging_assembly_location",
            "RXD.27",
        ),
        serialization_alias="RXD.27",
        title="Packaging/Assembly Location",
        description="Item #1478 | Table HL79999",
    )

    rxd_28: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxd_28",
            "actual_drug_strength_volume",
            "RXD.28",
        ),
        serialization_alias="RXD.28",
        title="Actual Drug Strength Volume",
        description="Item #1686",
    )

    rxd_29: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxd_29",
            "actual_drug_strength_volume_units",
            "RXD.29",
        ),
        serialization_alias="RXD.29",
        title="Actual Drug Strength Volume Units",
        description="Item #1687 | Table HL79999",
    )

    rxd_30: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxd_30",
            "dispense_to_pharmacy",
            "RXD.30",
        ),
        serialization_alias="RXD.30",
        title="Dispense to Pharmacy",
        description="Item #1688 | Table HL79999",
    )

    rxd_31: Optional[XAD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxd_31",
            "dispense_to_pharmacy_address",
            "RXD.31",
        ),
        serialization_alias="RXD.31",
        title="Dispense to Pharmacy Address",
        description="Item #1689",
    )

    rxd_32: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxd_32",
            "pharmacy_order_type",
            "RXD.32",
        ),
        serialization_alias="RXD.32",
        title="Pharmacy Order Type",
        description="Item #1690 | Table HL70480",
    )

    rxd_33: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxd_33",
            "dispense_type",
            "RXD.33",
        ),
        serialization_alias="RXD.33",
        title="Dispense Type",
        description="Item #1691 | Table HL70484",
    )

    rxd_34: Optional[List[XTN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxd_34",
            "pharmacy_phone_number",
            "RXD.34",
        ),
        serialization_alias="RXD.34",
        title="Pharmacy Phone Number",
        description="Item #2311",
    )

    rxd_35: Optional[List[EI]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxd_35",
            "dispense_tag_identifier",
            "RXD.35",
        ),
        serialization_alias="RXD.35",
        title="Dispense Tag Identifier",
        description="Item #3392",
    )

    model_config = {"populate_by_name": True}
