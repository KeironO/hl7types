"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: RXG
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, ValidationInfo, field_validator
from hl7types.hl7 import HL7Model
from hl7types.hl7._validators import _apply_dt_fallback

from ..datatypes.CWE import CWE
from ..datatypes.LA2 import LA2
from ..datatypes.PL import PL
from ..datatypes.XAD import XAD

_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')
_RE_DTM = re.compile(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?')


class RXG(HL7Model):
    """Pharmacy/Treatment Give (S4.A.4.5).

    Attributes
    ----------
    rxg_1 : str
        RXG.1 - Give Sub-ID Counter (NM) R S4.A.4.5.1

    rxg_2 : str | None
        RXG.2 - Dispense Sub-ID Counter (NM) O S4.A.4.4.1

    rxg_4 : CWE
        RXG.4 - Give Code (CWE) R S4.A.4.3.2 | 0292 - Vaccines administered

    rxg_5 : str
        RXG.5 - Give Amount - Minimum (NM) R S4.A.4.3.3

    rxg_6 : str | None
        RXG.6 - Give Amount - Maximum (NM) O S4.A.4.3.4

    rxg_7 : CWE
        RXG.7 - Give Units (CWE) R S4.A.4.3.5 | 9999 - no table for CE

    rxg_8 : CWE | None
        RXG.8 - Give Dosage Form (CWE) O S4.A.4.3.6 | 9999 - no table for CE

    rxg_9 : list[CWE] | None
        RXG.9 - Administration Notes (CWE) O rep S4.A.4.5.9 | 9999 - no table for CE

    rxg_10 : str | None
        RXG.10 - Substitution Status (ID) O S4.A.4.3.9 | 0167 - Substitution Status

    rxg_11 : LA2 | None
        RXG.11 - Dispense-to Location (LA2) O S4.A.4.4.13

    rxg_12 : str | None
        RXG.12 - Needs Human Review (ID) O S4.A.4.0.16 | 0136 - Yes/no Indicator

    rxg_13 : list[CWE] | None
        RXG.13 - Pharmacy/Treatment Supplier's Special Administration Instructions (CWE) O rep S4.A.4.5.13 | 9999 - no table for CE

    rxg_14 : str | None
        RXG.14 - Give Per (Time Unit) (ST) C S4.A.4.3.22

    rxg_15 : str | None
        RXG.15 - Give Rate Amount (ST) O S4.A.4.3.23

    rxg_16 : CWE | None
        RXG.16 - Give Rate Units (CWE) O S4.A.4.3.24 | 9999 - no table for CE

    rxg_17 : str | None
        RXG.17 - Give Strength (NM) O S4.A.4.3.25

    rxg_18 : CWE | None
        RXG.18 - Give Strength Units (CWE) O S4.A.4.3.26 | 9999 - no table for CE

    rxg_19 : list[str] | None
        RXG.19 - Substance Lot Number (ST) O rep S13.4.11.2

    rxg_20 : list[str] | None
        RXG.20 - Substance Expiration Date (DTM) O rep S4.A.4.4.19

    rxg_21 : list[CWE] | None
        RXG.21 - Substance Manufacturer Name (CWE) O rep S4.A.4.4.20 | 0227 - Manufacturers of Vaccines (code=MVX)

    rxg_22 : list[CWE] | None
        RXG.22 - Indication (CWE) O rep S4.A.4.0.20 | 9999 - no table for CE

    rxg_23 : str | None
        RXG.23 - Give Drug Strength Volume (NM) O S4.A.4.5.23

    rxg_24 : CWE | None
        RXG.24 - Give Drug Strength Volume Units (CWE) O S4.A.4.5.24 | 9999 - no table for CE

    rxg_25 : CWE | None
        RXG.25 - Give Barcode Identifier (CWE) O S4.A.4.5.25 | 9999 - no table for CE

    rxg_26 : str | None
        RXG.26 - Pharmacy Order Type (ID) O S4.A.4.5.26 | 0480 - Pharmacy Order Types

    rxg_27 : CWE | None
        RXG.27 - Dispense to Pharmacy (CWE) O S4.A.4.4.30 | 9999 - no table for CE

    rxg_28 : XAD | None
        RXG.28 - Dispense to Pharmacy Address (XAD) O S4.A.4.4.31

    rxg_29 : PL | None
        RXG.29 - Deliver-to Patient Location (PL) O S4.A.4.0.34

    rxg_30 : XAD | None
        RXG.30 - Deliver-to Address (XAD) O S4.A.4.0.35
    """

    rxg_1: str = Field(
        validation_alias=AliasChoices(
            "rxg_1",
            "give_sub_id_counter",
            "RXG.1",
        ),
        serialization_alias="RXG.1",
        title="Give Sub-ID Counter",
        description="R | Item #00342",
    )

    rxg_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxg_2",
            "dispense_sub_id_counter",
            "RXG.2",
        ),
        serialization_alias="RXG.2",
        title="Dispense Sub-ID Counter",
        description="O | Item #00334",
    )

    rxg_4: CWE = Field(
        validation_alias=AliasChoices(
            "rxg_4",
            "give_code",
            "RXG.4",
        ),
        serialization_alias="RXG.4",
        title="Give Code",
        description="R | Item #00317 | Table 0292 - Vaccines administered",
    )

    rxg_5: str = Field(
        validation_alias=AliasChoices(
            "rxg_5",
            "give_amount_minimum",
            "RXG.5",
        ),
        serialization_alias="RXG.5",
        title="Give Amount - Minimum",
        description="R | Item #00318",
    )

    rxg_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxg_6",
            "give_amount_maximum",
            "RXG.6",
        ),
        serialization_alias="RXG.6",
        title="Give Amount - Maximum",
        description="O | Item #00319",
    )

    rxg_7: CWE = Field(
        validation_alias=AliasChoices(
            "rxg_7",
            "give_units",
            "RXG.7",
        ),
        serialization_alias="RXG.7",
        title="Give Units",
        description="R | Item #00320 | Table 9999 - no table for CE",
    )

    rxg_8: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxg_8",
            "give_dosage_form",
            "RXG.8",
        ),
        serialization_alias="RXG.8",
        title="Give Dosage Form",
        description="O | Item #00321 | Table 9999 - no table for CE",
    )

    rxg_9: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxg_9",
            "administration_notes",
            "RXG.9",
        ),
        serialization_alias="RXG.9",
        title="Administration Notes",
        description="O | Item #00351 | Table 9999 - no table for CE",
    )

    rxg_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxg_10",
            "substitution_status",
            "RXG.10",
        ),
        serialization_alias="RXG.10",
        title="Substitution Status",
        description=(
            "O | Item #00322 | Table 0167 - Substitution Status | LEN:1"
        ),
    )

    rxg_11: Optional[LA2] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxg_11",
            "dispense_to_location",
            "RXG.11",
        ),
        serialization_alias="RXG.11",
        title="Dispense-to Location",
        description="O | Item #01303",
    )

    rxg_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxg_12",
            "needs_human_review",
            "RXG.12",
        ),
        serialization_alias="RXG.12",
        title="Needs Human Review",
        description="O | Item #00307 | Table 0136 - Yes/no Indicator | LEN:1",
    )

    rxg_13: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxg_13",
            "pharmacy_treatment_supplier_s_special_administration_instructions",
            "RXG.13",
        ),
        serialization_alias="RXG.13",
        title=(
            "Pharmacy/Treatment Supplier's Special Administration Instructions"
        ),
        description="O | Item #00343 | Table 9999 - no table for CE",
    )

    rxg_14: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxg_14",
            "give_per_time_unit",
            "RXG.14",
        ),
        serialization_alias="RXG.14",
        title="Give Per (Time Unit)",
        description="C | Item #00331",
    )

    rxg_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxg_15",
            "give_rate_amount",
            "RXG.15",
        ),
        serialization_alias="RXG.15",
        title="Give Rate Amount",
        description="O | Item #00332",
    )

    rxg_16: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxg_16",
            "give_rate_units",
            "RXG.16",
        ),
        serialization_alias="RXG.16",
        title="Give Rate Units",
        description="O | Item #00333 | Table 9999 - no table for CE",
    )

    rxg_17: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxg_17",
            "give_strength",
            "RXG.17",
        ),
        serialization_alias="RXG.17",
        title="Give Strength",
        description="O | Item #01126",
    )

    rxg_18: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxg_18",
            "give_strength_units",
            "RXG.18",
        ),
        serialization_alias="RXG.18",
        title="Give Strength Units",
        description="O | Item #01127 | Table 9999 - no table for CE",
    )

    rxg_19: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxg_19",
            "substance_lot_number",
            "RXG.19",
        ),
        serialization_alias="RXG.19",
        title="Substance Lot Number",
        description="O | Item #01129",
    )

    rxg_20: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxg_20",
            "substance_expiration_date",
            "RXG.20",
        ),
        serialization_alias="RXG.20",
        title="Substance Expiration Date",
        description="O | Item #01130",
    )

    rxg_21: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxg_21",
            "substance_manufacturer_name",
            "RXG.21",
        ),
        serialization_alias="RXG.21",
        title="Substance Manufacturer Name",
        description=(
            "O | Item #01131 | Table 0227 - Manufacturers of Vaccines (code=MVX)"
        ),
    )

    rxg_22: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxg_22",
            "indication",
            "RXG.22",
        ),
        serialization_alias="RXG.22",
        title="Indication",
        description="O | Item #01123 | Table 9999 - no table for CE",
    )

    rxg_23: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxg_23",
            "give_drug_strength_volume",
            "RXG.23",
        ),
        serialization_alias="RXG.23",
        title="Give Drug Strength Volume",
        description="O | Item #01692",
    )

    rxg_24: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxg_24",
            "give_drug_strength_volume_units",
            "RXG.24",
        ),
        serialization_alias="RXG.24",
        title="Give Drug Strength Volume Units",
        description="O | Item #01693 | Table 9999 - no table for CE",
    )

    rxg_25: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxg_25",
            "give_barcode_identifier",
            "RXG.25",
        ),
        serialization_alias="RXG.25",
        title="Give Barcode Identifier",
        description="O | Item #01694 | Table 9999 - no table for CE",
    )

    rxg_26: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxg_26",
            "pharmacy_order_type",
            "RXG.26",
        ),
        serialization_alias="RXG.26",
        title="Pharmacy Order Type",
        description=(
            "O | Item #01695 | Table 0480 - Pharmacy Order Types | LEN:1"
        ),
    )

    rxg_27: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxg_27",
            "dispense_to_pharmacy",
            "RXG.27",
        ),
        serialization_alias="RXG.27",
        title="Dispense to Pharmacy",
        description="O | Item #01688 | Table 9999 - no table for CE",
    )

    rxg_28: Optional[XAD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxg_28",
            "dispense_to_pharmacy_address",
            "RXG.28",
        ),
        serialization_alias="RXG.28",
        title="Dispense to Pharmacy Address",
        description="O | Item #01689",
    )

    rxg_29: Optional[PL] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxg_29",
            "deliver_to_patient_location",
            "RXG.29",
        ),
        serialization_alias="RXG.29",
        title="Deliver-to Patient Location",
        description="O | Item #01683",
    )

    rxg_30: Optional[XAD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxg_30",
            "deliver_to_address",
            "RXG.30",
        ),
        serialization_alias="RXG.30",
        title="Deliver-to Address",
        description="O | Item #01684",
    )

    @field_validator("rxg_1", "rxg_2", "rxg_5", "rxg_6", "rxg_17", "rxg_23", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    @field_validator("rxg_20", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        if _RE_DTM.fullmatch(v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = ConfigDict(populate_by_name=True)
