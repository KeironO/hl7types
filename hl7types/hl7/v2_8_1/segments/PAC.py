"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: PAC
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE
from ..datatypes.EI import EI
from ..datatypes.NA import NA

_RE_SI = re.compile(r'\d*')


class PAC(HL7Model):
    """Shipment Package (S7.18.3).

    Attributes
    ----------
    pac_1 : str
        PAC.1 - Set Id - PAC (SI) R S7.18.3.1

    pac_2 : EI | None
        PAC.2 - Package ID (EI) C S7.18.3.2

    pac_3 : EI | None
        PAC.3 - Parent Package ID (EI) O S7.18.3.3

    pac_4 : NA | None
        PAC.4 - Position in Parent Package (NA) O S7.18.3.4

    pac_5 : CWE
        PAC.5 - Package Type (CWE) R S7.18.3.5 | 0908 - Package Type

    pac_6 : list[CWE] | None
        PAC.6 - Package Condition (CWE) O rep S7.18.3.6 | 0544 - Container Condition

    pac_7 : list[CWE] | None
        PAC.7 - Package Handling Code (CWE) O rep S7.18.3.7 | 0376 - Special Handling Code

    pac_8 : list[CWE] | None
        PAC.8 - Package Risk Code (CWE) O rep S7.18.3.8 | 0489 - Risk Codes
    """

    pac_1: str = Field(
        validation_alias=AliasChoices(
            "pac_1",
            "set_id_pac",
            "PAC.1",
        ),
        serialization_alias="PAC.1",
        title="Set Id - PAC",
        description="R | Item #02350 | LEN:4",
    )

    pac_2: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pac_2",
            "package_id",
            "PAC.2",
        ),
        serialization_alias="PAC.2",
        title="Package ID",
        description="C | Item #02351",
    )

    pac_3: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pac_3",
            "parent_package_id",
            "PAC.3",
        ),
        serialization_alias="PAC.3",
        title="Parent Package ID",
        description="O | Item #02352",
    )

    pac_4: Optional[NA] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pac_4",
            "position_in_parent_package",
            "PAC.4",
        ),
        serialization_alias="PAC.4",
        title="Position in Parent Package",
        description="O | Item #02353",
    )

    pac_5: CWE = Field(
        validation_alias=AliasChoices(
            "pac_5",
            "package_type",
            "PAC.5",
        ),
        serialization_alias="PAC.5",
        title="Package Type",
        description="R | Item #02354 | Table 0908 - Package Type",
    )

    pac_6: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pac_6",
            "package_condition",
            "PAC.6",
        ),
        serialization_alias="PAC.6",
        title="Package Condition",
        description="O | Item #02355 | Table 0544 - Container Condition",
    )

    pac_7: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pac_7",
            "package_handling_code",
            "PAC.7",
        ),
        serialization_alias="PAC.7",
        title="Package Handling Code",
        description="O | Item #02356 | Table 0376 - Special Handling Code",
    )

    pac_8: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pac_8",
            "package_risk_code",
            "PAC.8",
        ),
        serialization_alias="PAC.8",
        title="Package Risk Code",
        description="O | Item #02357 | Table 0489 - Risk Codes",
    )

    @field_validator("pac_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        if not _RE_SI.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    model_config = ConfigDict(populate_by_name=True)
