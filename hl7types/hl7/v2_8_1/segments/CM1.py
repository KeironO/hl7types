"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: CM1
Type: Segment
"""
from __future__ import annotations

from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE


class CM1(HL7Model):
    """Clinical Study Phase Master (S8.11.3).

    Attributes
    ----------
    cm1_1 : str
        CM1.1 - Set ID - CM1 (SI) R S8.11.3.1

    cm1_2 : CWE
        CM1.2 - Study Phase Identifier (CWE) R S8.11.3.2

    cm1_3 : str
        CM1.3 - Description of Study Phase (ST) R S8.11.3.3
    """

    cm1_1: str = Field(
        validation_alias=AliasChoices(
            "cm1_1",
            "set_id_cm1",
            "CM1.1",
        ),
        serialization_alias="CM1.1",
        title="Set ID - CM1",
        description="R | Item #01021 | LEN:4",
    )

    cm1_2: CWE = Field(
        validation_alias=AliasChoices(
            "cm1_2",
            "study_phase_identifier",
            "CM1.2",
        ),
        serialization_alias="CM1.2",
        title="Study Phase Identifier",
        description="R | Item #01022",
    )

    cm1_3: str = Field(
        validation_alias=AliasChoices(
            "cm1_3",
            "description_of_study_phase",
            "CM1.3",
        ),
        serialization_alias="CM1.3",
        title="Description of Study Phase",
        description="R | Item #01023",
    )

    @field_validator("cm1_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    model_config = {"populate_by_name": True}
