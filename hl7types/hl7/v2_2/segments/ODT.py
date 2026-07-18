"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: ODT
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE


class ODT(HL7Model):
    """DIET TRAY INSTRUCTION (S4.6.2).

    Attributes
    ----------
    odt_1 : CE
        ODT.1 - Tray Type (CE) R S4.6.2.1 | 0160 - TRAY TYPE

    odt_2 : list[CE] | None
        ODT.2 - Service Period (CE) NA rep S4.6.1.2

    odt_3 : list[str] | None
        ODT.3 - Text Instruction (ST) NA rep S4.6.2.3
    """

    odt_1: CE = Field(
        validation_alias=AliasChoices(
            "odt_1",
            "tray_type",
            "ODT.1",
        ),
        serialization_alias="ODT.1",
        title="Tray Type",
        description="R | Item #00273 | Table 0160 - TRAY TYPE",
    )

    odt_2: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "odt_2",
            "service_period",
            "ODT.2",
        ),
        serialization_alias="ODT.2",
        title="Service Period",
        description="NA | Item #00270",
    )

    odt_3: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "odt_3",
            "text_instruction",
            "ODT.3",
        ),
        serialization_alias="ODT.3",
        title="Text Instruction",
        description="NA | Item #00272 | LEN:80",
    )

    model_config = ConfigDict(populate_by_name=True)
