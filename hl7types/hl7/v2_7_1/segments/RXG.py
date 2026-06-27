"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: RXG
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE
from ..datatypes.LA2 import LA2
from ..datatypes.PL import PL
from ..datatypes.XAD import XAD


class RXG(HL7Model):
    """HL7 v2 RXG segment.

    Attributes
    ----------
    rxg_1 : str
        RXG.1 (req) - Give Sub-ID Counter (NM)

    rxg_2 : str | None
        RXG.2 (opt) - Dispense Sub-ID Counter (NM)

    rxg_4 : CWE
        RXG.4 (req) - Give Code (CWE)

    rxg_5 : str
        RXG.5 (req) - Give Amount - Minimum (NM)

    rxg_6 : str | None
        RXG.6 (opt) - Give Amount - Maximum (NM)

    rxg_7 : CWE
        RXG.7 (req) - Give Units (CWE)

    rxg_8 : CWE | None
        RXG.8 (opt) - Give Dosage Form (CWE)

    rxg_9 : list[CWE] | None
        RXG.9 (opt, rep) - Administration Notes (CWE)

    rxg_10 : str | None
        RXG.10 (opt) - Substitution Status (ID)

    rxg_11 : LA2 | None
        RXG.11 (opt) - Dispense-to Location (LA2)

    rxg_12 : str | None
        RXG.12 (opt) - Needs Human Review (ID)

    rxg_13 : list[CWE] | None
        RXG.13 (opt, rep) - Pharmacy/Treatment Supplier's Special Administration Instructions (CWE)

    rxg_14 : str | None
        RXG.14 (opt) - Give Per (Time Unit) (ST)

    rxg_15 : str | None
        RXG.15 (opt) - Give Rate Amount (ST)

    rxg_16 : CWE | None
        RXG.16 (opt) - Give Rate Units (CWE)

    rxg_17 : str | None
        RXG.17 (opt) - Give Strength (NM)

    rxg_18 : CWE | None
        RXG.18 (opt) - Give Strength Units (CWE)

    rxg_19 : list[str] | None
        RXG.19 (opt, rep) - Substance Lot Number (ST)

    rxg_20 : list[str] | None
        RXG.20 (opt, rep) - Substance Expiration Date (DTM)

    rxg_21 : list[CWE] | None
        RXG.21 (opt, rep) - Substance Manufacturer Name (CWE)

    rxg_22 : list[CWE] | None
        RXG.22 (opt, rep) - Indication (CWE)

    rxg_23 : str | None
        RXG.23 (opt) - Give Drug Strength Volume (NM)

    rxg_24 : CWE | None
        RXG.24 (opt) - Give Drug Strength Volume Units (CWE)

    rxg_25 : CWE | None
        RXG.25 (opt) - Give Barcode Identifier (CWE)

    rxg_26 : str | None
        RXG.26 (opt) - Pharmacy Order Type (ID)

    rxg_27 : CWE | None
        RXG.27 (opt) - Dispense to Pharmacy (CWE)

    rxg_28 : XAD | None
        RXG.28 (opt) - Dispense to Pharmacy Address (XAD)

    rxg_29 : PL | None
        RXG.29 (opt) - Deliver-to Patient Location (PL)

    rxg_30 : XAD | None
        RXG.30 (opt) - Deliver-to Address (XAD)
    """

    rxg_1: str = Field(
        validation_alias=AliasChoices(
            "rxg_1",
            "give_sub_id_counter",
            "RXG.1",
        ),
        serialization_alias="RXG.1",
        title="Give Sub-ID Counter",
        description="Item #342",
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
        description="Item #334",
    )

    rxg_4: CWE = Field(
        validation_alias=AliasChoices(
            "rxg_4",
            "give_code",
            "RXG.4",
        ),
        serialization_alias="RXG.4",
        title="Give Code",
        description="Item #317 | Table HL70292",
    )

    rxg_5: str = Field(
        validation_alias=AliasChoices(
            "rxg_5",
            "give_amount_minimum",
            "RXG.5",
        ),
        serialization_alias="RXG.5",
        title="Give Amount - Minimum",
        description="Item #318",
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
        description="Item #319",
    )

    rxg_7: CWE = Field(
        validation_alias=AliasChoices(
            "rxg_7",
            "give_units",
            "RXG.7",
        ),
        serialization_alias="RXG.7",
        title="Give Units",
        description="Item #320 | Table HL79999",
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
        description="Item #321 | Table HL79999",
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
        description="Item #351 | Table HL79999",
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
        description="Item #322 | Table HL70167",
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
        description="Item #1303",
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
        description="Item #307 | Table HL70136",
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
        description="Item #343 | Table HL79999",
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
        description="Item #331",
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
        description="Item #332",
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
        description="Item #333 | Table HL79999",
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
        description="Item #1126",
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
        description="Item #1127 | Table HL79999",
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
        description="Item #1129",
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
        description="Item #1130",
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
        description="Item #1131 | Table HL70227",
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
        description="Item #1123 | Table HL79999",
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
        description="Item #1692",
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
        description="Item #1693 | Table HL79999",
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
        description="Item #1694 | Table HL79999",
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
        description="Item #1695 | Table HL70480",
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
        description="Item #1688 | Table HL79999",
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
        description="Item #1689",
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
        description="Item #1683",
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
        description="Item #1684",
    )

    @field_validator("rxg_1", "rxg_2", "rxg_5", "rxg_6", "rxg_17", "rxg_23", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    @field_validator("rxg_20", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        import re
        if re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = {"populate_by_name": True}
