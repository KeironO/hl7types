"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
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
    """HL7 v2 ERQ segment.

    Attributes
    ----------
    erq_1 : str | None
        ERQ.1 (opt) - Query tag (ST)

    erq_2 : CE
        ERQ.2 (req) - Event identifier (CE)

    erq_3 : list[QIP] | None
        ERQ.3 (opt, rep) - Input parameter list (QIP)
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
        description="Item #696",
    )

    erq_2: CE = Field(
        validation_alias=AliasChoices(
            "erq_2",
            "event_identifier",
            "ERQ.2",
        ),
        serialization_alias="ERQ.2",
        title="Event identifier",
        description="Item #706",
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
        description="Item #705",
    )

    model_config = {"populate_by_name": True}
