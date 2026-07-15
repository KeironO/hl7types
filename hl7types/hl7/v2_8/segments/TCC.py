"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: TCC
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE
from ..datatypes.EI import EI
from ..datatypes.SN import SN


class TCC(HL7Model):
    """Test Code Configuration (S13.4.9).

    Attributes
    ----------
    tcc_1 : CWE
        TCC.1 - Universal Service Identifier (CWE) R S10.6.4.3

    tcc_2 : EI
        TCC.2 - Equipment Test Application Identifier (EI) R S13.4.9.2

    tcc_4 : SN | None
        TCC.4 - Auto-Dilution Factor Default (SN) O S13.4.9.4

    tcc_5 : SN | None
        TCC.5 - Rerun Dilution Factor Default (SN) O S13.4.9.5

    tcc_6 : SN | None
        TCC.6 - Pre-Dilution Factor Default (SN) O S13.4.9.6

    tcc_7 : SN | None
        TCC.7 - Endogenous Content of Pre-Dilution Diluent (SN) O S13.4.10.5

    tcc_8 : str | None
        TCC.8 - Inventory Limits Warning Level (NM) O S13.4.9.8

    tcc_9 : str | None
        TCC.9 - Automatic Rerun Allowed (ID) O S13.4.9.9 | 0136 - Yes/no Indicator

    tcc_10 : str | None
        TCC.10 - Automatic Repeat Allowed (ID) O S13.4.10.6 | 0136 - Yes/no Indicator

    tcc_11 : str | None
        TCC.11 - Automatic Reflex Allowed (ID) O S13.4.9.11 | 0136 - Yes/no Indicator

    tcc_12 : SN | None
        TCC.12 - Equipment Dynamic Range (SN) O S13.4.9.12

    tcc_13 : CWE | None
        TCC.13 - Units (CWE) O S7.16.4.6

    tcc_14 : CWE | None
        TCC.14 - Processing Type (CWE) O S13.4.9.14 | 0388 - Processing Type

    tcc_15 : CWE | None
        TCC.15 - Test Criticality (CWE) O S13.4.9.15
    """

    tcc_1: CWE = Field(
        validation_alias=AliasChoices(
            "tcc_1",
            "universal_service_identifier",
            "TCC.1",
        ),
        serialization_alias="TCC.1",
        title="Universal Service Identifier",
        description="R | Item #00238",
    )

    tcc_2: EI = Field(
        validation_alias=AliasChoices(
            "tcc_2",
            "equipment_test_application_identifier",
            "TCC.2",
        ),
        serialization_alias="TCC.2",
        title="Equipment Test Application Identifier",
        description="R | Item #01408",
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
        description="O | Item #01410",
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
        description="O | Item #01411",
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
        description="O | Item #01412",
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
        description="O | Item #01413",
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
        description="O | Item #01414",
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
        description="O | Item #01415 | Table 0136 - Yes/no Indicator | LEN:1",
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
        description="O | Item #01416 | Table 0136 - Yes/no Indicator | LEN:1",
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
        description="O | Item #01417 | Table 0136 - Yes/no Indicator | LEN:1",
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
        description="O | Item #01418",
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
        description="O | Item #00574",
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
        description="O | Item #01419 | Table 0388 - Processing Type",
    )

    tcc_15: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "tcc_15",
            "test_criticality",
            "TCC.15",
        ),
        serialization_alias="TCC.15",
        title="Test Criticality",
        description="O | Item #03313",
    )

    @field_validator("tcc_8", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
