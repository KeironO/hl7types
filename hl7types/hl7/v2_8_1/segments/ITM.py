"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: ITM
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CNE import CNE
from ..datatypes.CP import CP
from ..datatypes.CWE import CWE
from ..datatypes.EI import EI
from ..datatypes.MO import MO
from ..datatypes.XON import XON

_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class ITM(HL7Model):
    """Material Item (S17.4.2).

    Attributes
    ----------
    itm_1 : EI
        ITM.1 - Item Identifier (EI) R S17.4.2.1

    itm_2 : str | None
        ITM.2 - Item Description (ST) O S17.4.2.2

    itm_3 : CWE | None
        ITM.3 - Item Status (CWE) O S17.4.2.3 | 0776 - Item Status

    itm_4 : CWE | None
        ITM.4 - Item Type (CWE) O S17.4.2.4 | 0778 - Item Type

    itm_5 : CWE | None
        ITM.5 - Item Category (CWE) O S17.4.2.5

    itm_6 : CNE | None
        ITM.6 - Subject to Expiration Indicator (CNE) O S17.4.2.6 | 0532 - Expanded Yes/no Indicator

    itm_7 : EI | None
        ITM.7 - Manufacturer Identifier (EI) O S17.4.2.7

    itm_8 : str | None
        ITM.8 - Manufacturer Name (ST) O S17.4.2.8

    itm_9 : str | None
        ITM.9 - Manufacturer Catalog Number (ST) O S17.4.2.9

    itm_10 : CWE | None
        ITM.10 - Manufacturer Labeler Identification Code (CWE) O S17.4.2.10

    itm_11 : CNE | None
        ITM.11 - Patient Chargeable Indicator (CNE) O S17.4.2.11 | 0532 - Expanded Yes/no Indicator

    itm_12 : CWE | None
        ITM.12 - Transaction Code (CWE) O S17.4.2.12 | 0132 - Transaction Code

    itm_13 : CP | None
        ITM.13 - Transaction amount - unit (CP) O S17.4.2.13

    itm_14 : CNE | None
        ITM.14 - Stocked Item Indicator (CNE) O S17.4.2.14 | 0532 - Expanded Yes/no Indicator

    itm_15 : CWE | None
        ITM.15 - Supply Risk Codes (CWE) O S17.4.2.15 | 0871 - Supply Risk Codes

    itm_16 : list[XON] | None
        ITM.16 - Approving Regulatory Agency (XON) O rep S17.4.2.16 | 0790 - Approving Regulatory Agency

    itm_17 : CNE | None
        ITM.17 - Latex Indicator (CNE) O S17.4.2.17 | 0532 - Expanded Yes/no Indicator

    itm_18 : list[CWE] | None
        ITM.18 - Ruling Act (CWE) O rep S17.4.2.18 | 0793 - Ruling Act

    itm_19 : CWE | None
        ITM.19 - Item Natural Account Code (CWE) O S17.4.2.19 | 0320 - Item Natural Account Code

    itm_20 : str | None
        ITM.20 - Approved To Buy Quantity (NM) O S17.4.2.20

    itm_21 : MO | None
        ITM.21 - Approved To Buy Price (MO) O S17.4.2.21

    itm_22 : CNE | None
        ITM.22 - Taxable Item Indicator (CNE) O S17.4.2.22 | 0532 - Expanded Yes/no Indicator

    itm_23 : CNE | None
        ITM.23 - Freight Charge Indicator (CNE) O S17.4.2.23 | 0532 - Expanded Yes/no Indicator

    itm_24 : CNE | None
        ITM.24 - Item Set Indicator (CNE) O S17.4.2.24 | 0532 - Expanded Yes/no Indicator

    itm_25 : EI | None
        ITM.25 - Item Set Identifier (EI) O S17.4.2.25

    itm_26 : CNE | None
        ITM.26 - Track Department Usage Indicator (CNE) O S17.4.2.26 | 0532 - Expanded Yes/no Indicator

    itm_27 : CNE | None
        ITM.27 - Procedure Code (CNE) O S17.4.1.14 | 0088 - Procedure Code

    itm_28 : list[CNE] | None
        ITM.28 - Procedure Code Modifier (CNE) O rep S17.4.1.15 | 0340 - Procedure Code Modifier

    itm_29 : CWE | None
        ITM.29 - Special Handling Code (CWE) O S13.4.3.43 | 0376 - Special Handling Code

    itm_30 : CNE | None
        ITM.30 - Hazardous Indicator (CNE) O S17.4.2.30 | 0532 - Expanded Yes/no Indicator

    itm_31 : CNE | None
        ITM.31 - Sterile Indicator (CNE) O S17.4.2.31 | 0532 - Expanded Yes/no Indicator

    itm_32 : EI | None
        ITM.32 - Material Data Safety Sheet Number (EI) O S17.4.2.32

    itm_33 : CWE | None
        ITM.33 - United Nations Standard Products and Services Code (UNSPSC) (CWE) O S17.4.2.33 | 0396 - Coding System
    """

    itm_1: EI = Field(
        validation_alias=AliasChoices(
            "itm_1",
            "item_identifier",
            "ITM.1",
        ),
        serialization_alias="ITM.1",
        title="Item Identifier",
        description="R | Item #02186",
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
        description="O | Item #02274",
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
        description="O | Item #02187 | Table 0776 - Item Status",
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
        description="O | Item #02188 | Table 0778 - Item Type",
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
        description="O | Item #02189",
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
        description="O | Item #02190 | Table 0532 - Expanded Yes/no Indicator",
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
        description="O | Item #02191",
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
        description="O | Item #02275",
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
        description="O | Item #02192",
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
        description="O | Item #02193",
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
        description="O | Item #02070 | Table 0532 - Expanded Yes/no Indicator",
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
        description="O | Item #00361 | Table 0132 - Transaction Code",
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
        description="O | Item #00366",
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
        description="O | Item #02197 | Table 0532 - Expanded Yes/no Indicator",
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
        description="O | Item #02266 | Table 0871 - Supply Risk Codes",
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
        description=(
            "O | Item #02199 | Table 0790 - Approving Regulatory Agency"
        ),
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
        description="O | Item #02200 | Table 0532 - Expanded Yes/no Indicator",
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
        description="O | Item #02201 | Table 0793 - Ruling Act",
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
        description="O | Item #00282 | Table 0320 - Item Natural Account Code",
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
        description="O | Item #02203",
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
        description="O | Item #02204",
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
        description="O | Item #02205 | Table 0532 - Expanded Yes/no Indicator",
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
        description="O | Item #02206 | Table 0532 - Expanded Yes/no Indicator",
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
        description="O | Item #02207 | Table 0532 - Expanded Yes/no Indicator",
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
        description="O | Item #02208",
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
        description="O | Item #02209 | Table 0532 - Expanded Yes/no Indicator",
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
        description="O | Item #00393 | Table 0088 - Procedure Code",
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
        description="O | Item #01316 | Table 0340 - Procedure Code Modifier",
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
        description="O | Item #01370 | Table 0376 - Special Handling Code",
    )

    itm_30: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "itm_30",
            "hazardous_indicator",
            "ITM.30",
        ),
        serialization_alias="ITM.30",
        title="Hazardous Indicator",
        description="O | Item #03388 | Table 0532 - Expanded Yes/no Indicator",
    )

    itm_31: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "itm_31",
            "sterile_indicator",
            "ITM.31",
        ),
        serialization_alias="ITM.31",
        title="Sterile Indicator",
        description="O | Item #03304 | Table 0532 - Expanded Yes/no Indicator",
    )

    itm_32: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "itm_32",
            "material_data_safety_sheet_number",
            "ITM.32",
        ),
        serialization_alias="ITM.32",
        title="Material Data Safety Sheet Number",
        description="O | Item #03305",
    )

    itm_33: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "itm_33",
            "united_nations_standard_products_and_services_code_unspsc",
            "ITM.33",
        ),
        serialization_alias="ITM.33",
        title="United Nations Standard Products and Services Code (UNSPSC)",
        description="O | Item #03306 | Table 0396 - Coding System",
    )

    @field_validator("itm_20", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
