"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: QID
Type: Segment
"""
from __future__ import annotations

from pydantic import AliasChoices, ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE


class QID(HL7Model):
    """Query Identification (S5.5.3).

    Attributes
    ----------
    qid_1 : str
        QID.1 - Query Tag (ST) R S5.5.2.1

    qid_2 : CWE
        QID.2 - Message Query Name (CWE) R S5.5.2.3 | 0471 - Query Name
    """

    qid_1: str = Field(
        validation_alias=AliasChoices(
            "qid_1",
            "query_tag",
            "QID.1",
        ),
        serialization_alias="QID.1",
        title="Query Tag",
        description="R | Item #00696",
    )

    qid_2: CWE = Field(
        validation_alias=AliasChoices(
            "qid_2",
            "message_query_name",
            "QID.2",
        ),
        serialization_alias="QID.2",
        title="Message Query Name",
        description="R | Item #01375 | Table 0471 - Query Name",
    )

    model_config = ConfigDict(populate_by_name=True)
