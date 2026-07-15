"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: QPD
Type: Segment
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE


class QPD(HL7Model):
    """Query Parameter Definition (S5.5.4).

    Attributes
    ----------
    qpd_1 : CE
        QPD.1 - Message Query Name (CE) R S5.5.2.3 | 0471 - Query name

    qpd_2 : str | None
        QPD.2 - Query Tag (ST) C S5.10.5.1.1

    qpd_3 : str | None
        QPD.3 - User Parameters (in successive fields) (var) O S5.5.4.3
    """

    qpd_1: CE = Field(
        validation_alias=AliasChoices(
            "qpd_1",
            "message_query_name",
            "QPD.1",
        ),
        serialization_alias="QPD.1",
        title="Message Query Name",
        description="R | Item #01375 | Table 0471 - Query name",
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
        description="C | Item #00696 | LEN:32",
    )

    qpd_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "qpd_3",
            "user_parameters_in_successive_fields",
            "QPD.3",
        ),
        serialization_alias="QPD.3",
        title="User Parameters (in successive fields)",
        description="O | Item #01435",
    )

    model_config = {"populate_by_name": True}
