"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: ERQ
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.QIP import QIP


class ERQ(HL7Model):
    """Event Replay Query Segment (S2.24.21).

    Attributes
    ----------
    erq_1 : str | None
        ERQ.1 - Query tag (ST) O S2.24.16

    erq_2 : CE
        ERQ.2 - Event identifier (CE) R S2.24.21.2

    erq_3 : list[QIP] | None
        ERQ.3 - Input parameter list (QIP) O rep S2.24.20
    """

    erq_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "erq_1",
            "query_tag",
            "ERQ.1",
        ),
        serialization_alias="ERQ.1",
        title="Query tag",
        description="O | Item #00696 | LEN:32",
    )

    erq_2: CE = Field(
        validation_alias=AliasChoices(
            "erq_2",
            "event_identifier",
            "ERQ.2",
        ),
        serialization_alias="ERQ.2",
        title="Event identifier",
        description="R | Item #00706",
    )

    erq_3: Optional[List[QIP]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "erq_3",
            "input_parameter_list",
            "ERQ.3",
        ),
        serialization_alias="ERQ.3",
        title="Input parameter list",
        description="O | Item #00705",
    )

    model_config = ConfigDict(populate_by_name=True)
