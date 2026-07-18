"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: CDM
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.CK import CK
from ..datatypes.XON import XON

_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class CDM(HL7Model):
    """CDM -  charge description master segment (S8.9.2).

    Attributes
    ----------
    cdm_1 : CE
        CDM.1 - Primary Key Value - CDM (CE) R S8.9.2.1 | 0132 - Transaction Code

    cdm_2 : list[CE] | None
        CDM.2 - Charge Code Alias (CE) O rep S8.9.2.2

    cdm_3 : str
        CDM.3 - Charge Description Short (ST) R S8.9.2.3

    cdm_4 : str | None
        CDM.4 - Charge Description Long (ST) O S8.9.2.4

    cdm_5 : str | None
        CDM.5 - Description Override Indicator (IS) O S8.9.2.5 | 0268 - Override

    cdm_6 : list[CE] | None
        CDM.6 - Exploding Charges (CE) O rep S8.9.2.6

    cdm_7 : list[CE] | None
        CDM.7 - Procedure Code (CE) O rep S8.9.2.7 | 0088 - Procedure Code

    cdm_8 : str | None
        CDM.8 - Active/Inactive Flag (ID) O S8.9.3.16 | 0183 - Active/inactive

    cdm_9 : list[CE] | None
        CDM.9 - Inventory Number (CE) O rep S8.9.2.9

    cdm_10 : str | None
        CDM.10 - Resource Load (NM) O S8.9.2.10

    cdm_11 : list[CK] | None
        CDM.11 - Contract Number (CK) O rep S8.9.2.11

    cdm_12 : list[XON] | None
        CDM.12 - Contract Organization (XON) O rep S8.9.2.12

    cdm_13 : str | None
        CDM.13 - Room Fee Indicator (ID) O S8.9.2.13 | 0136 - Yes/no indicator
    """

    cdm_1: CE = Field(
        validation_alias=AliasChoices(
            "cdm_1",
            "primary_key_value_cdm",
            "CDM.1",
        ),
        serialization_alias="CDM.1",
        title="Primary Key Value - CDM",
        description="R | Item #01306 | Table 0132 - Transaction Code",
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
        description="O | Item #00983",
    )

    cdm_3: str = Field(
        validation_alias=AliasChoices(
            "cdm_3",
            "charge_description_short",
            "CDM.3",
        ),
        serialization_alias="CDM.3",
        title="Charge Description Short",
        description="R | Item #00984 | LEN:20",
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
        description="O | Item #00985 | LEN:250",
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
        description="O | Item #00986 | Table 0268 - Override | LEN:1",
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
        description="O | Item #00987",
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
        description="O | Item #00393 | Table 0088 - Procedure Code",
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
        description="O | Item #00675 | Table 0183 - Active/inactive | LEN:1",
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
        description="O | Item #00990",
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
        description="O | Item #00991 | LEN:12",
    )

    cdm_11: Optional[List[CK]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cdm_11",
            "contract_number",
            "CDM.11",
        ),
        serialization_alias="CDM.11",
        title="Contract Number",
        description="O | Item #00992",
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
        description="O | Item #00993",
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
        description="O | Item #00994 | Table 0136 - Yes/no indicator | LEN:1",
    )

    @field_validator("cdm_10", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
