"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: HD
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model


class HD(HL7Model):
    """HL7 v2 HD data type.

    Attributes
    ----------
    hd_1 : str | None
        HD.1 (opt) - Namespace ID (IS)

    hd_2 : str | None
        HD.2 (opt) - Universal ID (ST)

    hd_3 : str | None
        HD.3 (opt) - Universal ID Type (ID)
    """

    hd_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "hd_1",
            "namespace_id",
            "HD.1",
        ),
        serialization_alias="HD.1",
        title="Namespace ID",
    )

    hd_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "hd_2",
            "universal_id",
            "HD.2",
        ),
        serialization_alias="HD.2",
        title="Universal ID",
    )

    hd_3: Optional[str] = Field(
        default=None,
        max_length=6,
        validation_alias=AliasChoices(
            "hd_3",
            "universal_id_type",
            "HD.3",
        ),
        serialization_alias="HD.3",
        title="Universal ID Type",
    )

    model_config = {"populate_by_name": True}
