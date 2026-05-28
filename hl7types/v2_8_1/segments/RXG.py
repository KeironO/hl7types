"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: RXG
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CWE import CWE
from ..datatypes.EI import EI
from ..datatypes.PL import PL
from ..datatypes.XAD import XAD


class RXG(BaseModel):
    """HL7 v2 RXG segment."""

    rxg_1: str = Field(
        default=...,
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
        default=...,
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
        default=...,
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
        default=...,
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
            "special_administration_instructions",
            "RXG.13",
        ),
        serialization_alias="RXG.13",
        title="Special Administration Instructions",
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
        description="Item #1131",
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

    rxg_31: Optional[List[EI]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxg_31",
            "give_tag_identifier",
            "RXG.31",
        ),
        serialization_alias="RXG.31",
        title="Give Tag Identifier",
        description="Item #3393",
    )

    rxg_32: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxg_32",
            "dispense_amount",
            "RXG.32",
        ),
        serialization_alias="RXG.32",
        title="Dispense Amount",
        description="Item #3316",
    )

    rxg_33: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxg_33",
            "dispense_units",
            "RXG.33",
        ),
        serialization_alias="RXG.33",
        title="Dispense Units",
        description="Item #3317 | Table HL79999",
    )

    model_config = {"populate_by_name": True}
