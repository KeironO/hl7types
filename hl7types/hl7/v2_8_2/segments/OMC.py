"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: OMC
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE
from ..datatypes.EI import EI
from ..datatypes.varies import varies


class OMC(HL7Model):
    """HL7 v2 OMC segment.

    Attributes
    ----------
    omc_1 : str | None
        OMC.1 (opt) - Sequence Number - Test/Observation Master File (NM)

    omc_2 : str | None
        OMC.2 (opt) - Segment Action Code (ID)

    omc_3 : EI | None
        OMC.3 (opt) - Segment Unique Key (EI)

    omc_4 : CWE
        OMC.4 (req) - Clinical Information Request (CWE)

    omc_5 : list[CWE] | None
        OMC.5 (req, rep) - Collection Event/Process Step (CWE) [optional: CWE has no required components]

    omc_6 : CWE
        OMC.6 (req) - Communication Location (CWE)

    omc_7 : str | None
        OMC.7 (opt) - Answer Required (ID)

    omc_8 : str | None
        OMC.8 (opt) - Hint/Help Text (ST)

    omc_9 : varies | None
        OMC.9 (opt) - Type of Answer (varies)

    omc_10 : str | None
        OMC.10 (opt) - Multiple Answers Allowed (ID)

    omc_11 : list[CWE] | None
        OMC.11 (opt, rep) - Answer Choices (CWE)

    omc_12 : str | None
        OMC.12 (opt) - Character Limit (NM)

    omc_13 : str | None
        OMC.13 (opt) - Number of Decimals (NM)
    """

    omc_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "omc_1",
            "sequence_number_test_observation_master_file",
            "OMC.1",
        ),
        serialization_alias="OMC.1",
        title="Sequence Number - Test/Observation Master File",
        description="Item #586",
    )

    omc_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "omc_2",
            "segment_action_code",
            "OMC.2",
        ),
        serialization_alias="OMC.2",
        title="Segment Action Code",
        description="Item #763 | Table HL70206",
    )

    omc_3: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "omc_3",
            "segment_unique_key",
            "OMC.3",
        ),
        serialization_alias="OMC.3",
        title="Segment Unique Key",
        description="Item #764",
    )

    omc_4: CWE = Field(
        validation_alias=AliasChoices(
            "omc_4",
            "clinical_information_request",
            "OMC.4",
        ),
        serialization_alias="OMC.4",
        title="Clinical Information Request",
        description="Item #3444 | Table HL79999",
    )

    omc_5: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "omc_5",
            "collection_event_process_step",
            "OMC.5",
        ),
        serialization_alias="OMC.5",
        title="Collection Event/Process Step",
        description="Item #3445 | Table HL70938",
    )

    omc_6: CWE = Field(
        validation_alias=AliasChoices(
            "omc_6",
            "communication_location",
            "OMC.6",
        ),
        serialization_alias="OMC.6",
        title="Communication Location",
        description="Item #3446 | Table HL70939",
    )

    omc_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "omc_7",
            "answer_required",
            "OMC.7",
        ),
        serialization_alias="OMC.7",
        title="Answer Required",
        description="Item #3447 | Table HL70136",
    )

    omc_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "omc_8",
            "hint_help_text",
            "OMC.8",
        ),
        serialization_alias="OMC.8",
        title="Hint/Help Text",
        description="Item #3448",
    )

    omc_9: Optional[varies] = Field(
        default=None,
        validation_alias=AliasChoices(
            "omc_9",
            "type_of_answer",
            "OMC.9",
        ),
        serialization_alias="OMC.9",
        title="Type of Answer",
        description="Item #3449 | Table HL70125",
    )

    omc_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "omc_10",
            "multiple_answers_allowed",
            "OMC.10",
        ),
        serialization_alias="OMC.10",
        title="Multiple Answers Allowed",
        description="Item #3450 | Table HL70136",
    )

    omc_11: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "omc_11",
            "answer_choices",
            "OMC.11",
        ),
        serialization_alias="OMC.11",
        title="Answer Choices",
        description="Item #3451 | Table HL79999",
    )

    omc_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "omc_12",
            "character_limit",
            "OMC.12",
        ),
        serialization_alias="OMC.12",
        title="Character Limit",
        description="Item #3452",
    )

    omc_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "omc_13",
            "number_of_decimals",
            "OMC.13",
        ),
        serialization_alias="OMC.13",
        title="Number of Decimals",
        description="Item #3453",
    )

    @field_validator("omc_1", "omc_12", "omc_13", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
