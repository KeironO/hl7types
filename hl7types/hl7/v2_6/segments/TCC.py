"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: TCC
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CWE import CWE
from ..datatypes.EI import EI
from ..datatypes.SN import SN
from ..datatypes.SPS import SPS


class TCC(BaseModel):
    """HL7 v2 TCC segment.

    Attributes
    ----------
    tcc_1 : CWE
        TCC.1 (req) - Universal Service Identifier (CWE)

    tcc_2 : EI
        TCC.2 (req) - Equipment Test Application Identifier (EI)

    tcc_3 : SPS | None
        TCC.3 (opt) - Specimen Source (SPS)

    tcc_4 : SN | None
        TCC.4 (opt) - Auto-Dilution Factor Default (SN)

    tcc_5 : SN | None
        TCC.5 (opt) - Rerun Dilution Factor Default (SN)

    tcc_6 : SN | None
        TCC.6 (opt) - Pre-Dilution Factor Default (SN)

    tcc_7 : SN | None
        TCC.7 (opt) - Endogenous Content of Pre-Dilution Diluent (SN)

    tcc_8 : str | None
        TCC.8 (opt) - Inventory Limits Warning Level (NM)

    tcc_9 : str | None
        TCC.9 (opt) - Automatic Rerun Allowed (ID)

    tcc_10 : str | None
        TCC.10 (opt) - Automatic Repeat Allowed (ID)

    tcc_11 : str | None
        TCC.11 (opt) - Automatic Reflex Allowed (ID)

    tcc_12 : SN | None
        TCC.12 (opt) - Equipment Dynamic Range (SN)

    tcc_13 : CWE | None
        TCC.13 (opt) - Units (CWE)

    tcc_14 : CWE | None
        TCC.14 (opt) - Processing Type (CWE)
    """

    tcc_1: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "tcc_1",
            "universal_service_identifier",
            "TCC.1",
        ),
        serialization_alias="TCC.1",
        title="Universal Service Identifier",
        description="Item #238",
    )

    tcc_2: EI = Field(
        default=...,
        validation_alias=AliasChoices(
            "tcc_2",
            "equipment_test_application_identifier",
            "TCC.2",
        ),
        serialization_alias="TCC.2",
        title="Equipment Test Application Identifier",
        description="Item #1408",
    )

    tcc_3: Optional[SPS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tcc_3",
            "specimen_source",
            "TCC.3",
        ),
        serialization_alias="TCC.3",
        title="Specimen Source",
        description="Item #249",
    )

    tcc_4: Optional[SN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tcc_4",
            "auto_dilution_factor_default",
            "TCC.4",
        ),
        serialization_alias="TCC.4",
        title="Auto-Dilution Factor Default",
        description="Item #1410",
    )

    tcc_5: Optional[SN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tcc_5",
            "rerun_dilution_factor_default",
            "TCC.5",
        ),
        serialization_alias="TCC.5",
        title="Rerun Dilution Factor Default",
        description="Item #1411",
    )

    tcc_6: Optional[SN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tcc_6",
            "pre_dilution_factor_default",
            "TCC.6",
        ),
        serialization_alias="TCC.6",
        title="Pre-Dilution Factor Default",
        description="Item #1412",
    )

    tcc_7: Optional[SN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tcc_7",
            "endogenous_content_of_pre_dilution_diluent",
            "TCC.7",
        ),
        serialization_alias="TCC.7",
        title="Endogenous Content of Pre-Dilution Diluent",
        description="Item #1413",
    )

    tcc_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tcc_8",
            "inventory_limits_warning_level",
            "TCC.8",
        ),
        serialization_alias="TCC.8",
        title="Inventory Limits Warning Level",
        description="Item #1414",
    )

    tcc_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tcc_9",
            "automatic_rerun_allowed",
            "TCC.9",
        ),
        serialization_alias="TCC.9",
        title="Automatic Rerun Allowed",
        description="Item #1415 | Table HL70136",
    )

    tcc_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tcc_10",
            "automatic_repeat_allowed",
            "TCC.10",
        ),
        serialization_alias="TCC.10",
        title="Automatic Repeat Allowed",
        description="Item #1416 | Table HL70136",
    )

    tcc_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tcc_11",
            "automatic_reflex_allowed",
            "TCC.11",
        ),
        serialization_alias="TCC.11",
        title="Automatic Reflex Allowed",
        description="Item #1417 | Table HL70136",
    )

    tcc_12: Optional[SN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tcc_12",
            "equipment_dynamic_range",
            "TCC.12",
        ),
        serialization_alias="TCC.12",
        title="Equipment Dynamic Range",
        description="Item #1418",
    )

    tcc_13: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tcc_13",
            "units",
            "TCC.13",
        ),
        serialization_alias="TCC.13",
        title="Units",
        description="Item #574 | Table HL79999",
    )

    tcc_14: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tcc_14",
            "processing_type",
            "TCC.14",
        ),
        serialization_alias="TCC.14",
        title="Processing Type",
        description="Item #1419 | Table HL70388",
    )

    model_config = {"populate_by_name": True}
