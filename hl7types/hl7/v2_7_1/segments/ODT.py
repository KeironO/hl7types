"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: ODT
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE


class ODT(HL7Model):
    """Diet Tray Instructions (S4.7.2).

    Attributes
    ----------
    odt_1 : CWE
        ODT.1 - Tray Type (CWE) R S4.7.2.1 | 0160 - Tray Type

    odt_2 : list[CWE] | None
        ODT.2 - Service Period (CWE) O rep S4.7.1.2 | 9999 - no table for CE

    odt_3 : str | None
        ODT.3 - Text Instruction (ST) O S4.7.1.4
    """

    odt_1: CWE = Field(
        validation_alias=AliasChoices(
            "odt_1",
            "tray_type",
            "ODT.1",
        ),
        serialization_alias="ODT.1",
        title="Tray Type",
        description="R | Item #00273 | Table 0160 - Tray Type",
    )

    odt_2: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "odt_2",
            "service_period",
            "ODT.2",
        ),
        serialization_alias="ODT.2",
        title="Service Period",
        description="O | Item #00270 | Table 9999 - no table for CE",
    )

    odt_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "odt_3",
            "text_instruction",
            "ODT.3",
        ),
        serialization_alias="ODT.3",
        title="Text Instruction",
        description="O | Item #00272",
    )

    model_config = ConfigDict(populate_by_name=True)
