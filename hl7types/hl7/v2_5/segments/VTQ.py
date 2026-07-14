"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: VTQ
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.QSC import QSC


class VTQ(HL7Model):
    """Virtual Table Query Request (S5.10.5.8).

    Attributes
    ----------
    vtq_1 : str | None
        VTQ.1 (opt) - Query Tag (ST) S5.5.2.1

    vtq_2 : str
        VTQ.2 (req) - Query/Response Format Code (ID) S5.10.5.1.2 | 0106 - Query/response format code

    vtq_3 : CE
        VTQ.3 (req) - VT Query Name (CE) S5.10.5.8.3

    vtq_4 : CE
        VTQ.4 (req) - Virtual Table Name (CE) S5.10.5.8.4

    vtq_5 : list[QSC] | None
        VTQ.5 (opt, rep) - Selection Criteria (QSC) S5.10.5.8.5
    """

    vtq_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "vtq_1",
            "query_tag",
            "VTQ.1",
        ),
        serialization_alias="VTQ.1",
        title="Query Tag",
        description="Item #696",
    )

    vtq_2: str = Field(
        validation_alias=AliasChoices(
            "vtq_2",
            "query_response_format_code",
            "VTQ.2",
        ),
        serialization_alias="VTQ.2",
        title="Query/Response Format Code",
        description="Item #697 | Table HL70106",
    )

    vtq_3: CE = Field(
        validation_alias=AliasChoices(
            "vtq_3",
            "vt_query_name",
            "VTQ.3",
        ),
        serialization_alias="VTQ.3",
        title="VT Query Name",
        description="Item #698",
    )

    vtq_4: CE = Field(
        validation_alias=AliasChoices(
            "vtq_4",
            "virtual_table_name",
            "VTQ.4",
        ),
        serialization_alias="VTQ.4",
        title="Virtual Table Name",
        description="Item #699",
    )

    vtq_5: Optional[List[QSC]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "vtq_5",
            "selection_criteria",
            "VTQ.5",
        ),
        serialization_alias="VTQ.5",
        title="Selection Criteria",
        description="Item #700",
    )

    model_config = {"populate_by_name": True}
