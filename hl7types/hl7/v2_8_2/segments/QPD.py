"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: QPD
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CWE import CWE
from ..datatypes.varies import varies


class QPD(BaseModel):
    """HL7 v2 QPD segment.

    Attributes
    ----------
    qpd_1 : CWE
        QPD.1 (req) - Message Query Name (CWE)

    qpd_2 : str | None
        QPD.2 (opt) - Query Tag (ST)

    qpd_3 : varies | None
        QPD.3 (opt) - User Parameters (in successive fields) (varies)
    """

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

    qpd_2: Optional[str] = Field(
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

    qpd_3: Optional[varies] = Field(
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
