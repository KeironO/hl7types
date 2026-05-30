"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: QAK
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model


class QAK(HL7Model):
    """HL7 v2 QAK segment.

    Attributes
    ----------
    qak_1 : str | None
        QAK.1 (opt) - Query tag (ST)

    qak_2 : str | None
        QAK.2 (opt) - Query response status (ID)
    """

    qak_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "qak_1",
            "query_tag",
            "QAK.1",
        ),
        serialization_alias="QAK.1",
        title="Query tag",
        description="Item #696",
    )

    qak_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "qak_2",
            "query_response_status",
            "QAK.2",
        ),
        serialization_alias="QAK.2",
        title="Query response status",
        description="Item #708 | Table HL70208",
    )

    model_config = {"populate_by_name": True}
