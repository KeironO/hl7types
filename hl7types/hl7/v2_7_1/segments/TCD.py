"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: TCD
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CWE import CWE
from ..datatypes.SN import SN


class TCD(BaseModel):
    """HL7 v2 TCD segment."""

    tcd_1: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "tcd_1",
            "universal_service_identifier",
            "TCD.1",
        ),
        serialization_alias="TCD.1",
        title="Universal Service Identifier",
        description="Item #238",
    )

    tcd_2: Optional[SN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tcd_2",
            "auto_dilution_factor",
            "TCD.2",
        ),
        serialization_alias="TCD.2",
        title="Auto-Dilution Factor",
        description="Item #1420",
    )

    tcd_3: Optional[SN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tcd_3",
            "rerun_dilution_factor",
            "TCD.3",
        ),
        serialization_alias="TCD.3",
        title="Rerun Dilution Factor",
        description="Item #1421",
    )

    tcd_4: Optional[SN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tcd_4",
            "pre_dilution_factor",
            "TCD.4",
        ),
        serialization_alias="TCD.4",
        title="Pre-Dilution Factor",
        description="Item #1422",
    )

    tcd_5: Optional[SN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tcd_5",
            "endogenous_content_of_pre_dilution_diluent",
            "TCD.5",
        ),
        serialization_alias="TCD.5",
        title="Endogenous Content of Pre-Dilution Diluent",
        description="Item #1413",
    )

    tcd_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tcd_6",
            "automatic_repeat_allowed",
            "TCD.6",
        ),
        serialization_alias="TCD.6",
        title="Automatic Repeat Allowed",
        description="Item #1416 | Table HL70136",
    )

    tcd_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tcd_7",
            "reflex_allowed",
            "TCD.7",
        ),
        serialization_alias="TCD.7",
        title="Reflex Allowed",
        description="Item #1424 | Table HL70136",
    )

    tcd_8: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tcd_8",
            "analyte_repeat_status",
            "TCD.8",
        ),
        serialization_alias="TCD.8",
        title="Analyte Repeat Status",
        description="Item #1425 | Table HL70389",
    )

    model_config = {"populate_by_name": True}
