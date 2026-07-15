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
    """Supporting Clinical Information (S8.8.16).

    Attributes
    ----------
    omc_1 : str | None
        OMC.1 - Sequence Number - Test/Observation Master File (NM) O S8.8.10.1

    omc_2 : str | None
        OMC.2 - Segment Action Code (ID) NA S8.8.16.2 | 0206 - Segment Action Code

    omc_3 : EI | None
        OMC.3 - Segment Unique Key (EI) NA S8.8.16.3

    omc_4 : CWE
        OMC.4 - Clinical Information Request (CWE) R S8.8.16.4 | 9999 - no table for CE

    omc_5 : list[CWE]
        OMC.5 - Collection Event/Process Step (CWE) R rep S8.8.16.5 | 0938 - Collection Event/Process Step Limit

    omc_6 : CWE
        OMC.6 - Communication Location (CWE) R S8.8.16.6 | 0939 - Communication Location

    omc_7 : str | None
        OMC.7 - Answer Required (ID) O S8.8.16.7 | 0136 - Yes/no Indicator

    omc_8 : str | None
        OMC.8 - Hint/Help Text (ST) O S8.8.16.8

    omc_9 : varies | None
        OMC.9 - Type of Answer (varies) O S8.8.16.9 | 0125 - Value Type

    omc_10 : str | None
        OMC.10 - Multiple Answers Allowed (ID) O S8.8.16.10 | 0136 - Yes/no Indicator

    omc_11 : list[CWE] | None
        OMC.11 - Answer Choices (CWE) O rep S8.8.16.11 | 9999 - no table for CE

    omc_12 : str | None
        OMC.12 - Character Limit (NM) O S8.8.16.12

    omc_13 : str | None
        OMC.13 - Number of Decimals (NM) O S8.8.16.13
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
        description="O | Item #00586",
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
        description="NA | Item #00763 | Table 0206 - Segment Action Code",
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
        description="NA | Item #00764",
    )

    omc_4: CWE = Field(
        validation_alias=AliasChoices(
            "omc_4",
            "clinical_information_request",
            "OMC.4",
        ),
        serialization_alias="OMC.4",
        title="Clinical Information Request",
        description="R | Item #03444 | Table 9999 - no table for CE",
    )

    omc_5: List[CWE] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "omc_5",
            "collection_event_process_step",
            "OMC.5",
        ),
        serialization_alias="OMC.5",
        title="Collection Event/Process Step",
        description=(
            "R | Item #03445 | Table 0938 - Collection Event/Process Step Limit"
        ),
    )

    omc_6: CWE = Field(
        validation_alias=AliasChoices(
            "omc_6",
            "communication_location",
            "OMC.6",
        ),
        serialization_alias="OMC.6",
        title="Communication Location",
        description="R | Item #03446 | Table 0939 - Communication Location",
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
        description="O | Item #03447 | Table 0136 - Yes/no Indicator",
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
        description="O | Item #03448",
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
        description="O | Item #03449 | Table 0125 - Value Type",
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
        description="O | Item #03450 | Table 0136 - Yes/no Indicator",
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
        description="O | Item #03451 | Table 9999 - no table for CE",
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
        description="O | Item #03452",
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
        description="O | Item #03453",
    )

    @field_validator("omc_1", "omc_12", "omc_13", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
