"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: QPD
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CWE import CWE
from ..datatypes.varies import varies


class QPD(BaseModel):
    """HL7 v2 QPD segment."""

    qpd_1: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "qpd_1",
            "message_query_name",
            "QPD.1",
        ),
        serialization_alias="QPD.1",
        title="Message Query Name",
        description="Item #1375 | Table HL70471",
    )

    qpd_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "qpd_2",
            "query_tag",
            "QPD.2",
        ),
        serialization_alias="QPD.2",
        title="Query Tag",
        description="Item #696",
    )

    qpd_3: varies | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "qpd_3",
            "user_parameters_in_successive_fields",
            "QPD.3",
        ),
        serialization_alias="QPD.3",
        title="User Parameters (in successive fields)",
        description="Item #1435",
    )

    model_config = {"populate_by_name": True}
