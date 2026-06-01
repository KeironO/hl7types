"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: ITM
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator

from ..datatypes.CNE import CNE
from ..datatypes.CP import CP
from ..datatypes.CWE import CWE
from ..datatypes.EI import EI
from ..datatypes.MO import MO
from ..datatypes.XON import XON


class ITM(HL7Model):
    """HL7 v2 ITM segment.

    Attributes
    ----------
    itm_1 : EI
        ITM.1 (req) - Item Identifier (EI)

    itm_2 : str | None
        ITM.2 (opt) - Item Description (ST)

    itm_3 : CWE | None
        ITM.3 (opt) - Item Status (CWE)

    itm_4 : CWE | None
        ITM.4 (opt) - Item Type (CWE)

    itm_5 : CWE | None
        ITM.5 (opt) - Item Category (CWE)

    itm_6 : CNE | None
        ITM.6 (opt) - Subject to Expiration Indicator (CNE)

    itm_7 : EI | None
        ITM.7 (opt) - Manufacturer Identifier (EI)

    itm_8 : str | None
        ITM.8 (opt) - Manufacturer Name (ST)

    itm_9 : str | None
        ITM.9 (opt) - Manufacturer Catalog Number (ST)

    itm_10 : CWE | None
        ITM.10 (opt) - Manufacturer Labeler Identification Code (CWE)

    itm_11 : CNE | None
        ITM.11 (opt) - Patient Chargeable Indicator (CNE)

    itm_12 : CWE | None
        ITM.12 (opt) - Transaction Code (CWE)

    itm_13 : CP | None
        ITM.13 (opt) - Transaction amount - unit (CP)

    itm_14 : CNE | None
        ITM.14 (opt) - Stocked Item Indicator (CNE)

    itm_15 : CWE | None
        ITM.15 (opt) - Supply Risk Codes (CWE)

    itm_16 : list[XON] | None
        ITM.16 (opt, rep) - Approving Regulatory Agency (XON)

    itm_17 : CNE | None
        ITM.17 (opt) - Latex Indicator (CNE)

    itm_18 : list[CWE] | None
        ITM.18 (opt, rep) - Ruling Act (CWE)

    itm_19 : CWE | None
        ITM.19 (opt) - Item Natural Account Code (CWE)

    itm_20 : str | None
        ITM.20 (opt) - Approved To Buy Quantity (NM)

    itm_21 : MO | None
        ITM.21 (opt) - Approved To Buy Price (MO)

    itm_22 : CNE | None
        ITM.22 (opt) - Taxable Item Indicator (CNE)

    itm_23 : CNE | None
        ITM.23 (opt) - Freight Charge Indicator (CNE)

    itm_24 : CNE | None
        ITM.24 (opt) - Item Set Indicator (CNE)

    itm_25 : EI | None
        ITM.25 (opt) - Item Set Identifier (EI)

    itm_26 : CNE | None
        ITM.26 (opt) - Track Department Usage Indicator (CNE)

    itm_27 : CNE | None
        ITM.27 (opt) - Procedure Code (CNE)

    itm_28 : list[CNE] | None
        ITM.28 (opt, rep) - Procedure Code Modifier (CNE)

    itm_29 : CWE | None
        ITM.29 (opt) - Special Handling Code (CWE)
    """

    itm_1: EI = Field(
        default=...,
        validation_alias=AliasChoices(
            "itm_1",
            "item_identifier",
            "ITM.1",
        ),
        serialization_alias="ITM.1",
        title="Item Identifier",
        description="Item #2186",
    )

    itm_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "itm_2",
            "item_description",
            "ITM.2",
        ),
        serialization_alias="ITM.2",
        title="Item Description",
        description="Item #2274",
    )

    itm_3: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "itm_3",
            "item_status",
            "ITM.3",
        ),
        serialization_alias="ITM.3",
        title="Item Status",
        description="Item #2187 | Table HL70776",
    )

    itm_4: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "itm_4",
            "item_type",
            "ITM.4",
        ),
        serialization_alias="ITM.4",
        title="Item Type",
        description="Item #2188 | Table HL70778",
    )

    itm_5: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "itm_5",
            "item_category",
            "ITM.5",
        ),
        serialization_alias="ITM.5",
        title="Item Category",
        description="Item #2189",
    )

    itm_6: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "itm_6",
            "subject_to_expiration_indicator",
            "ITM.6",
        ),
        serialization_alias="ITM.6",
        title="Subject to Expiration Indicator",
        description="Item #2190 | Table HL70532",
    )

    itm_7: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "itm_7",
            "manufacturer_identifier",
            "ITM.7",
        ),
        serialization_alias="ITM.7",
        title="Manufacturer Identifier",
        description="Item #2191",
    )

    itm_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "itm_8",
            "manufacturer_name",
            "ITM.8",
        ),
        serialization_alias="ITM.8",
        title="Manufacturer Name",
        description="Item #2275",
    )

    itm_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "itm_9",
            "manufacturer_catalog_number",
            "ITM.9",
        ),
        serialization_alias="ITM.9",
        title="Manufacturer Catalog Number",
        description="Item #2192",
    )

    itm_10: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "itm_10",
            "manufacturer_labeler_identification_code",
            "ITM.10",
        ),
        serialization_alias="ITM.10",
        title="Manufacturer Labeler Identification Code",
        description="Item #2193",
    )

    itm_11: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "itm_11",
            "patient_chargeable_indicator",
            "ITM.11",
        ),
        serialization_alias="ITM.11",
        title="Patient Chargeable Indicator",
        description="Item #2070 | Table HL70532",
    )

    itm_12: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "itm_12",
            "transaction_code",
            "ITM.12",
        ),
        serialization_alias="ITM.12",
        title="Transaction Code",
        description="Item #361 | Table HL70132",
    )

    itm_13: Optional[CP] = Field(
        default=None,
        validation_alias=AliasChoices(
            "itm_13",
            "transaction_amount_unit",
            "ITM.13",
        ),
        serialization_alias="ITM.13",
        title="Transaction amount - unit",
        description="Item #366",
    )

    itm_14: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "itm_14",
            "stocked_item_indicator",
            "ITM.14",
        ),
        serialization_alias="ITM.14",
        title="Stocked Item Indicator",
        description="Item #2197 | Table HL70532",
    )

    itm_15: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "itm_15",
            "supply_risk_codes",
            "ITM.15",
        ),
        serialization_alias="ITM.15",
        title="Supply Risk Codes",
        description="Item #2266 | Table HL70871",
    )

    itm_16: Optional[List[XON]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "itm_16",
            "approving_regulatory_agency",
            "ITM.16",
        ),
        serialization_alias="ITM.16",
        title="Approving Regulatory Agency",
        description="Item #2199 | Table HL70790",
    )

    itm_17: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "itm_17",
            "latex_indicator",
            "ITM.17",
        ),
        serialization_alias="ITM.17",
        title="Latex Indicator",
        description="Item #2200 | Table HL70532",
    )

    itm_18: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "itm_18",
            "ruling_act",
            "ITM.18",
        ),
        serialization_alias="ITM.18",
        title="Ruling Act",
        description="Item #2201 | Table HL70793",
    )

    itm_19: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "itm_19",
            "item_natural_account_code",
            "ITM.19",
        ),
        serialization_alias="ITM.19",
        title="Item Natural Account Code",
        description="Item #282 | Table HL70320",
    )

    itm_20: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "itm_20",
            "approved_to_buy_quantity",
            "ITM.20",
        ),
        serialization_alias="ITM.20",
        title="Approved To Buy Quantity",
        description="Item #2203",
    )

    itm_21: Optional[MO] = Field(
        default=None,
        validation_alias=AliasChoices(
            "itm_21",
            "approved_to_buy_price",
            "ITM.21",
        ),
        serialization_alias="ITM.21",
        title="Approved To Buy Price",
        description="Item #2204",
    )

    itm_22: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "itm_22",
            "taxable_item_indicator",
            "ITM.22",
        ),
        serialization_alias="ITM.22",
        title="Taxable Item Indicator",
        description="Item #2205 | Table HL70532",
    )

    itm_23: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "itm_23",
            "freight_charge_indicator",
            "ITM.23",
        ),
        serialization_alias="ITM.23",
        title="Freight Charge Indicator",
        description="Item #2206 | Table HL70532",
    )

    itm_24: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "itm_24",
            "item_set_indicator",
            "ITM.24",
        ),
        serialization_alias="ITM.24",
        title="Item Set Indicator",
        description="Item #2207 | Table HL70532",
    )

    itm_25: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "itm_25",
            "item_set_identifier",
            "ITM.25",
        ),
        serialization_alias="ITM.25",
        title="Item Set Identifier",
        description="Item #2208",
    )

    itm_26: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "itm_26",
            "track_department_usage_indicator",
            "ITM.26",
        ),
        serialization_alias="ITM.26",
        title="Track Department Usage Indicator",
        description="Item #2209 | Table HL70532",
    )

    itm_27: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "itm_27",
            "procedure_code",
            "ITM.27",
        ),
        serialization_alias="ITM.27",
        title="Procedure Code",
        description="Item #393 | Table HL70088",
    )

    itm_28: Optional[List[CNE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "itm_28",
            "procedure_code_modifier",
            "ITM.28",
        ),
        serialization_alias="ITM.28",
        title="Procedure Code Modifier",
        description="Item #1316 | Table HL70340",
    )

    itm_29: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "itm_29",
            "special_handling_code",
            "ITM.29",
        ),
        serialization_alias="ITM.29",
        title="Special Handling Code",
        description="Item #1370 | Table HL70376",
    )

    @field_validator("itm_20", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
