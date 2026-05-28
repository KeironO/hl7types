"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: CDM
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE
from ..datatypes.CX import CX
from ..datatypes.XON import XON


class CDM(BaseModel):
    """HL7 v2 CDM segment."""

    cdm_1: CE = Field(
        default=...,
        validation_alias=AliasChoices(
            "cdm_1",
            "primary_key_value_cdm",
            "CDM.1",
        ),
        serialization_alias="CDM.1",
        title="Primary Key Value - CDM",
        description="Item #1306 | Table HL70132",
    )

    cdm_2: list[CE] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cdm_2",
            "charge_code_alias",
            "CDM.2",
        ),
        serialization_alias="CDM.2",
        title="Charge Code Alias",
        description="Item #983",
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

    cdm_4: str | None = Field(
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

    cdm_5: str | None = Field(
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

    cdm_6: list[CE] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cdm_6",
            "exploding_charges",
            "CDM.6",
        ),
        serialization_alias="CDM.6",
        title="Exploding Charges",
        description="Item #987",
    )

    cdm_7: list[CE] | None = Field(
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

    cdm_8: str | None = Field(
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

    cdm_9: list[CE] | None = Field(
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

    cdm_10: str | None = Field(
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

    cdm_11: list[CX] | None = Field(
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

    cdm_12: list[XON] | None = Field(
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

    cdm_13: str | None = Field(
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
