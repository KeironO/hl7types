"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: RXA
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE
from ..datatypes.EI import EI
from ..datatypes.PL import PL
from ..datatypes.XAD import XAD
from ..datatypes.XCN import XCN


class RXA(HL7Model):
    """HL7 v2 RXA segment.

    Attributes
    ----------
    rxa_1 : str
        RXA.1 (req) - Give Sub-ID Counter (NM)

    rxa_2 : str
        RXA.2 (req) - Administration Sub-ID Counter (NM)

    rxa_3 : str
        RXA.3 (req) - Date/Time Start of Administration (DTM)

    rxa_4 : str
        RXA.4 (req) - Date/Time End of Administration (DTM)

    rxa_5 : CWE
        RXA.5 (req) - Administered Code (CWE)

    rxa_6 : str
        RXA.6 (req) - Administered Amount (NM)

    rxa_7 : CWE | None
        RXA.7 (opt) - Administered Units (CWE)

    rxa_8 : CWE | None
        RXA.8 (opt) - Administered Dosage Form (CWE)

    rxa_9 : list[CWE] | None
        RXA.9 (opt, rep) - Administration Notes (CWE)

    rxa_10 : list[XCN] | None
        RXA.10 (opt, rep) - Administering Provider (XCN)

    rxa_12 : str | None
        RXA.12 (opt) - Administered Per (Time Unit) (ST)

    rxa_13 : str | None
        RXA.13 (opt) - Administered Strength (NM)

    rxa_14 : CWE | None
        RXA.14 (opt) - Administered Strength Units (CWE)

    rxa_15 : list[str] | None
        RXA.15 (opt, rep) - Substance Lot Number (ST)

    rxa_16 : list[str] | None
        RXA.16 (opt, rep) - Substance Expiration Date (DTM)

    rxa_17 : list[CWE] | None
        RXA.17 (opt, rep) - Substance Manufacturer Name (CWE)

    rxa_18 : list[CWE] | None
        RXA.18 (opt, rep) - Substance/Treatment Refusal Reason (CWE)

    rxa_19 : list[CWE] | None
        RXA.19 (opt, rep) - Indication (CWE)

    rxa_20 : str | None
        RXA.20 (opt) - Completion Status (ID)

    rxa_21 : str | None
        RXA.21 (opt) - Action Code - RXA (ID)

    rxa_22 : str | None
        RXA.22 (opt) - System Entry Date/Time (DTM)

    rxa_23 : str | None
        RXA.23 (opt) - Administered Drug Strength Volume (NM)

    rxa_24 : CWE | None
        RXA.24 (opt) - Administered Drug Strength Volume Units (CWE)

    rxa_25 : CWE | None
        RXA.25 (opt) - Administered Barcode Identifier (CWE)

    rxa_26 : str | None
        RXA.26 (opt) - Pharmacy Order Type (ID)

    rxa_27 : PL | None
        RXA.27 (opt) - Administer-at (PL)

    rxa_28 : XAD | None
        RXA.28 (opt) - Administered-at Address (XAD)

    rxa_29 : list[EI] | None
        RXA.29 (opt, rep) - Administered Tag Identifier (EI)
    """

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

    rxa_3: str = Field(
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

    rxa_4: str = Field(
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

    rxa_5: CWE = Field(
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

    rxa_7: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_7",
            "administered_units",
            "RXA.7",
        ),
        serialization_alias="RXA.7",
        title="Administered Units",
        description="Item #349 | Table HL79999",
    )

    rxa_8: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_8",
            "administered_dosage_form",
            "RXA.8",
        ),
        serialization_alias="RXA.8",
        title="Administered Dosage Form",
        description="Item #350 | Table HL79999",
    )

    rxa_9: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_9",
            "administration_notes",
            "RXA.9",
        ),
        serialization_alias="RXA.9",
        title="Administration Notes",
        description="Item #351 | Table HL79999",
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

    rxa_14: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_14",
            "administered_strength_units",
            "RXA.14",
        ),
        serialization_alias="RXA.14",
        title="Administered Strength Units",
        description="Item #1135 | Table HL79999",
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

    rxa_16: Optional[List[str]] = Field(
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

    rxa_17: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_17",
            "substance_manufacturer_name",
            "RXA.17",
        ),
        serialization_alias="RXA.17",
        title="Substance Manufacturer Name",
        description="Item #1131",
    )

    rxa_18: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_18",
            "substance_treatment_refusal_reason",
            "RXA.18",
        ),
        serialization_alias="RXA.18",
        title="Substance/Treatment Refusal Reason",
        description="Item #1136 | Table HL79999",
    )

    rxa_19: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_19",
            "indication",
            "RXA.19",
        ),
        serialization_alias="RXA.19",
        title="Indication",
        description="Item #1123 | Table HL79999",
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
        description="Item #1224 | Table HL70206",
    )

    rxa_22: Optional[str] = Field(
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
        description="Item #1697 | Table HL79999",
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
        description="Item #1698 | Table HL79999",
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

    rxa_27: Optional[PL] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_27",
            "administer_at",
            "RXA.27",
        ),
        serialization_alias="RXA.27",
        title="Administer-at",
        description="Item #2264",
    )

    rxa_28: Optional[XAD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_28",
            "administered_at_address",
            "RXA.28",
        ),
        serialization_alias="RXA.28",
        title="Administered-at Address",
        description="Item #2265",
    )

    rxa_29: Optional[List[EI]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rxa_29",
            "administered_tag_identifier",
            "RXA.29",
        ),
        serialization_alias="RXA.29",
        title="Administered Tag Identifier",
        description="Item #3396",
    )

    model_config = {"populate_by_name": True}
