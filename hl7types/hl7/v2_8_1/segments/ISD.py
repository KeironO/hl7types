"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: ISD
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE

_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class ISD(HL7Model):
    """Interaction Status Detail (S13.4.2).

    Attributes
    ----------
    isd_1 : str
        ISD.1 - Reference Interaction Number (NM) R S13.4.2.1

    isd_2 : CWE | None
        ISD.2 - Interaction Type Identifier (CWE) O S13.4.2.2 | 0368 - Remote Control Command

    isd_3 : CWE
        ISD.3 - Interaction Active State (CWE) R S13.4.2.3 | 0387 - Command Response
    """

    isd_1: str = Field(
        validation_alias=AliasChoices(
            "isd_1",
            "reference_interaction_number",
            "ISD.1",
        ),
        serialization_alias="ISD.1",
        title="Reference Interaction Number",
        description="R | Item #01326",
    )

    isd_2: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "isd_2",
            "interaction_type_identifier",
            "ISD.2",
        ),
        serialization_alias="ISD.2",
        title="Interaction Type Identifier",
        description="O | Item #01327 | Table 0368 - Remote Control Command",
    )

    isd_3: CWE = Field(
        validation_alias=AliasChoices(
            "isd_3",
            "interaction_active_state",
            "ISD.3",
        ),
        serialization_alias="ISD.3",
        title="Interaction Active State",
        description="R | Item #01328 | Table 0387 - Command Response",
    )

    @field_validator("isd_1", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
