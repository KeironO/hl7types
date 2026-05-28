"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: PAC
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CWE import CWE
from ..datatypes.EI import EI
from ..datatypes.NA import NA


class PAC(BaseModel):
    """HL7 v2 PAC segment."""

    pac_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "pac_1",
            "set_id_pac",
            "PAC.1",
        ),
        serialization_alias="PAC.1",
        title="Set Id - PAC",
        description="Item #2350",
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
        description="Item #2351",
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
        description="Item #2352",
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
        description="Item #2353",
    )

    pac_5: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "pac_5",
            "package_type",
            "PAC.5",
        ),
        serialization_alias="PAC.5",
        title="Package Type",
        description="Item #2354 | Table HL70908",
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
        description="Item #2355 | Table HL70544",
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
        description="Item #2356 | Table HL70376",
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
        description="Item #2357 | Table HL70489",
    )

    model_config = {"populate_by_name": True}
