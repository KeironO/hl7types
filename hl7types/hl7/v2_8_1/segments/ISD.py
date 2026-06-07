"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: ISD
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE


class ISD(HL7Model):
    """HL7 v2 ISD segment.

    Attributes
    ----------
    isd_1 : str
        ISD.1 (req) - Reference Interaction Number (NM)

    isd_2 : CWE | None
        ISD.2 (opt) - Interaction Type Identifier (CWE)

    isd_3 : CWE
        ISD.3 (req) - Interaction Active State (CWE)
    """

    isd_1: str = Field(
        validation_alias=AliasChoices(
            "isd_1",
            "reference_interaction_number",
            "ISD.1",
        ),
        serialization_alias="ISD.1",
        title="Reference Interaction Number",
        description="Item #1326",
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
        description="Item #1327 | Table HL70368",
    )

    isd_3: CWE = Field(
        validation_alias=AliasChoices(
            "isd_3",
            "interaction_active_state",
            "ISD.3",
        ),
        serialization_alias="ISD.3",
        title="Interaction Active State",
        description="Item #1328 | Table HL70387",
    )

    @field_validator("isd_1", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
