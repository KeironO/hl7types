"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: ED
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from .HD import HD


class ED(BaseModel):
    """HL7 v2 ED data type.

    Attributes
    ----------
    ed_1 : HD | None
        ED.1 (opt) - source application (HD)

    ed_2 : str | None
        ED.2 (opt) - type of data (ID)

    ed_3 : str | None
        ED.3 (opt) - data (ID)

    ed_4 : str | None
        ED.4 (opt) - encoding (ID)

    ed_5 : str | None
        ED.5 (opt) - data (ST)
    """

    ed_1: Optional[HD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ed_1",
            "source_application",
            "ED.1",
        ),
        serialization_alias="ED.1",
        title="source application",
    )

    ed_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ed_2",
            "type_of_data",
            "ED.2",
        ),
        serialization_alias="ED.2",
        title="type of data",
    )

    ed_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ed_3",
            "data",
            "ED.3",
        ),
        serialization_alias="ED.3",
        title="data",
    )

    ed_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ed_4",
            "encoding",
            "ED.4",
        ),
        serialization_alias="ED.4",
        title="encoding",
    )

    ed_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ed_5",
            "data",
            "ED.5",
        ),
        serialization_alias="ED.5",
        title="data",
    )

    model_config = {"populate_by_name": True}
