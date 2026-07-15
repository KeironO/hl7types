"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: OM3
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE


class OM3(HL7Model):
    """Categorical Service/Test/Observation (S8.8.10).

    Attributes
    ----------
    om3_1 : str | None
        OM3.1 - Sequence Number - Test/Observation Master File (NM) O S8.8.10.1

    om3_2 : CWE | None
        OM3.2 - Preferred Coding System (CWE) O S8.8.10.2 | 9999 - no table for CE

    om3_3 : list[CWE] | None
        OM3.3 - Valid Coded "Answers" (CWE) O rep S8.8.10.3 | 9999 - no table for CE

    om3_4 : list[CWE] | None
        OM3.4 - Normal Text/Codes for Categorical Observations (CWE) O rep S8.8.10.4 | 9999 - no table for CE

    om3_5 : list[CWE] | None
        OM3.5 - Abnormal Text/Codes for Categorical Observations (CWE) O rep S8.8.10.5 | 9999 - no table for CE

    om3_6 : list[CWE] | None
        OM3.6 - Critical Text/Codes for Categorical Observations (CWE) O rep S8.8.10.6 | 9999 - no table for CE

    om3_7 : str | None
        OM3.7 - Value Type (ID) O S7.4.2.2 | 0125 - Value type
    """

    om3_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om3_1",
            "sequence_number_test_observation_master_file",
            "OM3.1",
        ),
        serialization_alias="OM3.1",
        title="Sequence Number - Test/Observation Master File",
        description="O | Item #00586 | LEN:4",
    )

    om3_2: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om3_2",
            "preferred_coding_system",
            "OM3.2",
        ),
        serialization_alias="OM3.2",
        title="Preferred Coding System",
        description="O | Item #00636 | Table 9999 - no table for CE",
    )

    om3_3: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om3_3",
            "valid_coded_answers",
            "OM3.3",
        ),
        serialization_alias="OM3.3",
        title="Valid Coded \"Answers\"",
        description="O | Item #00637 | Table 9999 - no table for CE",
    )

    om3_4: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om3_4",
            "normal_text_codes_for_categorical_observations",
            "OM3.4",
        ),
        serialization_alias="OM3.4",
        title="Normal Text/Codes for Categorical Observations",
        description="O | Item #00638 | Table 9999 - no table for CE",
    )

    om3_5: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om3_5",
            "abnormal_text_codes_for_categorical_observations",
            "OM3.5",
        ),
        serialization_alias="OM3.5",
        title="Abnormal Text/Codes for Categorical Observations",
        description="O | Item #00639 | Table 9999 - no table for CE",
    )

    om3_6: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om3_6",
            "critical_text_codes_for_categorical_observations",
            "OM3.6",
        ),
        serialization_alias="OM3.6",
        title="Critical Text/Codes for Categorical Observations",
        description="O | Item #00640 | Table 9999 - no table for CE",
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
        description="O | Item #00570 | Table 0125 - Value type | LEN:3",
    )

    @field_validator("om3_1", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
