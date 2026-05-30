"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: ODS
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE


class ODS(HL7Model):
    """HL7 v2 ODS segment.

    Attributes
    ----------
    ods_1 : str
        ODS.1 (req) - Type (ID)

    ods_2 : list[CWE] | None
        ODS.2 (opt, rep) - Service Period (CWE)

    ods_3 : list[CWE]
        ODS.3 (req, rep) - Diet, Supplement, or Preference Code (CWE)

    ods_4 : list[str] | None
        ODS.4 (opt, rep) - Text Instruction (ST)
    """

    ods_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "ods_1",
            "type_",
            "ODS.1",
        ),
        serialization_alias="ODS.1",
        title="Type",
        description="Item #269 | Table HL70159",
    )

    ods_2: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ods_2",
            "service_period",
            "ODS.2",
        ),
        serialization_alias="ODS.2",
        title="Service Period",
        description="Item #270 | Table HL79999",
    )

    ods_3: List[CWE] = Field(
        default=...,
        validation_alias=AliasChoices(
            "ods_3",
            "diet_supplement_or_preference_code",
            "ODS.3",
        ),
        serialization_alias="ODS.3",
        title="Diet, Supplement, or Preference Code",
        description="Item #271 | Table HL79999",
    )

    ods_4: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ods_4",
            "text_instruction",
            "ODS.4",
        ),
        serialization_alias="ODS.4",
        title="Text Instruction",
        description="Item #272",
    )

    model_config = {"populate_by_name": True}
