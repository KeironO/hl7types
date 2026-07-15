"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: ODS
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE


class ODS(HL7Model):
    """Dietary Orders, Supplements, and Preferences (S4.8.1).

    Attributes
    ----------
    ods_1 : str
        ODS.1 - Type (ID) R S4.8.1.1 | 0159 - Diet Code Specification Type

    ods_2 : list[CWE] | None
        ODS.2 - Service Period (CWE) O rep S4.8.1.2 | 9999 - no table for CE

    ods_3 : list[CWE]
        ODS.3 - Diet, Supplement, or Preference Code (CWE) R rep S4.8.1.3 | 9999 - no table for CE

    ods_4 : list[str] | None
        ODS.4 - Text Instruction (ST) O rep S4.8.1.4
    """

    ods_1: str = Field(
        validation_alias=AliasChoices(
            "ods_1",
            "type_",
            "ODS.1",
        ),
        serialization_alias="ODS.1",
        title="Type",
        description=(
            "R | Item #00269 | Table 0159 - Diet Code Specification Type | LEN:1"
        ),
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
        description="O | Item #00270 | Table 9999 - no table for CE",
    )

    ods_3: List[CWE] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "ods_3",
            "diet_supplement_or_preference_code",
            "ODS.3",
        ),
        serialization_alias="ODS.3",
        title="Diet, Supplement, or Preference Code",
        description="R | Item #00271 | Table 9999 - no table for CE",
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
        description="O | Item #00272",
    )

    model_config = {"populate_by_name": True}
