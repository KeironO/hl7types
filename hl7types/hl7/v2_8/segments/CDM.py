"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: CDM
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CNE import CNE
from ..datatypes.CWE import CWE
from ..datatypes.CX import CX
from ..datatypes.XON import XON


class CDM(BaseModel):
    """HL7 v2 CDM segment.

    Attributes
    ----------
    cdm_1 : CWE
        CDM.1 (req) - Primary Key Value - CDM (CWE)

    cdm_2 : list[CWE] | None
        CDM.2 (opt, rep) - Charge Code Alias (CWE)

    cdm_3 : str
        CDM.3 (req) - Charge Description Short (ST)

    cdm_4 : str | None
        CDM.4 (opt) - Charge Description Long (ST)

    cdm_5 : CWE | None
        CDM.5 (opt) - Description Override Indicator (CWE)

    cdm_6 : list[CWE] | None
        CDM.6 (opt, rep) - Exploding Charges (CWE)

    cdm_7 : list[CNE] | None
        CDM.7 (opt, rep) - Procedure Code (CNE)

    cdm_8 : str | None
        CDM.8 (opt) - Active/Inactive Flag (ID)

    cdm_9 : list[CWE] | None
        CDM.9 (opt, rep) - Inventory Number (CWE)

    cdm_10 : str | None
        CDM.10 (opt) - Resource Load (NM)

    cdm_11 : list[CX] | None
        CDM.11 (opt, rep) - Contract Number (CX)

    cdm_12 : list[XON] | None
        CDM.12 (opt, rep) - Contract Organization (XON)

    cdm_13 : str | None
        CDM.13 (opt) - Room Fee Indicator (ID)
    """

    cdm_1: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "cdm_1",
            "primary_key_value_cdm",
            "CDM.1",
        ),
        serialization_alias="CDM.1",
        title="Primary Key Value - CDM",
        description="Item #1306",
    )

    cdm_2: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cdm_2",
            "charge_code_alias",
            "CDM.2",
        ),
        serialization_alias="CDM.2",
        title="Charge Code Alias",
        description="Item #983 | Table HL70132",
    )

    cdm_3: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "cdm_3",
            "charge_description_short",
            "CDM.3",
        ),
        serialization_alias="CDM.3",
        title="Charge Description Short",
        description="Item #984",
    )

    cdm_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cdm_4",
            "charge_description_long",
            "CDM.4",
        ),
        serialization_alias="CDM.4",
        title="Charge Description Long",
        description="Item #985",
    )

    cdm_5: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cdm_5",
            "description_override_indicator",
            "CDM.5",
        ),
        serialization_alias="CDM.5",
        title="Description Override Indicator",
        description="Item #986 | Table HL70268",
    )

    cdm_6: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cdm_6",
            "exploding_charges",
            "CDM.6",
        ),
        serialization_alias="CDM.6",
        title="Exploding Charges",
        description="Item #987 | Table HL70132",
    )

    cdm_7: Optional[List[CNE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cdm_7",
            "procedure_code",
            "CDM.7",
        ),
        serialization_alias="CDM.7",
        title="Procedure Code",
        description="Item #393 | Table HL70088",
    )

    cdm_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cdm_8",
            "active_inactive_flag",
            "CDM.8",
        ),
        serialization_alias="CDM.8",
        title="Active/Inactive Flag",
        description="Item #675 | Table HL70183",
    )

    cdm_9: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cdm_9",
            "inventory_number",
            "CDM.9",
        ),
        serialization_alias="CDM.9",
        title="Inventory Number",
        description="Item #990 | Table HL70463",
    )

    cdm_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cdm_10",
            "resource_load",
            "CDM.10",
        ),
        serialization_alias="CDM.10",
        title="Resource Load",
        description="Item #991",
    )

    cdm_11: Optional[List[CX]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cdm_11",
            "contract_number",
            "CDM.11",
        ),
        serialization_alias="CDM.11",
        title="Contract Number",
        description="Item #992",
    )

    cdm_12: Optional[List[XON]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cdm_12",
            "contract_organization",
            "CDM.12",
        ),
        serialization_alias="CDM.12",
        title="Contract Organization",
        description="Item #993",
    )

    cdm_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cdm_13",
            "room_fee_indicator",
            "CDM.13",
        ),
        serialization_alias="CDM.13",
        title="Room Fee Indicator",
        description="Item #994 | Table HL70136",
    )

    model_config = {"populate_by_name": True}
