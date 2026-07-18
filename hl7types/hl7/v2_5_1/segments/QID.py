"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: QID
Type: Segment
"""
from __future__ import annotations

from pydantic import AliasChoices, ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE


class QID(HL7Model):
    """Query Identification (S5.5.3).

    Attributes
    ----------
    qid_1 : str
        QID.1 - Query Tag (ST) R S5.10.5.1.1

    qid_2 : CE
        QID.2 - Message Query Name (CE) R S5.5.2.3 | 0471 - Query name
    """

    qid_1: str = Field(
        validation_alias=AliasChoices(
            "qid_1",
            "query_tag",
            "QID.1",
        ),
        serialization_alias="QID.1",
        title="Query Tag",
        description="R | Item #00696 | LEN:32",
    )

    qid_2: CE = Field(
        validation_alias=AliasChoices(
            "qid_2",
            "message_query_name",
            "QID.2",
        ),
        serialization_alias="QID.2",
        title="Message Query Name",
        description="R | Item #01375 | Table 0471 - Query name",
    )

    model_config = ConfigDict(populate_by_name=True)
