"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: CDM
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.CX import CX
from ..datatypes.XON import XON


class CDM(HL7Model):
    """Charge Description Master (S8.10.2).

    Attributes
    ----------
    cdm_1 : CE
        CDM.1 (req) - Primary Key Value - CDM (CE) S8.10.2.1 | 0132 - Transaction Code

    cdm_2 : list[CE] | None
        CDM.2 (opt, rep) - Charge Code Alias (CE) S8.10.2.2

    cdm_3 : str
        CDM.3 (req) - Charge Description Short (ST) S8.10.2.3

    cdm_4 : str | None
        CDM.4 (opt) - Charge Description Long (ST) S8.10.2.4

    cdm_5 : str | None
        CDM.5 (opt) - Description Override Indicator (IS) S8.10.2.5 | 0268 - Override

    cdm_6 : list[CE] | None
        CDM.6 (opt, rep) - Exploding Charges (CE) S8.10.2.6

    cdm_7 : list[CE] | None
        CDM.7 (opt, rep) - Procedure Code (CE) S4.5.3.44 | 0088 - Procedure Code

    cdm_8 : str | None
        CDM.8 (opt) - Active/Inactive Flag (ID) S15.4.8.7 | 0183 - Active/Inactive

    cdm_9 : list[CE] | None
        CDM.9 (opt, rep) - Inventory Number (CE) S8.10.2.9 | 0463 - Inventory Number

    cdm_10 : str | None
        CDM.10 (opt) - Resource Load (NM) S8.10.2.10

    cdm_11 : list[CX] | None
        CDM.11 (opt, rep) - Contract Number (CX) S8.10.2.11

    cdm_12 : list[XON] | None
        CDM.12 (opt, rep) - Contract Organization (XON) S8.10.2.12

    cdm_13 : str | None
        CDM.13 (opt) - Room Fee Indicator (ID) S8.10.2.13 | 0136 - Yes/no indicator
    """

    cdm_1: CE = Field(
        validation_alias=AliasChoices(
            "cdm_1",
            "primary_key_value_cdm",
            "CDM.1",
        ),
        serialization_alias="CDM.1",
        title="Primary Key Value - CDM",
        description="Item #1306 | Table HL70132",
    )

    cdm_2: Optional[List[CE]] = Field(
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

    cdm_5: Optional[str] = Field(
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

    cdm_6: Optional[List[CE]] = Field(
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

    cdm_7: Optional[List[CE]] = Field(
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

    cdm_9: Optional[List[CE]] = Field(
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

    @field_validator("cdm_10", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
