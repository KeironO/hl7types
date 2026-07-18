"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: RXD
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, ValidationInfo, field_validator
from hl7types.hl7 import HL7Model
from hl7types.hl7._validators import _apply_dt_fallback

from ..datatypes.CQ import CQ
from ..datatypes.CWE import CWE
from ..datatypes.EI import EI
from ..datatypes.XAD import XAD
from ..datatypes.XCN import XCN
from ..datatypes.XTN import XTN

_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')
_RE_DTM = re.compile(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?')


class RXD(HL7Model):
    """Pharmacy/Treatment Dispense (S4.A.5).

    Attributes
    ----------
    rxd_1 : str
        RXD.1 - Dispense Sub-ID Counter (NM) R S4.A.5.1

    rxd_2 : CWE
        RXD.2 - Dispense/Give Code (CWE) R S4.A.5.2 | 0292 - Vaccines administered

    rxd_3 : str
        RXD.3 - Date/Time Dispensed (DTM) R S4.A.5.3

    rxd_4 : str
        RXD.4 - Actual Dispense Amount (NM) R S4.A.5.4

    rxd_5 : CWE | None
        RXD.5 - Actual Dispense Units (CWE) C S4.A.5.5 | 9999 - no table for CE

    rxd_6 : CWE | None
        RXD.6 - Actual Dosage Form (CWE) O S4.A.5.6 | 9999 - no table for CE

    rxd_7 : str
        RXD.7 - Prescription Number (ST) R S4.A.4.15

    rxd_8 : str | None
        RXD.8 - Number of Refills Remaining (NM) C S4.A.4.16

    rxd_9 : list[str] | None
        RXD.9 - Dispense Notes (ST) O rep S4.A.5.9

    rxd_10 : list[XCN] | None
        RXD.10 - Dispensing Provider (XCN) O rep S4.A.5.10

    rxd_11 : str | None
        RXD.11 - Substitution Status (ID) O S4.A.4.9 | 0167 - Substitution Status

    rxd_12 : CQ | None
        RXD.12 - Total Daily Dose (CQ) O S4.A.1.23

    rxd_14 : str | None
        RXD.14 - Needs Human Review (ID) O S4.A.1.16 | 0136 - Yes/no Indicator

    rxd_15 : list[CWE] | None
        RXD.15 - Special Dispensing Instructions (CWE) O rep S4.A.4.21 | 9999 - no table for CE

    rxd_16 : str | None
        RXD.16 - Actual Strength (NM) O S4.A.5.16

    rxd_17 : CWE | None
        RXD.17 - Actual Strength Unit (CWE) O S4.A.5.17 | 9999 - no table for CE

    rxd_18 : list[str] | None
        RXD.18 - Substance Lot Number (ST) O rep S13.4.11.2

    rxd_19 : list[str] | None
        RXD.19 - Substance Expiration Date (DTM) O rep S4.A.1.16

    rxd_20 : list[CWE] | None
        RXD.20 - Substance Manufacturer Name (CWE) O rep S4.A.5.20

    rxd_21 : list[CWE] | None
        RXD.21 - Indication (CWE) O rep S4.A.1.19 | 9999 - no table for CE

    rxd_22 : str | None
        RXD.22 - Dispense Package Size (NM) O S4.A.4.28

    rxd_23 : CWE | None
        RXD.23 - Dispense Package Size Unit (CWE) O S4.A.4.29 | 9999 - no table for CE

    rxd_24 : str | None
        RXD.24 - Dispense Package Method (ID) O S4.A.4.30 | 0321 - Dispense Method

    rxd_25 : list[CWE] | None
        RXD.25 - Supplementary Code (CWE) O rep S4.A.1.24 | 9999 - no table for CE

    rxd_26 : CWE | None
        RXD.26 - Initiating Location (CWE) O S4.A.5.26 | 9999 - no table for CE

    rxd_27 : CWE | None
        RXD.27 - Packaging/Assembly Location (CWE) O S4.A.5.27 | 9999 - no table for CE

    rxd_28 : str | None
        RXD.28 - Actual Drug Strength Volume (NM) O S4.A.5.28

    rxd_29 : CWE | None
        RXD.29 - Actual Drug Strength Volume Units (CWE) O S4.A.5.29 | 9999 - no table for CE

    rxd_30 : CWE | None
        RXD.30 - Dispense to Pharmacy (CWE) O S4.A.5.30 | 9999 - no table for CE

    rxd_31 : XAD | None
        RXD.31 - Dispense to Pharmacy Address (XAD) O S4.A.5.31

    rxd_32 : str | None
        RXD.32 - Pharmacy Order Type (ID) O S4.A.5.32 | 0480 - Pharmacy Order Types

    rxd_33 : CWE | None
        RXD.33 - Dispense Type (CWE) O S4.A.5.33 | 0484 - Dispense Type

    rxd_34 : list[XTN] | None
        RXD.34 - Pharmacy Phone Number (XTN) O rep S4.A.5.34

    rxd_35 : list[EI] | None
        RXD.35 - Dispense Tag Identifier (EI) O rep S4.A.5.35
    """

    rxd_1: str = Field(
        validation_alias=AliasChoices(
            "rxd_1",
            "dispense_sub_id_counter",
            "RXD.1",
        ),
        serialization_alias="RXD.1",
        title="Dispense Sub-ID Counter",
        description="R | Item #00334",
    )

    rxd_2: CWE = Field(
        validation_alias=AliasChoices(
            "rxd_2",
            "dispense_give_code",
            "RXD.2",
        ),
        serialization_alias="RXD.2",
        title="Dispense/Give Code",
        description="R | Item #00335 | Table 0292 - Vaccines administered",
    )

    rxd_3: str = Field(
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
        description="R | Item #00337",
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
        description="C | Item #00338 | Table 9999 - no table for CE",
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
        description="O | Item #00339 | Table 9999 - no table for CE",
    )

    rxd_7: str = Field(
        validation_alias=AliasChoices(
            "rxd_7",
            "prescription_number",
            "RXD.7",
        ),
        serialization_alias="RXD.7",
        title="Prescription Number",
        description="R | Item #00325",
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
        description="C | Item #00326",
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
        description="O | Item #00340",
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
            "O | Item #00322 | Table 0167 - Substitution Status | LEN:1"
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

    rxd_14: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxd_14",
            "needs_human_review",
            "RXD.14",
        ),
        serialization_alias="RXD.14",
        title="Needs Human Review",
        description="O | Item #00307 | Table 0136 - Yes/no Indicator | LEN:1",
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
        description="O | Item #00330 | Table 9999 - no table for CE",
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
        description="O | Item #01132",
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
        description="O | Item #01133 | Table 9999 - no table for CE",
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
        description="O | Item #01129",
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
        description="O | Item #01130",
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
        description="O | Item #01131",
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
        description="O | Item #01123 | Table 9999 - no table for CE",
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
        description="O | Item #01220",
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
        description="O | Item #01221 | Table 9999 - no table for CE",
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
        description="O | Item #01222 | Table 0321 - Dispense Method | LEN:2",
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
        description="O | Item #01476 | Table 9999 - no table for CE",
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
        description="O | Item #01477 | Table 9999 - no table for CE",
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
        description="O | Item #01478 | Table 9999 - no table for CE",
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
        description="O | Item #01686",
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
        description="O | Item #01687 | Table 9999 - no table for CE",
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
        description="O | Item #01688 | Table 9999 - no table for CE",
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
        description="O | Item #01689",
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
        description=(
            "O | Item #01690 | Table 0480 - Pharmacy Order Types | LEN:1"
        ),
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
        description="O | Item #01691 | Table 0484 - Dispense Type",
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
        description="O | Item #02311",
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
        description="O | Item #03392",
    )

    @field_validator("rxd_1", "rxd_4", "rxd_8", "rxd_16", "rxd_22", "rxd_28", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    @field_validator("rxd_3", "rxd_19", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        if _RE_DTM.fullmatch(v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = ConfigDict(populate_by_name=True)
