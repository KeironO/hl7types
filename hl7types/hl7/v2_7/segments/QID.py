"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: QID
Type: Segment
"""
from __future__ import annotations

from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE


class QID(HL7Model):
    """HL7 v2 QID segment.

    Attributes
    ----------
    qid_1 : str
        QID.1 (req) - Query Tag (ST)

    qid_2 : CWE
        QID.2 (req) - Message Query Name (CWE)
    """

    qid_1: str = Field(
        validation_alias=AliasChoices(
            "qid_1",
            "query_tag",
            "QID.1",
        ),
        serialization_alias="QID.1",
        title="Query Tag",
        description="Item #696",
    )

    qid_2: CWE = Field(
        validation_alias=AliasChoices(
            "qid_2",
            "message_query_name",
            "QID.2",
        ),
        serialization_alias="QID.2",
        title="Message Query Name",
        description="Item #1375 | Table HL70471",
    )

    model_config = {"populate_by_name": True}
