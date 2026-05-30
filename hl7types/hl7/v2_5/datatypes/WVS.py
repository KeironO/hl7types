"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: WVS
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model


class WVS(HL7Model):
    """HL7 v2 WVS data type.

    Attributes
    ----------
    wvs_1 : str | None
        WVS.1 (opt) - Source One Name (ST)

    wvs_2 : str | None
        WVS.2 (opt) - Source Two Name (ST)
    """

    wvs_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "wvs_1",
            "source_one_name",
            "WVS.1",
        ),
        serialization_alias="WVS.1",
        title="Source One Name",
    )

    wvs_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "wvs_2",
            "source_two_name",
            "WVS.2",
        ),
        serialization_alias="WVS.2",
        title="Source Two Name",
    )

    model_config = {"populate_by_name": True}
