"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: CDM
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CNE import CNE
from ..datatypes.CWE import CWE
from ..datatypes.CX import CX
from ..datatypes.XON import XON

_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class CDM(HL7Model):
    """Charge Description Master (S8.10.2).

    Attributes
    ----------
    cdm_1 : CWE
        CDM.1 - Primary Key Value - CDM (CWE) R S8.8.14.24

    cdm_2 : list[CWE] | None
        CDM.2 - Charge Code Alias (CWE) O rep S8.10.2.2 | 0132 - Transaction Code

    cdm_3 : str
        CDM.3 - Charge Description Short (ST) R S8.10.2.3

    cdm_4 : str | None
        CDM.4 - Charge Description Long (ST) O S8.10.2.4

    cdm_5 : CWE | None
        CDM.5 - Description Override Indicator (CWE) O S8.10.2.5 | 0268 - Override

    cdm_6 : list[CWE] | None
        CDM.6 - Exploding Charges (CWE) O rep S8.10.2.6 | 0132 - Transaction Code

    cdm_7 : list[CNE] | None
        CDM.7 - Procedure Code (CNE) O rep S17.4.1.14 | 0088 - Procedure Code

    cdm_8 : str | None
        CDM.8 - Active/Inactive Flag (ID) O S15.4.8.7 | 0183 - Active/Inactive

    cdm_9 : list[CWE] | None
        CDM.9 - Inventory Number (CWE) O rep S8.10.2.9 | 0463 - Inventory Number

    cdm_10 : str | None
        CDM.10 - Resource Load (NM) O S8.10.2.10

    cdm_11 : list[CX] | None
        CDM.11 - Contract Number (CX) O rep S8.10.2.11

    cdm_12 : list[XON] | None
        CDM.12 - Contract Organization (XON) O rep S8.10.2.12

    cdm_13 : str | None
        CDM.13 - Room Fee Indicator (ID) O S8.10.2.13 | 0136 - Yes/no Indicator
    """

    cdm_1: CWE = Field(
        validation_alias=AliasChoices(
            "cdm_1",
            "primary_key_value_cdm",
            "CDM.1",
        ),
        serialization_alias="CDM.1",
        title="Primary Key Value - CDM",
        description="R | Item #01306",
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
        description="O | Item #00983 | Table 0132 - Transaction Code",
    )

    cdm_3: str = Field(
        validation_alias=AliasChoices(
            "cdm_3",
            "charge_description_short",
            "CDM.3",
        ),
        serialization_alias="CDM.3",
        title="Charge Description Short",
        description="R | Item #00984",
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
        description="O | Item #00985",
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
        description="O | Item #00986 | Table 0268 - Override",
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
        description="O | Item #00987 | Table 0132 - Transaction Code",
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
        description="O | Item #00675 | Table 0183 - Active/Inactive | LEN:1",
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
        description="O | Item #00990 | Table 0463 - Inventory Number",
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
        description="O | Item #00991",
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
        description="O | Item #00994 | Table 0136 - Yes/no Indicator | LEN:1",
    )

    @field_validator("cdm_10", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
