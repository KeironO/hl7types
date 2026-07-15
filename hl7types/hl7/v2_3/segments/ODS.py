"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: ODS
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE


class ODS(HL7Model):
    """Dietary orders, supplements, and preferences (S4.6.1).

    Attributes
    ----------
    ods_1 : str
        ODS.1 - Type (ID) R S4.6.1 | 0159 - Diet Type

    ods_2 : list[CE] | None
        ODS.2 - Service Period (CE) O rep S4.6.1.2

    ods_3 : list[CE]
        ODS.3 - Diet, Supplement, or Preference Code (CE) R rep S4.6.1.3

    ods_4 : str | None
        ODS.4 - Text Instruction (ST) O S4.6.1
    """

    ods_1: str = Field(
        validation_alias=AliasChoices(
            "ods_1",
            "type_",
            "ODS.1",
        ),
        serialization_alias="ODS.1",
        title="Type",
        description="R | Item #00269 | Table 0159 - Diet Type | LEN:1",
    )

    ods_2: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ods_2",
            "service_period",
            "ODS.2",
        ),
        serialization_alias="ODS.2",
        title="Service Period",
        description="O | Item #00270",
    )

    ods_3: List[CE] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "ods_3",
            "diet_supplement_or_preference_code",
            "ODS.3",
        ),
        serialization_alias="ODS.3",
        title="Diet, Supplement, or Preference Code",
        description="R | Item #00271",
    )

    ods_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ods_4",
            "text_instruction",
            "ODS.4",
        ),
        serialization_alias="ODS.4",
        title="Text Instruction",
        description="O | Item #00272 | LEN:80",
    )

    model_config = {"populate_by_name": True}
