"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: ERQ
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.QIP import QIP


class ERQ(HL7Model):
    """ERQ - event replay query segment (S2.24.21).

    Attributes
    ----------
    erq_1 : str | None
        ERQ.1 - Query Tag (ST) O S2.24.22.1

    erq_2 : CE
        ERQ.2 - Event Identifier (CE) R S2.24.21.2

    erq_3 : list[QIP] | None
        ERQ.3 - Input Parameter List (QIP) O rep S2.24.21.3
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

    model_config = {"populate_by_name": True}
