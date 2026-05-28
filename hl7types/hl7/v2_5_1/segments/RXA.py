"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: RXA
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE
from ..datatypes.CWE import CWE
from ..datatypes.LA2 import LA2
from ..datatypes.TS import TS
from ..datatypes.XCN import XCN


class RXA(BaseModel):
    """HL7 v2 RXA segment."""

    rxa_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "rxa_1",
            "give_sub_id_counter",
            "RXA.1",
        ),
        serialization_alias="RXA.1",
        title="Give Sub-ID Counter",
        description="Item #342",
    )

    rxa_2: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "rxa_2",
            "administration_sub_id_counter",
            "RXA.2",
        ),
        serialization_alias="RXA.2",
        title="Administration Sub-ID Counter",
        description="Item #344",
    )

    rxa_3: TS = Field(
        default=...,
        validation_alias=AliasChoices(
            "rxa_3",
            "date_time_start_of_administration",
            "RXA.3",
        ),
        serialization_alias="RXA.3",
        title="Date/Time Start of Administration",
        description="Item #345",
    )

    rxa_4: TS = Field(
        default=...,
        validation_alias=AliasChoices(
            "rxa_4",
            "date_time_end_of_administration",
            "RXA.4",
        ),
        serialization_alias="RXA.4",
        title="Date/Time End of Administration",
        description="Item #346",
    )

    rxa_5: CE = Field(
        default=...,
        validation_alias=AliasChoices(
            "rxa_5",
            "administered_code",
            "RXA.5",
        ),
        serialization_alias="RXA.5",
        title="Administered Code",
        description="Item #347 | Table HL70292",
    )

    rxa_6: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "rxa_6",
            "administered_amount",
            "RXA.6",
        ),
        serialization_alias="RXA.6",
        title="Administered Amount",
        description="Item #348",
    )

    rxa_7: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_7",
            "administered_units",
            "RXA.7",
        ),
        serialization_alias="RXA.7",
        title="Administered Units",
        description="Item #349",
    )

    rxa_8: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_8",
            "administered_dosage_form",
            "RXA.8",
        ),
        serialization_alias="RXA.8",
        title="Administered Dosage Form",
        description="Item #350",
    )

    rxa_9: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_9",
            "administration_notes",
            "RXA.9",
        ),
        serialization_alias="RXA.9",
        title="Administration Notes",
        description="Item #351",
    )

    rxa_10: Optional[List[XCN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_10",
            "administering_provider",
            "RXA.10",
        ),
        serialization_alias="RXA.10",
        title="Administering Provider",
        description="Item #352",
    )

    rxa_11: Optional[LA2] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_11",
            "administered_at_location",
            "RXA.11",
        ),
        serialization_alias="RXA.11",
        title="Administered-at Location",
        description="Item #353",
    )

    rxa_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_12",
            "administered_per_time_unit",
            "RXA.12",
        ),
        serialization_alias="RXA.12",
        title="Administered Per (Time Unit)",
        description="Item #354",
    )

    rxa_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_13",
            "administered_strength",
            "RXA.13",
        ),
        serialization_alias="RXA.13",
        title="Administered Strength",
        description="Item #1134",
    )

    rxa_14: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_14",
            "administered_strength_units",
            "RXA.14",
        ),
        serialization_alias="RXA.14",
        title="Administered Strength Units",
        description="Item #1135",
    )

    rxa_15: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_15",
            "substance_lot_number",
            "RXA.15",
        ),
        serialization_alias="RXA.15",
        title="Substance Lot Number",
        description="Item #1129",
    )

    rxa_16: Optional[List[TS]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_16",
            "substance_expiration_date",
            "RXA.16",
        ),
        serialization_alias="RXA.16",
        title="Substance Expiration Date",
        description="Item #1130",
    )

    rxa_17: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_17",
            "substance_manufacturer_name",
            "RXA.17",
        ),
        serialization_alias="RXA.17",
        title="Substance Manufacturer Name",
        description="Item #1131 | Table HL70227",
    )

    rxa_18: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_18",
            "substance_treatment_refusal_reason",
            "RXA.18",
        ),
        serialization_alias="RXA.18",
        title="Substance/Treatment Refusal Reason",
        description="Item #1136",
    )

    rxa_19: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_19",
            "indication",
            "RXA.19",
        ),
        serialization_alias="RXA.19",
        title="Indication",
        description="Item #1123",
    )

    rxa_20: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_20",
            "completion_status",
            "RXA.20",
        ),
        serialization_alias="RXA.20",
        title="Completion Status",
        description="Item #1223 | Table HL70322",
    )

    rxa_21: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_21",
            "action_code_rxa",
            "RXA.21",
        ),
        serialization_alias="RXA.21",
        title="Action Code - RXA",
        description="Item #1224 | Table HL70323",
    )

    rxa_22: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_22",
            "system_entry_date_time",
            "RXA.22",
        ),
        serialization_alias="RXA.22",
        title="System Entry Date/Time",
        description="Item #1225",
    )

    rxa_23: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_23",
            "administered_drug_strength_volume",
            "RXA.23",
        ),
        serialization_alias="RXA.23",
        title="Administered Drug Strength Volume",
        description="Item #1696",
    )

    rxa_24: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_24",
            "administered_drug_strength_volume_units",
            "RXA.24",
        ),
        serialization_alias="RXA.24",
        title="Administered Drug Strength Volume Units",
        description="Item #1697",
    )

    rxa_25: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_25",
            "administered_barcode_identifier",
            "RXA.25",
        ),
        serialization_alias="RXA.25",
        title="Administered Barcode Identifier",
        description="Item #1698",
    )

    rxa_26: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_26",
            "pharmacy_order_type",
            "RXA.26",
        ),
        serialization_alias="RXA.26",
        title="Pharmacy Order Type",
        description="Item #1699 | Table HL70480",
    )

    model_config = {"populate_by_name": True}
