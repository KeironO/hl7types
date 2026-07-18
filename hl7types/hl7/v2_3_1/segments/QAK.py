"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: QAK
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field
from hl7types.hl7 import HL7Model


class QAK(HL7Model):
    """Query Acknowledgement (S2.24.22).

    Attributes
    ----------
    qak_1 : str | None
        QAK.1 - Query Tag (ST) C S2.24.22.1

    qak_2 : str | None
        QAK.2 - Query Response Status (ID) O S2.24.22.2 | 0208 - Query response status
    """

    qak_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "qak_1",
            "query_tag",
            "QAK.1",
        ),
        serialization_alias="QAK.1",
        title="Query Tag",
        description="C | Item #00696 | LEN:32",
    )

    qak_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "qak_2",
            "query_response_status",
            "QAK.2",
        ),
        serialization_alias="QAK.2",
        title="Query Response Status",
        description=(
            "O | Item #00708 | Table 0208 - Query response status | LEN:2"
        ),
    )

    model_config = ConfigDict(populate_by_name=True)
