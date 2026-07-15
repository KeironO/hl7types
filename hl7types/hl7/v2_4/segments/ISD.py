"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: ISD
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE


class ISD(HL7Model):
    """Interaction Status Detail (S13.4.2).

    Attributes
    ----------
    isd_1 : str
        ISD.1 - Reference Interaction Number (unique identifier) (NM) R S13.4.2.1

    isd_2 : CE | None
        ISD.2 - Interaction Type Identifier (CE) O S13.4.2.2 | 0368 - Remote control command

    isd_3 : CE
        ISD.3 - Interaction Active State (CE) R S13.4.2.3 | 0387 - Command response
    """

    isd_1: str = Field(
        validation_alias=AliasChoices(
            "isd_1",
            "reference_interaction_number_unique_identifier",
            "ISD.1",
        ),
        serialization_alias="ISD.1",
        title="Reference Interaction Number (unique identifier)",
        description="R | Item #01326 | LEN:20",
    )

    isd_2: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "isd_2",
            "interaction_type_identifier",
            "ISD.2",
        ),
        serialization_alias="ISD.2",
        title="Interaction Type Identifier",
        description="O | Item #01327 | Table 0368 - Remote control command",
    )

    isd_3: CE = Field(
        validation_alias=AliasChoices(
            "isd_3",
            "interaction_active_state",
            "ISD.3",
        ),
        serialization_alias="ISD.3",
        title="Interaction Active State",
        description="R | Item #01328 | Table 0387 - Command response",
    )

    @field_validator("isd_1", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
