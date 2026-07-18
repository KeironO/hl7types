"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
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
    """Event Replay Query (S5.10.5.2).

    Attributes
    ----------
    erq_1 : str | None
        ERQ.1 - Query Tag (ST) O S5.10.5.8.1

    erq_2 : CE
        ERQ.2 - Event Identifier (CE) R S5.10.5.2.2

    erq_3 : list[QIP] | None
        ERQ.3 - Input Parameter List (QIP) O rep S5.10.5.5.4
    """

    erq_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "erq_1",
            "query_tag",
            "ERQ.1",
        ),
        serialization_alias="ERQ.1",
        title="Query Tag",
        description="O | Item #00696 | LEN:32",
    )

    erq_2: CE = Field(
        validation_alias=AliasChoices(
            "erq_2",
            "event_identifier",
            "ERQ.2",
        ),
        serialization_alias="ERQ.2",
        title="Event Identifier",
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
        title="Input Parameter List",
        description="O | Item #00705",
    )

    model_config = ConfigDict(populate_by_name=True)
