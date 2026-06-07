"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: ODT
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE


class ODT(HL7Model):
    """HL7 v2 ODT segment.

    Attributes
    ----------
    odt_1 : CWE
        ODT.1 (req) - Tray Type (CWE)

    odt_2 : list[CWE] | None
        ODT.2 (opt, rep) - Service Period (CWE)

    odt_3 : str | None
        ODT.3 (opt) - Text Instruction (ST)
    """

    odt_1: CWE = Field(
        validation_alias=AliasChoices(
            "odt_1",
            "tray_type",
            "ODT.1",
        ),
        serialization_alias="ODT.1",
        title="Tray Type",
        description="Item #273 | Table HL70160",
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
        description="Item #270 | Table HL79999",
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
        description="Item #272",
    )

    model_config = {"populate_by_name": True}
