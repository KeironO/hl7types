"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: OM3
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator

from ..datatypes.CE import CE


class OM3(HL7Model):
    """HL7 v2 OM3 segment.

    Attributes
    ----------
    om3_1 : str | None
        OM3.1 (opt) - Sequence Number - Test/ Observation Master File (NM)

    om3_2 : CE | None
        OM3.2 (opt) - Preferred Coding System (CE)

    om3_3 : CE | None
        OM3.3 (opt) - Valid Coded "Answers" (CE)

    om3_4 : list[CE] | None
        OM3.4 (opt, rep) - Normal Text/Codes for Categorical Observations (CE)

    om3_5 : CE | None
        OM3.5 (opt) - Abnormal Text/Codes for Categorical Observations (CE)

    om3_6 : CE | None
        OM3.6 (opt) - Critical Text/Codes for Categorical Observations (CE)

    om3_7 : str | None
        OM3.7 (opt) - Value Type (ID)
    """

    om3_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om3_1",
            "sequence_number_test_observation_master_file",
            "OM3.1",
        ),
        serialization_alias="OM3.1",
        title="Sequence Number - Test/ Observation Master File",
        description="Item #586",
    )

    om3_2: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om3_2",
            "preferred_coding_system",
            "OM3.2",
        ),
        serialization_alias="OM3.2",
        title="Preferred Coding System",
        description="Item #636 | Table HL79999",
    )

    om3_3: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om3_3",
            "valid_coded_answers",
            "OM3.3",
        ),
        serialization_alias="OM3.3",
        title="Valid Coded \"Answers\"",
        description="Item #637 | Table HL79999",
    )

    om3_4: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om3_4",
            "normal_text_codes_for_categorical_observations",
            "OM3.4",
        ),
        serialization_alias="OM3.4",
        title="Normal Text/Codes for Categorical Observations",
        description="Item #638 | Table HL79999",
    )

    om3_5: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om3_5",
            "abnormal_text_codes_for_categorical_observations",
            "OM3.5",
        ),
        serialization_alias="OM3.5",
        title="Abnormal Text/Codes for Categorical Observations",
        description="Item #639 | Table HL79999",
    )

    om3_6: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om3_6",
            "critical_text_codes_for_categorical_observations",
            "OM3.6",
        ),
        serialization_alias="OM3.6",
        title="Critical Text/Codes for Categorical Observations",
        description="Item #640 | Table HL79999",
    )

    om3_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om3_7",
            "value_type",
            "OM3.7",
        ),
        serialization_alias="OM3.7",
        title="Value Type",
        description="Item #570 | Table HL70125",
    )

    @field_validator("om3_1", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
