"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: FC
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from .TS import TS


class FC(HL7Model):
    """HL7 v2 FC data type.

    Attributes
    ----------
    fc_1 : str | None
        FC.1 (opt) - Financial Class (IS)

    fc_2 : TS | None
        FC.2 (opt) - Effective Date (TS)
    """

    fc_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "fc_1",
            "financial_class",
            "FC.1",
        ),
        serialization_alias="FC.1",
        title="Financial Class",
    )

    fc_2: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "fc_2",
            "effective_date",
            "FC.2",
        ),
        serialization_alias="FC.2",
        title="Effective Date",
    )

    model_config = {"populate_by_name": True}
